import pytest\r
from src.ocr.fast_spell_checker import SymSpellChecker\r
\r
@pytest.fixture(scope="module")\r
def symspell():\r
    checker = SymSpellChecker(max_edit_distance=2)\r
    # Manually load some words for testing to avoid loading full dict\r
    checker.word_frequency = {"xin": 100, "chào": 100, "sinh": 50, "viên": 50}\r
    checker._precompute_edit_distance()\r
    return checker\r
\r
def test_symspell_lookup(symspell):\r
    # Test dictionary exact match\r
    results = symspell.lookup("xin", max_edit_distance=0)\r
    assert len(results) > 0\r
    assert results[0].term == "xin"\r
\r
def test_symspell_correct_word(symspell):\r
    # "xjn" (typo) -> "xin" (dist=1)\r
    corrected = symspell.correct_word("xjn")\r
    assert corrected == "xin"\r
\r
def test_symspell_correct_text(symspell):\r
    # "xjn chào sjnh viên" -> "xin chào sinh viên"\r
    text = "xjn chào sjnh viên"\r
    corrected = symspell.correct_text(text)\r
    assert corrected == "xin chào sinh viên"\r
