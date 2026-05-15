import sys
import os

# Add paths
sys.path.insert(0, os.path.dirname(__file__))

# Use DocTR ONLY (no ProtonX)
from ocr_scanner.src.ocr.engine_doctr import ocr_doctr_image

def scan_without_protonx(image_path, output_txt_path):
    """Scan an image using DocTR only (no ProtonX)."""
    print(f"📄 Scanning: {image_path}")
    
    # Run OCR (DocTR only)
    print("🔍 Running OCR (DocTR only, no ProtonX)...")
    text_result = ocr_doctr_image(image_path)
    
    # Save to file
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(text_result)
    
    print(f"✅ Saved to: {output_txt_path}")
    print(f"\n📝 Preview (first 800 chars):")
    print("="*50)
    print(text_result[:800])
    print("="*50)

if __name__ == "__main__":
    # Scan the dl_2025_0003 image
    image_path = r"d:\Sources\-----OCR_Scanner\ocr_scanner\data\raw\dl_2025_0003\dl_2025_0003.jpg"
    output_path = r"d:\Sources\-----OCR_Scanner\ocr_scanner\data\raw\dl_2025_0003\scanned_output_doctr_only.txt"
    
    scan_without_protonx(image_path, output_path)
