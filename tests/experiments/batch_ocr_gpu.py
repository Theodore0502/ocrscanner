"""
Batch OCR Processing Script with GPU Acceleration
Processes multiple images/PDFs in parallel using ProtonX correction
"""

import os
import sys
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict

sys.path.insert(0, os.path.dirname(__file__))

from ocr_scanner.src.ocr.engine_paddle import ocr_paddle_image_detailed_with_protonx


def process_single_file(file_path: str, output_dir: str = None) -> Dict:
    """
    Process a single image/PDF file with OCR + ProtonX
    
    Args:
        file_path: Path to image file
        output_dir: Optional output directory for results
        
    Returns:
        Dict with results and metadata
    """
    start_time = time.time()
    file_name = Path(file_path).stem
    
    try:
        print(f"🔄 Processing: {file_name}...")
        
        # Run OCR + ProtonX
        result = ocr_paddle_image_detailed_with_protonx(file_path)
        
        processing_time = time.time() - start_time
        
        # Save output if directory specified
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f"{file_name}_ocr.txt")
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result['text'])
            
            print(f"✅ {file_name}: {processing_time:.2f}s | Saved to {output_path}")
        else:
            print(f"✅ {file_name}: {processing_time:.2f}s")
        
        return {
            'file': file_name,
            'success': True,
            'time': processing_time,
            'lines': len(result['lines']),
            'confidence': result['avg_confidence'],
            'text': result['text']
        }
        
    except Exception as e:
        processing_time = time.time() - start_time
        print(f"❌ {file_name}: Error - {e}")
        
        return {
            'file': file_name,
            'success': False,
            'time': processing_time,
            'error': str(e)
        }


def batch_process_directory(
    input_dir: str,
    output_dir: str = None,
    max_workers: int = 3,
    extensions: List[str] = None
) -> Dict:
    """
    Process all images in a directory using multi-threading
    
    Args:
        input_dir: Directory containing images
        output_dir: Directory to save OCR results
        max_workers: Number of parallel workers (default: 3 for GPU)
        extensions: File extensions to process
        
    Returns:
        Dict with batch statistics
    """
    if extensions is None:
        extensions = ['.jpg', '.jpeg', '.png', '.tiff', '.pdf']
    
    # Find all image files
    image_files = []
    for ext in extensions:
        image_files.extend(Path(input_dir).glob(f'**/*{ext}'))
        image_files.extend(Path(input_dir).glob(f'**/*{ext.upper()}'))
    
    image_files = [str(f) for f in image_files]
    
    if not image_files:
        print(f"❌ No image files found in {input_dir}")
        return {'success': False, 'error': 'No files found'}
    
    print(f"\n{'='*80}")
    print(f"BATCH OCR PROCESSING")
    print(f"{'='*80}")
    print(f"📂 Input:  {input_dir}")
    print(f"📂 Output: {output_dir or '(console only)'}")
    print(f"📊 Files:  {len(image_files)}")
    print(f"⚡ Workers: {max_workers} (GPU-accelerated)")
    print(f"{'='*80}\n")
    
    # Process files in parallel
    start_time = time.time()
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_file = {
            executor.submit(process_single_file, file_path, output_dir): file_path
            for file_path in image_files
        }
        
        # Collect results as they complete
        for future in as_completed(future_to_file):
            result = future.result()
            results.append(result)
    
    total_time = time.time() - start_time
    
    # Calculate statistics
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]
    
    avg_time = sum(r['time'] for r in successful) / len(successful) if successful else 0
    avg_confidence = sum(r['confidence'] for r in successful) / len(successful) if successful else 0
    
    # Print summary
    print(f"\n{'='*80}")
    print(f"BATCH PROCESSING SUMMARY")
    print(f"{'='*80}")
    print(f"✅ Successful: {len(successful)}/{len(results)}")
    print(f"❌ Failed: {len(failed)}")
    print(f"⏱️  Total time: {total_time:.2f}s")
    print(f"⚡ Avg time/file: {avg_time:.2f}s")
    print(f"📊 Avg confidence: {avg_confidence:.2%}")
    print(f"🚀 Throughput: {len(successful)/total_time:.2f} files/second")
    print(f"{'='*80}")
    
    if failed:
        print(f"\n⚠️  Failed files:")
        for r in failed:
            print(f"  - {r['file']}: {r.get('error', 'Unknown error')}")
    
    return {
        'success': True,
        'total_files': len(results),
        'successful': len(successful),
        'failed': len(failed),
        'total_time': total_time,
        'avg_time_per_file': avg_time,
        'avg_confidence': avg_confidence,
        'throughput': len(successful)/total_time if total_time > 0 else 0,
        'results': results
    }


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Batch OCR processing with GPU acceleration')
    parser.add_argument('input_dir', help='Input directory containing images')
    parser.add_argument('-o', '--output', help='Output directory for OCR results', default=None)
    parser.add_argument('-w', '--workers', type=int, default=3, help='Number of parallel workers (default: 3)')
    parser.add_argument('-e', '--extensions', nargs='+', default=['.jpg', '.jpeg', '.png', '.tiff', '.pdf'],
                       help='File extensions to process')
    
    args = parser.parse_args()
    
    # Run batch processing
    result = batch_process_directory(
        input_dir=args.input_dir,
        output_dir=args.output,
        max_workers=args.workers,
        extensions=args.extensions
    )
    
    # Exit with appropriate code
    sys.exit(0 if result['success'] else 1)
