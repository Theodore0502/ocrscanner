"""
Engine: Number files sequentially — adapted from pdf_number.py
"""
import shutil
from datetime import datetime
from pathlib import Path
from typing import Callable, List, Optional, Tuple


def get_files_sorted(
    directory: str,
    sort_by: str = "time",  # "time" | "name"
) -> List[Tuple[Path, object]]:
    """Return [(file_path, sort_key), ...] sorted by chosen criterion."""
    root = Path(directory)
    if not root.exists():
        return []

    files_info = []
    for item in root.iterdir():
        if item.is_file():
            key = item.stat().st_mtime if sort_by == "time" else item.name.lower()
            files_info.append((item, key))

    files_info.sort(key=lambda x: x[1])
    return files_info


def preview_numbering(
    files_info: List[Tuple[Path, object]],
    fmt: str = "02d",
) -> List[Tuple[str, str, str]]:
    """
    Compute (old_name, new_name, time_str) for each file.
    """
    results = []
    for i, (file_path, key) in enumerate(files_info, start=1):
        new_name = f"{i:{fmt}}.{file_path.name}"
        if isinstance(key, float):
            time_str = datetime.fromtimestamp(key).strftime("%Y-%m-%d %H:%M")
        else:
            time_str = "—"
        results.append((file_path.name, new_name, time_str))
    return results


def execute_numbering(
    files_info: List[Tuple[Path, object]],
    output_dir: str,
    fmt: str = "02d",
    log_callback: Optional[Callable[[str], None]] = None,
    progress_callback: Optional[Callable[[int, int], None]] = None,
) -> Tuple[int, int]:
    """Copy files to output_dir with numbered names. Returns (success, errors)."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    success = 0
    errors = 0

    for i, (file_path, _) in enumerate(files_info, start=1):
        new_name = f"{i:{fmt}}.{file_path.name}"
        dest = out / new_name
        try:
            shutil.copy2(file_path, dest)
            if log_callback:
                log_callback(f"✅ {new_name}")
            success += 1
        except Exception as e:
            if log_callback:
                log_callback(f"❌ {file_path.name}: {e}")
            errors += 1

        if progress_callback:
            progress_callback(i, len(files_info))

    return success, errors
