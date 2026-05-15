import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from src.ocr.engine_doctr import ocr_doctr_pdf

def main():
    pdf_path = r"data\raw\G11.31.KQ.19134.GXN.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"❌ Không tìm thấy file: {pdf_path}")
        return
    
    print(f"🔍 Đang scan PDF với DocTR Enhanced...")
    print(f"   Input: {pdf_path}")
    print()
    
    try:
        # OCR PDF
        text = ocr_doctr_pdf(pdf_path)
        
        # Tạo output path
        output_path = "data/results/G11.31.KQ.19134.GXN.txt"
        
        # Tạo thư mục output nếu chưa có
        output_dir = os.path.dirname(output_path)
        os.makedirs(output_dir, exist_ok=True)
        
        # Lưu ra file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f"✅ Hoàn thành!")
        print(f"   Đã lưu tại: {output_path}")
        print(f"   Kích thước: {len(text)} ký tự")
        print(f"   Số dòng: {text.count(chr(10)) + 1}")
        print()
        print("=" * 60)
        print("📄 NỘI DUNG:")
        print("=" * 60)
        print(text)
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Lỗi khi xử lý: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
