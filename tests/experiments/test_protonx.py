"""
Test script for ProtonX Text Correction integration

Tests:
1. Basic correction
2. PaddleOCR + ProtonX pipeline
3. Accuracy comparison
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

from ocr_scanner.src.ocr.engine_paddle import (
    ocr_paddle_image,
    ocr_paddle_image_with_protonx,
    ocr_paddle_image_detailed_with_protonx
)


def test_basic_correction():
    """Test basic ProtonX correction"""
    print("=" * 80)
    print("TEST 1: Basic ProtonX Correction")
    print("=" * 80)
    
    try:
        from ocr_scanner.src.ocr.engine_protonx_correction import correct_vietnamese_text_protonx
        
        test_cases = [
            "V vic np h so hc phí",
            "Điều kien bảo đm an ninh mạng",
            "Hệ thông thông tin x lý bí mt nhà nước",
            "BOCÔNG THƯNG",
            "CNG HOÀ XĂ HI CH NGHA VIT NAM"
        ]
        
        for i, test in enumerate(test_cases, 1):
            corrected = correct_vietnamese_text_protonx(test)
            print(f"\n{i}. Input:  {test}")
            print(f"   Output: {corrected}")
        
        print("\n✅ Basic correction test passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Basic correction test failed: {e}")
        return False


def test_paddle_protonx_pipeline(image_path: str):
    """Test PaddleOCR + ProtonX pipeline"""
    print("\n" + "=" * 80)
    print("TEST 2: PaddleOCR + ProtonX Pipeline")
    print("=" * 80)
    
    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        return False
    
    try:
        print(f"\n📷 Processing: {image_path}\n")
        
        # Test detailed output
        result = ocr_paddle_image_detailed_with_protonx(image_path)
        
        print(f"Lines detected: {len(result['lines'])}")
        print(f"Average confidence: {result['avg_confidence']:.2%}")
        print(f"ProtonX enabled: {result['protonx_enabled']}")
        
        print("\n" + "-" * 80)
        print("RAW OCR OUTPUT:")
        print("-" * 80)
        print(result['text_raw'])
        
        print("\n" + "-" * 80)
        print("PROTONX CORRECTED OUTPUT:")
        print("-" * 80)
        print(result['text'])
        
        print("\n✅ Pipeline test passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Pipeline test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_comparison(image_path: str):
    """Compare basic vs ProtonX correction"""
    print("\n" + "=" * 80)
    print("TEST 3: Comparison - Basic vs ProtonX")
    print("=" * 80)
    
    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        return False
    
    try:
        print(f"\n📷 Processing: {image_path}\n")
        
        # Basic post-processing
        print("Running basic post-processing...")
        basic_result = ocr_paddle_image(image_path, apply_postprocessing=True)
        
        # ProtonX correction
        print("Running ProtonX correction...")
        protonx_result = ocr_paddle_image_with_protonx(image_path)
        
        print("\n" + "-" * 80)
        print("BASIC POST-PROCESSING:")
        print("-" * 80)
        print(basic_result)
        
        print("\n" + "-" * 80)
        print("PROTONX CORRECTION:")
        print("-" * 80)
        print(protonx_result)
        
        # Simple comparison
        if basic_result != protonx_result:
            print("\n📊 DIFFERENCES DETECTED:")
            print("ProtonX made corrections to the text!")
        else:
            print("\n⚠️ No differences detected")
        
        print("\n✅ Comparison test passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Comparison test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("\n🚀 ProtonX Integration Test Suite\n")
    
    # Test 1: Basic correction
    test1_passed = test_basic_correction()
    
    # Test 2 & 3: Pipeline tests (need image)
    if len(sys.argv) > 1:
        test_image = sys.argv[1]
        test2_passed = test_paddle_protonx_pipeline(test_image)
        test3_passed = test_comparison(test_image)
    else:
        print("\n⚠️ No image provided for pipeline tests")
        print("Usage: python test_protonx.py <image_path>")
        test2_passed = None
        test3_passed = None
    
    # Summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print(f"Test 1 (Basic Correction): {'✅ PASSED' if test1_passed else '❌ FAILED'}")
    if test2_passed is not None:
        print(f"Test 2 (Pipeline): {'✅ PASSED' if test2_passed else '❌ FAILED'}")
        print(f"Test 3 (Comparison): {'✅ PASSED' if test3_passed else '❌ FAILED'}")
    print("=" * 80)
