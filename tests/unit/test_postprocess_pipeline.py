import pytest\r
from src.ocr.postprocess_pipeline import apply_rule_based_fixes\r
\r
def test_rule_based_fixes_basic():\r
    # Test space before punctuation\r
    assert apply_rule_based_fixes("hello , world") == "hello, world"\r
    assert apply_rule_based_fixes("test  . ") == "test."\r
\r
def test_rule_based_fixes_vietnamese_diacritics():\r
    # Test common diacritic issues defined in FIX_MAP\r
    # "ngưòi" -> "người"\r
    assert apply_rule_based_fixes("ngưòi") == "người"\r
    # "đưoc" -> "được"\r
    assert apply_rule_based_fixes("đưoc") == "được"\r
\r
def test_rule_based_fixes_line_continuation():\r
    # Test hyphenation at line breaks\r
    text = "sinh vi-\\nên"\r
    # Expected: "sinh viên"\r
    # Note: apply_rule_based_fixes replaces "-\\n" with ""\r
    assert apply_rule_based_fixes(text) == "sinh viên"\r
