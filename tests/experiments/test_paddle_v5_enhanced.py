"""
Simple test to verify PaddleOCR v5 engine works and measure accuracy
Saves output to file to avoid console encoding issues
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from ocr_scanner.src.ocr.engine_paddle import ocr_paddle_image_detailed
import difflib

def calculate_accuracy(ground_truth, ocr_output):
    """Calculate character-level accuracy"""
    gt_chars = list(ground_truth)
    ocr_chars = list(ocr_output)
    matcher = difflib.SequenceMatcher(None, gt_chars, ocr_chars)
    return matcher.ratio() * 100

# Test document
image_path = r"ocr_scanner\data\raw\dl_2025_0002\dl_2025_0002.jpg"
ground_truth_path = r"tests\accuracy\ground_truth\legit_0002.txt"
output_path = r"ocr_scanner\data\raw\dl_2025_0002\dl_2025_0002_paddle_v5_enhanced.txt"

print("Testing PaddleOCR v5 with Enhanced Post-Processing...")
print(f"Image: {image_path}")

# Run OCR
result = ocr_paddle_image_detailed(image_path, apply_postprocessing=True)

# Save output
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(result['text'])

print(f"\nSaved to: {output_path}")
print(f"Lines detected: {len(result['lines'])}")
print(f"Average confidence: {result['avg_confidence']:.2%}")

# Calculate accuracy
with open(ground_truth_path, 'r', encoding='utf-8') as f:
    ground_truth = f.read()

accuracy = calculate_accuracy(ground_truth, result['text'])

print(f"\n{'='*60}")
print(f"ACCURACY: {accuracy:.2f}%")
print(f"{'='*60}")

if accuracy >= 90:
    print("\nSUCCESS: Meets 90% accuracy threshold!")
else:
    print(f"\nNEEDS IMPROVEMENT: {90 - accuracy:.2f}% below target")

print(f"\nTo see output:\ntype {output_path}")
