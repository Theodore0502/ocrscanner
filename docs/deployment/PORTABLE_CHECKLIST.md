# 📦 Quick Checklist - Portable OCR Scanner

## ✅ Trước khi chuyển folder

- [x] Đã copy models vào `ocr_scanner/models/` (4.3GB)
- [x] Đã cập nhật code để load local models
- [x] Tất cả dependencies đã nằm trong `.venv`

## 📋 Trên máy mới

### 1. Kiểm tra Python

```powershell
python --version  # Cần >= 3.9
```

### 2. Activate Virtual Environment

```powershell
cd path\to\ocr_scanner
.\.venv\Scripts\Activate.ps1
```

### 3. Test

```powershell
# Test imports
python -c "from src.ocr import engine_doctr; print('OK')"

# Test local ProtonX model
python -c "from src.ocr.engine_protonx_correction import correct_vietnamese_text_protonx; print(correct_vietnamese_text_protonx('test'))"
```

## ⚠️ Lưu ý quan trọng

### Phải copy đầy đủ

- ✅ `ocr_scanner/.venv/` - Virtual environment (có thể rebuild)
- ✅ `ocr_scanner/models/` - **QUAN TRỌNG!** AI models (4.3GB)
- ✅ `ocr_scanner/data/processed/` - Vietnamese dictionary
- ✅ Toàn bộ source code

### Không cần copy

- ❌ `.git/` - Git history (không cần thiết)
- ❌ `__pycache__/` - Python cache (tự tạo lại)
- ❌ `uploads/` - Temporary uploads

## 🆘 Nếu gặp lỗi

### Virtual environment không chạy

```powershell
# Xóa và rebuild
Remove-Item -Recurse .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Model tải từ internet

→ Kiểm tra folder `models/protonx-legal-tc/` đã copy đủ chưa (4.3GB)

---

📖 **Chi tiết**: Xem file `PORTABLE_SETUP.md`
