"""Debug PaddleOCR v3 result structure"""
from paddleocr import PaddleOCR
from pathlib import Path
import json

vi_dir = Path(r"d:\Sources\-----OCR_Scanner\vi_00")
images = list(vi_dir.glob("*.jpg"))[:1]

if images:
    image_path = images[0]
    print(f"Testing: {image_path}\n")
    
    ocr = PaddleOCR(lang='vi')
    result = ocr.ocr(str(image_path))
    
    print(f"Result type: {type(result)}")
    print(f"Result length: {len(result) if hasattr(result, '__len__') else 'N/A'}")
    print(f"\nFirst 500 chars of result:")
    print(str(result)[:500])
    
    # Try to save as JSON for inspection
    try:
        with open('debug_result.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2, default=str)
        print(f"\n✓ Saved to debug_result.json")
    except Exception as e:
        print(f"\n✗ Could not save JSON: {e}")
