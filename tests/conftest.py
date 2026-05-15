import sys\r
from pathlib import Path\r
import pytest\r
\r
# Ensure ocr_scanner and desktop_app are on path\r
_PROJECT_ROOT = Path(__file__).resolve().parent.parent\r
sys.path.insert(0, str(_PROJECT_ROOT / "ocr_scanner"))\r
sys.path.insert(0, str(_PROJECT_ROOT / "desktop_app"))\r
