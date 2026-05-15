"""
Benchmark Logger — Ghi log kết quả OCR & Post-processing độc lập.

Mỗi bước (OCR engine / Sửa chính tả) được ghi thành 1 dòng riêng biệt
trong file CSV để dễ dàng so sánh, lọc và vẽ biểu đồ.

File output:
  - data/logs/ocr_benchmark.csv   (mở bằng Excel)
  - data/logs/ocr_history.jsonl   (lưu full text cho phân tích sâu)
"""
import os
import csv
import json
from datetime import datetime
from pathlib import Path
import threading


class BenchmarkLogger:
    _lock = threading.Lock()

    CSV_HEADERS = [
        "Timestamp",        # Thời điểm ghi log
        "Filename",         # Tên file đầu vào
        "Step",             # "OCR" hoặc "Post-Process"
        "Engine",           # doctr / paddle / erax / ensemble
        "Post-Method",      # none / symspell / protonx (chỉ có ở bước Post-Process)
        "Time (s)",         # Thời gian riêng của bước này
        "Confidence",       # Độ tin cậy (chỉ OCR engine trả về)
        "Char Count",       # Số ký tự output
        "Line Count",       # Số dòng output
        "Text Snippet",     # 200 ký tự đầu để preview
    ]

    def __init__(self, log_dir=None):
        if log_dir is None:
            base_path = Path(__file__).resolve().parent.parent.parent
            self.log_dir = base_path / "data" / "logs"
        else:
            self.log_dir = Path(log_dir)

        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.csv_path = self.log_dir / "ocr_benchmark.csv"
        self.jsonl_path = self.log_dir / "ocr_history.jsonl"
        self._init_csv()

    def _init_csv(self):
        with self._lock:
            if not self.csv_path.exists():
                with open(self.csv_path, mode='w', encoding='utf-8-sig', newline='') as f:
                    csv.writer(f).writerow(self.CSV_HEADERS)

    def _snippet(self, text: str, max_len: int = 200) -> str:
        s = text.replace('\n', ' ').replace('\r', '')
        return (s[:max_len] + "...") if len(s) > max_len else s

    # ── Public API ────────────────────────────────────────────────────────────

    def log_ocr_step(self, filename: str, engine: str,
                     elapsed: float, confidence: float, text: str):
        """Ghi 1 dòng log cho bước OCR engine (độc lập)."""
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        char_count = len(text)
        line_count = text.count("\n") + 1 if text.strip() else 0

        self._write_csv([
            ts, filename, "OCR", engine, "none",
            f"{elapsed:.3f}", f"{confidence:.4f}",
            char_count, line_count, self._snippet(text)
        ])
        self._write_jsonl({
            "timestamp": ts, "filename": filename,
            "step": "OCR", "engine": engine, "post_method": "none",
            "time_s": round(elapsed, 3), "confidence": confidence,
            "char_count": char_count, "line_count": line_count,
            "text": text
        })

    def log_postprocess_step(self, filename: str, engine: str,
                             post_method: str, elapsed: float,
                             text_before: str, text_after: str):
        """Ghi 1 dòng log cho bước sửa chính tả (độc lập)."""
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        char_count = len(text_after)
        line_count = text_after.count("\n") + 1 if text_after.strip() else 0

        self._write_csv([
            ts, filename, "Post-Process", engine, post_method,
            f"{elapsed:.3f}", "", char_count, line_count,
            self._snippet(text_after)
        ])
        self._write_jsonl({
            "timestamp": ts, "filename": filename,
            "step": "Post-Process", "engine": engine,
            "post_method": post_method,
            "time_s": round(elapsed, 3), "confidence": None,
            "char_count": char_count, "line_count": line_count,
            "text_before": text_before,
            "text_after": text_after
        })

    # ── Internal ──────────────────────────────────────────────────────────────

    def _write_csv(self, row: list):
        with self._lock:
            with open(self.csv_path, mode='a', encoding='utf-8-sig', newline='') as f:
                csv.writer(f).writerow(row)

    def _write_jsonl(self, data: dict):
        with self._lock:
            with open(self.jsonl_path, mode='a', encoding='utf-8') as f:
                f.write(json.dumps(data, ensure_ascii=False) + "\n")


# Singleton
_logger = BenchmarkLogger()

def log_ocr_step(filename, engine, elapsed, confidence, text):
    _logger.log_ocr_step(filename, engine, elapsed, confidence, text)

def log_postprocess_step(filename, engine, post_method, elapsed, text_before, text_after):
    _logger.log_postprocess_step(filename, engine, post_method, elapsed, text_before, text_after)
