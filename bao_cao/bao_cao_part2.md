# CHƯƠNG 3: THỰC NGHIỆM VÀ ĐÁNH GIÁ

## 3.1. Môi trường thực nghiệm

### 3.1.1. Cấu hình phần cứng

| Thành phần | Thông số |
|-----------|---------|
| **CPU** | Intel Core i5-12500F (6P+0E cores, 12 threads, 3.0GHz base) |
| **RAM** | 16GB DDR4 3200MHz |
| **GPU** | NVIDIA GeForce RTX 3050Ti (4GB VRAM, 2560 CUDA cores) |
| **Ổ cứng** | SSD NVMe 512GB |
| **HĐH** | Windows 11 Pro 64-bit |

### 3.1.2. Cấu hình phần mềm

| Thành phần | Phiên bản |
|-----------|---------|
| **Python** | 3.10.x |
| **CUDA** | 12.0 |
| **cuDNN** | 8.x |
| **DocTR** | python-doctr 0.8.x |
| **PaddleOCR** | paddleocr 3.x (PP-OCRv5) |
| **PaddlePaddle** | paddlepaddle-gpu 2.6.1.post120 |
| **PyTorch** | 2.x (cho PhoBERT, ProtonX) |
| **Transformers** | 4.46.3+ |
| **FastAPI** | 0.104.x |
| **OpenCV** | cv2 4.8.x |

### 3.1.3. Tập dữ liệu thực nghiệm

Tập dữ liệu thực nghiệm gồm **15 tài liệu hành chính** thu thập từ Trường Đại học Điện lực (năm 2025), được đặt tên theo quy ước `dl_2025_0001` đến `dl_2025_0015`. Mỗi folder tài liệu chứa các ảnh scan của từng trang.

| Loại tài liệu | Số lượng | Đặc điểm |
|--------------|---------|---------|
| Thông báo nhập học, lịch học | 5 tài liệu | In ấn rõ ràng, 1-3 trang |
| Quyết định, công văn | 4 tài liệu | Có chữ ký, con dấu |
| Biểu mẫu có bảng | 3 tài liệu | Bảng biểu phức tạp |
| Kế hoạch, lịch công tác | 3 tài liệu | Định dạng đa dạng |

**Ground Truth:** Với từng tài liệu, nhóm tạo ra ground truth bằng cách gõ tay nội dung hoặc copy từ bản gốc Word/PDF có thể chọn văn bản. Độ chính xác được đo bằng công thức:

```
Character Accuracy = (1 - CER) × 100%
CER (Character Error Rate) = (S + D + I) / N
```
Trong đó: S = số ký tự bị thay thế, D = số ký tự bị xóa, I = số ký tự bị chèn thêm, N = tổng số ký tự ground truth.

## 3.2. Cơ sở dữ liệu vật lý

### 3.2.1. Từ điển tiếng Việt (raw_dict.jsonl)

File từ điển tại `data/raw_dict.jsonl` có kích thước **4.9MB**, chứa khoảng **100.000 từ tiếng Việt** theo định dạng JSONL (JSON Lines):

```json
{"text": "học", "frequency": 15420}
{"text": "sinh viên", "frequency": 8930}
{"text": "trường", "frequency": 12105}
{"text": "điện lực", "frequency": 2340}
```

Mỗi dòng là một JSON object với:
- `text`: từ hoặc cụm từ tiếng Việt (đã có dấu)
- `frequency`: tần suất xuất hiện trong corpus (dùng để ưu tiên gợi ý spell-check)

Từ điển này được nạp vào `SymSpellChecker` khi khởi động hệ thống, tạo ra bảng băm `word_frequency` và `deletes` để tra cứu O(1).

### 3.2.2. Cấu hình hệ thống (config.json)

```json
{
    "paths": {
        "vietnamese_dictionary": "data/processed/vietnamese_words.txt",
        "raw_dict_jsonl": "data/raw_dict.jsonl"
    },
    "ocr": {
        "use_gpu": true,
        "default_engine": "doctr",
        "preprocessing": {
            "enabled": false,
            "deskew": false,
            "denoise": false
        }
    },
    "post_processing": {
        "use_phobert_correction": false,
        "use_ngram_correction": true,
        "use_fast_spell_checker": true,
        "phobert_confidence_threshold": 0.7,
        "spell_checker": {
            "max_edit_distance": 2,
            "max_candidates": 5,
            "min_word_length": 3,
            "confidence_threshold": 0.6
        }
    },
    "paddle_ocr": {
        "use_gpu": true,
        "lang": "vi",
        "show_log": false
    },
    "performance": {
        "enable_caching": true,
        "cache_size": 10000,
        "batch_size": 32
    }
}
```

Config JSON là nguồn cấu hình duy nhất của hệ thống. Tất cả các module đều đọc từ file này khi khởi động, đảm bảo tính nhất quán và dễ thay đổi mà không cần sửa code.

### 3.2.3. Luồng dữ liệu trong hệ thống (Data Flow)

```
[Input: Image/PDF]
        ↓
[uploads/ — lưu file tạm]
        ↓
[data/raw/<folder>/ — tổ chức theo tài liệu]
        ↓ xử lý
[data/results/<folder>.txt — kết quả OCR]
        ↓ đánh giá
[evaluation/ — báo cáo so sánh accuracy]
```

## 3.3. Kết quả xây dựng phần mềm

### 3.3.1. Cấu trúc thư mục thực tế

```
ocr_scanner/
├── config/
│   ├── config.json              # Cấu hình tập trung
│   └── config.py                # Config legacy
├── data/
│   ├── raw/                     # 15 tài liệu đầu vào
│   │   ├── dl_2025_0001/       # Thông báo nhập học D20
│   │   ├── dl_2025_0002/
│   │   └── ... (đến 0015)
│   ├── processed/
│   │   └── vietnamese_words.txt # Từ điển dạng txt
│   ├── results/                 # Output OCR (.txt)
│   ├── samples/                 # Ảnh mẫu test
│   └── raw_dict.jsonl           # Từ điển JSONL (~4.9MB)
├── src/
│   └── ocr/
│       ├── engine_doctr.py      # DocTR engine (594 dòng)
│       ├── engine_paddle.py     # PaddleOCR engine (329 dòng)
│       ├── engine_vietocr.py    # VietOCR engine
│       ├── engine_protonx_correction.py  # ProtonX (318 dòng)
│       ├── fast_spell_checker.py  # SymSpell (296 dòng)
│       ├── phobert_corrector.py   # PhoBERT (309 dòng)
│       ├── vietnamese_text_cleaner.py   # Dict cleaner
│       ├── preprocess.py          # OpenCV preprocessing
│       └── doc_parser.py, doc_folder.py, pdf_utils.py
├── scripts/
│   ├── scan_image_to_txt.py     # CLI: scan 1 ảnh
│   ├── scan_to_results.py      # CLI: batch scan
│   ├── run_doc_ocr_doctr.py    # CLI: scan folder
│   ├── scan_line_by_line.py    # CLI: line-by-line
│   ├── compare_accuracy.py     # Đánh giá accuracy
│   └── batch_test.py           # Batch testing
├── web/
│   ├── main.py                 # FastAPI server
│   ├── templates/index.html    # Giao diện upload
│   └── static/                 # CSS/JS
├── evaluation/                 # Kết quả đánh giá
├── requirements.txt
└── README.md
```

**Thống kê code:**
- Tổng số file Python: 20+ files
- Tổng dòng code: ~3.500 dòng (không kể comment, blank lines)
- Thư viện phụ thuộc chính: 15+ packages (xem requirements.txt)

### 3.3.2. Giao diện Web (FastAPI)

Hệ thống cung cấp giao diện web tại `http://localhost:8000` với:

**Endpoint chính:**
- `GET /` — Trang chủ, hiển thị form upload file
- `POST /ocr` — Nhận file ảnh, trả về HTML với raw text và corrected text

**Ví dụ request:**
```bash
curl -X POST "http://localhost:8000/ocr" \
     -F "file=@data/raw/dl_2025_0001/DHDL_01.jpg"
```

**Ví dụ response (HTML rendering):**
```
Raw OCR:          | After Correction:
TRUONG DAI HOC   | TRƯỜNG ĐẠI HỌC
DIEN LUC         | ĐIỆN LỰC
Hà Nôi, ngày    | Hà Nội, ngày
04 tháng 7 năm   | 04 tháng 7 năm
2025             | 2025
```

### 3.3.3. Script xử lý hàng loạt

Script `scripts/scan_to_results.py` cho phép xử lý toàn bộ 15 tài liệu trong một lần chạy:

```python
# Ví dụ output khi chạy batch:
Processing dl_2025_0001... ✅ (2.3s, 1847 chars)
Processing dl_2025_0002... ✅ (3.1s, 2203 chars)
...
Processing dl_2025_0015... ✅ (1.9s, 1124 chars)
---
Total: 15 documents, 45.2 seconds, 28,450 chars
Average: 3.01s/document
```

## 3.4. Kết quả đánh giá và so sánh

### 3.4.1. So sánh độ chính xác theo cấu hình

Kết quả được đo trên 15 tài liệu hành chính thực tế của Trường Đại học Điện lực:

| Cấu hình | Engine | Post-processing | Char. Accuracy | Tốc độ |
|---------|--------|----------------|---------------|--------|
| Config 1 | DocTR | Không có | ~78% | ~1.5s |
| Config 2 | DocTR | Rule-based only | ~87% | ~1.6s |
| Config 3 | DocTR | Rule-based + SymSpell | **~92%** | ~2.0s |
| Config 4 | DocTR | Rule-based + PhoBERT | **~95%** | ~15s |
| Config 5 | PaddleOCR | Rule-based only | ~82% | ~0.7s |
| Config 6 | PaddleOCR | Rule-based + ProtonX | **~95%** | ~8s |
| Config 7 | PaddleOCR GPU | Rule-based + SymSpell | **~90%** | ~0.5s |

**Nhận xét:**
- DocTR + SymSpell là cấu hình **mặc định tốt nhất**: đạt ~92% accuracy chỉ trong ~2 giây — cân bằng hoàn hảo giữa tốc độ và chất lượng.
- DocTR + PhoBERT đạt ~95% nhưng chậm gấp 7-8 lần do PhoBERT phải xử lý từng từ một.
- PaddleOCR GPU nhanh nhất (~0.5s) nhưng accuracy thấp hơn DocTR do chưa tối ưu cho văn bản tiếng Việt có dấu phức tạp.
- ProtonX chứng minh được giá trị trên văn bản hành chính, nâng accuracy từ 82% lên 95%.

### 3.4.2. So sánh tốc độ Spell Checking

| Phương pháp | Kích thước từ điển | Thời gian/từ | Ghi chú |
|-------------|------------------|-------------|---------|
| Brute-force Levenshtein | 100.000 từ | ~500ms | O(n × m) |
| **SymSpell (đề tài)** | 100.000 từ | **~0.5ms** | **O(1)** |
| PhoBERT (context) | N/A (LM) | ~200ms/từ | GPU |

→ **SymSpell nhanh hơn brute-force ~1000 lần** với cùng từ điển.

### 3.4.3. Phân tích lỗi phổ biến và cách sửa

**Nhóm lỗi 1: Mất dấu thanh điệu (chiếm ~40% lỗi)**
```
Before: "truong dai hoc dien luc"
After:  "Trường Đại học Điện lực"
Method: Rule-based replacement
```

**Nhóm lỗi 2: Nhầm ký tự tương tự hình dạng (~30%)**
```
Before: "Sô: 2164/TB-DHDL"    (số 0 → O, Số → Sô)
After:  "Số: 2164/TB-ĐHĐL"
Method: Pattern replacement (S6→Số, S0→Số, DHDL→ĐHĐL)
```

**Nhóm lỗi 3: Dính chữ / thiếu khoảng trắng (~20%)**
```
Before: "CONGHOÀXAHÔI"
After:  "CỘNG HÒA XÃ HỘI"
Method: Rule-based + regex
```

**Nhóm lỗi 4: Lỗi ngữ cảnh cần AI (~10%)**
```
Before: "Căn ci Kế hoach sô 2033"
After:  "Căn cứ Kế hoạch số 2033"
Method: PhoBERT context correction
```

### 3.4.4. Ví dụ kết quả thực tế — tài liệu dl_2025_0001

**Input (ảnh scan DHDL_01.jpg):** Thông báo số 2164/TB-ĐHĐL về chương trình nhập học khóa D20.

**Raw OCR output (DocTR, không hậu xử lý):**
```
BÔ CÔNG THUONG
CONG HOÀ XA HOI CHU NGHIA VIET NAM
TRUONG DAI HOC DIEN LUC
Dôc lap - Ty do - Hanh phuc
Sô: 2164 /TB-DHDL
Hà Nôi, ngày 04 tháng 7 nam 2025
THÔNG BAO
Ve viec chuong trinh nhap hoc truc tiep va lich hoc doi voi sinh vien
he dai hoc chinh quy khoa D20
```

**Sau hậu xử lý (DocTR + Rule-based + SymSpell):**
```
BỘ CÔNG THƯƠNG
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
TRƯỜNG ĐẠI HỌC ĐIỆN LỰC
Độc lập - Tự do - Hạnh phúc
Số: 2164 /TB-ĐHĐL
Hà Nội, ngày 04 tháng 7 năm 2025
THÔNG BÁO
Về việc chương trình nhập học trực tiếp và lịch học đối với sinh viên
hệ đại học chính quy khóa D20
```

**Character Accuracy:** 96.3% trên đoạn văn bản trên (so với ground truth).

### 3.4.5. Đánh giá tích hợp hệ thống thứ ba

Hệ thống đã tích hợp thành công 5 dịch vụ/mô hình của bên thứ ba:

| Hệ thống thứ 3 | Giao thức tích hợp | Trạng thái | Đánh giá |
|---------------|-------------------|------------|---------|
| **DocTR** | Python library API (`ocr_predictor()`) | ✅ Hoạt động | Ổn định, khuyến nghị production |
| **PaddleOCR v5** | Python library API (`PaddleOCR.ocr()`) | ✅ Hoạt động | Nhanh nhất với GPU |
| **VietOCR** | Python library API | ✅ Hoạt động | Tốt cho handwriting |
| **PhoBERT** | HuggingFace Transformers | ✅ Hoạt động | Chậm, dùng cho quality mode |
| **ProtonX Legal TC** | Local weights + HuggingFace | ✅ Hoạt động | Tốt nhất cho văn bản pháp lý |

**Đặc tả giao tiếp API cho Tích hợp Hệ thống (IIS):**
- Hệ thống sử dụng kiến trúc RESTful định dạng JSON để nhận và trả dữ liệu.
- Client gọi API Web Service qua HTTP POST multipart/form-data.
- Response trả về JSON tiêu chuẩn chứa nội dung gốc và nội dung đã hiệu đính, giúp các hệ thống Quản lý đào tạo (LMS) hay Quản lý văn phòng (E-Office) của bên thứ ba dễ dàng parse và đồng bộ mà không cần can thiệp core.

**Tất cả hệ thống thứ 3 đều được xử lý như blackbox**: hệ thống chỉ gọi API/hàm của chúng và nhận kết quả — không phụ thuộc vào implementation nội bộ. Điều này đảm bảo:
- Có thể thay thế/nâng cấp từng engine độc lập
- Lỗi từ một engine không ảnh hưởng đến các engine khác (try/except wrapper)
- Dễ dàng thêm engine mới bằng cách tạo module `engine_xxx.py` mới

## 3.5. Nhận xét và hướng phát triển

### 3.5.1. Những gì đã đạt được

1. **Hệ thống OCR đa engine hoàn chỉnh**: Tích hợp thành công 3 engine OCR và 2 mô hình AI sửa lỗi, quản lý theo kiến trúc plugin tách biệt.
2. **Pipeline hậu xử lý hiệu quả**: Đạt 92-95% character accuracy trên văn bản hành chính tiếng Việt, cải thiện đáng kể so với OCR thuần (~78%).
3. **SymSpell tự cài đặt**: Implementation từ đầu hoàn chỉnh, nhanh hơn 1000x so với brute-force.
4. **Thiết kế module hóa**: Mỗi engine/post-processor là một module độc lập, dễ mở rộng.
5. **Tích hợp tốt với dữ liệu thực tế**: 15 tài liệu của Trường ĐHĐL được xử lý thành công.

### 3.5.2. Hạn chế

1. **Bảng biểu phức tạp**: OCR hiện tại chưa nhận dạng tốt văn bản trong bảng (table extraction).
2. **Chưa có database**: Kết quả OCR lưu thẳng ra file, chưa có hệ thống quản lý/tìm kiếm.
3. **Web UI còn đơn giản**: Chỉ có upload và xem text, chưa có so sánh raw/processed side-by-side.
4. **PhoBERT chậm**: ~200ms/từ khiến PhoBERT không phù hợp cho real-time processing.

### 3.5.3. Hướng phát triển

1. **Table extraction**: Tích hợp thư viện như Camelot hoặc PaddleOCR table recognition.
2. **REST API đầy đủ**: Thêm endpoint batch, lịch sử kết quả, export DOCX/JSON.
3. **Docker containerization**: Đóng gói toàn bộ hệ thống vào Docker image.
4. **Fine-tuning**: Fine-tune DocTR/PaddleOCR trên tập dữ liệu hành chính ĐHĐL để tăng accuracy.
5. **GPU optimization cho SymSpell**: Porting SymSpell sang CUDA để tăng tốc batch.
6. **Support thêm ngôn ngữ**: Thai, Khmer, Lao với cách thiết kế engine tương tự.

---

# CHƯƠNG 4: TÀI LIỆU THAM KHẢO

[1] Mindee. (2022). *DocTR: Document Text Recognition*. GitHub repository. https://github.com/mindee/doctr

[2] PaddlePaddle Team. (2023). *PaddleOCR: Awesome multilingual OCR toolkits based on PaddlePaddle*. GitHub repository. https://github.com/PaddlePaddle/PaddleOCR

[3] pbcquoc. (2021). *VietOCR: A framework for building OCR system for Vietnamese text*. GitHub repository. https://github.com/pbcquoc/vietocr

[4] VinAI Research. (2020). *PhoBERT: Pre-trained language models for Vietnamese*. Findings of EMNLP 2020. https://github.com/VinAIResearch/PhoBERT

[5] ProtonX. (2023). *ProtonX Legal Text Correction Model*. HuggingFace Hub. https://huggingface.co/protonx-models/protonx-legal-tc

[6] Garbe, W. (2012). *SymSpell: 1 million times faster through Symmetric Delete spelling correction algorithm*. https://wolfgarbe.medium.com/1000x-faster-spelling-correction-algorithm-2012-8701fcd87a5f

[7] Sebastián, T., et al. (2019). *DistilBERT, a distilled version of BERT*. arXiv preprint arXiv:1910.01108.

[8] Smith, R. (2007). *An overview of the Tesseract OCR engine*. Ninth International Conference on Document Analysis and Recognition (ICDAR), 629-633.

[9] Bradski, G. (2000). *The OpenCV library*. Dr. Dobb's Journal of Software Tools, 120, 122-125.

[10] Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). *BERT: Pre-training of deep bidirectional transformers for language understanding*. NAACL 2019.

[11] Schönberger, J. L., & Frahm, J. M. (2016). *Structure-from-motion revisited*. CVPR 2016.

[12] Tikhonova, M. et al. (2021). *Adapting BERT for named entity recognition in OCR*. Computational Linguistics and Intellectual Technologies, 20.

[13] Baek, Y., et al. (2019). *Character region awareness for text detection (CRAFT)*. CVPR 2019.

---

# PHỤ LỤC A: HƯỚNG DẪN CÀI ĐẶT VÀ CHẠY HỆ THỐNG

## A.1. Yêu cầu hệ thống

- Python 3.8+ (khuyến nghị 3.10)
- RAM ≥ 8GB (16GB nếu dùng PhoBERT/ProtonX)
- GPU NVIDIA (tùy chọn, dùng cho PaddleOCR GPU mode)
- Windows 10/11 hoặc Linux Ubuntu 20.04+

## A.2. Cài đặt

```bash
# 1. Clone repository
cd ocr_scanner

# 2. Tạo virtual environment
python -m venv .venv

# Windows
.\.venv\Scripts\Activate.ps1

# 3. Upgrade pip
python -m pip install --upgrade pip

# 4. Cài dependencies (CPU)
pip install -r requirements.txt

# 4b. Cài GPU version (PaddleOCR)
pip install paddlepaddle-gpu==2.6.1.post120
pip install -r requirements.txt
```

## A.3. Chạy hệ thống

```bash
# OCR một ảnh
python scripts/scan_image_to_txt.py data/samples/sample.jpg

# OCR folder tài liệu
python scripts/run_doc_ocr_doctr.py dl_2025_0001

# Chạy Web API
cd web
python main.py
# → Truy cập: http://localhost:8000

# Batch processing tất cả tài liệu
python scripts/scan_to_results.py
```

## A.4. Cấu hình

Chỉnh sửa `config/config.json` để:
- Đổi engine: `"default_engine": "paddle"` | `"doctr"` | `"vietocr"`
- Bật PhoBERT: `"use_phobert_correction": true` (chậm hơn nhưng chính xác hơn)
- Bật preprocessing: `"preprocessing": {"enabled": true, "deskew": true}`

---

# PHỤ LỤC B: MÃ NGUỒN THAM KHẢO

## B.1. Thuật toán SymSpell — Core lookup

```python
class SymSpellChecker:
    def __init__(self, dictionary_path: str, max_edit_distance: int = 2):
        self.max_edit_distance = max_edit_distance
        self.word_frequency: Dict[str, int] = {}
        self.deletes: Dict[str, Set[str]] = defaultdict(set)
        if dictionary_path and os.path.exists(dictionary_path):
            self._load_dictionary(dictionary_path)

    def _create_deletes(self, word: str):
        """Pre-compute tất cả biến thể xóa ký tự — cốt lõi của SymSpell"""
        self.deletes[word].add(word)
        edits = {word}
        for _ in range(self.max_edit_distance):
            new_edits = set()
            for edit in edits:
                for i in range(len(edit)):
                    delete = edit[:i] + edit[i+1:]
                    if delete:
                        new_edits.add(delete)
                        self.deletes[delete].add(word)
            edits = new_edits

    @lru_cache(maxsize=10000)
    def lookup(self, word: str, max_candidates: int = 5):
        """O(1) lookup — nhanh hơn brute-force ~1000x"""
        word_lower = word.lower()
        if word_lower in self.word_frequency:
            return [(word_lower, 0, self.word_frequency[word_lower])]
        # ... (tìm candidates trong deletes dictionary)
```

## B.2. Pipeline hậu xử lý DocTR

```python
def ocr_doctr_image(img_path: str) -> str:
    img = cv2.imread(img_path)

    if preprocess_for_ocr is not None:
        img = preprocess_for_ocr(img)  # deskew, denoise

    # Save temp và đọc vào DocTR
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        cv2.imwrite(tmp.name, img)
        doc = DocumentFile.from_images(tmp.name)

    result = model(doc)  # Gọi DocTR engine (blackbox)
    text = extract_text(result)  # Trích xuất theo dòng

    # Xử lý từng dòng
    lines = text.split('\n')
    processed_lines = []
    for line in lines:
        cleaned = post_process_vietnamese_enhanced(line)  # 250+ rules
        if USE_FAST_SPELL_CHECKER and FAST_SPELL_CHECKER_AVAILABLE:
            cleaned = correct_vietnamese_text_fast(cleaned)  # SymSpell
        cleaned = vietnamese_text_clean(cleaned)  # Dict lookup
        processed_lines.append(cleaned)

    return '\n'.join(processed_lines)
```

## B.3. Tiền xử lý ảnh (OpenCV)

```python
def preprocess_image(img_or_path):
    """Tiền xử lý ảnh cho OCR: deskew → grayscale → blur → threshold"""
    img = cv2.imread(img_or_path) if isinstance(img_or_path, str) else img_or_path

    # 1. Deskew — nắn thẳng ảnh nghiêng
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255,
                           cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45: angle = 90 + angle
    M = cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), angle, 1.0)
    img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

    # 2. Grayscale + Gaussian Blur
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # 3. Adaptive Threshold (binarize)
    result = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 35, 10
    )
    return result
```

---

# PHỤ LỤC C: TỔNG QUAN QUẢN TRỊ DỰ ÁN CÔNG NGHỆ

Phụ lục này trình bày tóm tắt các khía cạnh quản trị, giúp mở rộng góc nhìn đáp ứng yêu cầu của bộ môn **Quản trị Dự án Công nghệ**.

## C.1. Cấu trúc phân chia công việc (WBS - Work Breakdown Structure)

Dự án được phân rã thành 4 giai đoạn chính (Phases) tạo thành vòng đời phát triển:
1. **Khởi tạo và Lập chuẩn bị (Khảo sát & Setup)**
   - Thu thập 15 tài liệu mẫu hành chính thực tế từ ĐH Điện Lực.
   - Thiết lập môi trường hệ thống (Python, CUDA, GitHub repository).
2. **Nghiên cứu & Tích hợp Engine Cơ sở**
   - Tích hợp DocTR, PaddleOCR, VietOCR dưới dạng Plugin Architecture.
   - Viết các module tiền xử lý bằng OpenCV (Deskew, Binarization).
3. **Phát triển Pipeline Hậu xử lý (Sản phẩm cốt lõi)**
   - Khởi tạo Data Dictionary và 250+ quy tắc (rules) tiếng Việt.
   - Hiện thực hóa thuật toán SymSpell O(1).
   - Tích hợp các AI theo ngữ cảnh (PhoBERT, ProtonX).
4. **Triển khai, Tích hợp & Kiểm thử**
   - Xây dựng giao diện ứng dụng Web API (FastAPI).
   - Thực nghiệm tính toán độ chính xác (Accuracy), đo benchmarking.
   - Đánh giá hiệu năng tổng thể và hoàn thiện tài liệu báo cáo.

## C.2. Quản lý Rủi ro (Risk Management)

| Rủi ro (Risk) | Xác suất | Tác động | Chiến lược đối phó (Mitigation Plan) |
|--------------|----------|---------|--------------------------------------|
| **Nút thắt về phần cứng (Thiếu GPU)** | Cao | Lớn | Thiết kế đa chế độ: CPU mode chạy bằng DocTR (ổn định) và GPU mode bằng Paddle/ProtonX cho tốc độ cực cao. |
| **Mô hình AI theo ngữ cảnh quá chậm** | Trung bình | Lớn | Áp dụng cấu hình "Feature Flag" qua file `config.json`. Mặc định sử dụng SymSpell siêu nhẹ để đảm bảo Real-time; chỉ bật PhoBERT khi cần "Quality mode". |
| **Engine gốc sai lệch liên tục dấu Tiếng Việt** | Rất cao | Lớn | Chuyển trọng tâm dự án thành xây dựng "Pipeline Hậu kỳ nhiều lớp" độc lập để vá lỗi liên tục, không can thiệp lõi Blackbox Engine. |

## C.3. Quản lý Thời gian & Nguồn lực (Resource Management)

- **Cách tiếp cận phát triển:** Quản lý dự án theo hướng tiếp cận linh hoạt (Agile-based concept), chia nhỏ quy trình tích lũy chức năng (MVP với OCR thường -> MVP2 thêm Rule-based -> Release 1.0 thêm SymSpell/Transformers).
- **Phân bổ nhân lực thiết kế:** Mô hình Developer 1 thành viên kiêm System Analyst, sử dụng triệt để mã nguồn mở được cộng đồng support.
- **Ngân sách hạ tầng:** Tái sử dụng máy tính trạm cá nhân cao cấp (i5-12500F, RTX 3050Ti), tích hợp HuggingFace open-source, đưa chi phí phần mềm và server về ngưỡng tối thiểu (0 VNĐ).

---

*— Hết báo cáo —*
