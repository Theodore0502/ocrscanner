"""
Engine: Rename files using regex — adapted from fix_filename.py & rename_pdf.py
"""
import re
from pathlib import Path
from typing import List, Tuple, Callable, Optional


def find_files_to_rename(
    directory: str,
    pattern: str,
    replacement: str,
    pdf_only: bool = True,
    recursive: bool = True,
    use_regex: bool = False,
) -> List[Tuple[Path, str, str]]:
    """
    Scan directory for files matching `pattern` and compute new names.
    Returns list of (file_path, old_name, new_name).
    If use_regex is False, performs simple text replacement.
    Raises ValueError if pattern is invalid regex.
    """
    directory = Path(directory)
    if not directory.exists():
        return []

    if use_regex:
        try:
            compiled = re.compile(pattern)
        except re.error as e:
            raise ValueError(f"Regex không hợp lệ: {e}")

    # Collect candidate files
    if recursive:
        all_files = [f for f in directory.rglob("*") if f.is_file()]
    else:
        all_files = [f for f in directory.iterdir() if f.is_file()]

    if pdf_only:
        all_files = [f for f in all_files if f.suffix.lower() == ".pdf"]

    results: List[Tuple[Path, str, str]] = []
    for file_path in sorted(all_files):
        old_name = file_path.name
        
        if use_regex:
            if compiled.search(old_name):
                new_name = compiled.sub(replacement, old_name)
                if new_name != old_name:
                    results.append((file_path, old_name, new_name))
        else:
            if pattern and pattern in old_name:
                new_name = old_name.replace(pattern, replacement)
                if new_name != old_name:
                    results.append((file_path, old_name, new_name))

    return results


def execute_rename(
    files_to_rename: List[Tuple[Path, str, str]],
    log_callback: Optional[Callable[[str], None]] = None,
) -> Tuple[int, int]:
    """
    Perform renames in-place.
    Returns (success_count, skip_count).
    """
    success = 0
    skipped = 0

    for file_path, old_name, new_name in files_to_rename:
        new_path = file_path.parent / new_name

        if new_path.exists():
            if log_callback:
                log_callback(f"⚠️  Bỏ qua (đã tồn tại): {old_name}")
            skipped += 1
            continue

        try:
            file_path.rename(new_path)
            if log_callback:
                log_callback(f"✅ {old_name}  →  {new_name}")
            success += 1
        except Exception as e:
            if log_callback:
                log_callback(f"❌ Lỗi khi đổi tên {old_name}: {e}")
            skipped += 1

    return success, skipped
