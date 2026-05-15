"""
Calculate accuracy metrics for OCR results
Computes CER (Character Error Rate) and WER (Word Error Rate)
"""
import os
import json
from pathlib import Path
from typing import Dict, List, Tuple
import difflib


def calculate_cer(reference: str, hypothesis: str) -> float:
    """
    Calculate Character Error Rate (CER)
    
    CER = (Substitutions + Deletions + Insertions) / Total Characters in Reference
    """
    if not reference:
        return 0.0 if not hypothesis else 1.0
    
    ref_chars = list(reference)
    hyp_chars = list(hypothesis)
    
    # Use difflib to compute edit distance
    sm = difflib.SequenceMatcher(None, ref_chars, hyp_chars)
    distance = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'replace':
            distance += max(i2 - i1, j2 - j1)
        elif tag == 'delete':
            distance += i2 - i1
        elif tag == 'insert':
            distance += j2 - j1
    
    cer = distance / len(ref_chars)
    return cer


def calculate_wer(reference: str, hypothesis: str) -> float:
    """
    Calculate Word Error Rate (WER)
    
    WER = (Substitutions + Deletions + Insertions) / Total Words in Reference
    """
    if not reference:
        return 0.0 if not hypothesis else 1.0
    
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    
    if not ref_words:
        return 0.0 if not hyp_words else 1.0
    
    # Use difflib to compute edit distance at word level
    sm = difflib.SequenceMatcher(None, ref_words, hyp_words)
    distance = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'replace':
            distance += max(i2 - i1, j2 - j1)
        elif tag == 'delete':
            distance += i2 - i1
        elif tag == 'insert':
            distance += j2 - j1
    
    wer = distance / len(ref_words)
    return wer


def normalize_text(text: str) -> str:
    """Normalize text for comparison (remove extra spaces, lowercase)"""
    import re
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text


def evaluate_document(doc_id: str, ocr_file: str, ground_truth_file: str) -> Dict:
    """
    Evaluate a single document
    
    Args:
        doc_id: Document identifier
        ocr_file: Path to OCR output file
        ground_truth_file: Path to ground truth file
    
    Returns:
        Dict with evaluation metrics
    """
    if not os.path.exists(ocr_file):
        return {
            'doc_id': doc_id,
            'error': f'OCR file not found: {ocr_file}'
        }
    
    if not os.path.exists(ground_truth_file):
        return {
            'doc_id': doc_id,
            'error': f'Ground truth file not found: {ground_truth_file}'
        }
    
    # Read files
    with open(ocr_file, 'r', encoding='utf-8') as f:
        ocr_text = f.read()
    
    with open(ground_truth_file, 'r', encoding='utf-8') as f:
        ground_truth = f.read()
    
    # Normalize
    ocr_normalized = normalize_text(ocr_text)
    gt_normalized = normalize_text(ground_truth)
    
    # Calculate metrics
    cer = calculate_cer(gt_normalized, ocr_normalized)
    wer = calculate_wer(gt_normalized, ocr_normalized)
    
    # Calculate accuracy (1 - error rate)
    char_accuracy = (1 - cer) * 100
    word_accuracy = (1 - wer) * 100
    
    return {
        'doc_id': doc_id,
        'cer': round(cer, 4),
        'wer': round(wer, 4),
        'char_accuracy': round(char_accuracy, 2),
        'word_accuracy': round(word_accuracy, 2),
        'char_count_gt': len(gt_normalized),
        'char_count_ocr': len(ocr_normalized),
        'word_count_gt': len(gt_normalized.split()),
        'word_count_ocr': len(ocr_normalized.split())
    }


def main():
    """Main evaluation function"""
    base_dir = Path(__file__).parent.parent / 'data' / 'raw'
    
    # Define document mappings (ground truth available)
    documents = [
        {
            'doc_id': 'dl_2025_0002',
            'ocr_file': base_dir / 'dl_2025_0002' / 'dl_2025_0002_scanned.txt',
            'ground_truth': base_dir / 'dl_2025_0002' / 'legit_0002.txt'
        },
        {
            'doc_id': 'dl_2025_0003',
            'ocr_file': base_dir / 'dl_2025_0003' / 'dl_2025_0003_protonx.txt',
            'ground_truth': base_dir / 'dl_2025_0003' / 'legit_dl_2025_0003.txt'
        },
        {
            'doc_id': 'dl_2025_0005',
            'ocr_file': base_dir / 'dl_2025_0005' / 'dl_2025_0005.jpg.txt',  # Will need to process
            'ground_truth': base_dir / 'dl_2025_0005' / 'legit_dl_2025_0005.txt'
        }
    ]
    
    results = []
    
    print("=" * 80)
    print("OCR ACCURACY EVALUATION")
    print("=" * 80)
    print()
    
    for doc in documents:
        print(f"📄 Evaluating {doc['doc_id']}...")
        result = evaluate_document(
            doc_id=doc['doc_id'],
            ocr_file=str(doc['ocr_file']),
            ground_truth_file=str(doc['ground_truth'])
        )
        results.append(result)
        
        if 'error' in result:
            print(f"   ❌ {result['error']}")
        else:
            print(f"   ✅ CER: {result['cer']:.4f} | WER: {result['wer']:.4f}")
            print(f"      Character Accuracy: {result['char_accuracy']:.2f}%")
            print(f"      Word Accuracy: {result['word_accuracy']:.2f}%")
        print()
    
    # Calculate average metrics (only successful evaluations)
    successful = [r for r in results if 'error' not in r]
    
    if successful:
        avg_cer = sum(r['cer'] for r in successful) / len(successful)
        avg_wer = sum(r['wer'] for r in successful) / len(successful)
        avg_char_acc = sum(r['char_accuracy'] for r in successful) / len(successful)
        avg_word_acc = sum(r['word_accuracy'] for r in successful) / len(successful)
        
        summary = {
            'total_documents': len(documents),
            'successful_evaluations': len(successful),
            'failed_evaluations': len(results) - len(successful),
            'average_cer': round(avg_cer, 4),
            'average_wer': round(avg_wer, 4),
            'average_char_accuracy': round(avg_char_acc, 2),
            'average_word_accuracy': round(avg_word_acc, 2),
            'details': results
        }
        
        print("=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"Successful evaluations: {len(successful)}/{len(documents)}")
        print(f"Average CER: {avg_cer:.4f}")
        print(f"Average WER: {avg_wer:.4f}")
        print(f"Average Character Accuracy: {avg_char_acc:.2f}%")
        print(f"Average Word Accuracy: {avg_word_acc:.2f}%")
        print("=" * 80)
    else:
        summary = {
            'error': 'No successful evaluations',
            'details': results
        }
    
    # Save results
    output_dir = Path(__file__).parent / 'results'
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / 'accuracy_report.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Results saved to: {output_file}")
    
    return summary


if __name__ == '__main__':
    main()
