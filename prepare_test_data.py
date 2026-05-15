import sys
import os
import shutil
from pathlib import Path

# Cấu hình encoding cho terminal Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

source_dir = Path(r'F:\2020\Tháng 1\A308')
dest_dir = Path(r'f:\-----OCR_Scanner\test_data\GXN_pdfs')
dest_dir.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print(f"Đang tìm kiếm các file PDF có chứa 'GXN' tại:\n{source_dir}")
print("=" * 60)

found_files = []
if source_dir.exists():
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if 'gxn' in file.lower() and file.lower().endswith('.pdf'):
                found_files.append(Path(root) / file)
else:
    print(f"LỖI: Thư mục không tồn tại: {source_dir}")
    sys.exit(1)

print(f"-> Tìm thấy {len(found_files)} files hợp lệ.")
if len(found_files) == 0:
    print("Không có file nào được copy.")
    sys.exit(0)

print("\nĐang copy file sang thư mục test_data...")
for file_path in found_files:
    dest_path = dest_dir / file_path.name
    try:
        shutil.copy2(file_path, dest_path)
        print(f" [OK] Đã copy: {file_path.name}")
    except Exception as e:
        print(f" [LỖI] {file_path.name}: {e}")

# Gộp file bằng PyPDF2
print("\nĐang gộp các file PDF lại thành 1 file duy nhất (merged_GXN_test.pdf)...")
try:
    from PyPDF2 import PdfReader, PdfWriter
    merger = PdfWriter()
    
    for file_path in dest_dir.glob("*.pdf"):
        if file_path.name != "merged_GXN_test.pdf":
            reader = PdfReader(str(file_path))
            merger.append(reader)
            
    merged_path = dest_dir / "merged_GXN_test.pdf"
    with open(merged_path, "wb") as f_out:
        merger.write(f_out)
    print(f"\n=> THÀNH CÔNG! Đã gộp tất cả thành file: {merged_path}")
    print(f"   (Sử dụng file này để test kịch bản 'OCR PDF nhiều trang' của chức năng Performance Test)")

except ImportError:
    print("Không tìm thấy thư viện PyPDF2 để gộp file. Bỏ qua bước gộp.")
except Exception as e:
    print(f"Lỗi khi gộp file: {e}")

print("=" * 60)
print(f"Hoàn tất việc tập hợp file. Thư mục chứa file: {dest_dir}")
