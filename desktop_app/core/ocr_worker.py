"""
OCR Worker — chạy OCR trên thread riêng, callback về UI thread an toàn.

Cải tiến v2:
  - preload_models(): warm-up DocTR/Paddle ngay khi mở app (background thread)
  - _run_pdf(): pre-render tất cả trang song song bằng ThreadPoolExecutor (CPU)
  - _paddle_lock: thread-safe singleton cho PaddleOCR
"""
import threading
import time
import os
import sys
from pathlib import Path
from typing import Callable, List, Optional
from dataclasses import dataclass, field
from concurrent.futures import ThreadPoolExecutor, as_completed

# Add ocr_scanner/src vào path
_ROOT = Path(__file__).resolve().parent.parent.parent / "ocr_scanner"
sys.path.insert(0, str(_ROOT))


# ─── Data classes ────────────────────────────────────────────────────────────

@dataclass
class FileResult:
    file_path: str
    engine: str
    status: str = "pending"          # pending | running | done | error
    raw_text: str = ""               # Text chưa qua post-process
    text: str = ""                   # Text cuối cùng
    error: str = ""
    start_time: float = 0.0
    end_time: float = 0.0
    elapsed: float = 0.0
    confidence: float = 0.0          # only Paddle returns this
    lines_count: int = 0
    char_count: int = 0


@dataclass
class BatchProgress:
    total: int = 0
    done: int = 0
    current_file: str = ""
    results: List[FileResult] = field(default_factory=list)
    batch_start: float = 0.0
    estimated_remaining: float = 0.0


# ─── OCR Worker ───────────────────────────────────────────────────────────────

class OCRWorker:
    """
    Chạy OCR cho một hay nhiều file trên một thread riêng.

    Callbacks (tất cả đều được gọi từ worker thread — UI phải dùng root.after):
        on_log(message: str)
        on_file_start(result: FileResult)
        on_file_done(result: FileResult)
        on_progress(progress: BatchProgress)
        on_batch_done(results: List[FileResult])
        on_error(error: str)
        on_models_ready()           ← fired khi preload xong
    """

    SUPPORTED_IMAGE_EXT = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif", ".webp"}
    SUPPORTED_PDF_EXT   = {".pdf"}
    SUPPORTED_ALL_EXT   = SUPPORTED_IMAGE_EXT | SUPPORTED_PDF_EXT

    # Thread-safe lock cho PaddleOCR singleton (không re-entrant safe)
    _paddle_lock = threading.Lock()

    def __init__(self):
        self._thread: Optional[threading.Thread] = None
        self._preload_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()

        # Callbacks
        self.on_log: Optional[Callable] = None
        self.on_file_start: Optional[Callable] = None
        self.on_file_done: Optional[Callable] = None
        self.on_progress: Optional[Callable] = None
        self.on_batch_done: Optional[Callable] = None
        self.on_error: Optional[Callable] = None
        self.on_models_ready: Optional[Callable] = None   # (engine: str) -> None

        # Model state
        self._models_loaded_for: Optional[str] = None    # engine đã được preload
        self._use_postprocess: bool = False               # SymSpell post-processing toggle
        self._use_protonx: bool = False                   # ProtonX post-processing toggle

    # ── Public API ────────────────────────────────────────────────────────────

    def preload_models(self, engine: str):
        """
        Warm-up DocTR/PaddleOCR trên background thread.
        Gọi ngay sau khi UI build xong để tránh chờ khi OCR lần đầu.
        """
        if self._preload_thread and self._preload_thread.is_alive():
            return  # đang load rồi
        if self._models_loaded_for == engine:
            return  # đã load engine này rồi

        self._preload_thread = threading.Thread(
            target=self._do_preload,
            args=(engine,),
            daemon=True,
            name="ModelPreload"
        )
        self._preload_thread.start()

    def start(self, files: List[str], engine: str, use_postprocess: bool = False, use_protonx: bool = False):
        """Bắt đầu xử lý batch (non-blocking).
        
        Args:
            files: Danh sách file cần OCR
            engine: 'ensemble' | 'doctr' | 'paddle' | 'erax'
            use_postprocess: Bật SymSpell spell check sau OCR
            use_protonx: Bật ProtonX AI post-process (chậm nhưng chính xác)
        """
        if self._thread and self._thread.is_alive():
            self._log("⚠️  Một tác vụ đang chạy, vui lòng chờ...")
            return
        self._use_postprocess = use_postprocess
        self._use_protonx = use_protonx
        self._stop_event.clear()
        self._thread = threading.Thread(
            target=self._run_batch,
            args=(files, engine),
            daemon=True,
            name="OCR-Worker"
        )
        self._thread.start()

    def stop(self):
        """Yêu cầu dừng sau file hiện tại."""
        self._stop_event.set()
        self._log("🛑 Đang dừng sau file hiện tại...")

    def is_running(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    def models_ready(self) -> bool:
        return self._models_loaded_for is not None

    @staticmethod
    def filter_valid_files(paths: List[str]) -> List[str]:
        valid = []
        for p in paths:
            ext = Path(p).suffix.lower()
            if ext in OCRWorker.SUPPORTED_ALL_EXT:
                valid.append(p)
        return valid

    # ── Model preload ─────────────────────────────────────────────────────────

    def _do_preload(self, engine: str):
        """Khởi tạo model trước để tránh chờ khi OCR lần đầu."""
        self._log(f"⏳ Đang tải model [{engine.upper()}] vào bộ nhớ...")
        t0 = time.time()

        try:
            if engine in ("doctr", "ensemble"):
                self._log("   • Khởi tạo DocTR...")
                # Import trigger model load
                from src.ocr.engine_doctr import ocr_doctr_image  # noqa: F401
                # DocTR load model lazy khi gọi lần đầu → cần chạy dummy
                import tempfile, numpy as np
                from PIL import Image as PILImage
                dummy = PILImage.fromarray(
                    np.ones((64, 256, 3), dtype=np.uint8) * 255
                )
                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tf:
                    dummy_path = tf.name
                try:
                    dummy.save(dummy_path)
                    ocr_doctr_image(dummy_path)
                finally:
                    try:
                        os.remove(dummy_path)
                    except Exception:
                        pass
                self._log("   ✅ DocTR ready")

            if engine in ("paddle", "ensemble", "paddle_fast"):
                self._log("   • Khởi tạo PaddleOCR fast (batch mode)...")
                with self._paddle_lock:
                    from src.ocr.engine_paddle import get_paddle_ocr_fast
                    get_paddle_ocr_fast()
                self._log("   ✅ PaddleOCR fast ready")

            if engine == "erax":
                self._log("   • Khởi tạo EraX-VL-2B (lần đầu tải ~4.5GB)...")
                from src.ocr.engine_erax import get_erax_model
                get_erax_model()
                self._log("   ✅ EraX-VL-2B ready")

            elapsed = time.time() - t0
            self._models_loaded_for = engine
            self._log(f"✅ Model sẵn sàng! (tải trong {elapsed:.1f}s)")

            if self.on_models_ready:
                self.on_models_ready(engine)

        except Exception as exc:
            self._log(f"⚠️  Preload thất bại: {exc}")
            self._log("   (Sẽ load lại khi bắt đầu OCR)")

    # ── Internal batch runner ─────────────────────────────────────────────────

    def _run_batch(self, files: List[str], engine: str):
        progress = BatchProgress(total=len(files), batch_start=time.time())
        results = []

        self._log(f"🚀 Bắt đầu xử lý {len(files)} file | Engine: {engine.upper()}")
        self._log("─" * 60)

        # Nếu model chưa load → load ngay
        if self._models_loaded_for != engine:
            self._log("⚠️  Model chưa được tải trước. Đang tải ngay...")
            self._do_preload(engine)

        elapsed_times = []

        for idx, file_path in enumerate(files):
            if self._stop_event.is_set():
                self._log("🛑 Đã dừng theo yêu cầu.")
                break

            result = FileResult(file_path=file_path, engine=engine)
            results.append(result)

            # Estimate remaining time
            if elapsed_times:
                avg = sum(elapsed_times) / len(elapsed_times)
                remaining = avg * (len(files) - idx)
                progress.estimated_remaining = remaining

            progress.current_file = os.path.basename(file_path)
            progress.done = idx
            self._emit_progress(progress)

            # --- Process file ---
            result.status = "running"
            result.start_time = time.time()
            self._emit_file_start(result)
            self._log(f"\n📄 [{idx+1}/{len(files)}] {os.path.basename(file_path)}")
            self._log(f"   Engine : {engine.upper()}")

            try:
                # ── Bước 1: OCR Engine (đo thời gian riêng) ──
                t_ocr_start = time.time()
                text, confidence = self._run_ocr(file_path, engine)
                t_ocr_elapsed = time.time() - t_ocr_start
                result.raw_text = text

                self._log(f"   ⏱️  OCR: {t_ocr_elapsed:.2f}s")

                # Log bước OCR độc lập
                try:
                    from src.ocr.benchmark_logger import log_ocr_step
                    log_ocr_step(os.path.basename(file_path), engine,
                                 t_ocr_elapsed, confidence, text)
                except Exception as log_exc:
                    self._log(f"   ⚠️ Lỗi ghi log OCR: {log_exc}")

                # ── Bước 2: Post-processing (đo thời gian riêng) ──
                if (self._use_postprocess or self._use_protonx) and text.strip():
                    post_method = "protonx" if self._use_protonx else "symspell"
                    self._log(f"   🔤 Đang sửa lỗi văn bản [{post_method}]...")
                    t_pp_start = time.time()
                    text = self._apply_postprocess(text)
                    t_pp_elapsed = time.time() - t_pp_start

                    self._log(f"   ⏱️  Sửa chính tả: {t_pp_elapsed:.2f}s")

                    # Log bước Post-process độc lập
                    try:
                        from src.ocr.benchmark_logger import log_postprocess_step
                        log_postprocess_step(os.path.basename(file_path), engine,
                                             post_method, t_pp_elapsed,
                                             result.raw_text, text)
                    except Exception as log_exc:
                        self._log(f"   ⚠️ Lỗi ghi log PP: {log_exc}")

                result.end_time = time.time()
                result.elapsed = result.end_time - result.start_time
                result.text = text
                result.confidence = confidence
                result.lines_count = text.count("\n") + 1 if text.strip() else 0
                result.char_count = len(text)
                result.status = "done"

                elapsed_times.append(result.elapsed)

                self._log(f"   ✅ Tổng: {result.elapsed:.2f}s")
                self._log(f"   📊 {result.lines_count} dòng | {result.char_count} ký tự"
                          + (f" | Confidence: {confidence:.1%}" if confidence > 0 else ""))

            except Exception as exc:
                result.end_time = time.time()
                result.elapsed = result.end_time - result.start_time
                result.status = "error"
                result.error = str(exc)
                self._log(f"   ❌ Lỗi: {exc}")

            self._emit_file_done(result)

        # Batch summary
        total_elapsed = time.time() - progress.batch_start
        done_count = sum(1 for r in results if r.status == "done")
        err_count  = sum(1 for r in results if r.status == "error")

        progress.done = len(files)
        progress.estimated_remaining = 0
        self._emit_progress(progress)

        self._log("\n" + "═" * 60)
        self._log(f"✅ Hoàn thành batch: {done_count}/{len(files)} file")
        if err_count:
            self._log(f"❌ Lỗi: {err_count} file")
        self._log(f"⏱️  Tổng thời gian: {total_elapsed:.1f}s"
                  + (f" | TB mỗi file: {total_elapsed/len(files):.1f}s" if files else ""))
        self._log("═" * 60)

        if self.on_batch_done:
            self.on_batch_done(results)

    # ── OCR dispatch ──────────────────────────────────────────────────────────

    def _run_ocr(self, file_path: str, engine: str):
        """Returns (text, confidence)."""
        ext = Path(file_path).suffix.lower()

        if ext == ".pdf":
            return self._run_pdf(file_path, engine)
        else:
            return self._run_image(file_path, engine)

    def _run_image(self, image_path: str, engine: str):
        if engine == "doctr":
            return self._ocr_doctr(image_path)
        elif engine == "paddle":
            return self._ocr_paddle(image_path)
        elif engine == "paddle_fast":
            return self._ocr_paddle_fast(image_path)
        elif engine == "ensemble":
            return self._ocr_ensemble(image_path)
        elif engine == "erax":
            return self._ocr_erax(image_path)
        else:
            raise ValueError(f"Unknown engine: {engine}")

    def _run_pdf(self, pdf_path: str, engine: str):
        """
        PDF pipeline tối ưu:
          Bước 1 — Pre-render song song (ThreadPoolExecutor, CPU-bound):
                   Render tất cả trang PDF → PNG cùng lúc (nhanh ~3-4x so với tuần tự)
          Bước 2 — OCR tuần tự:
                   OCR lần lượt từng ảnh PNG đã render sẵn

        Smart PDF mode:
          - PDF >= 3 trang + ensemble → tự động dùng PaddleOCR (nhanh ~2x, conf 95%+)
        """
        self._log("   📑 Đang đọc PDF bằng PyMuPDF...")
        import tempfile
        import fitz  # PyMuPDF

        doc = fitz.open(pdf_path)
        num_pages = len(doc)
        self._log(f"   📑 PDF có {num_pages} trang")

        # Smart PDF Mode:
        # - ensemble + PDF >= 3 trang → dùng paddle_fast (không unwarping, nhanh ~3-5x)
        # - paddle thường → dùng paddle_fast (PDF scan chuẩn không cần unwarping)
        pdf_engine = engine
        if engine in ("ensemble", "paddle") and num_pages >= 1:
            pdf_engine = "paddle_fast"
            self._log(f"   ⚡ Fast PDF Mode: tắt unwarping → nhanh ~3-5x/trang")

        # ── Bước 1: Pre-render tất cả trang song song (CPU) ──────────────────
        tmp_dir_obj = tempfile.TemporaryDirectory()
        tmp_dir = tmp_dir_obj.name

        self._log(f"   🖼️  Rendering {num_pages} trang song song...")
        t_render = time.time()

        # Render function (chạy độc lập trên mỗi thread)
        def render_page(args):
            page_idx, page_bytes, out_path = args
            # Mỗi thread deserialize page riêng từ bytes (fitz.Page không thread-safe)
            page_doc = fitz.open(pdf_path)
            page = page_doc[page_idx]
            mat = fitz.Matrix(2.0, 2.0)          # ~144 DPI — đủ rõ cho OCR, ít pixel hơn 2.78x ~48%
            pix = page.get_pixmap(matrix=mat, alpha=False)
            pix.save(out_path)
            page_doc.close()
            return page_idx, out_path

        render_args = [
            (i, None, os.path.join(tmp_dir, f"page_{i+1:03d}.png"))
            for i in range(num_pages)
        ]

        page_img_paths = [None] * num_pages
        max_render_workers = min(4, num_pages)   # tối đa 4 thread render (CPU-bound)
        with ThreadPoolExecutor(max_workers=max_render_workers,
                                thread_name_prefix="PDFRender") as executor:
            futures = {executor.submit(render_page, args): args[0]
                       for args in render_args}
            for future in as_completed(futures):
                if self._stop_event.is_set():
                    break
                page_idx, out_path = future.result()
                page_img_paths[page_idx] = out_path

        render_elapsed = time.time() - t_render
        self._log(f"   ✅ Render xong trong {render_elapsed:.1f}s "
                  f"({render_elapsed/num_pages:.1f}s/trang)")

        # ── Bước 2: OCR tuần tự trên ảnh đã render sẵn ───────────────────────
        all_texts = []
        page_confidences = []

        for i, page_img_path in enumerate(page_img_paths):
            if self._stop_event.is_set():
                self._log("🛑 Đã dừng theo yêu cầu.")
                break
            if page_img_path is None:
                all_texts.append(f"--- Trang {i+1} ---\n[Render thất bại]")
                continue

            self._log(f"   → Trang {i+1}/{num_pages}...")
            text, conf = self._run_image(page_img_path, pdf_engine)
            all_texts.append(f"--- Trang {i+1} ---\n{text}")
            if conf > 0:
                page_confidences.append(conf)

        # Cleanup
        try:
            tmp_dir_obj.cleanup()
        except Exception:
            pass

        doc.close()
        combined = "\n\n".join(all_texts)
        avg_conf = (sum(page_confidences) / len(page_confidences)
                    if page_confidences else 0.0)
        return combined, avg_conf

    # ── Engine wrappers ───────────────────────────────────────────────────────

    def _ocr_doctr(self, image_path: str):
        from src.ocr.engine_doctr import ocr_doctr_image
        text = ocr_doctr_image(image_path)
        return text, 0.0

    def _ocr_paddle(self, image_path: str):
        """Full quality — dùng cho ảnh đơn lẻ."""
        with self._paddle_lock:
            from src.ocr.engine_paddle import ocr_paddle_image_detailed
            result = ocr_paddle_image_detailed(image_path)
        return result["text"], result.get("avg_confidence", 0.0)

    def _ocr_paddle_fast(self, image_path: str):
        """Fast mode — dùng cho PDF batch (không unwarping, ~3-5x nhanh hơn)."""
        with self._paddle_lock:
            from src.ocr.engine_paddle import ocr_paddle_image_detailed_fast
            result = ocr_paddle_image_detailed_fast(image_path)
        return result["text"], result.get("avg_confidence", 0.0)

    def _ocr_erax(self, image_path: str):
        """EraX-VL-2B — Vision-Language Model cho tiếng Việt."""
        from src.ocr.engine_erax import ocr_erax_image
        text = ocr_erax_image(image_path)
        return text, 0.95   # VLM không có confidence box-level, ước lượng 0.95

    def _apply_postprocess(self, text: str) -> str:
        """Chạy post-processing pipeline (SymSpell hoặc ProtonX)."""
        try:
            if self._use_protonx:
                self._log("      [ProtonX] Đang chạy AI Correction...")
                # Kết hợp FIX_MAP + ProtonX để có hiệu quả tốt nhất
                from src.ocr.postprocess_pipeline import apply_postprocess
                from src.ocr.engine_protonx_correction import correct_vietnamese_text_protonx
                after_fixmap = apply_postprocess(text, use_spellcheck=False)
                text = correct_vietnamese_text_protonx(after_fixmap)
            elif self._use_postprocess:
                self._log("      [SymSpell] Đang chạy Spellcheck...")
                from src.ocr.postprocess_pipeline import apply_postprocess
                text = apply_postprocess(text, use_spellcheck=True)
                
            return self._apply_military_domain_filter(text)
        except Exception as e:
            self._log(f"   ⚠️  Post-process lỗi: {e}")
            return text

    def _apply_military_domain_filter(self, text: str) -> str:
        """Bộ lọc từ điển cứng chuyên ngành Quân đội."""
        lower_text = text.lower()
        military_keywords = ["phục viên", "tư lệnh", "quân lực", "binh đoàn", "sư đoàn", "bộ quốc phòng"]
        
        # Nếu văn bản chứa từ khóa quân đội, sửa "Nhập khẩu" -> "Nhập ngũ"
        if any(kw in lower_text for kw in military_keywords):
            if "Nhập khẩu" in text:
                self._log("      [Domain Filter] Đã sửa 'Nhập khẩu' → 'Nhập ngũ'")
                text = text.replace("Nhập khẩu", "Nhập ngũ")
            if "nhập khẩu" in text:
                text = text.replace("nhập khẩu", "nhập ngũ")
                
        return text

    def _ocr_ensemble(self, image_path: str):
        """Chạy cả DocTR và Paddle, chọn cái có confidence cao hơn."""
        self._log("   [Ensemble] Chạy DocTR...")
        doctr_text, _ = self._ocr_doctr(image_path)

        self._log("   [Ensemble] Chạy PaddleOCR...")
        paddle_text, paddle_conf = self._ocr_paddle(image_path)

        # Ước tính confidence DocTR từ chất lượng text
        words = doctr_text.split()
        doctr_conf = (sum(1 for w in words if len(w) > 2) / len(words)
                      if words else 0.0)

        self._log(f"   [Ensemble] DocTR: {doctr_conf:.1%} | Paddle: {paddle_conf:.1%}")

        if paddle_conf >= doctr_conf:
            self._log(f"   [Ensemble] → Chọn PaddleOCR")
            return paddle_text, paddle_conf
        else:
            self._log(f"   [Ensemble] → Chọn DocTR")
            return doctr_text, doctr_conf

    # ── Emit helpers ──────────────────────────────────────────────────────────

    def _log(self, msg: str):
        if self.on_log:
            self.on_log(msg)

    def _emit_file_start(self, result: FileResult):
        if self.on_file_start:
            self.on_file_start(result)

    def _emit_file_done(self, result: FileResult):
        if self.on_file_done:
            self.on_file_done(result)

    def _emit_progress(self, progress: BatchProgress):
        if self.on_progress:
            self.on_progress(progress)
