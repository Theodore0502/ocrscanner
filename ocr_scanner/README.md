# OCR Scanner Core - Vietnamese Document OCR System

Hệ thống OCR (Optical Character Recognition) tối ưu cho văn bản tiếng Việt với độ chính xác cao và khả năng xử lý hậu kỳ nâng cao. Lõi xử lý này được thiết kế theo dạng module (Plugin Pattern), có thể hoạt động độc lập như một thư viện hoặc kết nối với giao diện Desktop GUI (`desktop_app`).

## ✨ Tính năng chính

- 🔤 **Multi-Engine OCR**: Hỗ trợ 4 OCR engines khác nhau:
  - **DocTR** (mặc định) - Cân bằng giữa tốc độ và độ chính xác
  - **PaddleOCR v5** - Hỗ trợ GPU, tốc độ cao
  - **VietOCR** - Tối ưu cho chữ viết tay tiếng Việt
  - **EraX-VL-2B** - Vision-Language Model mạnh mẽ, độ chính xác rất cao
  
- 🧹 **Advanced Post-Processing (4 tầng)**: 
  - Rule-based: Hơn 250+ quy tắc sửa lỗi tự động
  - SymSpell: Sửa lỗi chính tả với độ phức tạp O(1) (Nhanh hơn 1000x brute-force)
  - PhoBERT: Sửa lỗi dựa trên ngữ cảnh (Masked Language Model)
  - ProtonX: Sửa lỗi chuyên sâu hành chính / pháp lý
  
- 📄 **Multi-Format Support**: Hình ảnh (JPG, PNG) và PDF.

## 📦 Cài đặt Core Engine

Yêu cầu: Python 3.9+

```bash
# Sử dụng virtual environment ở thư mục root
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Cài đặt (khuyến khích có CUDA)
pip install -r ../requirements.txt
```

## 🚀 Sử dụng như một Thư viện (Library)

```python
import sys
sys.path.append('path/to/ocr_scanner')

from src.ocr.engine_doctr import ocr_doctr_image
from src.ocr.postprocess_pipeline import apply_rule_based_fixes

# Chạy OCR cơ bản
raw_text = ocr_doctr_image("sample.jpg")

# Hậu xử lý
clean_text = apply_rule_based_fixes(raw_text)
print(clean_text)
```

## ⚙️ Configuration (`config.json`)

Tất cả cấu hình nằm trong `config.json`:

```json
{
  "ocr": {
    "default_engine": "doctr",
    "preprocessing": {
      "enabled": true,
      "deskew": true,
      "denoise": true
    }
  },
  "post_processing": {
    "use_fast_spell_checker": true,
    "use_phobert_correction": false,
    "use_protonx_correction": false
  }
}
```

## 📁 Cấu trúc Lõi OCR (`ocr_scanner/`)

```text
ocr_scanner/
├── config.json                     # Cấu hình trung tâm
├── data/
│   ├── raw/                        # Thư mục input mặc định
│   └── processed/
│       └── vietnamese_words.txt    # Từ điển tiếng Việt cho SymSpell
├── src/
│   └── ocr/
└── web/                            # Web API
    ├── main.py                     # FastAPI server
    ├── templates/                  # HTML templates
    └── static/                     # CSS/JS assets
```

---

## 🔧 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'doctr'`

**Solution:**
```bash
pip install python-doctr
```

### Issue: OCR kết quả kém với ảnh nghiêng

**Solution:** Bật preprocessing trong `config.json`:
```json
{
  "ocr": {
    "preprocessing": {
      "enabled": true,
      "deskew": true
    }
  }
}
```

### Issue: Spell checker chậm

**Solution:** Đảm bảo đang dùng SymSpell:
```json
{
  "post_processing": {
    "use_fast_spell_checker": true,
    "use_phobert_correction": false
  }
}
```

### Issue: `FileNotFoundError` khi load dictionary

**Solution:** Kiểm tra path trong `config.json`:
```json
{
  "paths": {
    "vietnamese_dictionary": "data/processed/vietnamese_words.txt"
  }
}
```

---

## 🎯 Roadmap

- [ ] Support more OCR engines (Tesseract 5.0, EasyOCR)
- [ ] Batch processing API endpoint
- [ ] Docker containerization
- [ ] Web UI with real-time preview
- [ ] Support more languages (Thai, Khmer, Lao)
- [ ] GPU optimization for SymSpell
- [ ] Export to structured formats (JSON, XML, DOCX)

---

## 📝 License

[Add your license here]

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📧 Contact

[Add contact information]

---

## 🙏 Acknowledgments

- **DocTR** - Mindee OCR toolkit
- **PaddleOCR** - PaddlePaddle OCR toolkit
- **VietOCR** - Vietnamese OCR by pbcquoc
- **PhoBERT** - VinAI Research
- **SymSpell** - Algorithm by Wolf Garbe
