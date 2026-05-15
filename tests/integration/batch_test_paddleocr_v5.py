"""Working PaddleOCR v3 test with proper result parsing"""
from paddleocr import PaddleOCR
from pathlib import Path
import time
import json

def test_vietnamese_images():
    print(f"\n{'#'*80}")
    print(f"# PaddleOCR v3 Batch Test - Vietnamese Documents")
    print(f"{'#'*80}\n")
    
    # Find Vietnamese images
    vi_dir = Path(r"d:\Sources\-----OCR_Scanner\vi_00")
    images = list(vi_dir.glob("*.jpg"))[:5]
    
    if not images:
        print(f"✗ No images found in {vi_dir}")
        return
    
    print(f"✓ Found {len(images)} image(s)\n")
    
    # Initialize OCR
    print("Initializing PaddleOCR...")
    ocr = PaddleOCR(
        lang='vi',
        use_textline_orientation=True,
        use_doc_orientation_classify=True,
        use_doc_unwarping=True
    )
    print("✓ Ready\n")
    
    # Process each image
    all_results = []
    
    for idx, image_path in enumerate(images, 1):
        print(f"\n{'='*80}")
        print(f"[{idx}/{len(images)}] Processing: {image_path.name}")
        print(f"{'='*80}\n")
        
        start_time = time.time()
        result = ocr.ocr(str(image_path))
        end_time = time.time()
        
        # Result is a list with one dict
        if result and len(result) > 0:
            res_dict = result[0]
            
            # Check if it's dict format (v3)
            if isinstance(res_dict, dict):
                rec_texts = res_dict.get('rec_texts', [])
                rec_scores = res_dict.get('rec_scores', [])
                
                if rec_texts:
                    print(f"✓ Detected {len(rec_texts)} text line(s)")
                    print(f"✓ Processing time: {end_time - start_time:.2f}s\n")
                    
                    # Display text
                    for i, (text, score) in enumerate(zip(rec_texts, rec_scores), 1):
                        print(f"[{i:2d}] {text} (conf: {score:.3f})")
                    
                    # Save result
                    output_txt = vi_dir / f"{image_path.stem}_paddleocr_v5.txt"
                    output_json = vi_dir / f"{image_path.stem}_paddleocr_v5.json"
                    
                    with open(output_txt, 'w', encoding='utf-8') as f:
                        f.write('\n'.join(rec_texts))
                    
                    with open(output_json, 'w', encoding='utf-8') as f:
                        json.dump({
                            "source": str(image_path),
                            "lines": len(rec_texts),
                            "avg_confidence": sum(rec_scores) / len(rec_scores) if rec_scores else 0.0,
                            "processing_time": round(end_time - start_time, 3),
                            "results": [
                                {"text": t, "confidence": float(s)} 
                                for t, s in zip(rec_texts, rec_scores)
                            ]
                        }, f, ensure_ascii=False, indent=2)
                    
                    print(f"\n✓ Saved to: {output_txt}")
                    print(f"✓ Details: {output_json}")
                    
                    all_results.append({
                        "image": image_path.name,
                        "lines": len(rec_texts),
                        "confidence": sum(rec_scores) / len(rec_scores) if rec_scores else 0.0,
                        "time": end_time - start_time
                    })
                else:
                    print(f"✗ No text detected (empty rec_texts)")
                    print(f"   Angle: {res_dict.get('doc_preprocessor_res', {}).get('angle', 'N/A')}")
                    print(f"   dt_polys: {len(res_dict.get('dt_polys', []))}")
            else:
                print(f"  Unexpected result format: {type(res_dict)}")
        else:
            print(f"✗ No result returned")
    
    # Summary
    if all_results:
        print(f"\n\n{'#'*80}")
        print(f"# SUMMARY")
        print(f"{'#'*80}\n")
        
        total_lines = sum([r['lines'] for r in all_results])
        avg_conf = sum([r['confidence'] for r in all_results]) / len(all_results)
        total_time = sum([r['time'] for r in all_results])
        
        print(f"Images processed: {len(all_results)}/{len(images)}")
        print(f"Total text lines: {total_lines}")
        print(f"Average confidence: {avg_conf:.4f}")
        print(f"Total time: {total_time:.2f}s")
        print(f"Average time/image: {total_time/len(all_results):.2f}s")
        print(f"\n✓ Results saved in: {vi_dir}\n")
    else:
        print(f"\n✗ No successful results")

if __name__ == "__main__":
    test_vietnamese_images()
