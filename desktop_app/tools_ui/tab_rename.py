"""
Tab: ✏️ Đổi Tên File
Layout: left settings panel | right results table + log
"""
import queue
import threading
import tkinter as tk
from tkinter import filedialog, ttk

import customtkinter as ctk

from tools_ui.colors import *
from tools_ui.engine.rename_engine import execute_rename, find_files_to_rename


def _apply_treeview_style():
    style = ttk.Style()
    try:
        style.theme_use("default")
    except Exception:
        pass
    style.configure("Pink.Treeview",
                    background=BG_MAIN, foreground=TEXT_PRIMARY,
                    rowheight=26, fieldbackground=BG_MAIN,
                    borderwidth=0)
    style.configure("Pink.Treeview.Heading",
                    background=BG_HEADER, foreground=TEXT_PRIMARY,
                    font=("Segoe UI", 10, "bold"), relief="flat", padding=(8, 4))
    style.map("Pink.Treeview",
              background=[("selected", ACCENT_SOFT)],
              foreground=[("selected", TEXT_PRIMARY)])
    style.map("Pink.Treeview.Heading",
              background=[("active", BG_HEADER)])


class TabRename(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color=BG_MAIN, corner_radius=0, **kwargs)
        self.pack(fill="both", expand=True)
        self._queue: queue.Queue = queue.Queue()
        self._pending: list = []          # [(Path, old, new)]
        self._stop_event = threading.Event()
        _apply_treeview_style()
        self._build()
        self._pump()

    # ── Build UI ──────────────────────────────────────────────────────────────

    def _build(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._build_settings()
        self._build_results()

    # ── Left: settings panel ──────────────────────────────────────────────────

    def _build_settings(self):
        panel = ctk.CTkFrame(self, width=290, fg_color=BG_SIDEBAR, corner_radius=0)
        panel.grid(row=0, column=0, sticky="nsew")
        panel.grid_propagate(False)
        panel.grid_rowconfigure(99, weight=1)

        # Header
        hdr = ctk.CTkFrame(panel, fg_color=BG_HEADER, corner_radius=0)
        hdr.grid(row=0, column=0, sticky="ew")
        ctk.CTkLabel(hdr, text="✏️  Đổi Tên File",
                     font=FONT_TITLE, text_color=TEXT_PRIMARY,
                     padx=16, pady=10).pack(anchor="w")

        body = ctk.CTkFrame(panel, fg_color="transparent")
        body.grid(row=1, column=0, sticky="nsew", padx=14, pady=8)
        body.columnconfigure(0, weight=1)
        r = 0

        # ── Folder ──
        ctk.CTkLabel(body, text="📂 Thư mục nguồn", font=FONT_LABEL,
                     text_color=TEXT_PRIMARY).grid(row=r, column=0, sticky="w"); r += 1
        frow = ctk.CTkFrame(body, fg_color="transparent")
        frow.grid(row=r, column=0, sticky="ew", pady=(0, 8)); r += 1
        frow.columnconfigure(0, weight=1)
        self._folder_var = ctk.StringVar()
        ctk.CTkEntry(frow, textvariable=self._folder_var,
                     placeholder_text="Chọn thư mục...",
                     fg_color=BG_INPUT, border_color=BORDER,
                     text_color=TEXT_PRIMARY, font=FONT_SMALL,
                     height=30).grid(row=0, column=0, sticky="ew", padx=(0, 4))
        ctk.CTkButton(frow, text="Browse", width=60, height=30,
                      command=self._browse_folder,
                      fg_color=ACCENT2, hover_color=ACCENT2_HOVER,
                      text_color="white", font=FONT_SMALL,
                      corner_radius=6).grid(row=0, column=1)

        # ── Pattern ──
        ctk.CTkLabel(body, text="🔍 Tìm văn bản", font=FONT_LABEL,
                     text_color=TEXT_PRIMARY).grid(row=r, column=0, sticky="w"); r += 1
        self._pattern_var = ctk.StringVar(value="văn_bản_cũ")
        ctk.CTkEntry(body, textvariable=self._pattern_var,
                     fg_color=BG_INPUT, border_color=BORDER,
                     text_color=TEXT_PRIMARY, font=FONT_MONO,
                     height=30).grid(row=r, column=0, sticky="ew", pady=(0, 8)); r += 1

        # ── Replacement ──
        ctk.CTkLabel(body, text="🔁 Thay thế bằng", font=FONT_LABEL,
                     text_color=TEXT_PRIMARY).grid(row=r, column=0, sticky="w"); r += 1
        self._replace_var = ctk.StringVar(value="văn_bản_mới")
        ctk.CTkEntry(body, textvariable=self._replace_var,
                     fg_color=BG_INPUT, border_color=BORDER,
                     text_color=TEXT_PRIMARY, font=FONT_MONO,
                     height=30).grid(row=r, column=0, sticky="ew", pady=(0, 8)); r += 1

        # ── Options ──
        self._pdf_only_var = ctk.BooleanVar(value=True)
        self._recursive_var = ctk.BooleanVar(value=True)
        self._regex_mode_var = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(body, text="Chỉ file PDF",
                        variable=self._pdf_only_var, font=FONT_SMALL,
                        text_color=TEXT_SECONDARY, fg_color=ACCENT,
                        hover_color=ACCENT_HOVER, border_color=BORDER,
                        checkmark_color="white", width=14, height=14
                        ).grid(row=r, column=0, sticky="w", pady=2); r += 1
        ctk.CTkCheckBox(body, text="Tìm trong thư mục con",
                        variable=self._recursive_var, font=FONT_SMALL,
                        text_color=TEXT_SECONDARY, fg_color=ACCENT,
                        hover_color=ACCENT_HOVER, border_color=BORDER,
                        checkmark_color="white", width=14, height=14
                        ).grid(row=r, column=0, sticky="w", pady=(2, 2)); r += 1
        ctk.CTkCheckBox(body, text="Sử dụng Regex (Nâng cao)",
                        variable=self._regex_mode_var, font=FONT_SMALL,
                        text_color=TEXT_SECONDARY, fg_color=ACCENT,
                        hover_color=ACCENT_HOVER, border_color=BORDER,
                        checkmark_color="white", width=14, height=14
                        ).grid(row=r, column=0, sticky="w", pady=(2, 10)); r += 1

        # ── Divider ──
        ctk.CTkFrame(body, height=1, fg_color=DIVIDER).grid(
            row=r, column=0, sticky="ew", pady=(0, 10)); r += 1

        # ── Status badge ──
        self._status_label = ctk.CTkLabel(
            body, text="—  file sẽ đổi tên",
            font=FONT_SMALL, text_color=TEXT_DIM)
        self._status_label.grid(row=r, column=0, sticky="w", pady=(0, 8)); r += 1

        # ── Buttons ──
        ctk.CTkButton(body, text="🔍  Xem trước (Dry Run)",
                      command=self._run_preview,
                      fg_color=BG_MAIN, hover_color=BG_HEADER,
                      text_color=ACCENT, border_width=1, border_color=ACCENT,
                      font=FONT_UI, height=34, corner_radius=8
                      ).grid(row=r, column=0, sticky="ew", pady=(0, 6)); r += 1

        self._exec_btn = ctk.CTkButton(
            body, text="✅  Thực hiện đổi tên",
            command=self._run_execute,
            fg_color=ACCENT, hover_color=ACCENT_HOVER,
            text_color="white", font=FONT_UI, height=34, corner_radius=8,
            state="disabled")
        self._exec_btn.grid(row=r, column=0, sticky="ew"); r += 1

    # ── Right: results panel ───────────────────────────────────────────────────

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
        ctk.CTkLabel(thdr, text="📋  Danh sách thay đổi",
                     font=FONT_TITLE, text_color=TEXT_PRIMARY,
                     padx=16, pady=10).pack(side="left")
        self._count_label = ctk.CTkLabel(thdr, text="",
                                          font=FONT_SMALL, text_color=TEXT_DIM,
                                          padx=16)
        self._count_label.pack(side="right")

        # Treeview table
        tree_frame = tk.Frame(panel, bg=BG_MAIN)
        tree_frame.grid(row=1, column=0, sticky="nsew")
        tree_frame.rowconfigure(0, weight=1)
        tree_frame.columnconfigure(0, weight=1)

        self._tree = ttk.Treeview(
            tree_frame, style="Pink.Treeview",
            columns=("stt", "old", "new"), show="headings",
            selectmode="browse")
        self._tree.heading("stt", text="#")
        self._tree.heading("old", text="Tên cũ")
        self._tree.heading("new", text="Tên mới")
        self._tree.column("stt", width=46, anchor="center", stretch=False)
        self._tree.column("old", width=280, anchor="w")
        self._tree.column("new", width=280, anchor="w")
        self._tree.tag_configure("odd",  background=BG_MAIN)
        self._tree.tag_configure("even", background=BG_SIDEBAR)
        self._tree.tag_configure("done", foreground=SUCCESS)
        self._tree.tag_configure("skip", foreground=WARNING)

        vsb = ttk.Scrollbar(tree_frame, orient="vertical",
                            command=self._tree.yview)
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

        # Log textbox
        self._log = ctk.CTkTextbox(panel, font=FONT_MONO, fg_color=BG_LOG,
                                    text_color=TEXT_SECONDARY, corner_radius=0,
                                    wrap="word", state="disabled")
        self._log.grid(row=3, column=0, sticky="nsew")

    # ── Actions ───────────────────────────────────────────────────────────────

    def _browse_folder(self):
        path = filedialog.askdirectory(title="Chọn thư mục")
        if path:
            self._folder_var.set(path)

    def _run_preview(self):
        folder = self._folder_var.get().strip()
        pattern = self._pattern_var.get().strip()
        replacement = self._replace_var.get()
        if not folder or not pattern:
            self._log_msg("⚠️  Vui lòng nhập thư mục và pattern.")
            return
        self._clear_tree()
        self._log_msg(f"🔍 Đang quét: {folder}")
        threading.Thread(target=self._preview_worker,
                         args=(folder, pattern, replacement),
                         daemon=True).start()

    def _preview_worker(self, folder, pattern, replacement):
        try:
            results = find_files_to_rename(
                folder, pattern, replacement,
                pdf_only=self._pdf_only_var.get(),
                recursive=self._recursive_var.get(),
                use_regex=self._regex_mode_var.get())
            self._queue.put(("preview_done", results))
        except ValueError as e:
            self._queue.put(("log", f"❌ {e}"))

    def _run_execute(self):
        if not self._pending:
            return
        self._exec_btn.configure(state="disabled")
        self._log_msg(f"🚀 Bắt đầu đổi tên {len(self._pending)} file...")
        threading.Thread(target=self._execute_worker, daemon=True).start()

    def _execute_worker(self):
        success, skipped = execute_rename(
            self._pending, log_callback=lambda m: self._queue.put(("log", m)))
        self._queue.put(("exec_done", (success, skipped)))

    # ── Queue pump ────────────────────────────────────────────────────────────

    def _pump(self):
        try:
            while True:
                msg = self._queue.get_nowait()
                kind = msg[0]
                if kind == "log":
                    self._log_msg(msg[1])
                elif kind == "preview_done":
                    self._on_preview_done(msg[1])
                elif kind == "exec_done":
                    s, sk = msg[1]
                    self._log_msg(f"\n✅ Hoàn thành — Đổi tên: {s}  |  Bỏ qua: {sk}")
                    self._pending.clear()
        except queue.Empty:
            pass
        self.after(60, self._pump)

    def _on_preview_done(self, results):
        self._pending = results
        self._clear_tree()
        for i, (path, old, new) in enumerate(results):
            tag = "even" if i % 2 == 0 else "odd"
            self._tree.insert("", "end", values=(i + 1, old, new), tags=(tag,))
        count = len(results)
        self._count_label.configure(text=f"{count} file")
        self._status_label.configure(
            text=f"{count}  file sẽ đổi tên",
            text_color=ACCENT if count else TEXT_DIM)
        self._exec_btn.configure(state="normal" if count else "disabled")
        self._log_msg(f"✅ Tìm thấy {count} file cần đổi tên.")

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _clear_tree(self):
        for item in self._tree.get_children():
            self._tree.delete(item)
        self._count_label.configure(text="")

    def _log_msg(self, msg: str):
        self._log.configure(state="normal")
        self._log.insert("end", msg + "\n")
        self._log.see("end")
        self._log.configure(state="disabled")

    def _clear_log(self):
        self._log.configure(state="normal")
        self._log.delete("1.0", "end")
        self._log.configure(state="disabled")
