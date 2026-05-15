import sys
import os

# Add parent directory to path so we can import ocr_scanner
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Use current ocr_scanner package
from ocr_scanner.scripts.scan_image_to_txt import scan_image_to_txt


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Use command-line argument
        image_path = sys.argv[1]
        # Generate output path from input path
        base_dir = os.path.dirname(image_path)
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        output_path = os.path.join(base_dir, f"{base_name}_scanned.txt")
        
        scan_image_to_txt(image_path, output_path)
    else:
        print("Usage: python tools/scan_single_image.py <image_path>")
        sys.exit(1)
