"""
Tab: ✂️ Tách PDF
Layout: left settings | right log + progress
"""
import queue
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk

from tools_ui.colors import *
from tools_ui.engine.split_engine import batch_split, find_pdfs, split_single_pdf


class TabSplitPDF(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color=BG_MAIN, corner_radius=0, **kwargs)
        self.pack(fill="both", expand=True)
        self._queue: queue.Queue = queue.Queue()
        self._stop_event = threading.Event()
        self._running = False
        self._build()
        self._pump()

    # ── Build ─────────────────────────────────────────────────────────────────

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
        ctk.CTkLabel(hdr, text="✂️  Tách PDF",
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
        btn_frame = ctk.CTkFrame(irow, fg_color="transparent")
        btn_frame.grid(row=0, column=1)
        ctk.CTkButton(btn_frame, text="File", width=40, height=30,
                      command=self._browse_file,
                      fg_color=ACCENT2, hover_color=ACCENT2_HOVER,
                      text_color="white", font=FONT_SMALL,
                      corner_radius=6).pack(side="left", padx=(0, 2))
        ctk.CTkButton(btn_frame, text="Folder", width=50, height=30,
                      command=self._browse_input_folder,
                      fg_color=ACCENT, hover_color=ACCENT_HOVER,
                      text_color="white", font=FONT_SMALL,
                      corner_radius=6).pack(side="left")

        # ── Output ──
        ctk.CTkLabel(body, text="📁 Thư mục output", font=FONT_LABEL,
                     text_color=TEXT_PRIMARY).grid(row=r, column=0, sticky="w"); r += 1
        orow = ctk.CTkFrame(body, fg_color="transparent")
        orow.grid(row=r, column=0, sticky="ew", pady=(0, 8)); r += 1
        orow.columnconfigure(0, weight=1)
        self._output_var = ctk.StringVar()
        ctk.CTkEntry(orow, textvariable=self._output_var,
                     placeholder_text="Chọn thư mục lưu kết quả...",
                     fg_color=BG_INPUT, border_color=BORDER,
                     text_color=TEXT_PRIMARY, font=FONT_SMALL, height=30
                     ).grid(row=0, column=0, sticky="ew", padx=(0, 4))
        ctk.CTkButton(orow, text="Browse", width=60, height=30,
                      command=self._browse_output,
                      fg_color=ACCENT2, hover_color=ACCENT2_HOVER,
                      text_color="white", font=FONT_SMALL,
                      corner_radius=6).grid(row=0, column=1)

        # ── Options ──
        ctk.CTkFrame(body, height=1, fg_color=DIVIDER).grid(
            row=r, column=0, sticky="ew", pady=(0, 8)); r += 1

        self._recursive_var = ctk.BooleanVar(value=True)
        self._preserve_var = ctk.BooleanVar(value=True)
        self._delete_var = ctk.BooleanVar(value=False)

        for text, var in [
            ("Tìm đệ quy trong thư mục con", self._recursive_var),
            ("Giữ cấu trúc thư mục gốc", self._preserve_var),
        ]:
            ctk.CTkCheckBox(body, text=text, variable=var, font=FONT_SMALL,
                            text_color=TEXT_SECONDARY, fg_color=ACCENT,
                            hover_color=ACCENT_HOVER, border_color=BORDER,
                            checkmark_color="white", width=14, height=14
                            ).grid(row=r, column=0, sticky="w", pady=2); r += 1

        # Delete source — warn with red color
        del_cb = ctk.CTkCheckBox(body, text="⚠️ Xóa file gốc sau khi tách",
                                  variable=self._delete_var, font=FONT_SMALL,
                                  text_color=ERROR, fg_color=ERROR,
                                  hover_color="#C0392B", border_color=BORDER,
                                  checkmark_color="white", width=14, height=14)
        del_cb.grid(row=r, column=0, sticky="w", pady=(2, 10)); r += 1

        ctk.CTkFrame(body, height=1, fg_color=DIVIDER).grid(
            row=r, column=0, sticky="ew", pady=(0, 10)); r += 1

        # Buttons
        self._run_btn = ctk.CTkButton(
            body, text="▶  Bắt đầu Tách PDF",
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

        # Header + progress
        hdr = ctk.CTkFrame(panel, fg_color=BG_HEADER, corner_radius=0, height=48)
        hdr.grid(row=0, column=0, sticky="ew")
        hdr.grid_propagate(False)
        hdr.grid_columnconfigure(1, weight=1)
        ctk.CTkLabel(hdr, text="📋  Nhật ký xử lý",
                     font=FONT_TITLE, text_color=TEXT_PRIMARY,
                     padx=16, pady=12).grid(row=0, column=0, sticky="w")

        prog_frame = ctk.CTkFrame(hdr, fg_color="transparent")
        prog_frame.grid(row=0, column=1, sticky="e", padx=12)
        self._prog_label = ctk.CTkLabel(prog_frame, text="0 / 0",
                                         font=FONT_UI, text_color=TEXT_DIM, width=60)
        self._prog_label.pack(side="left", padx=(0, 8))
        self._prog_bar = ctk.CTkProgressBar(prog_frame, width=200, height=10,
                                             progress_color=ACCENT, fg_color=DIVIDER,
                                             corner_radius=5)
        self._prog_bar.set(0)
        self._prog_bar.pack(side="left", padx=(0, 10))

        ctk.CTkButton(hdr, text="Xóa log", width=64, height=26,
                      command=self._clear_log,
                      fg_color="transparent", hover_color=BG_MAIN,
                      text_color=TEXT_DIM, font=FONT_SMALL,
                      corner_radius=5).grid(row=0, column=2, padx=10)

        # Stats bar
        stats = ctk.CTkFrame(panel, fg_color=BG_PANEL, corner_radius=0, height=32)
        stats.grid(row=1, column=0, sticky="ew")
        stats.grid_propagate(False)
        stats.grid_columnconfigure((0, 1, 2), weight=1)
        self._st_total = self._stat(stats, "Tổng", "—", 0)
        self._st_ok    = self._stat(stats, "Thành công", "—", 1)
        self._st_err   = self._stat(stats, "Lỗi", "—", 2)

        # Log
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

    # ── Browse ────────────────────────────────────────────────────────────────

    def _browse_file(self):
        p = filedialog.askopenfilename(title="Chọn file PDF",
                                       filetypes=[("PDF", "*.pdf"), ("All", "*.*")])
        if p:
            self._input_var.set(p)

    def _browse_input_folder(self):
        p = filedialog.askdirectory(title="Chọn thư mục chứa PDF")
        if p:
            self._input_var.set(p)

    def _browse_output(self):
        p = filedialog.askdirectory(title="Chọn thư mục output")
        if p:
            self._output_var.set(p)

    # ── Run / Stop ────────────────────────────────────────────────────────────

    def _start(self):
        inp = self._input_var.get().strip()
        out = self._output_var.get().strip()
        if not inp or not out:
            self._log_msg("⚠️  Vui lòng chọn input và output.")
            return
        if self._running:
            return
        self._running = True
        self._stop_event.clear()
        self._run_btn.configure(state="disabled")
        self._stop_btn.configure(state="normal")
        self._prog_bar.set(0)
        self._log_msg(f"🚀 Bắt đầu tách PDF...")
        threading.Thread(target=self._worker, args=(inp, out), daemon=True).start()

    def _stop(self):
        self._stop_event.set()
        self._stop_btn.configure(state="disabled")

    def _worker(self, inp, out):
        p = Path(inp)
        if p.is_file():
            ok = split_single_pdf(p, Path(out),
                                   log_callback=lambda m: self._queue.put(("log", m)))
            total, success = 1, int(ok)
        else:
            success, errors = batch_split(
                inp, out,
                recursive=self._recursive_var.get(),
                preserve_structure=self._preserve_var.get(),
                delete_source=self._delete_var.get(),
                log_callback=lambda m: self._queue.put(("log", m)),
                progress_callback=lambda d, t: self._queue.put(("prog", d, t)),
                stop_event=self._stop_event)
            total = success + errors
        self._queue.put(("done", total, success))

    # ── Queue pump ────────────────────────────────────────────────────────────

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
                    self._log_msg(f"\n✅ Hoàn thành — {success}/{total} file thành công.")
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
