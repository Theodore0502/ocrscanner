"""
Entry point — OCR Scanner Desktop App
"""
import sys
import os
import io
from pathlib import Path

# Fix Windows console encoding: cho phép print emoji/Unicode (PaddleOCR, DocTR dùng nhiều emoji)
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Ensure ocr_scanner is on path
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_OCR_ROOT = _PROJECT_ROOT / "ocr_scanner"
sys.path.insert(0, str(_OCR_ROOT))

from app import OCRScannerApp

if __name__ == "__main__":
    app = OCRScannerApp()
    app.mainloop()
