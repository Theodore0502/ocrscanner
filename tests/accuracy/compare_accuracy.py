import difflib
from pathlib import Path

def calculate_accuracy(ground_truth_path, ocr_output_path):
    """Calculate detailed accuracy metrics between ground truth and OCR output."""
    
    # Read files
    with open(ground_truth_path, 'r', encoding='utf-8') as f:
        ground_truth = f.read()
    
    with open(ocr_output_path, 'r', encoding='utf-8') as f:
        ocr_output = f.read()
    
    # Basic stats
    print("="*80)
    print("📊 BASIC STATISTICS")
    print("="*80)
    print(f"Ground Truth: {len(ground_truth)} characters, {len(ground_truth.split())} words, {len(ground_truth.splitlines())} lines")
    print(f"OCR Output:   {len(ocr_output)} characters, {len(ocr_output.split())} words, {len(ocr_output.splitlines())} lines")
    
    # Character-level accuracy
    gt_chars = list(ground_truth)
    ocr_chars = list(ocr_output)
    
    matcher = difflib.SequenceMatcher(None, gt_chars, ocr_chars)
    char_ratio = matcher.ratio() * 100
    
    print(f"\n📝 CHARACTER-LEVEL ACCURACY: {char_ratio:.2f}%")
    
    # Word-level accuracy
    gt_words = ground_truth.split()
    ocr_words = ocr_output.split()
    
    matcher_words = difflib.SequenceMatcher(None, gt_words, ocr_words)
    word_ratio = matcher_words.ratio() * 100
    
    print(f"📝 WORD-LEVEL ACCURACY: {word_ratio:.2f}%")
    
    # Line-by-line comparison
    print("\n" + "="*80)
    print("📋 LINE-BY-LINE COMPARISON")
    print("="*80)
    
    gt_lines = ground_truth.splitlines()
    ocr_lines = ocr_output.splitlines()
    
    max_lines = max(len(gt_lines), len(ocr_lines))
    
    correct_lines = 0
    for i in range(max_lines):
        gt_line = gt_lines[i] if i < len(gt_lines) else ""
        ocr_line = ocr_lines[i] if i < len(ocr_lines) else ""
        
        gt_clean = gt_line.strip()
        ocr_clean = ocr_line.strip()
        
        if gt_clean == ocr_clean:
            status = "✅"
            correct_lines += 1
        else:
            status = "❌"
        
        print(f"\n{status} Line {i+1}:")
        print(f"  GT:  [{gt_clean}]")
        print(f"  OCR: [{ocr_clean}]")
        
        if gt_clean != ocr_clean:
            # Show differences
            s = difflib.SequenceMatcher(None, gt_clean, ocr_clean)
            diff_ratio = s.ratio() * 100
            print(f"  Similarity: {diff_ratio:.1f}%")
    
    line_accuracy = (correct_lines / max_lines * 100) if max_lines > 0 else 0
    print(f"\n📊 LINE ACCURACY: {correct_lines}/{max_lines} ({line_accuracy:.2f}%)")
    
    # Detailed diff
    print("\n" + "="*80)
    print("🔍 DETAILED CHARACTER DIFFERENCES")
    print("="*80)
    
    diff = difflib.unified_diff(
        ground_truth.splitlines(keepends=True),
        ocr_output.splitlines(keepends=True),
        fromfile='Ground Truth',
        tofile='OCR Output',
        lineterm=''
    )
    
    diff_lines = list(diff)
    if diff_lines:
        for line in diff_lines[:50]:  # Show first 50 lines of diff
            print(line.rstrip())
    else:
        print("✅ No differences found!")
    
    # Summary
    print("\n" + "="*80)
    print("📈 ACCURACY SUMMARY")
    print("="*80)
    print(f"Character-level: {char_ratio:.2f}%")
    print(f"Word-level:      {word_ratio:.2f}%")
    print(f"Line-level:      {line_accuracy:.2f}%")
    
    if char_ratio >= 90:
        grade = "🌟 EXCELLENT"
    elif char_ratio >= 80:
        grade = "👍 GOOD"
    elif char_ratio >= 70:
        grade = "⚠️ FAIR"
    else:
        grade = "❌ POOR"
    
    print(f"\nOverall Grade: {grade}")
    print("="*80)

if __name__ == "__main__":
    ground_truth_path = r"d:\Sources\-----OCR_Scanner\ocr_scanner\data\raw\dl_2025_0002\legit_0002.txt"
    ocr_output_path = r"d:\Sources\-----OCR_Scanner\ocr_scanner\data\raw\dl_2025_0002\dl_2025_0002_scanned.txt"
    
    calculate_accuracy(ground_truth_path, ocr_output_path)
