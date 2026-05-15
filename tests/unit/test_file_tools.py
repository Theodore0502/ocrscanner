import pytest\r
import re\r
from tools_ui.engine.numbering_engine import _extract_number\r
\r
def test_extract_number_basic():\r
    # Test number extraction logic from numbering tool\r
    assert _extract_number("file_01.txt") == 1\r
    assert _extract_number("report_2025.pdf") == 2025\r
\r
def test_extract_number_no_number():\r
    assert _extract_number("document.pdf") == 0\r
    assert _extract_number("scan_no_num.jpg") == 0\r
\r
def test_extract_number_multiple_numbers():\r
    # Should extract the first continuous number group\r
    assert _extract_number("doc_12_v2.pdf") == 12\r
    assert _extract_number("v3_final_99.png") == 3\r
