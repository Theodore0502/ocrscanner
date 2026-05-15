"""
Compare ProtonX output with ground truth (legit) for document 0003
Calculate actual character-level accuracy
"""

import sys
import os
import difflib

sys.path.insert(0, os.path.dirname(__file__))

# File paths
legit_file = r"ocr_scanner\data\raw\dl_2025_0003\legit_dl_2025_0003.txt"
basic_file = r"ocr_scanner\data\raw\dl_2025_0003\dl_2025_0003_basic.txt"
protonx_file = r"ocr_scanner\data\raw\dl_2025_0003\dl_2025_0003_protonx.txt"

# Read files
with open(legit_file, 'r', encoding='utf-8') as f:
    legit_text = f.read()

with open(basic_file, 'r', encoding='utf-8') as f:
    basic_text = f.read()

with open(protonx_file, 'r', encoding='utf-8') as f:
    protonx_text = f.read()

# Calculate character-level accuracy
def calculate_accuracy(ground_truth, ocr_output):
    """Calculate character-level accuracy using sequence matcher"""
    matcher = difflib.SequenceMatcher(None, ground_truth, ocr_output)
    return matcher.ratio() * 100

# Line-by-line comparison
legit_lines = legit_text.split('\n')
basic_lines = basic_text.split('\n')
protonx_lines = protonx_text.split('\n')

print("=" * 80)
print("ACCURACY COMPARISON - Document 0003")
print("=" * 80)

# Overall accuracy
basic_accuracy = calculate_accuracy(legit_text, basic_text)
protonx_accuracy = calculate_accuracy(legit_text, protonx_text)

print(f"\n📊 CHARACTER-LEVEL ACCURACY:")
print(f"{'Method':<20} {'Accuracy':<15} {'Improvement'}")
print("-" * 50)
print(f"{'Basic Post-Process':<20} {basic_accuracy:>6.2f}%")
print(f"{'ProtonX Correction':<20} {protonx_accuracy:>6.2f}%      +{protonx_accuracy - basic_accuracy:.2f}%")

print(f"\n📈 LINE-BY-LINE ANALYSIS:")
print(f"Total lines: {len(legit_lines)}")

# Count perfect matches
basic_perfect = sum(1 for l, b in zip(legit_lines, basic_lines) if l == b)
protonx_perfect = sum(1 for l, p in zip(legit_lines, protonx_lines) if l == p)

print(f"Perfect line matches:")
print(f"  Basic:   {basic_perfect}/{len(legit_lines)} ({basic_perfect/len(legit_lines)*100:.1f}%)")
print(f"  ProtonX: {protonx_perfect}/{len(legit_lines)} ({protonx_perfect/len(legit_lines)*100:.1f}%)")

# Show differences
print(f"\n🔍 SAMPLE DIFFERENCES:")
print("-" * 80)

shown = 0
max_show = 10

for i, (legit, basic, protonx) in enumerate(zip(legit_lines, basic_lines, protonx_lines), 1):
    if legit != protonx and shown < max_show:
        shown += 1
        print(f"\nLine {i}:")
        print(f"  Legit:   {legit}")
        print(f"  Basic:   {basic}")
        print(f"  ProtonX: {protonx}")
        
        # Show if ProtonX is closer to legit than basic
        legit_basic_sim = difflib.SequenceMatcher(None, legit, basic).ratio()
        legit_protonx_sim = difflib.SequenceMatcher(None, legit, protonx).ratio()
        
        if legit_protonx_sim > legit_basic_sim:
            print(f"  ✅ ProtonX closer to ground truth ({legit_protonx_sim:.2%} vs {legit_basic_sim:.2%})")
        elif legit_protonx_sim < legit_basic_sim:
            print(f"  ⚠️ Basic was better ({legit_basic_sim:.2%} vs {legit_protonx_sim:.2%})")
        else:
            print(f"  ≈ Same similarity")

print("\n" + "=" * 80)
print("CONCLUSION")
print("=" * 80)
print(f"ProtonX achieved {protonx_accuracy:.2f}% accuracy")
print(f"Improvement over basic: +{protonx_accuracy - basic_accuracy:.2f}%")
print(f"Perfect lines: {protonx_perfect}/{len(legit_lines)} ({protonx_perfect/len(legit_lines)*100:.1f}%)")
