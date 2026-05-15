"""
Vietnamese Post-Processing Pipeline
Tích hợp SymSpell spell checker + text cleaner vào một entry point duy nhất.

Dùng sau bất kỳ OCR engine nào để cải thiện chất lượng văn bản.
"""

import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent
_SPELL_CHECKER = None
_DICT_LOADED = False


def _get_spell_checker():
    """Lazy-load SymSpell checker với Vietnamese dictionary."""
    global _SPELL_CHECKER, _DICT_LOADED

    if _SPELL_CHECKER is not None:
        return _SPELL_CHECKER

    # Tìm đường dẫn dictionary
    dict_candidates = [
        _ROOT / "data" / "processed" / "vietnamese_words.txt",
        _ROOT / "ocr_scanner" / "data" / "processed" / "vietnamese_words.txt",
        Path(_ROOT).parent / "ocr_scanner" / "data" / "processed" / "vietnamese_words.txt",
    ]

    dict_path = None
    for p in dict_candidates:
        if p.exists():
            dict_path = str(p)
            break

    try:
        from src.ocr.fast_spell_checker import SymSpellChecker
        _SPELL_CHECKER = SymSpellChecker(
            dictionary_path=dict_path,
            max_edit_distance=1    # edit_distance=1 đủ để fix missing dấu thanh, tránh false positive
        )
        _DICT_LOADED = dict_path is not None
    except Exception as e:
        print(f"[PostProcess] Spell checker load failed: {e}")
        _SPELL_CHECKER = None

    return _SPELL_CHECKER


def apply_postprocess(text: str, use_spellcheck: bool = True) -> str:
    """
    Áp dụng post-processing pipeline lên text OCR.

    Pipeline:
    1. Sửa lỗi pattern thường gặp (header document, tiêu đề...)
    2. SymSpell spell check (từng âm tiết tiếng Việt)

    Args:
        text: Văn bản từ OCR engine
        use_spellcheck: Có chạy SymSpell không (mặc định True)

    Returns:
        Văn bản đã được cải thiện
    """
    if not text or not text.strip():
        return text

    # Bước 1: Fix pattern cố định
    result = _fix_common_patterns(text)

    # Bước 2: SymSpell word-level correction
    if use_spellcheck:
        result = _apply_symspell(result)

    return result


def _fix_common_patterns(text: str) -> str:
    """Fix các lỗi pattern hay gặp trong văn bản hành chính VN."""
    import re

    # Các từ viết tắt phổ biến bị OCR sai
    FIX_MAP = {
        # Header
        "B CÔNG THƯNG": "BỘ CÔNG THƯƠNG",
        "BOCÔNG THƯNG": "BỘ CÔNG THƯƠNG",
        "CNG HOÀ": "CỘNG HÒA",
        "CH NGHA VIT NAM": "CHỦ NGHĨA VIỆT NAM",
        "VIT NAM": "VIỆT NAM",
        "VIÊT NAM": "VIỆT NAM",
        "TRƯNG ĐI HC": "TRƯỜNG ĐẠI HỌC",
        "ĐIN LC": "ĐIỆN LỰC",
        "DAIHOD": "ĐẠI HỌC ĐIỆN LỰC",
        # Common words
        "Đc lp - T do - Hnh phc": "Độc lập - Tự do - Hạnh phúc",
        "hc k": "học kỳ",
        "năm hc": "năm học",
        "h so": "hồ sơ",
        "np h": "nộp hồ",
        "t ngày": "từ ngày",
        "đn ht": "đến hết",
        "min giảm": "miễn giảm",
        "h tr": "hỗ trợ",
        "kinh phí hc tp": "kinh phí học tập",
        "hc tp": "học tập",
        "sinh viên l ngưi": "sinh viên là người",
        "ngưi dân tc": "người dân tộc",
        "thiu s": "thiểu số",
        "cơ s giáo dc": "cơ sở giáo dục",
        "đi vi": "đối với",
        "đi hc": "đại học",
        "c s": "cơ sở",
        "Nơi nhn": "Nơi nhận",
        "TL HIU TRUÖNG": "TL. HIỆU TRƯỞNG",
        "HIU TRUÖNG": "HIỆU TRƯỞNG",
        "TRUÖNG PHÒNG": "TRƯỞNG PHÒNG",
        "Nơi nhận h so": "Nơi nhận hồ sơ",
        "triển khai thc hin": "triển khai thực hiện",
        "đưc tư vn": "được tư vấn",
        "np đầy đ": "nộp đầy đủ",
        "hướng dn": "hướng dẫn",
        "ph lc": "phụ lục",
        "Hn np": "Hạn nộp",
        "theo đúng thi gian": "theo đúng thời gian",
        "quy đnh": "quy định",
        # ── Bổ sung từ lỗi thực tế ───────────────────────────────────────
        # Địa danh
        "thành ph Hà Ni": "thành phố Hà Nội",
        "thành ph Hà Nội": "thành phố Hà Nội",
        "thành ph": "thành phố",
        "Hà Nôi": "Hà Nội",
        # Từ hay mất dấu — phổ biến trong văn bản hành chính
        "ca Chính ph": "của Chính phủ",
        "Chính ph": "Chính phủ",
        "giá dch v": "giá dịch vụ",
        "dch v": "dịch vụ",
        "co s giáo dục": "cơ sở giáo dục",
        "ơ s giáo dục": "cơ sở giáo dục",
        "co s": "cơ sở",
        "ngưi": "người",
        "ngày9": "ngày 9",
        "Sa đi": "Sửa đổi",
        "b sung": "bổ sung",
        "mt s": "một số",
        "mt số": "một số",
        "điu": "điều",
        "hc ti": "học tại",
        "hc tại": "học tại",
        "trong quá trình": "trong quá trình",
        # Từ bị drop âm tiết / ghép sai
        "quá trìnhỗ": "quá trình. Hỗ",      # merge 2 dòng
        "trìnhỗ trợin": "trình hỗ trợ triển", # merge 3 từ
        "nu gp": "nếu gặp",
        "nu gặp": "nếu gặp",
        "nếu gp": "nếu gặp",
        "gp vướng": "gặp vướng",
        "vướng mc": "vướng mắc",
        "Đ triển": "Để triển",
        "Để trin": "Để triển",
        "trin khai": "triển khai",
        "np đầy đủ h so": "nộp đầy đủ hồ sơ",
        "np đầy đ": "nộp đầy đủ",
        "np đầy đủ": "nộp đầy đủ",
        "np h sơ": "nộp hồ sơ",
        "t ngày": "từ ngày",
        "đn ht ngày": "đến hết ngày",
        "đn hết ngày": "đến hết ngày",
        "đến ht ngày": "đến hết ngày",
        # Người ký & chức vụ
        "Nguyn Th Mai Lý": "Nguyễn Thị Mai Lý",
        "Nguyn Thị Mai Lý": "Nguyễn Thị Mai Lý",
        "Nguyễn Th Mai Lý": "Nguyễn Thị Mai Lý",
        "Phùng Th Xuân Bình": "Phùng Thị Xuân Bình",
        "Phùng Thị Xuân Bình": "Phùng Thị Xuân Bình",
        # Ký hiệu số văn bản
        "Só:": "Số:",
        "Sô:": "Số:",
        "Sô ": "Số ",
        "Só ": "Số ",
        "TB-ĐHDL": "TB-ĐHDL",
        # Từ phổ biến bị mất dấu
        "nghiêm túc thc hin": "nghiêm túc thực hiện",
        "thc hin": "thực hiện",
        "liên h ": "liên hệ ",
        "liên hệ c": "liên hệ cô",
        "đưc tư vấn": "được tư vấn",
        "đưc tư vn": "được tư vấn",
        "đưc": "được",
        "vic xét": "việc xét",
        "Nhà trưng": "Nhà trường",
        "phổ bin": "phổ biến",
        "phổ biến đn": "phổ biến đến",
        "phổ biến đến": "phổ biến đến",
        "đn sinh": "đến sinh",
        "Nhn đưc": "Nhận được",
        "Nhận đưc": "Nhận được",
        "Cố vn": "Cố vấn",
        "cố vn": "cố vấn",
        "ph Xm": "phố Xốm",
        "ph Xốm": "phố Xốm",
        # Đơn vị thường gặp
        "Phòng CTSV": "Phòng Công tác Sinh viên",
        "Phòng Công tác SV": "Phòng Công tác Sinh viên",
        "đi vi sinh viên": "đối với sinh viên",
        "sinh viên l ngưi": "sinh viên là người",
        "khóa D20": "khóa D20",  # giữ nguyên
        "CBL các lp": "CBL các lớp",
        "CBL các l p": "CBL các lớp",
        "các lp": "các lớp",
        "các lớp": "các lớp",
    }

    result = text
    for wrong, correct in FIX_MAP.items():
        result = result.replace(wrong, correct)

    # Fix date patterns: "ngày9" → "ngày 9"
    result = re.sub(r'ngày(\d)', r'ngày \1', result)
    # Fix missing space after punctuation before uppercase
    result = re.sub(r'([.;:])([A-ZÀÁẢÃẠĂẮẰẲẴẶ])', r'\1 \2', result)

    # ── Fix lỗi PDF layout: "hỗ trợ" bị nhúng vào giữa từ ──────────────────
    # Dấu hiệu nhận biết: chữ thường LIỀN trước "hỗ trợ" (không có khoảng trắng)
    # Xóa "hỗ trợ" và thay bằng khoảng trắng để tách 2 phần ra
    result = re.sub(r'(?<=[a-zàáảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵ])hỗ trợ', ' ', result)
    # Dọn "chỗ trợ" (OCR đọc nhầm "hỗ" thành "chỗ") cùng pattern
    result = re.sub(r'(?<=[a-zàáảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵ])chỗ trợ', ' ', result)

    # ── Fix double vowels do FIX_MAP replace 2 lần ───────────────────────────
    # Dùng regex: bất kỳ ký tự Unicode có dấu nào bị lặp đôi liên tiếp
    # Ví dụ: "ốố" → "ố", "ởở" → "ở", "ủủ" → "ủ"
    result = re.sub(
        r'([àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵ])\1',
        r'\1', result
    )

    # ── Fix "Tt cà/cơ sởinh viên" → "Tất cả sinh viên" ───────────────────────
    result = re.sub(r'Tt\s+c[àaả]\s+sinh viên', 'Tất cả sinh viên', result)
    result = re.sub(r'Tt\s+c[ơ]\s*s[ở]\s*inh viên', 'Tất cả sinh viên', result)
    result = re.sub(r'Tt\s+c[åa]\s+sinh', 'Tất cả sinh', result)

    # ── Fix số văn bản dính nhau: "S:2164" → "Số: 2164" ─────────────────────
    result = re.sub(r'\bS[óôo]:\s*(\d)', r'Số: \1', result)
    result = re.sub(r'\bS[óôo]\s+(\d)', r'Số \1', result)

    # ── Fix "thành phố" thiếu dấu ─────────────────────────────────────────────
    result = re.sub(r'thành\s+ph[oô]\b', 'thành phố', result)

    return result


def _apply_symspell(text: str) -> str:
    """
    Chạy SymSpell correction trên từng dòng văn bản.
    Chỉ sửa từ nếu edit_distance == 1 (tránh over-correct).
    """
    checker = _get_spell_checker()
    if checker is None or not _DICT_LOADED:
        return text   # Không có dictionary → bỏ qua

    import re
    lines = text.split('\n')
    corrected_lines = []

    for line in lines:
        # Chỉ xử lý dòng có chữ cái tiếng Việt
        if not re.search(r'[a-zA-ZÀ-ỹ]', line):
            corrected_lines.append(line)
            continue

        # Tokenize: giữ nguyên ký tự đặc biệt, chỉ sửa từ thuần chữ
        tokens = re.split(r'(\s+|[^\wÀ-ỹ]+)', line)
        corrected_tokens = []
        for token in tokens:
            if re.match(r'^[\wÀ-ỹ]+$', token) and len(token) >= 3:
                suggestions = checker.lookup(token, max_candidates=1)
                if suggestions:
                    best_word, dist, freq = suggestions[0]
                    # Chỉ sửa nếu:
                    # - edit distance = 1 (sửa nhỏ)
                    # - từ gốc không phải là proper noun (không viết hoa)
                    # - từ đề xuất dài hơn hoặc bằng (tránh rút gọn sai)
                    if (dist == 1
                            and not token[0].isupper()
                            and len(best_word) >= len(token) - 1):
                        corrected_tokens.append(best_word)
                    else:
                        corrected_tokens.append(token)
                else:
                    corrected_tokens.append(token)
            else:
                corrected_tokens.append(token)

        corrected_lines.append(''.join(corrected_tokens))

    return '\n'.join(corrected_lines)


def is_spell_checker_available() -> bool:
    """Kiểm tra SymSpell có dictionary không."""
    checker = _get_spell_checker()
    return checker is not None and _DICT_LOADED
