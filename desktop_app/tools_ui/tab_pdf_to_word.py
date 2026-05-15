"""
Tab: 🔄 PDF → Word
Layout: left settings | right log + progress
"""
import queue
import threading
from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk

from tools_ui.colors import *
from tools_ui.engine.convert_engine import batch_convert, find_pdfs


class TabPDFToWord(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color=BG_MAIN, corner_radius=0, **kwargs)
        self.pack(fill="both", expand=True)
        self._queue: queue.Queue = queue.Queue()
        self._stop_event = threading.Event()
        self._running = False
        self._build()
        self._pump()

    def _build(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._build_settings()
        self._build_right()

    def _build_settings(self):
        panel = ctk.CTkFrame(self, width=290, fg_color=BG_SIDEBAR, corner_radius=0)
        panel.grid(row=0, column=0, sticky="nsew")
        panel.grid_propagate(False)

        hdr = ctk.CTkFrame(panel, fg_color=BG_HEADER, corner_radius=0)
        hdr.grid(row=0, column=0, sticky="ew")
        ctk.CTkLabel(hdr, text="🔄  PDF → Word",
                     font=FONT_TITLE, text_color=TEXT_PRIMARY,
                     padx=16, pady=10).pack(anchor="w")

        body = ctk.CTkFrame(panel, fg_color="transparent")
        body.grid(row=1, column=0, sticky="nsew", padx=14, pady=8)
        body.columnconfigure(0, weight=1)
        r = 0

        # ── Input ──
        ctk.CTkLabel(body, text="📂 Input (file hoặc thư mục)", font=FONT_LABEL,
                     text_color=TEXT_PRIMARY).grid(row=r, column=0, sticky="w"); r += 1
        irow = ctk.CTkFrame(body, fg_color="transparent")
        irow.grid(row=r, column=0, sticky="ew", pady=(0, 8)); r += 1
        irow.columnconfigure(0, weight=1)
        self._input_var = ctk.StringVar()
        ctk.CTkEntry(irow, textvariable=self._input_var,
                     placeholder_text="Chọn file PDF hoặc thư mục...",
                     fg_color=BG_INPUT, border_color=BORDER,
                     text_color=TEXT_PRIMARY, font=FONT_SMALL, height=30
                     ).grid(row=0, column=0, sticky="ew", padx=(0, 4))
        brow = ctk.CTkFrame(irow, fg_color="transparent")
        brow.grid(row=0, column=1)
        ctk.CTkButton(brow, text="File", width=40, height=30,
                      command=self._browse_file,
                      fg_color=ACCENT2, hover_color=ACCENT2_HOVER,
                      text_color="white", font=FONT_SMALL, corner_radius=6
                      ).pack(side="left", padx=(0, 2))
        ctk.CTkButton(brow, text="Folder", width=50, height=30,
                      command=self._browse_folder,
                      fg_color=ACCENT, hover_color=ACCENT_HOVER,
                      text_color="white", font=FONT_SMALL, corner_radius=6
                      ).pack(side="left")

        # ── Output ──
        ctk.CTkLabel(body, text="📁 Thư mục output", font=FONT_LABEL,
                     text_color=TEXT_PRIMARY).grid(row=r, column=0, sticky="w"); r += 1
        orow = ctk.CTkFrame(body, fg_color="transparent")
        orow.grid(row=r, column=0, sticky="ew", pady=(0, 8)); r += 1
        orow.columnconfigure(0, weight=1)
        self._output_var = ctk.StringVar()
        ctk.CTkEntry(orow, textvariable=self._output_var,
                     placeholder_text="Để trống = cùng thư mục với PDF",
                     fg_color=BG_INPUT, border_color=BORDER,
                     text_color=TEXT_PRIMARY, font=FONT_SMALL, height=30
                     ).grid(row=0, column=0, sticky="ew", padx=(0, 4))
        ctk.CTkButton(orow, text="Browse", width=60, height=30,
                      command=self._browse_output,
                      fg_color=ACCENT2, hover_color=ACCENT2_HOVER,
                      text_color="white", font=FONT_SMALL, corner_radius=6
                      ).grid(row=0, column=1)

        # ── Info note ──
        ctk.CTkFrame(body, height=1, fg_color=DIVIDER).grid(
            row=r, column=0, sticky="ew", pady=(4, 8)); r += 1
        ctk.CTkLabel(body, text="ℹ️  Yêu cầu: pip install pdf2docx",
                     font=FONT_SMALL, text_color=TEXT_DIM,
                     wraplength=240).grid(row=r, column=0, sticky="w", pady=(0, 10)); r += 1

        # ── File count badge ──
        self._count_label = ctk.CTkLabel(body, text="",
                                          font=FONT_SMALL, text_color=TEXT_DIM)
        self._count_label.grid(row=r, column=0, sticky="w", pady=(0, 8)); r += 1

        # ── Scan button ──
        ctk.CTkButton(body, text="📊  Quét số file PDF",
                      command=self._scan,
                      fg_color=BG_MAIN, hover_color=BG_HEADER,
                      text_color=ACCENT, border_width=1, border_color=ACCENT,
                      font=FONT_UI, height=32, corner_radius=8
                      ).grid(row=r, column=0, sticky="ew", pady=(0, 6)); r += 1

        # ── Run / Stop ──
        self._run_btn = ctk.CTkButton(
            body, text="▶  Bắt đầu Chuyển đổi",
            command=self._start,
            fg_color=SUCCESS, hover_color=SUCCESS_HOVER,
            text_color="white", font=FONT_UI, height=38, corner_radius=8)
        self._run_btn.grid(row=r, column=0, sticky="ew", pady=(0, 6)); r += 1

        self._stop_btn = ctk.CTkButton(
            body, text="⏹  Dừng", command=self._stop,
            fg_color="#FFCDD2", hover_color="#EF9A9A",
            text_color=ERROR, font=FONT_UI, height=30,
            corner_radius=8, state="disabled")
        self._stop_btn.grid(row=r, column=0, sticky="ew"); r += 1

    def _build_right(self):
        panel = ctk.CTkFrame(self, fg_color=BG_MAIN, corner_radius=0)
        panel.grid(row=0, column=1, sticky="nsew")
        panel.grid_rowconfigure(2, weight=1)
        panel.grid_columnconfigure(0, weight=1)

        hdr = ctk.CTkFrame(panel, fg_color=BG_HEADER, corner_radius=0, height=48)
        hdr.grid(row=0, column=0, sticky="ew")
        hdr.grid_propagate(False)
        hdr.grid_columnconfigure(1, weight=1)
        ctk.CTkLabel(hdr, text="📋  Nhật ký chuyển đổi",
                     font=FONT_TITLE, text_color=TEXT_PRIMARY,
                     padx=16, pady=12).grid(row=0, column=0, sticky="w")
        prog_f = ctk.CTkFrame(hdr, fg_color="transparent")
        prog_f.grid(row=0, column=1, sticky="e", padx=12)
        self._prog_label = ctk.CTkLabel(prog_f, text="0 / 0",
                                         font=FONT_UI, text_color=TEXT_DIM, width=60)
        self._prog_label.pack(side="left", padx=(0, 8))
        self._prog_bar = ctk.CTkProgressBar(prog_f, width=200, height=10,
                                             progress_color=ACCENT, fg_color=DIVIDER,
                                             corner_radius=5)
        self._prog_bar.set(0)
        self._prog_bar.pack(side="left")
        ctk.CTkButton(hdr, text="Xóa log", width=64, height=26,
                      command=self._clear_log,
                      fg_color="transparent", hover_color=BG_MAIN,
                      text_color=TEXT_DIM, font=FONT_SMALL,
                      corner_radius=5).grid(row=0, column=2, padx=10)

        stats = ctk.CTkFrame(panel, fg_color=BG_PANEL, corner_radius=0, height=32)
        stats.grid(row=1, column=0, sticky="ew")
        stats.grid_propagate(False)
        stats.grid_columnconfigure((0, 1, 2), weight=1)
        self._st_total = self._stat(stats, "Tổng", "—", 0)
        self._st_ok    = self._stat(stats, "Thành công", "—", 1)
        self._st_err   = self._stat(stats, "Lỗi", "—", 2)

        self._log = ctk.CTkTextbox(panel, font=FONT_MONO, fg_color=BG_LOG,
                                    text_color=TEXT_SECONDARY, corner_radius=0,
                                    wrap="word", state="disabled")
        self._log.grid(row=2, column=0, sticky="nsew")

    def _stat(self, parent, title, val, col):
        f = ctk.CTkFrame(parent, fg_color="transparent")
        f.grid(row=0, column=col, padx=8, pady=4, sticky="ew")
        ctk.CTkLabel(f, text=title, font=FONT_SMALL, text_color=TEXT_DIM).pack(side="left", padx=(0, 4))
        lbl = ctk.CTkLabel(f, text=val, font=("Segoe UI", 10, "bold"), text_color=TEXT_PRIMARY)
        lbl.pack(side="left")
        return lbl

    # ── Browse ─────────────────────────────────────────────────────────────────

    def _browse_file(self):
        p = filedialog.askopenfilename(title="Chọn file PDF",
                                       filetypes=[("PDF", "*.pdf"), ("All", "*.*")])
        if p:
            self._input_var.set(p)
            self._scan()

    def _browse_folder(self):
        p = filedialog.askdirectory(title="Chọn thư mục chứa PDF")
        if p:
            self._input_var.set(p)
            self._scan()

    def _browse_output(self):
        p = filedialog.askdirectory(title="Chọn thư mục output")
        if p:
            self._output_var.set(p)

    def _scan(self):
        inp = self._input_var.get().strip()
        if not inp:
            return
        pdfs = find_pdfs(inp)
        self._count_label.configure(
            text=f"📄 Tìm thấy {len(pdfs)} file PDF",
            text_color=ACCENT if pdfs else TEXT_DIM)

    # ── Run / Stop ─────────────────────────────────────────────────────────────

    def _start(self):
        inp = self._input_var.get().strip()
        if not inp:
            self._log_msg("⚠️  Vui lòng chọn input.")
            return
        if self._running:
            return
        out = self._output_var.get().strip() or None
        self._running = True
        self._stop_event.clear()
        self._run_btn.configure(state="disabled")
        self._stop_btn.configure(state="normal")
        self._prog_bar.set(0)
        self._log_msg("🚀 Bắt đầu chuyển đổi PDF → Word...")
        threading.Thread(target=self._worker, args=(inp, out), daemon=True).start()

    def _stop(self):
        self._stop_event.set()
        self._stop_btn.configure(state="disabled")

    def _worker(self, inp, out):
        success, errors = batch_convert(
            inp, out,
            log_callback=lambda m: self._queue.put(("log", m)),
            progress_callback=lambda d, t: self._queue.put(("prog", d, t)),
            stop_event=self._stop_event)
        self._queue.put(("done", success + errors, success))

    # ── Queue pump ─────────────────────────────────────────────────────────────

    def _pump(self):
        try:
            while True:
                msg = self._queue.get_nowait()
                k = msg[0]
                if k == "log":
                    self._log_msg(msg[1])
                elif k == "prog":
                    done, total = msg[1], msg[2]
                    self._prog_bar.set(done / total if total else 0)
                    self._prog_label.configure(text=f"{done} / {total}")
                elif k == "done":
                    total, success = msg[1], msg[2]
                    self._running = False
                    self._run_btn.configure(state="normal")
                    self._stop_btn.configure(state="disabled")
                    self._prog_bar.set(1.0)
                    self._st_total.configure(text=str(total))
                    self._st_ok.configure(text=str(success), text_color=SUCCESS)
                    self._st_err.configure(text=str(total - success),
                                           text_color=ERROR if total - success else TEXT_DIM)
                    self._log_msg(f"\n✅ Hoàn thành — {success}/{total} file.")
        except queue.Empty:
            pass
        self.after(60, self._pump)

    def _log_msg(self, msg):
        self._log.configure(state="normal")
        self._log.insert("end", msg + "\n")
        self._log.see("end")
        self._log.configure(state="disabled")

    def _clear_log(self):
        self._log.configure(state="normal")
        self._log.delete("1.0", "end")
        self._log.configure(state="disabled")
