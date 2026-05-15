import sys
import os
import cv2
import pytesseract

# Configure Tesseract path (adjust if needed)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def scan_with_tesseract(image_path, output_txt_path):
    """Scan an image using Tesseract OCR."""
    print(f"📄 Scanning: {image_path}")
    
    # Read image
    image = cv2.imread(image_path)
    
    # Run OCR with Tesseract (Vietnamese)
    print("🔍 Running OCR (Tesseract + Vietnamese)...")
    try:
        text_result = pytesseract.image_to_string(image, lang='vie')
    except Exception as e:
        print(f"❌ Tesseract error: {e}")
        print("Trying with default language...")
        text_result = pytesseract.image_to_string(image)
    
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
    output_path = r"d:\Sources\-----OCR_Scanner\ocr_scanner\data\raw\dl_2025_0003\scanned_output_tesseract.txt"
    
    scan_with_tesseract(image_path, output_path)
