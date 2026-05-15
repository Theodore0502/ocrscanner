"""
Engine: Convert PDF → DOCX — adapted from pdf_to_word.py
"""
from pathlib import Path
from typing import Callable, List, Optional, Tuple


def convert_single_pdf(
    pdf_path: Path,
    output_dir: Optional[Path] = None,
    log_callback: Optional[Callable[[str], None]] = None,
) -> Tuple[bool, str]:
    """Convert one PDF to DOCX. Returns (success, docx_path_or_error)."""
    try:
        from pdf2docx import Converter
    except ImportError:
        msg = "❌ Thiếu thư viện: pip install pdf2docx"
        if log_callback:
            log_callback(msg)
        return False, msg

    try:
        dest_dir = output_dir if output_dir else pdf_path.parent
        dest_dir.mkdir(parents=True, exist_ok=True)
        docx_path = dest_dir / (pdf_path.stem + ".docx")

        cv = Converter(str(pdf_path))
        cv.convert(str(docx_path), start=0, end=None)
        cv.close()

        if log_callback:
            log_callback(f"✅ {pdf_path.name}  →  {docx_path.name}")
        return True, str(docx_path)

    except Exception as e:
        msg = f"❌ {pdf_path.name}: {e}"
        if log_callback:
            log_callback(msg)
        return False, str(e)


def find_pdfs(path: str) -> List[Path]:
    p = Path(path)
    if p.is_file() and p.suffix.lower() == ".pdf":
        return [p]
    if p.is_dir():
        return sorted(f for f in p.rglob("*") if f.suffix.lower() == ".pdf")
    return []


def batch_convert(
    input_path: str,
    output_dir: Optional[str] = None,
    log_callback: Optional[Callable[[str], None]] = None,
    progress_callback: Optional[Callable[[int, int], None]] = None,
    stop_event=None,
) -> Tuple[int, int]:
    """Convert all PDFs in input_path. Returns (success, errors)."""
    pdfs = find_pdfs(input_path)
    if not pdfs:
        if log_callback:
            log_callback("⚠️  Không tìm thấy file PDF nào.")
        return 0, 0

    out = Path(output_dir) if output_dir else None
    success = 0
    errors = 0

    for i, pdf in enumerate(pdfs):
        if stop_event and stop_event.is_set():
            if log_callback:
                log_callback("⏹  Đã dừng.")
            break

        ok, _ = convert_single_pdf(pdf, out, log_callback)
        if ok:
            success += 1
        else:
            errors += 1

        if progress_callback:
            progress_callback(i + 1, len(pdfs))

    return success, errors
