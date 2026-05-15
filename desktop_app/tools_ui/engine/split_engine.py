"""
Engine: Split PDF into Part1/Part2 — adapted from split_pdf.py
"""
from pathlib import Path
from typing import Callable, List, Optional, Tuple


def find_pdfs(directory: str, recursive: bool = True) -> List[Path]:
    root = Path(directory)
    if not root.exists():
        return []
    if recursive:
        return sorted(f for f in root.rglob("*") if f.suffix.lower() == ".pdf")
    return sorted(f for f in root.iterdir() if f.is_file() and f.suffix.lower() == ".pdf")


def split_single_pdf(
    input_path: Path,
    output_dir: Path,
    preserve_structure: bool = True,
    input_root: Optional[Path] = None,
    delete_source: bool = False,
    log_callback: Optional[Callable[[str], None]] = None,
) -> bool:
    """Split a single PDF into _Part1 (page 1) and _Part2 (remaining pages)."""
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        try:
            from PyPDF2 import PdfReader, PdfWriter  # type: ignore
        except ImportError:
            if log_callback:
                log_callback("❌ Thiếu thư viện: pip install pypdf")
            return False

    try:
        reader = PdfReader(str(input_path))
        total_pages = len(reader.pages)
        base_name = input_path.stem

        # Determine output sub-folder
        if preserve_structure and input_root:
            try:
                rel = input_path.parent.relative_to(input_root)
                pdf_folder = output_dir / rel / base_name
            except ValueError:
                pdf_folder = output_dir / base_name
        else:
            pdf_folder = output_dir / base_name

        pdf_folder.mkdir(parents=True, exist_ok=True)

        # Write Part1 (page 1 only)
        w1 = PdfWriter()
        w1.add_page(reader.pages[0])
        p1 = pdf_folder / f"{base_name}_Part1.pdf"
        with open(p1, "wb") as f:
            w1.write(f)

        # Write Part2 (remaining pages, if any)
        if total_pages > 1:
            w2 = PdfWriter()
            for i in range(1, total_pages):
                w2.add_page(reader.pages[i])
            p2 = pdf_folder / f"{base_name}_Part2.pdf"
            with open(p2, "wb") as f:
                w2.write(f)
            msg = f"✅ {input_path.name}  →  Part1 + Part2 ({total_pages} trang)"
        else:
            msg = f"✅ {input_path.name}  →  Part1 (1 trang)"

        if log_callback:
            log_callback(msg)

        if delete_source:
            input_path.unlink(missing_ok=True)

        return True

    except Exception as e:
        if log_callback:
            log_callback(f"❌ {input_path.name}: {e}")
        return False


def batch_split(
    input_dir: str,
    output_dir: str,
    recursive: bool = True,
    preserve_structure: bool = True,
    delete_source: bool = False,
    log_callback: Optional[Callable[[str], None]] = None,
    progress_callback: Optional[Callable[[int, int], None]] = None,
    stop_event=None,
) -> Tuple[int, int]:
    """Split all PDFs in a directory. Returns (success, errors)."""
    pdfs = find_pdfs(input_dir, recursive)
    if not pdfs:
        if log_callback:
            log_callback("⚠️  Không tìm thấy file PDF nào.")
        return 0, 0

    input_root = Path(input_dir)
    out_root = Path(output_dir)
    success = 0
    errors = 0

    for i, pdf in enumerate(pdfs):
        if stop_event and stop_event.is_set():
            if log_callback:
                log_callback("⏹  Đã dừng.")
            break

        ok = split_single_pdf(
            pdf, out_root, preserve_structure, input_root,
            delete_source, log_callback
        )
        if ok:
            success += 1
        else:
            errors += 1

        if progress_callback:
            progress_callback(i + 1, len(pdfs))

    return success, errors
