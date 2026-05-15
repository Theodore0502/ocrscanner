"""
Main application window — OCR Scanner & File Tools
Tab-based layout: OCR Scanner | Đổi Tên | Tách PDF | PDF→Word | Đánh Số
Giao diện: Light mode, white + pink pastel (Excel-like tabs)
"""
import sys
import os
import time
import threading
import queue
from pathlib import Path
from typing import List, Optional

import customtkinter as ctk
from tkinter import filedialog, messagebox
import tkinter as tk
from PIL import Image, ImageTk

# Add ocr_scanner to sys.path
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_OCR_ROOT = _PROJECT_ROOT / "ocr_scanner"
sys.path.insert(0, str(_OCR_ROOT))

from core.ocr_worker import OCRWorker, FileResult, BatchProgress


# ─── Palette: White + Pink Pastel ─────────────────────────────────────────────

ACCENT        = "#D63384"       # Hồng đậm — nút chính
ACCENT_HOVER  = "#B5276E"       # Hồng tối — hover
ACCENT_SOFT   = "#F48FB1"       # Hồng nhạt — highlight nhẹ
ACCENT2       = "#9C89CC"       # Tím lavender — nút phụ
ACCENT2_HOVER = "#7B6BAA"

SUCCESS       = "#28A745"       # Xanh lá
SUCCESS_HOVER = "#1E7E34"
WARNING       = "#E67E22"       # Cam
ERROR         = "#DC3545"       # Đỏ

BG_MAIN       = "#FFFFFF"       # Trắng tinh — nền chính
BG_SIDEBAR    = "#FFF0F5"       # Hồng cực nhạt — sidebar
BG_PANEL      = "#FAF7F9"       # Trắng hơi hồng — panels
BG_HEADER     = "#FFE4EE"       # Hồng pastel — header bars
BG_INPUT      = "#FFFBFD"       # Trắng — input areas
BG_LOG        = "#FDF6F9"       # Kem hồng — log background

TEXT_PRIMARY  = "#2C1A2E"       # Tím tối — text chính
TEXT_SECONDARY= "#6D4C61"       # Hồng tím — text phụ
TEXT_DIM      = "#B08090"       # Hồng xám — placeholder

DIVIDER       = "#F0D0E0"       # Hồng nhạt — đường kẻ
BORDER        = "#EBC0D0"       # Hồng border

FONT_MONO  = ("Consolas", 11)
FONT_UI    = ("Segoe UI", 11)
FONT_TITLE = ("Segoe UI", 12, "bold")
FONT_SMALL = ("Segoe UI", 9)

SUPPORTED_EXTS = "*.jpg *.jpeg *.png *.bmp *.tiff *.tif *.webp *.pdf"


# ─── Main App ─────────────────────────────────────────────────────────────────

class OCRScannerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")   # base theme; pink palette applied via fg_color constants

        self.title("🌸  OCR Scanner & File Tools")
        self.geometry("1420x860")
        self.minsize(1100, 650)
        self.configure(fg_color=BG_MAIN)

        # State
        self._selected_files: List[str] = []
        self._results: List[FileResult] = []
        self._current_preview_idx: int = 0
        self._preview_img_cache = None
        self._ui_queue: queue.Queue = queue.Queue()
        self._worker = OCRWorker()
        self._timer_running = False
        self._batch_start: float = 0.0
        self._estimated_remaining: float = 0.0
        self._admin_mode = False  # False = User Mode, True = Admin Mode

        self._setup_worker_callbacks()
        self._build_ui()
        self._start_ui_pump()

        # Preload model sau khi UI hiển thị (100ms delay để window ổn định)
        self.after(100, self._trigger_preload)
        self.after(0, lambda: self.state('zoomed')) # Gọi duy nhất 1 lần để tránh giật hình
        self.after(300, self._apply_mode)  # Áp dụng User Mode mặc định

    # ── Worker callbacks ──────────────────────────────────────────────────────

    def _setup_worker_callbacks(self):
        def safe(fn):
            def wrapper(*args, **kwargs):
                self._ui_queue.put((fn, args, kwargs))
            return wrapper

        self._worker.on_log          = safe(self._on_log)
        self._worker.on_file_start   = safe(self._on_file_start)
        self._worker.on_file_done    = safe(self._on_file_done)
        self._worker.on_progress     = safe(self._on_progress)
        self._worker.on_batch_done   = safe(self._on_batch_done)
        self._worker.on_models_ready = safe(self._on_models_ready)

    def _start_ui_pump(self):
        """Poll queue mỗi 50ms để update UI an toàn từ main thread."""
        try:
            while True:
                fn, args, kwargs = self._ui_queue.get_nowait()
                fn(*args, **kwargs)
        except queue.Empty:
            pass
        self.after(50, self._start_ui_pump)

    # ── Build UI ───────────────────────────────────────────────────────────────

    def _build_ui(self):
        # ── Outer TabView (Excel-style tabs) ─────────────────────────────────
        self._tabview = ctk.CTkTabview(
            self,
            fg_color=BG_MAIN,
            segmented_button_fg_color=BG_SIDEBAR,
            segmented_button_selected_color=BG_MAIN,
            segmented_button_selected_hover_color=BG_HEADER,
            segmented_button_unselected_color=BG_SIDEBAR,
            segmented_button_unselected_hover_color=BG_HEADER,
            text_color=TEXT_PRIMARY,
            text_color_disabled=TEXT_DIM,
            corner_radius=0,
        )
        self._tabview.pack(fill="both", expand=True, padx=0, pady=0)

        # ── Add tabs ─────────────────────────────────────────────────────────
        TAB_OCR    = "📄  OCR Scanner"
        TAB_RENAME = "✏️  Đổi Tên File"
        TAB_SPLIT  = "✂️  Tách PDF"
        TAB_WORD   = "🔄  PDF → Word"
        TAB_NUM    = "🔢  Đánh Số File"

        for name in [TAB_OCR, TAB_RENAME, TAB_SPLIT, TAB_WORD, TAB_NUM]:
            self._tabview.add(name)

        # ── Build OCR tab (existing 3-panel layout) ───────────────────────────
        self._build_ocr_tab(self._tabview.tab(TAB_OCR))

        # ── Inject tool tabs from tools_ui package ────────────────────────────
        try:
            from tools_ui.tab_rename import TabRename
            TabRename(self._tabview.tab(TAB_RENAME))
        except Exception as e:
            self._tool_error(self._tabview.tab(TAB_RENAME), "Đổi Tên File", e)

        try:
            from tools_ui.tab_split_pdf import TabSplitPDF
            TabSplitPDF(self._tabview.tab(TAB_SPLIT))
        except Exception as e:
            self._tool_error(self._tabview.tab(TAB_SPLIT), "Tách PDF", e)

        try:
            from tools_ui.tab_pdf_to_word import TabPDFToWord
            TabPDFToWord(self._tabview.tab(TAB_WORD))
        except Exception as e:
            self._tool_error(self._tabview.tab(TAB_WORD), "PDF → Word", e)

        try:
            from tools_ui.tab_numbering import TabNumbering
            TabNumbering(self._tabview.tab(TAB_NUM))
        except Exception as e:
            self._tool_error(self._tabview.tab(TAB_NUM), "Đánh Số File", e)

    def _tool_error(self, frame, name: str, err: Exception):
        """Fallback khi tab tool load thất bại."""
        ctk.CTkLabel(
            frame,
            text=f"❌  Không thể tải tab '{name}':\n{err}",
            font=FONT_UI, text_color=ERROR,
            wraplength=600).pack(expand=True)

    def _build_ocr_tab(self, parent):
        """Gắn toàn bộ giao diện OCR 3-cột vào frame tab OCR."""
        parent.grid_columnconfigure(0, weight=0)   # Sidebar (fixed)
        parent.grid_columnconfigure(1, weight=3)   # Preview
        parent.grid_columnconfigure(2, weight=4)   # Result + Log
        parent.grid_rowconfigure(0, weight=1)

        self._build_sidebar(parent)
        self._build_preview_panel(parent)
        self._build_right_panel(parent)

    # ── Sidebar ────────────────────────────────────────────────────────────────

    def _build_sidebar(self, parent):
        sidebar = ctk.CTkFrame(parent, width=280, corner_radius=0,
                               fg_color=BG_SIDEBAR, border_width=0)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)

        # ── Logo / title ───────────────────────────────────────────────────────
        title_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        title_frame.grid(row=0, column=0, padx=16, pady=(12, 4), sticky="ew")

        ctk.CTkLabel(title_frame, text="🌸  OCR Scanner",
                     font=("Segoe UI", 15, "bold"),
                     text_color=ACCENT).pack(anchor="w")
        ctk.CTkLabel(title_frame, text="Số hóa Tài liệu Hành chính",
                     font=("Segoe UI", 8), text_color=TEXT_DIM).pack(anchor="w")

        # Model status badge — inline, nhỏ gọn
        self._model_status_frame = ctk.CTkFrame(
            title_frame, fg_color=BG_HEADER, corner_radius=5)
        self._model_status_frame.pack(anchor="w", pady=(4, 0))
        self._model_status_label = ctk.CTkLabel(
            self._model_status_frame,
            text="⏳ Đang tải model...",
            font=("Segoe UI", 8), text_color=WARNING,
            padx=6, pady=2)
        self._model_status_label.pack()

        # Toggle User/Admin mode
        self._mode_btn = ctk.CTkButton(
            title_frame, text="🔧 Admin", width=80, height=22,
            command=self._toggle_mode,
            fg_color="transparent", hover_color=BG_HEADER,
            text_color=TEXT_DIM, font=("Segoe UI", 8),
            corner_radius=5, border_width=1, border_color=BORDER)
        self._mode_btn.pack(anchor="w", pady=(4, 0))

        self._divider(sidebar, row=1)

        # ── Engine selector ────────────────────────────────────────────────────
        self._engine_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        self._engine_frame.grid(row=2, column=0, padx=16, pady=(4, 2), sticky="ew")
        engine_frame = self._engine_frame

        ctk.CTkLabel(engine_frame, text="⚙️  Engine OCR",
                     font=("Segoe UI", 10, "bold"), text_color=TEXT_PRIMARY
                     ).pack(anchor="w", pady=(0, 2))

        self._engine_var = ctk.StringVar(value="ensemble")
        engines = [
            ("Ensemble (Tốt nhất)", "ensemble"),
            ("DocTR", "doctr"),
            ("PaddleOCR v5", "paddle"),
            ("PaddleOCR Fast ⚡", "paddle_fast"),
            ("EraX-VL-2B (VLM)", "erax"),
        ]
        for label, val in engines:
            rb = ctk.CTkRadioButton(
                engine_frame, text=label, variable=self._engine_var,
                value=val, font=("Segoe UI", 10),
                text_color=TEXT_PRIMARY,
                fg_color=ACCENT, hover_color=ACCENT_HOVER,
                radiobutton_width=14, radiobutton_height=14,
                command=self._on_engine_change)
            rb.pack(anchor="w", pady=1)

        # SymSpell checkbox
        self._postprocess_var = ctk.BooleanVar(value=False)
        pp_frame = ctk.CTkFrame(engine_frame, fg_color="transparent")
        pp_frame.pack(fill="x", pady=(4, 0))
        ctk.CTkFrame(pp_frame, height=1, fg_color=DIVIDER).pack(fill="x", pady=(0, 3))
        self._postprocess_cb = ctk.CTkCheckBox(
            pp_frame, text="Sửa chính tả (SymSpell)",
            variable=self._postprocess_var,
            font=("Segoe UI", 9),
            text_color=TEXT_SECONDARY,
            fg_color=ACCENT, hover_color=ACCENT_HOVER,
            checkmark_color="white", border_color=BORDER,
            width=14, height=14)
        self._postprocess_cb.pack(anchor="w", pady=(0,4))

        self._protonx_var = ctk.BooleanVar(value=False)
        self._protonx_cb = ctk.CTkCheckBox(
            pp_frame, text="Sửa lỗi AI (ProtonX Nano)",
            variable=self._protonx_var,
            font=("Segoe UI", 9),
            text_color=TEXT_SECONDARY,
            fg_color=ACCENT, hover_color=ACCENT_HOVER,
            checkmark_color="white", border_color=BORDER,
            width=14, height=14)
        self._protonx_cb.pack(anchor="w")

        self._engine_divider = ctk.CTkFrame(sidebar, height=1, fg_color=DIVIDER)
        self._engine_divider.grid(row=3, column=0, padx=12, pady=4, sticky="ew")

        # ── File section ───────────────────────────────────────────────────────
        file_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        file_frame.grid(row=4, column=0, padx=16, pady=(3, 2), sticky="ew")

        ctk.CTkLabel(file_frame, text="📂  File đầu vào",
                     font=("Segoe UI", 10, "bold"), text_color=TEXT_PRIMARY
                     ).pack(anchor="w", pady=(0, 3))

        ctk.CTkButton(
            file_frame, text="Chọn File(s)...", command=self._browse_files,
            fg_color=ACCENT, hover_color=ACCENT_HOVER,
            text_color="white", font=("Segoe UI", 10), height=30,
            corner_radius=7).pack(fill="x", pady=(0, 2))

        ctk.CTkButton(
            file_frame, text="Chọn Thư mục...", command=self._browse_folder,
            fg_color=ACCENT2, hover_color=ACCENT2_HOVER,
            text_color="white", font=("Segoe UI", 10), height=30,
            corner_radius=7).pack(fill="x", pady=(0, 2))

        ctk.CTkButton(
            file_frame, text="✕  Xóa danh sách", command=self._clear_files,
            fg_color="transparent", hover_color=BG_HEADER,
            text_color=TEXT_DIM, font=("Segoe UI", 9), height=24,
            corner_radius=7, border_width=1,
            border_color=BORDER).pack(fill="x")

        ctk.CTkLabel(
            file_frame, text="JPG · PNG · BMP · TIFF · WEBP · PDF",
            font=("Segoe UI", 7), text_color=TEXT_DIM,
            wraplength=230).pack(anchor="w", pady=(3, 0))

        self._divider(sidebar, row=5)

        # File count badge
        self._file_count_label = ctk.CTkLabel(
            sidebar, text="0 file đã chọn",
            font=("Segoe UI", 9), text_color=TEXT_DIM)
        self._file_count_label.grid(row=6, column=0, padx=16, pady=(0, 3), sticky="w")

        # File list — grows to fill remaining space
        self._file_listbox = ctk.CTkScrollableFrame(
            sidebar, height=60,
            fg_color=BG_INPUT, corner_radius=7,
            border_color=BORDER, border_width=1)
        self._file_listbox.grid(row=7, column=0, padx=16, pady=(0, 3), sticky="nsew")
        sidebar.grid_rowconfigure(7, weight=1)   # listbox co giãn → buttons luôn ở dưới

        self._divider(sidebar, row=8)

        # ── Run / Stop buttons ─────────────────────────────────────────────────
        btn_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        btn_frame.grid(row=10, column=0, padx=18, pady=(6, 20), sticky="ew")
        btn_frame.columnconfigure((0, 1), weight=1)

        self._run_btn = ctk.CTkButton(
            btn_frame, text="▶  Bắt đầu OCR",
            command=self._start_ocr,
            fg_color=SUCCESS, hover_color=SUCCESS_HOVER,
            text_color="white",
            font=("Segoe UI", 12, "bold"), height=42,
            corner_radius=10)
        self._run_btn.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 4))

        self._stop_btn = ctk.CTkButton(
            btn_frame, text="⏹  Dừng",
            command=self._stop_ocr,
            fg_color="#FFCDD2", hover_color="#EF9A9A",
            text_color=ERROR,
            font=FONT_UI, height=30,
            corner_radius=8, state="disabled")
        self._stop_btn.grid(row=1, column=0, columnspan=2, sticky="ew")

    def _divider(self, parent, row):
        ctk.CTkFrame(parent, height=1, fg_color=DIVIDER).grid(
            row=row, column=0, padx=12, pady=4, sticky="ew")

    # ── Preview panel ──────────────────────────────────────────────────────────

    def _build_preview_panel(self, parent):
        panel = ctk.CTkFrame(parent, corner_radius=0, fg_color=BG_PANEL)
        panel.grid(row=0, column=1, sticky="nsew")
        panel.grid_rowconfigure(1, weight=1)
        panel.grid_columnconfigure(0, weight=1)

        # Header
        hdr = ctk.CTkFrame(panel, height=48, fg_color=BG_HEADER, corner_radius=0)
        hdr.grid(row=0, column=0, sticky="ew")
        hdr.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(hdr, text="🖼️  Xem trước",
                     font=FONT_TITLE, text_color=TEXT_PRIMARY).grid(
            row=0, column=0, padx=16, pady=12, sticky="w")

        nav_fr = ctk.CTkFrame(hdr, fg_color="transparent")
        nav_fr.grid(row=0, column=1, sticky="e", padx=12)

        self._prev_btn = ctk.CTkButton(
            nav_fr, text="◀", width=32, height=28,
            command=self._prev_preview,
            fg_color=BG_MAIN, hover_color=BG_HEADER,
            text_color=ACCENT, corner_radius=6,
            border_width=1, border_color=BORDER)
        self._prev_btn.pack(side="left", padx=2)

        self._preview_nav_label = ctk.CTkLabel(
            nav_fr, text="—", font=FONT_UI,
            text_color=TEXT_DIM, width=80)
        self._preview_nav_label.pack(side="left")

        self._next_btn = ctk.CTkButton(
            nav_fr, text="▶", width=32, height=28,
            command=self._next_preview,
            fg_color=BG_MAIN, hover_color=BG_HEADER,
            text_color=ACCENT, corner_radius=6,
            border_width=1, border_color=BORDER)
        self._next_btn.pack(side="left", padx=2)

        # Canvas
        self._preview_canvas = tk.Canvas(
            panel, bg="#FFF5F8", highlightthickness=0)
        self._preview_canvas.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self._preview_canvas.bind("<Configure>", self._on_canvas_resize)

        # File name label
        self._preview_filename = ctk.CTkLabel(
            panel, text="Chưa chọn file",
            font=("Segoe UI", 10), text_color=TEXT_DIM)
        self._preview_filename.grid(row=2, column=0, pady=(0, 8))

    # ── Right panel (Result + Log) ─────────────────────────────────────────────

    def _build_right_panel(self, parent):
        self._right_panel = ctk.CTkFrame(parent, corner_radius=0, fg_color=BG_MAIN)
        panel = self._right_panel
        panel.grid(row=0, column=2, sticky="nsew")
        panel.grid_rowconfigure(1, weight=3)
        panel.grid_rowconfigure(4, weight=2)
        panel.grid_columnconfigure(0, weight=1)

        # ── Result section header ──────────────────────────────────────────────
        res_hdr = ctk.CTkFrame(panel, height=48, fg_color=BG_HEADER, corner_radius=0)
        res_hdr.grid(row=0, column=0, sticky="ew")

        action_fr = ctk.CTkFrame(res_hdr, fg_color="transparent")
        action_fr.grid(row=0, column=0, sticky="w", padx=16, pady=9)

        ctk.CTkLabel(action_fr, text="📄  Kết quả OCR",
                     font=FONT_TITLE, text_color=TEXT_PRIMARY).pack(side="left", padx=(0, 16))

        self._prev_res_btn = ctk.CTkButton(
            action_fr, text="◀", width=32, height=28,
            command=self._prev_result,
            fg_color=BG_MAIN, hover_color=BG_HEADER,
            text_color=ACCENT, corner_radius=6,
            border_width=1, border_color=BORDER)
        self._prev_res_btn.pack(side="left", padx=(0, 2))

        self._result_file_var = ctk.StringVar(value="Chọn file để xem kết quả")
        self._result_selector = ctk.CTkOptionMenu(
            action_fr, variable=self._result_file_var,
            values=["Chọn file để xem kết quả"],
            command=self._on_result_select,
            fg_color=BG_MAIN, button_color=ACCENT,
            button_hover_color=ACCENT_HOVER,
            dropdown_fg_color=BG_MAIN,
            text_color=TEXT_PRIMARY,
            width=220, font=("Segoe UI", 10))
        self._result_selector.pack(side="left", padx=(0, 2))

        self._next_res_btn = ctk.CTkButton(
            action_fr, text="▶", width=32, height=28,
            command=self._next_result,
            fg_color=BG_MAIN, hover_color=BG_HEADER,
            text_color=ACCENT, corner_radius=6,
            border_width=1, border_color=BORDER)
        self._next_res_btn.pack(side="left", padx=(0, 8))

        ctk.CTkButton(
            action_fr, text="📋 Copy", width=72, height=30,
            command=self._copy_result,
            fg_color=BG_MAIN, hover_color=BG_HEADER,
            text_color=TEXT_SECONDARY,
            corner_radius=8, border_width=1, border_color=BORDER,
            font=FONT_UI).pack(side="left", padx=2)

        ctk.CTkButton(
            action_fr, text="💾 Lưu .txt", width=92, height=30,
            command=self._save_result,
            fg_color=ACCENT, hover_color=ACCENT_HOVER,
            text_color="white",
            corner_radius=8,
            font=FONT_UI).pack(side="left", padx=2)

        ctk.CTkButton(
            action_fr, text="💾 Lưu tất cả", width=102, height=30,
            command=self._save_all_results,
            fg_color=ACCENT2, hover_color=ACCENT2_HOVER,
            text_color="white",
            corner_radius=8,
            font=FONT_UI).pack(side="left", padx=2)

        # Result text area (Top-Bottom Split)
        self._text_fr = ctk.CTkFrame(panel, fg_color="transparent")
        text_fr = self._text_fr
        text_fr.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        text_fr.grid_columnconfigure(0, weight=1)
        text_fr.grid_rowconfigure(1, weight=1)
        text_fr.grid_rowconfigure(3, weight=1)

        self._raw_label = ctk.CTkLabel(text_fr, text="📝 Văn bản gốc (Raw OCR)", font=("Segoe UI", 10, "bold"), text_color=TEXT_PRIMARY)
        self._raw_label.grid(row=0, column=0, sticky="w")
        self._result_raw = ctk.CTkTextbox(
            text_fr, font=("Consolas", 11), fg_color=BG_INPUT, text_color=TEXT_PRIMARY,
            scrollbar_button_color=ACCENT_SOFT, wrap="word", corner_radius=5)
        self._result_raw.grid(row=1, column=0, sticky="nsew", pady=(0, 8))

        ctk.CTkLabel(text_fr, text="✨ Văn bản đã sửa", font=("Segoe UI", 10, "bold"), text_color=TEXT_PRIMARY).grid(row=2, column=0, sticky="w")
        self._result_corrected = ctk.CTkTextbox(
            text_fr, font=("Consolas", 11), fg_color=BG_INPUT, text_color=TEXT_PRIMARY,
            scrollbar_button_color=ACCENT_SOFT, wrap="word", corner_radius=5)
        self._result_corrected.grid(row=3, column=0, sticky="nsew")

        # ── Metrics bar ────────────────────────────────────────────────────────
        metrics_bar = ctk.CTkFrame(panel, height=38, fg_color=BG_HEADER, corner_radius=0)
        metrics_bar.grid(row=2, column=0, sticky="ew")
        metrics_bar.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self._m_status  = self._metric_label(metrics_bar, "Trạng thái", "—", 0)
        self._m_elapsed = self._metric_label(metrics_bar, "Đã xử lý",   "—", 1)
        self._m_eta     = self._metric_label(metrics_bar, "Còn lại",    "—", 2)
        self._m_conf    = self._metric_label(metrics_bar, "Confidence", "—", 3)
        self._m_lines   = self._metric_label(metrics_bar, "Dòng/Ký tự","—", 4)

        # ── Log section header ─────────────────────────────────────────────────
        self._log_header = ctk.CTkFrame(panel, height=42, fg_color=BG_HEADER, corner_radius=0)
        log_hdr = self._log_header
        log_hdr.grid(row=3, column=0, sticky="ew")
        log_hdr.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(log_hdr, text="📋  Nhật ký xử lý",
                     font=FONT_TITLE, text_color=TEXT_PRIMARY).grid(
            row=0, column=0, padx=16, pady=10, sticky="w")

        prog_fr = ctk.CTkFrame(log_hdr, fg_color="transparent")
        prog_fr.grid(row=0, column=1, sticky="e", padx=10)

        self._progress_label = ctk.CTkLabel(
            prog_fr, text="0 / 0", font=FONT_UI,
            text_color=TEXT_DIM, width=60)
        self._progress_label.pack(side="left", padx=(0, 8))

        self._progress_bar = ctk.CTkProgressBar(
            prog_fr, width=180, height=10,
            progress_color=ACCENT,
            fg_color=DIVIDER, corner_radius=5)
        self._progress_bar.set(0)
        self._progress_bar.pack(side="left", padx=(0, 10))

        self._timer_label = ctk.CTkLabel(
            prog_fr, text="⏱ 00:00",
            font=FONT_MONO, text_color=ACCENT, width=80)
        self._timer_label.pack(side="left")

        ctk.CTkButton(
            log_hdr, text="Xóa log", width=70, height=26,
            command=self._clear_log,
            fg_color="transparent", hover_color=BG_MAIN,
            text_color=TEXT_DIM, font=("Segoe UI", 9),
            corner_radius=6).grid(row=0, column=2, padx=10, pady=8)

        # Log text area
        self._log_text = ctk.CTkTextbox(
            panel, font=("Consolas", 10),
            fg_color=BG_LOG,
            text_color=TEXT_SECONDARY,
            scrollbar_button_color=ACCENT_SOFT,
            wrap="word", corner_radius=0)
        self._log_text.grid(row=4, column=0, sticky="nsew")
        self._log_text.configure(state="disabled")

    def _metric_label(self, parent, title, value, col):
        f = ctk.CTkFrame(parent, fg_color="transparent")
        f.grid(row=0, column=col, padx=4, pady=2, sticky="ew")
        ctk.CTkLabel(f, text=title, font=("Segoe UI", 8),
                     text_color=TEXT_DIM).pack()
        val_lbl = ctk.CTkLabel(f, text=value,
                               font=("Segoe UI", 10, "bold"),
                               text_color=TEXT_PRIMARY)
        val_lbl.pack()
        return val_lbl

    # ── Model preload ──────────────────────────────────────────────────────────

    def _trigger_preload(self):
        """Khởi động preload model sau khi UI hiển thị xong."""
        engine = self._engine_var.get()
        self._model_status_label.configure(
            text="⏳ Đang tải model...", text_color=WARNING)
        self._worker.preload_models(engine)

    def _on_engine_change(self):
        """Khi user đổi engine → preload engine mới nếu chưa load."""
        engine = self._engine_var.get()
        if not self._worker.models_ready():
            return  # đang load rồi
        if self._worker._models_loaded_for != engine:
            self._model_status_label.configure(
                text=f"⏳ Đang tải [{engine.upper()}]...", text_color=WARNING)
            self._worker.preload_models(engine)

    def _on_models_ready(self, engine: str):
        """Callback khi model load xong."""
        self._model_status_label.configure(
            text=f"✅ Model sẵn sàng [{engine.upper()}]",
            text_color=SUCCESS)

    # ── File management ────────────────────────────────────────────────────────

    def _browse_files(self):
        files = filedialog.askopenfilenames(
            title="Chọn file ảnh/PDF",
            filetypes=[
                ("Tất cả định dạng hỗ trợ",
                 "*.jpg *.jpeg *.png *.bmp *.tiff *.tif *.webp *.pdf"),
                ("Ảnh", "*.jpg *.jpeg *.png *.bmp *.tiff *.tif *.webp"),
                ("PDF", "*.pdf"),
            ]
        )
        if files:
            self._add_files(list(files))

    def _browse_folder(self):
        folder = filedialog.askdirectory(title="Chọn thư mục chứa file")
        if folder:
            paths = []
            for ext in ["*.jpg", "*.jpeg", "*.png", "*.bmp",
                        "*.tiff", "*.tif", "*.webp", "*.pdf"]:
                from glob import glob
                paths.extend(glob(os.path.join(folder, ext)))
                paths.extend(glob(os.path.join(folder, ext.upper())))
            if paths:
                self._add_files(sorted(set(paths)))
            else:
                messagebox.showinfo("Thông báo",
                    "Không tìm thấy file ảnh/PDF nào trong thư mục này.")

    def _add_files(self, files: List[str]):
        existing = set(self._selected_files)
        added = 0
        for f in files:
            if f not in existing:
                self._selected_files.append(f)
                existing.add(f)
                added += 1
        self._refresh_file_list()
        if added:
            self._load_preview(0)

    def _clear_files(self):
        self._selected_files.clear()
        self._refresh_file_list()
        self._preview_canvas.delete("all")
        self._preview_filename.configure(text="Chưa chọn file")
        self._preview_nav_label.configure(text="—")

    def _refresh_file_list(self):
        for w in self._file_listbox.winfo_children():
            w.destroy()

        count = len(self._selected_files)
        self._file_count_label.configure(
            text=f"{count} file đã chọn",
            text_color=ACCENT if count else TEXT_DIM)

        for i, fp in enumerate(self._selected_files):
            name = os.path.basename(fp)
            row = ctk.CTkFrame(self._file_listbox,
                               fg_color="transparent", height=24)
            row.pack(fill="x", pady=1)
            icon = "📄" if fp.lower().endswith(".pdf") else "🖼️"
            lbl = ctk.CTkLabel(
                row, text=f"{icon} {name}",
                font=("Segoe UI", 9), text_color=TEXT_SECONDARY,
                anchor="w", cursor="hand2")
            lbl.pack(side="left", fill="x", expand=True)
            lbl.bind("<Button-1>", lambda e, idx=i: self._load_preview(idx))

            btn_del = ctk.CTkButton(
                row, text="✖", width=24, height=24,
                fg_color="transparent", hover_color="#FFEAEA",
                text_color=ERROR, font=("Segoe UI", 10, "bold"),
                command=lambda idx=i: self._remove_file(idx)
            )
            btn_del.pack(side="right", padx=(2, 5))

    def _remove_file(self, idx: int):
        if 0 <= idx < len(self._selected_files):
            self._selected_files.pop(idx)
            self._refresh_file_list()
            if self._selected_files:
                if self._current_preview_idx >= len(self._selected_files):
                    self._current_preview_idx = len(self._selected_files) - 1
                self._load_preview(self._current_preview_idx)
            else:
                self._preview_canvas.delete("all")
                self._preview_filename.configure(text="Chưa chọn file")
                self._preview_nav_label.configure(text="—")
                self._current_preview_idx = 0

    # ── Preview ────────────────────────────────────────────────────────────────

    def _load_preview(self, idx: int):
        if not self._selected_files:
            return
        idx = max(0, min(idx, len(self._selected_files) - 1))
        self._current_preview_idx = idx
        fp = self._selected_files[idx]
        name = os.path.basename(fp)
        self._preview_filename.configure(text=name)
        self._preview_nav_label.configure(
            text=f"{idx+1} / {len(self._selected_files)}")

        # Sync sang OCR Result
        if not getattr(self, '_is_syncing', False):
            self._is_syncing = True
            try:
                for r in self._results:
                    if r.file_path == fp:
                        self._result_file_var.set(name)
                        self._show_result(r)
                        break
            finally:
                self._is_syncing = False

        try:
            if fp.lower().endswith(".pdf"):
                try:
                    import fitz
                    doc = fitz.open(fp)
                    page = doc[0]
                    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    self._preview_img_cache = img
                    doc.close()
                    self._render_preview()
                except ImportError:
                    self._preview_canvas.delete("all")
                    self._preview_canvas.create_text(
                        200, 200, text="Cần cài đặt PyMuPDF (fitz)\nđể xem trước PDF.",
                        fill=ERROR, font=FONT_UI, justify="center")
                    self._preview_img_cache = None
            else:
                img = Image.open(fp)
                self._preview_img_cache = img
                self._render_preview()
        except Exception as e:
            self._preview_canvas.delete("all")
            self._preview_canvas.create_text(
                100, 100, text=f"Không đọc được file:\n{e}",
                fill=ERROR, font=FONT_UI)

    def _render_preview(self):
        if not self._preview_img_cache:
            return
        canvas = self._preview_canvas
        cw = canvas.winfo_width()
        ch = canvas.winfo_height()
        if cw < 10 or ch < 10:
            return
        img = self._preview_img_cache.copy()
        iw, ih = img.size
        scale = min(cw / iw, ch / ih)
        nw, nh = int(iw * scale), int(ih * scale)
        img = img.resize((nw, nh), Image.LANCZOS)
        self._tk_img = ImageTk.PhotoImage(img)
        canvas.delete("all")
        canvas.create_image(cw // 2, ch // 2,
                            image=self._tk_img, anchor="center")

    def _on_canvas_resize(self, event):
        self.after(100, self._render_preview)

    def _prev_preview(self):
        self._load_preview(self._current_preview_idx - 1)

    def _next_preview(self):
        self._load_preview(self._current_preview_idx + 1)

    # ── OCR control ────────────────────────────────────────────────────────────

    def _start_ocr(self):
        if not self._selected_files:
            messagebox.showwarning("Chưa chọn file",
                                   "Vui lòng chọn ít nhất một file.")
            return
        if self._worker.is_running():
            messagebox.showinfo("Đang chạy",
                                "Đang có tác vụ OCR đang xử lý.")
            return

        self._results.clear()
        self._clear_log()
        self._result_raw.delete("1.0", "end")
        self._result_corrected.delete("1.0", "end")
        self._progress_bar.set(0)
        self._progress_label.configure(text="0 / 0")
        self._run_btn.configure(state="disabled")
        self._stop_btn.configure(state="normal")

        engine = self._engine_var.get()
        use_pp = self._postprocess_var.get()
        use_protonx = self._protonx_var.get()

        # User Mode: tự động chọn cấu hình tốt nhất
        if not self._admin_mode:
            engine = "ensemble"
            use_pp = False
            use_protonx = True
        self._batch_start = time.time()
        self._start_timer()

        self._worker.start(self._selected_files, engine, use_postprocess=use_pp, use_protonx=use_protonx)

    def _stop_ocr(self):
        self._worker.stop()
        self._stop_btn.configure(state="disabled")

    # ── Timer ──────────────────────────────────────────────────────────────────

    def _start_timer(self):
        self._timer_running = True
        self._tick_timer()

    def _stop_timer(self):
        self._timer_running = False

    def _tick_timer(self):
        if not self._timer_running:
            return
        elapsed = time.time() - self._batch_start
        e_str = self._fmt_time(elapsed)
        eta = self._estimated_remaining
        eta_str = self._fmt_time(eta) if eta > 0 else "—"

        self._timer_label.configure(text=f"⏱ {e_str}")
        self._m_elapsed.configure(text=e_str)
        self._m_eta.configure(text=eta_str)
        self.after(500, self._tick_timer)

    @staticmethod
    def _fmt_time(s: float) -> str:
        s = max(0, int(s))
        m, sec = divmod(s, 60)
        return f"{m:02d}:{sec:02d}"

    # ── Worker event handlers ──────────────────────────────────────────────────

    def _on_log(self, message: str):
        self._log_text.configure(state="normal")
        self._log_text.insert("end", message + "\n")
        self._log_text.see("end")
        self._log_text.configure(state="disabled")

    def _on_file_start(self, result: FileResult):
        name = os.path.basename(result.file_path)
        self._m_status.configure(
            text=f"🔄 {name[:20]}...", text_color=WARNING)

    def _on_file_done(self, result: FileResult):
        self._results.append(result)
        name = os.path.basename(result.file_path)

        if result.status == "done":
            self._m_status.configure(
                text=f"✅ {name[:20]}", text_color=SUCCESS)
            conf_str = (f"{result.confidence:.1%}"
                        if result.confidence > 0 else "—")
            self._m_conf.configure(text=conf_str)
            self._m_lines.configure(
                text=f"{result.lines_count} / {result.char_count}")
        else:
            self._m_status.configure(
                text=f"❌ {name[:20]}", text_color=ERROR)

        names = [os.path.basename(r.file_path) for r in self._results]
        self._result_selector.configure(values=names)
        self._result_file_var.set(name)
        self._show_result(result)

    def _on_progress(self, progress: BatchProgress):
        self._estimated_remaining = progress.estimated_remaining
        frac = progress.done / progress.total if progress.total else 0
        self._progress_bar.set(frac)
        self._progress_label.configure(
            text=f"{progress.done} / {progress.total}")

    def _on_batch_done(self, results: List[FileResult]):
        self._stop_timer()
        elapsed = time.time() - self._batch_start
        self._m_elapsed.configure(text=self._fmt_time(elapsed))
        self._m_eta.configure(text="—")
        self._m_status.configure(text="✅ Hoàn thành", text_color=SUCCESS)
        self._progress_bar.set(1.0)
        self._run_btn.configure(state="normal")
        self._stop_btn.configure(state="disabled")

    # ── Result display ─────────────────────────────────────────────────────────

    def _prev_result(self):
        if not self._results: return
        names = [os.path.basename(r.file_path) for r in self._results]
        curr = self._result_file_var.get()
        if curr in names:
            idx = names.index(curr)
            if idx > 0:
                self._result_file_var.set(names[idx - 1])
                self._on_result_select(names[idx - 1])

    def _next_result(self):
        if not self._results: return
        names = [os.path.basename(r.file_path) for r in self._results]
        curr = self._result_file_var.get()
        if curr in names:
            idx = names.index(curr)
            if idx < len(names) - 1:
                self._result_file_var.set(names[idx + 1])
                self._on_result_select(names[idx + 1])

    def _on_result_select(self, choice: str):
        # Sync ngược lại Preview
        if not getattr(self, '_is_syncing', False):
            self._is_syncing = True
            try:
                for idx, fp in enumerate(self._selected_files):
                    if os.path.basename(fp) == choice:
                        self._load_preview(idx)
                        break
            finally:
                self._is_syncing = False

        for r in self._results:
            if os.path.basename(r.file_path) == choice:
                self._show_result(r)
                break

    def _show_result(self, result: FileResult):
        self._result_raw.delete("1.0", "end")
        self._result_corrected.delete("1.0", "end")
        if result.status == "done":
            self._result_raw.configure(text_color=TEXT_PRIMARY)
            self._result_corrected.configure(text_color=TEXT_PRIMARY)
            
            # Nếu có raw_text (chạy qua worker), hiển thị riêng
            if hasattr(result, 'raw_text') and result.raw_text:
                self._result_raw.insert("1.0", result.raw_text)
            else:
                self._result_raw.insert("1.0", result.text)
                
            self._result_corrected.insert("1.0", result.text)
        else:
            self._result_raw.configure(text_color=ERROR)
            self._result_corrected.configure(text_color=ERROR)
            self._result_raw.insert("1.0", f"[LỖI] {result.error}")
            self._result_corrected.insert("1.0", f"[LỖI] {result.error}")

    def _copy_result(self):
        text = self._result_corrected.get("1.0", "end").strip()
        if not text:
            text = self._result_raw.get("1.0", "end").strip()
        if text:
            self.clipboard_clear()
            self.clipboard_append(text)
            messagebox.showinfo("✅ Đã copy",
                                "Kết quả đã được sao chép vào clipboard.")

    def _save_result(self):
        text = self._result_corrected.get("1.0", "end").strip()
        if not text:
            text = self._result_raw.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("Trống", "Không có kết quả để lưu.")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text file", "*.txt"), ("All files", "*.*")])
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            messagebox.showinfo("✅ Đã lưu", f"Đã lưu tại:\n{path}")

    def _save_all_results(self):
        done = [r for r in self._results if r.status == "done"]
        if not done:
            messagebox.showwarning("Trống", "Chưa có kết quả nào.")
            return
        folder = filedialog.askdirectory(
            title="Chọn thư mục để lưu tất cả kết quả")
        if not folder:
            return
        count = 0
        for result in done:
            stem = Path(result.file_path).stem
            out_path = os.path.join(folder, f"{stem}_ocr.txt")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(result.text)
            count += 1
        messagebox.showinfo("✅ Đã lưu",
                            f"Đã lưu {count} file vào:\n{folder}")

    # ── Utility ────────────────────────────────────────────────────────────────

    def _clear_log(self):
        self._log_text.configure(state="normal")
        self._log_text.delete("1.0", "end")
        self._log_text.configure(state="disabled")

    # ── Mode toggle (User / Admin) ─────────────────────────────────────────────

    def _toggle_mode(self):
        self._admin_mode = not self._admin_mode
        self._apply_mode()

    def _apply_mode(self):
        """Show/hide UI elements based on mode."""
        if self._admin_mode:
            # ── Admin Mode: hiện tất cả ──
            self._mode_btn.configure(text="👤 User", fg_color=ACCENT, text_color="white")
            self._engine_frame.grid()
            self._engine_divider.grid()
            self._model_status_frame.pack(anchor="w", pady=(4, 0))
            self._raw_label.grid()
            self._result_raw.grid()
            self._text_fr.grid_rowconfigure(1, weight=1)
            self._log_header.grid()
            self._log_text.grid()
            self._right_panel.grid_rowconfigure(4, weight=2)
            # Hiện tab bar
            try:
                self._tabview._segmented_button.grid()
            except Exception:
                pass
        else:
            # ── User Mode: ẩn những thứ phức tạp ──
            self._mode_btn.configure(text="🔧 Admin", fg_color="transparent", text_color=TEXT_DIM)
            self._engine_frame.grid_remove()
            self._engine_divider.grid_remove()
            self._model_status_frame.pack_forget()
            self._raw_label.grid_remove()
            self._result_raw.grid_remove()
            self._text_fr.grid_rowconfigure(1, weight=0)
            self._log_header.grid_remove()
            self._log_text.grid_remove()
            self._right_panel.grid_rowconfigure(4, weight=0)
            # Ẩn tab bar (chỉ giữ tab OCR)
            try:
                self._tabview._segmented_button.grid_remove()
                self._tabview.set("📄  OCR Scanner")
            except Exception:
                pass
