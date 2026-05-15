"""
Test PaddleOCR v5 with REAL Vietnamese administrative documents
"""
from paddleocr import PaddleOCR
from pathlib import Path
import time
import json

def test_real_documents():
    print(f"\n{'#'*80}")
    print(f"# PaddleOCR v5 - REAL Vietnamese Administrative Documents Test")
    print(f"{'#'*80}\n")
    
    # Real document paths
    base_dir = Path(r"d:\Sources\-----OCR_Scanner\ocr_scanner\data\raw")
    
    # Find all JPG files in subdirectories
    image_files = []
    for subdir in base_dir.iterdir():
        if subdir.is_dir():
            for img in subdir.glob("*.jpg"):
                image_files.append(img)
    
    if not image_files:
        print(f"✗ No images found in {base_dir}")
        return
    
    print(f"✓ Found {len(image_files)} real document(s)\n")
    
    # Initialize OCR with PP-OCRv5 optimizations
    print("Initializing PaddleOCR v5 with optimizations...")
    ocr = PaddleOCR(
        lang='vi',
        use_textline_orientation=True,
        use_doc_orientation_classify=True,
        use_doc_unwarping=True
    )
    print("✓ Ready\n")
    
    # Process each document
    all_results = []
    
    for idx, image_path in enumerate(image_files, 1):
        print(f"\n{'='*80}")
        print(f"[{idx}/{len(image_files)}] Processing: {image_path.parent.name}/{image_path.name}")
        print(f"{'='*80}\n")
        
        start_time = time.time()
        result = ocr.ocr(str(image_path))
        end_time = time.time()
        
        # Parse result
        if result and len(result) > 0:
            res_dict = result[0]
            
            if isinstance(res_dict, dict):
                rec_texts = res_dict.get('rec_texts', [])
                rec_scores = res_dict.get('rec_scores', [])
                
                if rec_texts:
                    print(f"✓ Detected {len(rec_texts)} text line(s)")
                    print(f"✓ Processing time: {end_time - start_time:.2f}s\n")
                    
                    # Display text (first 20 lines)
                    print("--- Text Preview (first 20 lines) ---")
                    for i, (text, score) in enumerate(zip(rec_texts[:20], rec_scores[:20]), 1):
                        print(f"[{i:2d}] {text} (conf: {score:.3f})")
                    if len(rec_texts) > 20:
                        print(f"... ({len(rec_texts) - 20} more lines)")
                    
                    # Save to same folder as source image
                    output_dir = image_path.parent
                    output_txt = output_dir / f"{image_path.stem}_paddleocr_v5.txt"
                    output_json = output_dir / f"{image_path.stem}_paddleocr_v5.json"
                    
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
                    
                    print(f"\n✓ Saved to: {output_txt.relative_to(base_dir)}")
                    print(f"✓ Details: {output_json.relative_to(base_dir)}")
                    
                    all_results.append({
                        "document": f"{image_path.parent.name}/{image_path.name}",
                        "lines": len(rec_texts),
                        "confidence": sum(rec_scores) / len(rec_scores) if rec_scores else 0.0,
                        "time": end_time - start_time
                    })
                else:
                    print(f"✗ No text detected")
            else:
                print(f"✗ Unexpected result format")
        else:
            print(f"✗ No result returned")
    
    # Summary
    if all_results:
        print(f"\n\n{'#'*80}")
        print(f"# REAL DOCUMENTS TEST SUMMARY")
        print(f"{'#'*80}\n")
        
        total_lines = sum([r['lines'] for r in all_results])
        avg_conf = sum([r['confidence'] for r in all_results]) / len(all_results)
        total_time = sum([r['time'] for r in all_results])
        
        print(f"Documents processed: {len(all_results)}/{len(image_files)}")
        print(f"Total text lines: {total_lines}")
        print(f"Average confidence: {avg_conf:.4f} ({avg_conf*100:.2f}%)")
        print(f"Total time: {total_time:.2f}s")
        print(f"Average time/document: {total_time/len(all_results):.2f}s\n")
        
        # Per document breakdown
        print("Per-document breakdown:")
        for r in all_results:
            print(f"  • {r['document']:30s} | {r['lines']:3d} lines | {r['confidence']:.4f} conf | {r['time']:.2f}s")
        
        print(f"\n✓ All results saved in: {base_dir}\n")
    else:
        print(f"\n✗ No documents were successfully processed\n")

if __name__ == "__main__":
    test_real_documents()
