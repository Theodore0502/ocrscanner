"""
Tab: 🔢 Đánh Số File
Layout: left settings | right preview table + log
"""
import queue
import threading
import tkinter as tk
from tkinter import filedialog, ttk

import customtkinter as ctk

from tools_ui.colors import *
from tools_ui.engine.numbering_engine import (execute_numbering,
                                               get_files_sorted,
                                               preview_numbering)


def _apply_treeview_style():
    style = ttk.Style()
    try:
        style.theme_use("default")
    except Exception:
        pass
    style.configure("Pink.Treeview",
                    background=BG_MAIN, foreground=TEXT_PRIMARY,
                    rowheight=26, fieldbackground=BG_MAIN, borderwidth=0)
    style.configure("Pink.Treeview.Heading",
                    background=BG_HEADER, foreground=TEXT_PRIMARY,
                    font=("Segoe UI", 10, "bold"), relief="flat", padding=(8, 4))
    style.map("Pink.Treeview",
              background=[("selected", ACCENT_SOFT)],
              foreground=[("selected", TEXT_PRIMARY)])


class TabNumbering(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color=BG_MAIN, corner_radius=0, **kwargs)
        self.pack(fill="both", expand=True)
        self._queue: queue.Queue = queue.Queue()
        self._files_info: list = []
        _apply_treeview_style()
        self._build()
        self._pump()

    def _build(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._build_settings()
        self._build_results()

    def _build_settings(self):
        panel = ctk.CTkFrame(self, width=290, fg_color=BG_SIDEBAR, corner_radius=0)
        panel.grid(row=0, column=0, sticky="nsew")
        panel.grid_propagate(False)

        hdr = ctk.CTkFrame(panel, fg_color=BG_HEADER, corner_radius=0)
        hdr.grid(row=0, column=0, sticky="ew")
        ctk.CTkLabel(hdr, text="🔢  Đánh Số File",
                     font=FONT_TITLE, text_color=TEXT_PRIMARY,
                     padx=16, pady=10).pack(anchor="w")

        body = ctk.CTkFrame(panel, fg_color="transparent")
        body.grid(row=1, column=0, sticky="nsew", padx=14, pady=8)
        body.columnconfigure(0, weight=1)
        r = 0

        # ── Input folder ──
        ctk.CTkLabel(body, text="📂 Thư mục nguồn", font=FONT_LABEL,
                     text_color=TEXT_PRIMARY).grid(row=r, column=0, sticky="w"); r += 1
        irow = ctk.CTkFrame(body, fg_color="transparent")
        irow.grid(row=r, column=0, sticky="ew", pady=(0, 8)); r += 1
        irow.columnconfigure(0, weight=1)
        self._input_var = ctk.StringVar()
        ctk.CTkEntry(irow, textvariable=self._input_var,
                     placeholder_text="Chọn thư mục...",
                     fg_color=BG_INPUT, border_color=BORDER,
                     text_color=TEXT_PRIMARY, font=FONT_SMALL, height=30
                     ).grid(row=0, column=0, sticky="ew", padx=(0, 4))
        ctk.CTkButton(irow, text="Browse", width=60, height=30,
                      command=self._browse_input,
                      fg_color=ACCENT2, hover_color=ACCENT2_HOVER,
                      text_color="white", font=FONT_SMALL, corner_radius=6
                      ).grid(row=0, column=1)

        # ── Output folder ──
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
                      text_color="white", font=FONT_SMALL, corner_radius=6
                      ).grid(row=0, column=1)

        # ── Sort mode ──
        ctk.CTkFrame(body, height=1, fg_color=DIVIDER).grid(
            row=r, column=0, sticky="ew", pady=(0, 8)); r += 1
        ctk.CTkLabel(body, text="Sắp xếp theo", font=FONT_LABEL,
                     text_color=TEXT_PRIMARY).grid(row=r, column=0, sticky="w"); r += 1
        self._sort_var = ctk.StringVar(value="time")
        for label, val in [("⏰ Thời gian tạo/sửa", "time"),
                            ("🔤 Tên file (A → Z)", "name")]:
            ctk.CTkRadioButton(body, text=label, variable=self._sort_var, value=val,
                               font=FONT_SMALL, text_color=TEXT_SECONDARY,
                               fg_color=ACCENT, hover_color=ACCENT_HOVER,
                               radiobutton_width=14, radiobutton_height=14
                               ).grid(row=r, column=0, sticky="w", pady=2); r += 1

        # ── Number format ──
        ctk.CTkFrame(body, height=1, fg_color=DIVIDER).grid(
            row=r, column=0, sticky="ew", pady=(8, 8)); r += 1
        ctk.CTkLabel(body, text="Định dạng số (VD: 02d → 01, 02...)",
                     font=FONT_SMALL, text_color=TEXT_DIM,
                     wraplength=240).grid(row=r, column=0, sticky="w"); r += 1
        self._fmt_var = ctk.StringVar(value="02d")
        ctk.CTkEntry(body, textvariable=self._fmt_var,
                     fg_color=BG_INPUT, border_color=BORDER,
                     text_color=TEXT_PRIMARY, font=FONT_MONO, height=30,
                     width=100).grid(row=r, column=0, sticky="w", pady=(2, 10)); r += 1

        # ── Buttons ──
        ctk.CTkButton(body, text="🔍  Xem trước",
                      command=self._preview,
                      fg_color=BG_MAIN, hover_color=BG_HEADER,
                      text_color=ACCENT, border_width=1, border_color=ACCENT,
                      font=FONT_UI, height=34, corner_radius=8
                      ).grid(row=r, column=0, sticky="ew", pady=(0, 6)); r += 1

        self._exec_btn = ctk.CTkButton(
            body, text="✅  Thực hiện đánh số",
            command=self._execute,
            fg_color=ACCENT, hover_color=ACCENT_HOVER,
            text_color="white", font=FONT_UI, height=34, corner_radius=8,
            state="disabled")
        self._exec_btn.grid(row=r, column=0, sticky="ew"); r += 1

    def _build_results(self):
        panel = ctk.CTkFrame(self, fg_color=BG_MAIN, corner_radius=0)
        panel.grid(row=0, column=1, sticky="nsew")
        panel.grid_rowconfigure(1, weight=3)
        panel.grid_rowconfigure(3, weight=1)
        panel.grid_columnconfigure(0, weight=1)

        # Table header
        thdr = ctk.CTkFrame(panel, fg_color=BG_HEADER, corner_radius=0, height=42)
        thdr.grid(row=0, column=0, sticky="ew")
        thdr.grid_propagate(False)
        ctk.CTkLabel(thdr, text="📋  Xem trước thứ tự",
                     font=FONT_TITLE, text_color=TEXT_PRIMARY,
                     padx=16, pady=10).pack(side="left")
        self._count_label = ctk.CTkLabel(thdr, text="",
                                          font=FONT_SMALL, text_color=TEXT_DIM, padx=16)
        self._count_label.pack(side="right")

        # Treeview
        tf = tk.Frame(panel, bg=BG_MAIN)
        tf.grid(row=1, column=0, sticky="nsew")
        tf.rowconfigure(0, weight=1)
        tf.columnconfigure(0, weight=1)

        self._tree = ttk.Treeview(tf, style="Pink.Treeview",
                                   columns=("new", "old", "time"),
                                   show="headings", selectmode="browse")
        self._tree.heading("new",  text="Tên mới")
        self._tree.heading("old",  text="Tên cũ")
        self._tree.heading("time", text="Thời gian sửa")
        self._tree.column("new",  width=220, anchor="w")
        self._tree.column("old",  width=220, anchor="w")
        self._tree.column("time", width=140, anchor="center")
        self._tree.tag_configure("odd",  background=BG_MAIN)
        self._tree.tag_configure("even", background=BG_SIDEBAR)

        vsb = ttk.Scrollbar(tf, orient="vertical", command=self._tree.yview)
        self._tree.configure(yscrollcommand=vsb.set)
        self._tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

        # Log header
        lhdr = ctk.CTkFrame(panel, fg_color=BG_HEADER, corner_radius=0, height=34)
        lhdr.grid(row=2, column=0, sticky="ew")
        lhdr.grid_propagate(False)
        ctk.CTkLabel(lhdr, text="📋  Nhật ký",
                     font=FONT_LABEL, text_color=TEXT_PRIMARY,
                     padx=16, pady=8).pack(side="left")
        ctk.CTkButton(lhdr, text="Xóa log", width=64, height=22,
                      command=self._clear_log,
                      fg_color="transparent", hover_color=BG_MAIN,
                      text_color=TEXT_DIM, font=FONT_SMALL,
                      corner_radius=5).pack(side="right", padx=8)

        self._log = ctk.CTkTextbox(panel, font=FONT_MONO, fg_color=BG_LOG,
                                    text_color=TEXT_SECONDARY, corner_radius=0,
                                    wrap="word", state="disabled")
        self._log.grid(row=3, column=0, sticky="nsew")

    # ── Actions ──────────────────────────────────────────────────────────────

    def _browse_input(self):
        p = filedialog.askdirectory(title="Chọn thư mục nguồn")
        if p:
            self._input_var.set(p)
            self._preview()

    def _browse_output(self):
        p = filedialog.askdirectory(title="Chọn thư mục output")
        if p:
            self._output_var.set(p)

    def _preview(self):
        inp = self._input_var.get().strip()
        if not inp:
            self._log_msg("⚠️  Vui lòng chọn thư mục nguồn.")
            return
        self._files_info = get_files_sorted(inp, sort_by=self._sort_var.get())
        previews = preview_numbering(self._files_info, fmt=self._fmt_var.get())
        self._populate_tree(previews)
        self._exec_btn.configure(state="normal" if self._files_info else "disabled")
        self._log_msg(f"✅ Xem trước {len(previews)} file.")

    def _populate_tree(self, previews):
        for item in self._tree.get_children():
            self._tree.delete(item)
        for i, (old, new, ts) in enumerate(previews):
            tag = "even" if i % 2 == 0 else "odd"
            self._tree.insert("", "end", values=(new, old, ts), tags=(tag,))
        self._count_label.configure(text=f"{len(previews)} file")

    def _execute(self):
        out = self._output_var.get().strip()
        if not out:
            self._log_msg("⚠️  Vui lòng chọn thư mục output.")
            return
        if not self._files_info:
            return
        self._exec_btn.configure(state="disabled")
        self._log_msg(f"🚀 Đang đánh số {len(self._files_info)} file...")
        threading.Thread(target=self._execute_worker, args=(out,), daemon=True).start()

    def _execute_worker(self, out):
        success, errors = execute_numbering(
            self._files_info,
            output_dir=out,
            fmt=self._fmt_var.get(),
            log_callback=lambda m: self._queue.put(("log", m)))
        self._queue.put(("done", success, errors))

    # ── Queue pump ────────────────────────────────────────────────────────────

    def _pump(self):
        try:
            while True:
                msg = self._queue.get_nowait()
                k = msg[0]
                if k == "log":
                    self._log_msg(msg[1])
                elif k == "done":
                    s, e = msg[1], msg[2]
                    self._exec_btn.configure(state="normal")
                    self._log_msg(f"\n✅ Hoàn thành — {s} file thành công, {e} lỗi.")
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
