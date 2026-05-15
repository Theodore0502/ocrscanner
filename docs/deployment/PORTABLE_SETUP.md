# 📦 OCR Scanner - Portable Setup Guide

Hướng dẫn setup dự án OCR Scanner trên máy mới (hoàn toàn offline sau khi copy).

---

## ✅ Điều kiện tiên quyết

### 1. Python 3.9+

Dự án yêu cầu Python 3.9 trở lên. Kiểm tra version hiện tại:

```powershell
python --version
```

Nếu chưa có, tải Python tại: https://www.python.org/downloads/

### 2. Visual C++ Redistributable (Windows)

Một số packages cần Visual C++ runtime. Download tại:

- https://aka.ms/vs/17/release/vc_redist.x64.exe

---

## 🚀 Hướng dẫn cài đặt

### Bước 1: Copy toàn bộ folder dự án

Copy toàn bộ folder `-----OCR_Scanner` sang ổ cứng mới (ví dụ: `F:\-----OCR_Scanner`)

### Bước 2: Activate Virtual Environment

Mở PowerShell và navigate đến folder dự án:

```powershell
cd F:\-----OCR_Scanner\ocr_scanner
```

Activate virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

> **Lưu ý**: Nếu gặp lỗi execution policy, chạy:
>
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### Bước 3: Test cài đặt

Kiểm tra xem virtual environment đã hoạt động:

```powershell
python --version
pip list
```

Bạn sẽ thấy danh sách các packages đã cài (torch, transformers, paddleocr, v.v.)

---

## 🧪 Test chức năng OCR

### Test 1: Import modules

```powershell
python -c "from src.ocr import engine_doctr, engine_paddle; print('✅ Imports OK')"
```

### Test 2: Test ProtonX model (local)

```powershell
python -c "from src.ocr.engine_protonx_correction import correct_vietnamese_text_protonx; print(correct_vietnamese_text_protonx('V vic np h so hc phí'))"
```

Nếu thành công, bạn sẽ thấy:

```
🔧 Initializing ProtonX Text Correction...
📁 Using local model: D:\Sources\...\models\protonx-legal-tc\...
✅ ProtonX ready on CPU
```

### Test 3: OCR một ảnh

```powershell
python scripts\scan_image_to_txt.py data\samples\sample.jpg
```

---

## ⚙️ Cấu hình nâng cao

### Sử dụng GPU (PaddleOCR)

Nếu máy mới có GPU CUDA, cài PaddlePaddle GPU version:

```powershell
pip install paddlepaddle-gpu==2.6.1.post120
```

### Rebuild virtual environment (nếu cần)

Nếu `.venv` không hoạt động do Python path khác, rebuild:

```powershell
# Xóa venv cũ
Remove-Item -Recurse -Force .venv

# Tạo venv mới
python -m venv .venv

# Activate
.\.venv\Scripts\Activate.ps1

# Cài lại packages
pip install -r requirements.txt
```

---

## 📂 Cấu trúc folder quan trọng

```
ocr_scanner/
├── .venv/                  # Virtual environment (có thể rebuild)
├── models/                 # Local AI models (QUAN TRỌNG!)
│   └── protonx-legal-tc/   # ProtonX model (4.3GB)
├── data/
│   ├── processed/
│   │   └── vietnamese_words.txt  # Vietnamese dictionary
│   └── samples/            # Test images
├── src/ocr/                # Source code
├── scripts/                # CLI scripts
└── requirements.txt        # Python dependencies
```

> **⚠️ QUAN TRỌNG**: Folder `models/` chứa AI models (4.3GB). Đảm bảo folder này được copy đầy đủ!

---

## 🔧 Troubleshooting

### Lỗi: `ModuleNotFoundError`

**Nguyên nhân**: Virtual environment chưa được activate hoặc bị hỏng

**Giải pháp**:

```powershell
# Activate lại venv
.\.venv\Scripts\Activate.ps1

# Hoặc rebuild nếu không được (xem phần "Cấu hình nâng cao")
```

### Lỗi: ProtonX model download từ internet

**Nguyên nhân**: Folder `models/protonx-legal-tc/` không được copy đầy đủ

**Giải pháp**: Đảm bảo toàn bộ folder `ocr_scanner/models/` được copy (4.3GB)

### Lỗi: DLL load failed (Windows)

**Nguyên nhân**: Thiếu Visual C++ Redistributable

**Giải pháp**: Cài Visual C++ runtime (xem "Điều kiện tiên quyết")

---

## ✨ Các tính năng hoạt động offline

✅ **DocTR OCR** - Engine mặc định
✅ **PaddleOCR** - CPU/GPU support  
✅ **VietOCR** - Chữ viết tay tiếng Việt
✅ **ProtonX Text Correction** - Load từ local models
✅ **SymSpell Spell Checker** - Vietnamese dictionary
✅ **Image Preprocessing** - Deskew, denoise

❌ **PhoBERT Correction** - Cần internet để download (tính năng tùy chọn, ít dùng)

---

## 📞 Support

Nếu gặp vấn đề, kiểm tra:

1. Python version (>= 3.9)
2. Virtual environment đã activate chưa
3. Folder `models/` có đầy đủ không (4.3GB)
4. Visual C++ Redistributable đã cài chưa

---

**Chúc bạn sử dụng thành công! 🎉**
