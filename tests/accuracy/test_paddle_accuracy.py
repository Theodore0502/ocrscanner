"""
Test PaddleOCR v5 on real Vietnamese documents from ocr_scanner/data/raw/
Calculate accuracy by comparing with ground truth files
"""
from paddleocr import PaddleOCR
from pathlib import Path
import time
import json
import difflib

def calculate_accuracy(ground_truth, ocr_output):
    """Calculate character-level accuracy"""
    gt_chars = list(ground_truth)
    ocr_chars = list(ocr_output)
    matcher = difflib.SequenceMatcher(None, gt_chars, ocr_chars)
    return matcher.ratio() * 100

def test_real_documents():
    print(f"\n{'#'*80}")
    print(f"# PaddleOCR v5 Accuracy Test - Real Vietnamese Documents")
    print(f"{'#'*80}\n")
    
    # Find documents with both image and ground truth
    data_dir = Path(r"d:\Sources\-----OCR_Scanner\ocr_scanner\data\raw")
    ground_truth_dir = Path(r"d:\Sources\-----OCR_Scanner\tests\accuracy\ground_truth")
    
    # Documents to test (with known ground truth)
    test_cases = [
        {
            "name": "dl_2025_0002",
            "image": data_dir / "dl_2025_0002" / "dl_2025_0002.jpg",
            "ground_truth": ground_truth_dir / "legit_0002.txt"
        }
    ]
    
    # Find other available images
    for img_file in data_dir.glob("*/dl_*.jpg"):
        doc_name = img_file.stem
        if doc_name not in [tc["name"] for tc in test_cases]:
            test_cases.append({
                "name": doc_name,
                "image": img_file,
                "ground_truth": None  # No ground truth available
            })
    
    # Limit to first 5 documents
    test_cases = test_cases[:5]
    
    print(f"✓ Found {len(test_cases)} document(s) to test\n")
    
    # Initialize PaddleOCR
    print("Initializing PaddleOCR v5...")
    ocr = PaddleOCR(
        lang='vi',
        use_textline_orientation=True,
        use_doc_orientation_classify=True,
        use_doc_unwarping=True
    )
    print("✓ Ready\n")
    
    # Test results
    results = []
    
    for idx, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"[{idx}/{len(test_cases)}] Testing: {test_case['name']}")
        print(f"{'='*80}\n")
        
        image_path = test_case['image']
        
        if not image_path.exists():
            print(f"✗ Image not found: {image_path}")
            continue
        
        # Run OCR
        start_time = time.time()
        result = ocr.ocr(str(image_path))
        end_time = time.time()
        processing_time = end_time - start_time
        
        # Parse result
        ocr_text = ""
        confidence_scores = []
        
        if result and len(result) > 0:
            res_dict = result[0]
            
            if isinstance(res_dict, dict):
                rec_texts = res_dict.get('rec_texts', [])
                rec_scores = res_dict.get('rec_scores', [])
                
                if rec_texts:
                    ocr_text = '\n'.join(rec_texts)
                    confidence_scores = rec_scores
                    avg_confidence = sum(rec_scores) / len(rec_scores) if rec_scores else 0.0
                    
                    print(f"✓ Detected {len(rec_texts)} text line(s)")
                    print(f"✓ Average confidence: {avg_confidence:.2%}")
                    print(f"✓ Processing time: {processing_time:.2f}s\n")
                else:
                    print(f"✗ No text detected")
                    continue
            else:
                print(f"✗ Unexpected result format")
                continue
        else:
            print(f"✗ OCR failed")
            continue
        
        # Calculate accuracy if ground truth exists
        accuracy = None
        if test_case['ground_truth'] and test_case['ground_truth'].exists():
            with open(test_case['ground_truth'], 'r', encoding='utf-8') as f:
                ground_truth = f.read()
            
            accuracy = calculate_accuracy(ground_truth, ocr_text)
            print(f"📊 ACCURACY: {accuracy:.2f}%")
            
            if accuracy < 90:
                print(f"   ⚠️ Below 90% threshold!")
            else:
                print(f"   ✅ Meets 90% threshold!")
        else:
            print(f"📊 ACCURACY: N/A (no ground truth)")
        
        # Save OCR output
        output_txt = image_path.parent / f"{image_path.stem}_paddle_output.txt"
        output_json = image_path.parent / f"{image_path.stem}_paddle_output.json"
        
        with open(output_txt, 'w', encoding='utf-8') as f:
            f.write(ocr_text)
        
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump({
                "source": str(image_path),
                "lines": len(rec_texts) if 'rec_texts' in locals() else 0,
                "avg_confidence": float(avg_confidence),
                "processing_time": round(processing_time, 3),
                "accuracy": accuracy,
                "results": [
                    {"text": t, "confidence": float(s)} 
                    for t, s in zip(rec_texts, confidence_scores)
                ] if rec_texts else []
            }, f, ensure_ascii=False, indent=2)
        
        print(f"\n✓ Saved to: {output_txt}")
        
        # Store result
        results.append({
            "name": test_case['name'],
            "lines": len(rec_texts) if 'rec_texts' in locals() else 0,
            "confidence": float(avg_confidence) if 'avg_confidence' in locals() else 0.0,
            "time": processing_time,
            "accuracy": accuracy
        })
    
    # Summary
    print(f"\n\n{'#'*80}")
    print(f"# FINAL RESULTS")
    print(f"{'#'*80}\n")
    
    if results:
        print(f"Documents tested: {len(results)}")
        
        # Calculate averages
        avg_conf = sum(r['confidence'] for r in results) / len(results)
        avg_time = sum(r['time'] for r in results) / len(results)
        
        print(f"Average confidence: {avg_conf:.2%}")
        print(f"Average time/document: {avg_time:.2f}s")
        
        # Accuracy summary
        accuracy_results = [r for r in results if r['accuracy'] is not None]
        if accuracy_results:
            avg_accuracy = sum(r['accuracy'] for r in accuracy_results) / len(accuracy_results)
            print(f"\n📊 ACCURACY RESULTS:")
            print(f"   Average accuracy: {avg_accuracy:.2f}%")
            
            for r in accuracy_results:
                status = "✅" if r['accuracy'] >= 90 else "❌"
                print(f"   {status} {r['name']}: {r['accuracy']:.2f}%")
            
            # Decision
            print(f"\n{'='*80}")
            if avg_accuracy >= 90:
                print(f"✅ DECISION: PaddleOCR v5 meets 90% threshold!")
                print(f"   → Can use PaddleOCR v5 as primary engine")
            else:
                print(f"❌ DECISION: PaddleOCR v5 below 90% threshold ({avg_accuracy:.2f}%)")
                print(f"   → Need to migrate to PaddleOCR v5 with enhanced post-processing")
            print(f"{'='*80}\n")
        else:
            print(f"\n⚠️ No ground truth available for accuracy calculation")
            print(f"   Need to manually verify OCR quality")
    else:
        print(f"✗ No successful OCR results")

if __name__ == "__main__":
    test_real_documents()
