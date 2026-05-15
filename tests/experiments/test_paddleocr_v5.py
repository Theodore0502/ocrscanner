"""
Test script to compare PaddleOCR v5 accuracy with existing DocTR implementation.

Usage:
    python ocr_scanner/test_paddleocr_v5.py
"""
from paddleocr import PaddleOCR
import os
from pathlib import Path
import time
import sys

def test_paddleocr_v5_basic():
    """Test basic PaddleOCR v5 functionality"""
    print(f"\n{'='*80}")
    print(f"PaddleOCR v5 Test - Vietnamese Document Recognition")
    print(f"{'='*80}\n")
    
    # Import version
    try:
        import paddleocr
        print(f"✓ PaddleOCR version: {paddleocr.__version__}")
    except Exception as e:
        print(f"✗ Error getting version: {e}")
    
    # Initialize PaddleOCR with v5 optimizations
    print("\n[1/4] Initializing PaddleOCR with PP-OCRv5 optimizations...")
    try:
        ocr = PaddleOCR(
            lang='vi',
            use_textline_orientation=True,
            use_doc_orientation_classify=True,
            use_doc_unwarping=True
        )
        print("✓ PaddleOCR initialized successfully")
    except Exception as e:
        print(f"✗ Error initializing PaddleOCR: {e}")
        sys.exit(1)
    
    # Find test images
    print("\n[2/4] Looking for test images...")
    test_dirs = [
        'data/raw',
        'ocr_scanner/data/raw',
        'data'
    ]
    
    test_images = []
    for test_dir in test_dirs:
        if os.path.exists(test_dir):
            for ext in ['*.jpg', '*.jpeg', '*.png']:
                images = list(Path(test_dir).glob(ext))
                test_images.extend(images)
            if test_images:
                break
    
    if not test_images:
        print("✗ No test images found. Please place Vietnamese document images in data/raw/")
        print("\nSearched in:")
        for d in test_dirs:
            print(f"  - {d}")
        return
    
    # Use first image for testing
    test_image = str(test_images[0])
    print(f"✓ Found test image: {test_image}")
    
    # Run OCR
    print(f"\n[3/4] Running OCR recognition...")
    try:
        start_time = time.time()
        result = ocr.ocr(test_image, cls=True)
        end_time = time.time()
        print(f"✓ OCR completed in {end_time - start_time:.2f}s")
    except Exception as e:
        print(f"✗ Error during OCR: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Display results
    print(f"\n[4/4] OCR Results:")
    print(f"{'='*80}\n")
    
    if result and result[0]:
        total_lines = len(result[0])
        print(f"Total lines detected: {total_lines}\n")
        
        for idx, line in enumerate(result[0], 1):
            box, (text, confidence) = line
            print(f"[{idx:2d}] {text} (confidence: {confidence:.3f})")
        
        # Calculate average confidence
        avg_confidence = sum([line[1][1] for line in result[0]]) / total_lines
        print(f"\n{'='*80}")
        print(f"Average confidence: {avg_confidence:.3f}")
        print(f"Processing time: {end_time - start_time:.2f}s")
        print(f"{'='*80}\n")
    else:
        print("✗ No text detected in image")
    
    print("\n✓ Test completed successfully!\n")

def test_configuration_flags():
    """Test different configuration combinations"""
    print(f"\n{'='*80}")
    print(f"Testing PP-OCRv5 Configuration Flags")
    print(f"{'='*80}\n")
    
    configs = [
        {
            "name": "Minimal (v2.x compatible)",
            "params": {
                "lang": "vi",
                "use_textline_orientation": False,
                "use_doc_orientation_classify": False,
                "use_doc_unwarping": False,
            }
        },
        {
            "name": "With Orientation Detection",
            "params": {
                "lang": "vi",
                "use_textline_orientation": True,
                "use_doc_orientation_classify": True,
                "use_doc_unwarping": False,
            }
        },
        {
            "name": "Full PP-OCRv5 (Recommended)",
            "params": {
                "lang": "vi",
                "use_textline_orientation": True,
                "use_doc_orientation_classify": True,
                "use_doc_unwarping": True,
            }
        }
    ]
    
    for idx, config in enumerate(configs, 1):
        print(f"\n[{idx}/3] Testing: {config['name']}")
        try:
            ocr = PaddleOCR(**config['params'])
            print(f"✓ Configuration works")
        except Exception as e:
            print(f"✗ Configuration failed: {e}")
    
    print(f"\n{'='*80}\n")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Test PaddleOCR v5 functionality')
    parser.add_argument('--config-test', action='store_true', 
                        help='Test different configuration flags')
    
    args = parser.parse_args()
    
    if args.config_test:
        test_configuration_flags()
    else:
        test_paddleocr_v5_basic()
