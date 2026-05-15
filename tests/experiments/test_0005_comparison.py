"""
Test ProtonX with document 0005
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from ocr_scanner.src.ocr.engine_paddle import (
    ocr_paddle_image,
    ocr_paddle_image_with_protonx
)

# Test image
image_path = r"ocr_scanner\data\raw\dl_2025_0005\dl_2025_0005.jpg"

print("=" * 80)
print("Testing: dl_2025_0005.jpg")
print("=" * 80)

# Check if file exists
if not os.path.exists(image_path):
    print(f"❌ File not found: {image_path}")
    exit(1)

# 1. Basic post-processing
print("\n🔧 Running with BASIC post-processing...")
basic_result = ocr_paddle_image(image_path, apply_postprocessing=True)

# 2. ProtonX correction
print("🔧 Running with PROTONX correction...")
protonx_result = ocr_paddle_image_with_protonx(image_path)

# Save outputs
basic_output = r"ocr_scanner\data\raw\dl_2025_0005\dl_2025_0005_basic.txt"
protonx_output = r"ocr_scanner\data\raw\dl_2025_0005\dl_2025_0005_protonx.txt"

with open(basic_output, 'w', encoding='utf-8') as f:
    f.write(basic_result)

with open(protonx_output, 'w', encoding='utf-8') as f:
    f.write(protonx_result)

print("\n" + "=" * 80)
print("BASIC POST-PROCESSING:")
print("=" * 80)
print(basic_result)

print("\n" + "=" * 80)
print("PROTONX CORRECTION:")
print("=" * 80)
print(protonx_result)

print("\n" + "=" * 80)
print("FILES SAVED:")
print("=" * 80)
print(f"Basic:   {basic_output}")
print(f"ProtonX: {protonx_output}")
print("=" * 80)

# Simple diff
basic_lines = basic_result.split('\n')
protonx_lines = protonx_result.split('\n')

differences = 0
for i, (b, p) in enumerate(zip(basic_lines, protonx_lines)):
    if b != p:
        differences += 1

print(f"\n📊 SUMMARY:")
print(f"Total lines: {len(basic_lines)}")
print(f"Lines with differences: {differences}")
if len(basic_lines) > 0:
    print(f"Improvement: {(differences/len(basic_lines)*100):.1f}% of lines corrected")
