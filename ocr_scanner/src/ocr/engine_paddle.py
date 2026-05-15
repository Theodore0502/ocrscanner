"""
PaddleOCR v5 Engine for Vietnamese OCR
Optimized for Vietnamese administrative documents with PP-OCRv5 features
"""
from paddleocr import PaddleOCR
import os
import sys

# Add parent directory to path for config access
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Initialize PaddleOCR once (expensive operation)
_paddle_ocr = None

# Fast instance for PDF batch processing (no unwarping, no orientation classify)
# Saves ~60-90s per page vs full config
_paddle_ocr_fast = None

# Try import ProtonX correction (optional)
try:
    from .engine_protonx_correction import correct_vietnamese_text_protonx
    PROTONX_AVAILABLE = True
except Exception as e:
    PROTONX_AVAILABLE = False
    print(f"\u26a0\ufe0f ProtonX not available: {e}")


def get_paddle_ocr():
    """Full-featured PaddleOCR — dùng cho ảnh đơn lẻ cần chất lượng cao nhất."""
    global _paddle_ocr
    if _paddle_ocr is None:
        print("Initializing PaddleOCR v5 (full)...")
        _paddle_ocr = PaddleOCR(
            lang='vi',
            use_textline_orientation=True,      # Detect text line orientation
            use_doc_orientation_classify=True,  # Classify document orientation
            use_doc_unwarping=True              # Unwarp distorted documents (~60-90s overhead)
        )
        print("PaddleOCR v5 (full) ready")
    return _paddle_ocr


def get_paddle_ocr_fast():
    """
    Rút gọn PaddleOCR — dùng cho PDF batch processing.
    Tắt doc_unwarping và orientation_classify → nhanh hơn ~3-5x so với full config.
    Phù hợp cho PDF scan thẳng (không bị méo, đúng chiều).
    """
    global _paddle_ocr_fast
    if _paddle_ocr_fast is None:
        print("Initializing PaddleOCR v5 (fast/batch mode)...")
        _paddle_ocr_fast = PaddleOCR(
            lang='vi',
            use_textline_orientation=False,     # Bỏ: PDF scan thường đúng chiều
            use_doc_orientation_classify=False, # Bỏ: tiết kiệm ~10-20s/trang
            use_doc_unwarping=False             # Bỏ: tiết kiệm ~60-90s/trang (chi phí lớn nhất)
        )
        print("PaddleOCR v5 (fast) ready")
    return _paddle_ocr_fast


def extract_text_from_result(result):
    """
    Extract text from PaddleOCR result (handles multiple API versions)
    
    Args:
        result: PaddleOCR result object
        
    Returns:
        tuple: (full_text, lines_info)
    """
    if not result or len(result) == 0:
        return "", []
    
    res_dict = result[0]
    
    # Handle PaddleOCR v3.x format
    if isinstance(res_dict, dict):
        rec_texts = res_dict.get('rec_texts', [])
        rec_scores = res_dict.get('rec_scores', [])
        dt_polys = res_dict.get('dt_polys', [])
        
        lines_info = []
        for i, (text, score) in enumerate(zip(rec_texts, rec_scores)):
            bbox = dt_polys[i] if i < len(dt_polys) else None
            lines_info.append({
                'text': text,
                'confidence': float(score),
                'bbox': bbox
            })
        
        full_text = '\n'.join(rec_texts)
        return full_text, lines_info
    
    # Handle PaddleOCR v2.x format
    elif isinstance(res_dict, list):
        lines_info = []
        texts = []
        
        for item in res_dict:
            if len(item) >= 2:
                bbox = item[0]
                text_info = item[1]
                if isinstance(text_info, (list, tuple)) and len(text_info) >= 2:
                    text = text_info[0]
                    confidence = text_info[1]
                    
                    lines_info.append({
                        'text': text,
                        'confidence': float(confidence),
                        'bbox': bbox
                    })
                    texts.append(text)
        
        full_text = '\n'.join(texts)
        return full_text, lines_info
    
    return "", []


def post_process_vietnamese(text: str) -> str:
    """
    Enhanced post-processing for Vietnamese text
    Fixes common OCR errors in Vietnamese administrative documents
    """
    import re
    
    # Phase 1: Fix common Vietnamese diacritics errors
    replacements = {
        # Header/Organization patterns
        'B CÔNG THƯNG': 'BỘ CÔNG THƯƠNG',
        'BOCÔNG THƯNG': 'BỘ CÔNG THƯƠNG',
        'CNG HOÀ XĂ HI': 'CỘNG HÒA XÃ HỘI',
        'CH NGHA VIT NAM': 'CHỦ NGHĨA VIỆT NAM',
        'VIT NAM': 'VIỆT NAM',
        'VIÊT NAM': 'VIỆT NAM',
        'TRƯNG ĐI HC': 'TRƯỜNG ĐẠI HỌC',
        'ĐIN LC': 'ĐIỆN LỰC',
        'DIEN LU': 'ĐIỆN LỰC',
        'DAIHOD': 'ĐẠI HỌC ĐIỆN LỰC',
        'B0': 'BỘ',
        
        # Common phrases
        'Đc lp - T do - Hnh phc': 'Độc lập - Tự do - Hạnh phúc',
        'Đc lp': 'Độc lập',
        'T do': 'Tự do',
        'Hnh phc': 'Hạnh phúc',
        
        # Common words with missing diacritics
        'V vic': 'Về việc',
        'np h so': 'nộp hồ sơ',
        'min': 'miễn',
        'gim': 'giảm',
        'hc phí': 'học phí',
        'h tr': 'hỗ trợ',
        'hc tp': 'học tập',
        'Thc hin': 'Thực hiện',
        'Ngh đnh': 'Nghị định',
        'Quy đnh': 'Quy định',
        'co ch': 'cơ chế',
        'qun lý': 'quản lý',
        'giáo dc': 'giáo dục',
        'thuc': 'thuộc',
        'h thng': 'hệ thống',
        'quc dân': 'quốc dân',
        'lĩnh vc': 'lĩnh vực',
        'đào to': 'đào tạo',
        'Quyt đnh': 'Quyết định',
        'dân tc': 'dân tộc',
        'thiu s': 'thiểu số',
        'trin khai': 'triển khai',
        'xćt': 'xét',
        'yêu cu': 'yêu cầu',
        'đy đ': 'đầy đủ',
        'hưóng dãn': 'hướng dẫn',
        'ph lc': 'phụ lục',
        'Hn np': 'Hạn nộp',
        'Noi nhn': 'Nơi nhận',
        'phưng': 'phường',
        'vưng mc': 'vướng mắc',
        'liên h': 'liên hệ',
        'tư vn': 'tư vấn',
        'gii đáp': 'giải đáp',
        'C vn': 'Cố vấn',
        'ph bin': 'phổ biến',
        'Đ ngh': 'Đề nghị',
        'đơn v': 'đơn vị',
        'cá nhân': 'cá nhân',
        'thi gian': 'thời gian',
        'quy đnh': 'quy định',
        
        # Signature/titles
        'TL HIU TRUÖNG': 'TL. HIỆU TRƯỞNG',
        'HIU TRUÖNG': 'HIỆU TRƯỞNG',
        'TRUÖNG RHÒNG': 'TRƯỞNG PHÒNG',
        'TRUNG': 'TRƯỞNG',
        'Hiu trưng': 'Hiệu trưởng',
        'Phing Phi': 'Phùng Thị',
    }
    
    result = text
    for wrong, correct in replacements.items():
        result = result.replace(wrong, correct)
    
    # Phase 2: Fix date patterns (ngày9 → ngày 29)
    result = re.sub(r'ngày(\d+)', r'ngày \1', result)
    
    # Phase 3: Fix missing spaces after punctuation
    result = re.sub(r'(\.)([A-ZÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉẺẼẸ])', r'\1 \2', result)
    result = re.sub(r'(;)([A-ZÀÁẢÃẠ])', r'\1 \2', result)
    result = re.sub(r'(:)([A-ZÀÁẢÃẠ])', r': \2', result)
    
    return result


def ocr_paddle_image(image_path: str, apply_postprocessing: bool = True) -> str:
    """OCR an image using PaddleOCR v5"""
    ocr = get_paddle_ocr()
    result = ocr.ocr(image_path)
    text, lines_info = extract_text_from_result(result)
    
    if apply_postprocessing and text:
        text = post_process_vietnamese(text)
    
    return text


def ocr_paddle_image_detailed(image_path: str, apply_postprocessing: bool = True) -> dict:
    """OCR an image and return detailed results"""
    ocr = get_paddle_ocr()
    result = ocr.ocr(image_path)
    text, lines_info = extract_text_from_result(result)
    
    # Calculate average confidence
    if lines_info:
        avg_confidence = sum(line['confidence'] for line in lines_info) / len(lines_info)
    else:
        avg_confidence = 0.0
    
    # Apply post-processing
    if apply_postprocessing and text:
        text = post_process_vietnamese(text)
        for line in lines_info:
            line['text_cleaned'] = post_process_vietnamese(line['text'])
    
    return {
        'text': text,
        'lines': lines_info,
        'avg_confidence': avg_confidence
    }



def ocr_paddle_image_detailed_fast(image_path: str, apply_postprocessing: bool = True) -> dict:
    """OCR nhanh cho PDF batch - dung fast singleton (khong unwarping) -> nhanh ~3-5x."""
    ocr = get_paddle_ocr_fast()
    result = ocr.ocr(image_path)
    text, lines_info = extract_text_from_result(result)
    avg_confidence = (
        sum(l['confidence'] for l in lines_info) / len(lines_info)
        if lines_info else 0.0
    )
    if apply_postprocessing and text:
        text = post_process_vietnamese(text)
        for line in lines_info:
            line['text_cleaned'] = post_process_vietnamese(line['text'])
    return {'text': text, 'lines': lines_info, 'avg_confidence': avg_confidence}


def ocr_paddle_image_with_protonx(image_path: str) -> str:
    """
    OCR an image using PaddleOCR v5 + ProtonX text correction.
    
    This combines:
    1. PaddleOCR v5 for fast OCR
    2. ProtonX Legal Text Correction for high-accuracy post-processing
    
    Args:
        image_path: Path to image file
        
    Returns:
        Corrected Vietnamese text
    """
    if not PROTONX_AVAILABLE:
        print("⚠️ ProtonX not available, falling back to basic post-processing")
        return ocr_paddle_image(image_path, apply_postprocessing=True)
    
    # Step 1: OCR with PaddleOCR (no post-processing)
    ocr = get_paddle_ocr()
    result = ocr.ocr(image_path)
    text, lines_info = extract_text_from_result(result)
    
    if not text:
        return text
    
    # Step 2: Apply ProtonX correction
    print("🔧 Applying ProtonX text correction...")
    corrected_text = correct_vietnamese_text_protonx(text, preserve_formatting=True)
    
    return corrected_text


def ocr_paddle_image_detailed_with_protonx(image_path: str) -> dict:
    """
    OCR an image with ProtonX correction and return detailed results.
    
    Args:
        image_path: Path to image file
        
    Returns:
        dict with keys:
        - text: Corrected text
        - text_raw: Raw OCR output
        - lines: Line-level information
        - avg_confidence: Average OCR confidence
        - protonx_enabled: Whether ProtonX was used
    """
    if not PROTONX_AVAILABLE:
        print("⚠️ ProtonX not available, using basic post-processing")
        result = ocr_paddle_image_detailed(image_path, apply_postprocessing=True)
        result['protonx_enabled'] = False
        result['text_raw'] = result['text']
        return result
    
    # Step 1: OCR with PaddleOCR (no post-processing)
    ocr = get_paddle_ocr()
    result = ocr.ocr(image_path)
    text, lines_info = extract_text_from_result(result)
    
    # Calculate average confidence
    if lines_info:
        avg_confidence = sum(line['confidence'] for line in lines_info) / len(lines_info)
    else:
        avg_confidence = 0.0
    
    # Step 2: Apply ProtonX correction
    if text:
        print("🔧 Applying ProtonX text correction...")
        corrected_text = correct_vietnamese_text_protonx(text, preserve_formatting=True)
    else:
        corrected_text = text
    
    return {
        'text': corrected_text,
        'text_raw': text,
        'lines': lines_info,
        'avg_confidence': avg_confidence,
        'protonx_enabled': True
    }



if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        test_image = sys.argv[1]
        print(f"Testing PaddleOCR v5 on: {test_image}\n")
        
        result = ocr_paddle_image_detailed(test_image)
        
        print(f"Lines detected: {len(result['lines'])}")
        print(f"Average confidence: {result['avg_confidence']:.2%}\n")
        print("=" * 80)
        print(result['text'])
        print("=" * 80)
    else:
        print("Usage: python engine_paddle.py <image_path>")
