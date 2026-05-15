"""
Simple single image test for PaddleOCR v5 debugging
"""
from paddleocr import PaddleOCR
from pathlib import Path
import sys
import traceback

def test_single_image():
    # Find first Vietnamese image
    vi_dir = Path(r"d:\Sources\-----OCR_Scanner\vi_00")
    
    if not vi_dir.exists():
        print(f"✗ Directory not found: {vi_dir}")
        return
    
    images = list(vi_dir.glob("*.jpg"))[:1]
    if not images:
        print(f"✗ No JPG images found in {vi_dir}")
        return
    
    image_path = images[0]
    print(f"Testing image: {image_path}")
    print(f"{'='*80}\n")
    
    # Initialize PaddleOCR with minimal config first
    print("[1/3] Initializing PaddleOCR...")
    try:
        ocr = PaddleOCR(lang='vi')
        print("✓ PaddleOCR initialized\n")
    except Exception as e:
        print(f"✗ Error initializing: {e}")
        traceback.print_exc()
        return
    
    # Run OCR
    print("[2/3] Running OCR...")
    try:
        result = ocr.ocr(str(image_path))
        print(f"✓ OCR completed\n")
    except Exception as e:
        print(f"✗ Error during OCR: {e}")
        traceback.print_exc()
        return
    
    # Display results
    print("[3/3] Results:")
    print(f"{'='*80}\n")
    
    if result and result[0]:
        print(f"DEBUG: Result type: {type(result[0])}")
        print(f"DEBUG: First item type: {type(result[0][0]) if result[0] else 'empty'}")
        
        all_lines = []
        for idx, line in enumerate(result[0], 1):
            # Handle different formats
            if isinstance(line, (list, tuple)) and len(line) >= 2:
                try:
                    # Format: [box, (text, confidence)]
                    box, text_info = line
                    if isinstance(text_info, (list, tuple)) and len(text_info) >= 2:
                        text, confidence = text_info[0], text_info[1]
                    else:
                        text, confidence = str(text_info), 0.0
                    print(f"[{idx:2d}] {text} (conf: {confidence:.3f})")
                    all_lines.append(text)
                except Exception as e:
                    print(f"[{idx:2d}] Error parsing line: {e}")
                    print(f"       Raw data: {line}")
            else:
                print(f"[{idx:2d}] Unexpected format: {line}")
        
        if all_lines:
            # Save to file
            output_file = vi_dir / f"{image_path.stem}_test_result.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(all_lines))
            
            print(f"\n{'='*80}")
            print(f"✓ Total lines: {len(all_lines)}")
            print(f"✓ Saved to: {output_file}")
        else:
            print("\n✗ No text lines extracted")
    else:
        print("✗ No text detected")

if __name__ == "__main__":
    test_single_image()
