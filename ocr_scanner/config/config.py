USE_GPU = True

PADDLE_OCR_CONFIG = {
    "use_gpu": True,      # ✅ GPU enabled for RTX 3050 Ti!
    "lang": "vi",
    
    # PP-OCRv5 optimizations (new in v3.x)
    "use_textline_orientation": True,  # Phát hiện hướng text line
    "use_doc_orientation_classify": True,  # Phân loại hướng document
    "use_doc_unwarping": True,  # Khử méo document
}

# Post-processing configuration
USE_PHOBERT_CORRECTION = False  # PhoBERT is slow, enable for max accuracy
USE_NGRAM_CORRECTION = True      # N-gram based correction (fast)
PHOBERT_CONFIDENCE_THRESHOLD = 0.7  # Only correct words with confidence < 0.7
