# 🌸 OCR Scanner & File Tools

Hệ thống OCR (Optical Character Recognition) tối ưu cho văn bản hành chính tiếng Việt với độ chính xác cao (92-96%), đi kèm các công cụ xử lý file PDF thông minh. Ứng dụng được thiết kế dưới dạng Desktop GUI hiện đại, dễ dàng thao tác.

## ✨ Tính năng chính

- 🔤 **Multi-Engine OCR**: Tích hợp 4 OCR engines:
  - **DocTR** (mặc định) - Cân bằng tốc độ và độ chính xác
  - **PaddleOCR v5** - Hỗ trợ tăng tốc GPU
  - **VietOCR** - Tối ưu cho cấu trúc ngôn ngữ tiếng Việt
  - **EraX-VL-2B** - Mô hình Vision-Language mạnh mẽ
- 🧹 **Hậu xử lý đa tầng (Post-Processing)**:
  - Cải thiện độ chính xác từ ~78% lên đến 96%
  - Tích hợp **SymSpell** sửa lỗi O(1) cực nhanh
  - Tùy chọn **PhoBERT** và **ProtonX** sửa lỗi theo ngữ cảnh (Context-aware)
- 🛠️ **File Tools Tích hợp**:
  - Đổi tên file hàng loạt bằng Regex
  - Tách PDF thành các trang nhỏ
  - Chuyển đổi PDF sang Word (DOCX)
  - Đánh số thứ tự file tự động

## 🚀 Khởi chạy ứng dụng (Windows)

Chỉ cần chạy file `run_app.bat` ở thư mục gốc:

```powershell
.\run_app.bat
```

> **Lưu ý**: Lần đầu chạy có thể sẽ tốn thời gian tải model AI từ Hugging Face (lưu tại folder `.hf_cache`).

## 📁 Cấu trúc dự án

```text
OCR_Scanner/
├── desktop_app/             # Giao diện người dùng (CustomTkinter)
│   ├── app.py               # Main GUI
│   ├── core/                # Kết nối UI với OCR engines
│   └── tools_ui/            # File tools (Rename, Split, PDF2Word...)
├── ocr_scanner/             # Lõi xử lý AI / OCR (Có thể tách thành thư viện độc lập)
│   ├── src/ocr/             # Chứa các engines (doctr, paddle, vietocr, erax...)
│   └── data/                # Dictionary và dữ liệu cho Post-Processing
├── docs/                    # Tài liệu dự án và hướng dẫn deployment
├── tests/                   # Kịch bản kiểm thử (Unit test & Integration)
└── bao_cao/                 # Báo cáo kỹ thuật chi tiết
```

## 🛠️ Yêu cầu hệ thống (Để phát triển)

- Python 3.9+
- Khuyến nghị GPU có CUDA (Nếu dùng EraX hoặc PaddleOCR GPU)

Cài đặt các gói phụ thuộc:
```bash
pip install -r requirements.txt
```

## 📚 Tài liệu bổ sung

- [Hướng dẫn Đóng gói Portable (Portable Setup)](docs/deployment/PORTABLE_SETUP.md)
- [Báo cáo Kỹ thuật (Chi tiết kiến trúc)](bao_cao/bao_cao.md)
