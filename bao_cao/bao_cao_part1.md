# BÁO CÁO THỰC TẬP
## Hệ thống Nhận dạng và Xử lý Văn bản Tiếng Việt Tích hợp Đa Engine OCR

**Sinh viên:** [Họ và tên] | **Mã SV:** [Mã SV]
**Đơn vị thực tập:** [Đơn vị] | **GVHD:** [Họ và tên GV]
**Năm học:** 2024 – 2025

---

# MỤC LỤC

1. Giới thiệu bài toán
2. Phân tích và thiết kế hệ thống
3. Thực nghiệm và đánh giá
4. Tài liệu tham khảo

---

# CHƯƠNG 1: GIỚI THIỆU BÀI TOÁN

## 1.1. Bối cảnh và nhu cầu thực tiễn

Trong bối cảnh chuyển đổi số đang diễn ra mạnh mẽ tại Việt Nam, các cơ quan nhà nước, trường đại học, doanh nghiệp và tổ chức hành chính đang phải đối mặt với khối lượng khổng lồ các văn bản giấy tờ cần được số hóa. Từ thông báo, quyết định, công văn đến các tài liệu hành chính phức tạp — tất cả đang tồn tại dưới dạng vật lý, gây ra những khó khăn nghiêm trọng trong việc lưu trữ, tìm kiếm, chia sẻ và xử lý thông tin.

Tại Trường Đại học Điện lực, mỗi năm học phát sinh hàng ngàn tài liệu hành chính: thông báo nhập học, kế hoạch giảng dạy, quyết định học bổng, bảng điểm, biên bản họp hội đồng và nhiều loại khác. Phần lớn các tài liệu này vẫn được lưu trữ dưới dạng bản in hoặc file ảnh scan chất lượng thấp, không có khả năng tìm kiếm nội dung. Khi cần truy xuất thông tin, cán bộ phải tốn nhiều thời gian tìm kiếm thủ công, gây ra tình trạng kém hiệu quả trong quản lý.

Công nghệ OCR (Optical Character Recognition — Nhận dạng Ký tự Quang học) cung cấp giải pháp để chuyển đổi hình ảnh tài liệu thành văn bản kỹ thuật số có thể tìm kiếm và xử lý. Tuy nhiên, tiếng Việt đặt ra những thách thức đặc biệt so với các ngôn ngữ Latin thông thường:

- **Hệ thống dấu thanh và dấu phụ phức tạp**: Tiếng Việt có 6 thanh điệu và 3 nhóm dấu phụ, tạo ra hơn 130 ký tự duy nhất cần phân biệt.
- **Tỷ lệ lỗi OCR cao**: Các engine OCR phổ thông thường nhầm lẫn các ký tự tiếng Việt có dấu, dẫn đến kết quả không sử dụng được nếu không có bước hậu xử lý.
- **Chất lượng ảnh scan đa dạng**: Tài liệu hành chính thường được scan với điều kiện ánh sáng không đều, bị nghiêng lệch, mờ nhạt hoặc có nền phức tạp.
- **Thiếu công cụ chuyên biệt**: Hầu hết các giải pháp OCR thương mại không tối ưu cho văn bản hành chính tiếng Việt.

Xuất phát từ những nhu cầu thực tiễn đó, đề tài **"Hệ thống Nhận dạng và Xử lý Văn bản Tiếng Việt Tích hợp Đa Engine OCR"** được xây dựng nhằm giải quyết bài toán số hóa tài liệu tiếng Việt một cách hiệu quả, chính xác và có thể mở rộng.

**Góc nhìn Hệ thống Thông tin Quản lý (MIS):** 
Việc triển khai hệ thống giúp xóa bỏ nút thắt trong quy trình xử lý giấy tờ:
- **Tiết kiệm thời gian:** Giảm thiểu 80-90% thời gian gõ lại văn bản thủ công (từ 5-10 phút/trang xuống còn dưới 5 giây/trang).
- **Quản trị tập trung:** Tạo tiền đề xây dựng cơ sở dữ liệu số hóa có thể tìm kiếm toàn văn (full-text search), hỗ trợ lưu trữ vĩnh viễn và chia sẻ tài nguyên nhanh chóng giữa các phòng ban.
- **Tăng năng suất:** Chuyển dịch nhân sự từ công việc hành chính lặp đi lặp lại sang các công việc có giá trị gia tăng cao hơn.

## 1.2. Phát biểu bài toán

**Đầu vào:** Hình ảnh (JPG, PNG, JPEG) hoặc tài liệu PDF đơn/nhiều trang chứa văn bản tiếng Việt, thường là văn bản hành chính, văn bản in ấn.

**Đầu ra:** Văn bản tiếng Việt dạng thuần văn bản (plain text) đã được:
- Nhận dạng chính xác các ký tự, bao gồm dấu thanh và dấu phụ
- Sửa lỗi OCR phổ biến thông qua hậu xử lý đa lớp
- Định dạng đúng cấu trúc tài liệu (xuống dòng, đoạn văn)

**Yêu cầu phi chức năng:**
- Độ chính xác ký tự (Character Accuracy) ≥ 90% trên văn bản hành chính
- Tốc độ xử lý ≤ 5 giây/trang (CPU), ≤ 1 giây/trang (GPU)
- Hỗ trợ xử lý hàng loạt (batch processing)
- Giao diện API để tích hợp với hệ thống khác

## 1.3. Phạm vi đề tài

**Trong phạm vi:**
- Nhận dạng văn bản in ấn tiếng Việt từ ảnh và PDF
- Tích hợp 3 engine OCR bên thứ ba: DocTR (Mindee), PaddleOCR v5 (Baidu), VietOCR
- Hậu xử lý đa lớp: rule-based (250+ quy tắc), SymSpell, PhoBERT, ProtonX Legal TC
- Giao diện Web API (FastAPI)
- Dữ liệu thử nghiệm: 15 tài liệu hành chính thực tế của Trường Đại học Điện lực

**Ngoài phạm vi:**
- Nhận dạng chữ viết tay
- Trích xuất bảng biểu phức tạp
- Dịch thuật hay phân tích ngữ nghĩa
- Hỗ trợ ngôn ngữ khác ngoài tiếng Việt

## 1.4. Mục tiêu đề tài

1. **Kỹ thuật:** Xây dựng hệ thống OCR đa engine với pipeline hậu xử lý tiếng Việt đạt độ chính xác ≥ 90%, tích hợp các mô hình AI bên thứ ba theo kiến trúc blackbox.
2. **Ứng dụng:** Cung cấp công cụ thực tiễn hỗ trợ số hóa tài liệu cho các đơn vị giáo dục.
3. **Nghiên cứu:** So sánh và đánh giá hiệu quả của các phương pháp hậu xử lý OCR tiếng Việt.

## 1.5. Tổng quan công nghệ sử dụng

### 1.5.1. DocTR (Document Text Recognition)
DocTR là thư viện OCR mã nguồn mở do Mindee phát triển, sử dụng kiến trúc deep learning End-to-End gồm: **DBNet** (phát hiện vùng văn bản) và **CRNN/SAR** (nhận dạng ký tự). DocTR hỗ trợ cả CPU lẫn GPU, cân bằng tốt giữa tốc độ và độ chính xác (~92% character accuracy trên văn bản hành chính tiếng Việt trong thử nghiệm của đề tài).

DocTR nhận đầu vào là ảnh hoặc PDF, trả về kết quả dạng cây phân cấp: **Document → Page → Block → Line → Word**, giúp hệ thống tái tạo cấu trúc dòng văn bản một cách tự nhiên.

### 1.5.2. PaddleOCR v5 (PP-OCRv5)
PaddleOCR là hệ thống OCR của Baidu, xây dựng trên PaddlePaddle framework. Phiên bản PP-OCRv5 được tích hợp trong đề tài này có những cải tiến quan trọng:

- **use_textline_orientation=True**: Phát hiện và sửa hướng của từng dòng văn bản
- **use_doc_orientation_classify=True**: Phân loại hướng tổng thể của tài liệu (0°, 90°, 180°, 270°)
- **use_doc_unwarping=True**: Tự động làm phẳng tài liệu bị cong vênh (perspective correction)

PaddleOCR đặc biệt hiệu quả khi sử dụng GPU, đạt tốc độ ~0.5 giây/trang (so với ~2 giây của DocTR trên CPU).

### 1.5.3. VietOCR
VietOCR là engine OCR chuyên biệt cho tiếng Việt, phát triển bởi cộng đồng người Việt. Engine này được huấn luyện trên tập dữ liệu tiếng Việt lớn, đặc biệt tối ưu cho chữ viết tay và các font chữ không chuẩn — bổ sung cho DocTR và PaddleOCR vốn mạnh hơn với văn bản in.

### 1.5.4. PhoBERT (VinAI Research)
PhoBERT là mô hình ngôn ngữ BERT được VinAI Research huấn luyện trên 20GB dữ liệu tiếng Việt, sử dụng kiến trúc **Masked Language Model (MLM)**. Trong hệ thống này, PhoBERT thực hiện sửa lỗi theo ngữ cảnh: từng từ nghi ngờ được thay bằng token `[MASK]`, sau đó PhoBERT dự đoán từ phù hợp nhất dựa vào các từ xung quanh. Phương pháp này hiệu quả hơn nhiều so với spell-check đơn thuần vì có thể phân biệt "cần cứ" vs "căn cứ" dựa trên ngữ cảnh câu.

### 1.5.5. ProtonX Legal Text Correction
ProtonX Legal TC là mô hình **Seq2Seq (Encoder-Decoder)** được ProtonX huấn luyện trên 800.000 cặp văn bản pháp lý/hành chính tiếng Việt (trong đó 30.000 cặp được chú thích thủ công bởi chuyên gia ngôn ngữ). Điểm khác biệt quan trọng so với PhoBERT là ProtonX sửa cả đoạn văn thay vì từng từ, cho phép phục hồi ngữ nghĩa tốt hơn trong văn bản hành chính. Mô hình đạt ~95%+ accuracy trên văn bản pháp lý/hành chính.

### 1.5.6. SymSpell Algorithm
SymSpell là thuật toán kiểm tra chính tả nhanh do Wolf Garbe phát triển. Nguyên lý: thay vì tính khoảng cách Levenshtein brute-force trong runtime với độ phức tạp O(n × m), SymSpell **pre-compute** tất cả các biến thể xóa ký tự (delete variations) của từ điển ngay khi load, sau đó tra cứu runtime chỉ mất O(1). Kết quả là SymSpell nhanh hơn ~1000 lần so với brute-force trên từ điển 100.000 từ tiếng Việt.

Trong đề tài, SymSpellChecker được cài đặt hoàn toàn từ đầu (không dùng thư viện ngoài), hỗ trợ:
- Max edit distance có thể cấu hình (mặc định: 2)
- LRU cache 10.000 kết quả tra cứu gần nhất
- Nạp từ điển định dạng JSONL (~4.9MB, ~100.000 từ tiếng Việt)

### 1.5.7. FastAPI
FastAPI là framework Python hiện đại để xây dựng REST API. Đề tài sử dụng FastAPI cho Web Interface, hỗ trợ:
- Upload file qua `multipart/form-data`
- Render HTML template với Jinja2
- Serve static files (CSS/JS)
- Tự động sinh tài liệu OpenAPI

---

# CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG

## 2.1. Xác định yêu cầu và tác nhân

### 2.1.1. Các tác nhân (Actors)

**Tác nhân chính:**

| Tác nhân | Mô tả |
|----------|-------|
| **Người dùng cuối (End User)** | Cán bộ, nhân viên, sinh viên cần số hóa tài liệu. Tương tác qua giao diện Web hoặc API. |
| **Quản trị viên (Admin)** | Cấu hình hệ thống, chọn engine, điều chỉnh tham số hậu xử lý qua `config.json`. |
| **Hệ thống ngoài (External System)** | Các ứng dụng tích hợp với OCR qua REST API. |

**Hệ thống thứ ba (Third-party — được coi là blackbox):**

| Tác nhân | Vai trò trong hệ thống |
|----------|----------------------|
| **DocTR Engine** | Nhận dạng văn bản từ ảnh/PDF; giao tiếp qua Python library API |
| **PaddleOCR v5** | Nhận dạng văn bản có hỗ trợ GPU; giao tiếp qua `PaddleOCR.ocr()` |
| **VietOCR Engine** | Nhận dạng văn bản tiếng Việt; giao tiếp qua Python library API |
| **PhoBERT (vinai/phobert-base)** | Dự đoán từ theo ngữ cảnh; giao tiếp qua HuggingFace Transformers |
| **ProtonX Legal TC** | Sửa lỗi Seq2Seq; giao tiếp qua HuggingFace hoặc local model files |

### 2.1.2. Yêu cầu chức năng

| Mã | Yêu cầu |
|----|---------|
| FR-01 | Nhận dạng văn bản từ ảnh (JPG/PNG/JPEG) |
| FR-02 | Nhận dạng văn bản từ PDF (đơn trang và đa trang) |
| FR-03 | Tiền xử lý ảnh: deskew, denoise, adaptive threshold |
| FR-04 | Hậu xử lý đa lớp: rule-based, SymSpell, PhoBERT, ProtonX |
| FR-05 | REST API endpoint nhận file, trả về văn bản |
| FR-06 | Giao diện web upload file và hiển thị kết quả |
| FR-07 | Xử lý hàng loạt (batch) nhiều file |
| FR-08 | Cấu hình linh hoạt qua `config.json` |

### 2.1.3. Yêu cầu phi chức năng

| Mã | Yêu cầu | Chỉ tiêu |
|----|---------|---------|
| NFR-01 | Độ chính xác | Character Accuracy ≥ 90% |
| NFR-02 | Tốc độ CPU | ≤ 5 giây/trang |
| NFR-03 | Tốc độ GPU | ≤ 1 giây/trang |
| NFR-04 | Khả năng mở rộng | Thêm engine mới không sửa core |
| NFR-05 | Tính di động | Windows / Linux / macOS |

## 2.2. Kiến trúc tổng thể

Hệ thống theo kiến trúc **Layered Architecture** kết hợp **Plugin Pattern** cho phần engine:

```
┌──────────────────────────────────────────────────┐
│              PRESENTATION LAYER                   │
│      FastAPI Web API  |  CLI Scripts              │
├──────────────────────────────────────────────────┤
│              APPLICATION LAYER                    │
│    OCR Orchestrator   |   Config Manager          │
├───────────────┬───────────────┬──────────────────┤
│  DocTR Engine │ PaddleOCR Eng │  VietOCR Engine  │
│  (blackbox)   │  (blackbox)   │   (blackbox)     │
├───────────────┴───────────────┴──────────────────┤
│            POST-PROCESSING LAYER                  │
│  Rule-based | SymSpell | PhoBERT | ProtonX        │
├──────────────────────────────────────────────────┤
│            INFRASTRUCTURE LAYER                   │
│    File I/O  |  Image Preprocessing (OpenCV)      │
└──────────────────────────────────────────────────┘
```

## 2.3. Biểu đồ Usecase tổng quát

Hệ thống có 6 usecase chính, phân theo tác nhân:

**[Người dùng cuối]**
- UC-01: Upload và nhận dạng văn bản (ảnh/PDF)
- UC-02: Chọn engine OCR
- UC-03: Xem và tải kết quả OCR

**[Admin]**
- UC-04: Cấu hình hệ thống (config.json)
- UC-05: Chạy batch processing

**[Hệ thống ngoài]**
- UC-06: Gọi OCR qua REST API

**[Hệ thống thứ 3 — blackbox]** tham gia vào UC-01, UC-05, UC-06 với vai trò engine nhận dạng và mô hình sửa lỗi.

## 2.4. Usecase chi tiết UC-01: Nhận dạng văn bản

### Đặc tả Usecase UC-01

| Thuộc tính | Nội dung |
|------------|---------|
| **Mã** | UC-01 |
| **Tên** | Upload và nhận dạng văn bản |
| **Tác nhân chính** | Người dùng cuối |
| **Tác nhân thứ cấp** | DocTR / PaddleOCR / VietOCR (blackbox) |
| **Điều kiện tiên quyết** | File hợp lệ (JPG/PNG/PDF), kích thước ≤ 10MB |
| **Kết quả** | Văn bản tiếng Việt đã xử lý hậu kỳ |

**Luồng chính:**
1. Người dùng truy cập `http://localhost:8000` hoặc gửi POST `/ocr`
2. Người dùng chọn file và (tùy chọn) engine OCR
3. Hệ thống kiểm tra định dạng và kích thước file
4. Hệ thống lưu file tạm vào `uploads/`
5. Nếu cấu hình cho phép: tiền xử lý ảnh (deskew → grayscale → GaussianBlur → adaptive threshold)
6. Gọi engine OCR (blackbox call): trả về cấu trúc Document/Page/Block/Line/Word
7. Trích xuất văn bản, giữ nguyên cấu trúc dòng
8. Hậu xử lý Lớp 1: thay thế 250+ mẫu lỗi cố định (rule-based)
9. Hậu xử lý Lớp 2: SymSpell spell checking (nếu bật)
10. Hậu xử lý Lớp 3: PhoBERT context correction (nếu bật)
11. Hậu xử lý Lớp 4: Vietnamese text cleaner (dictionary lookup + unidecode fallback)
12. Trả kết quả về người dùng

**Luồng thay thế:**
- **A1**: File không hợp lệ → báo lỗi, yêu cầu upload lại
- **A2**: Engine không khởi động → fallback engine dự phòng
- **A3**: OCR trả về rỗng → thông báo "Không tìm thấy văn bản"

## 2.5. Usecase chi tiết UC-05: Batch Processing

### Đặc tả Usecase UC-05

| Thuộc tính | Nội dung |
|------------|---------|
| **Mã** | UC-05 |
| **Tên** | Xử lý hàng loạt tài liệu |
| **Tác nhân chính** | Admin |
| **Tác nhân thứ cấp** | DocTR / PaddleOCR (blackbox) |
| **Điều kiện tiên quyết** | Thư mục `data/raw/` chứa các folder tài liệu |
| **Kết quả** | File `.txt` tương ứng trong `data/results/` |

**Luồng chính:**
1. Admin chạy script: `python scripts/scan_to_results.py`
2. Script quét tất cả folder trong `data/raw/`
3. Với mỗi folder (ví dụ `dl_2025_0001/`): lấy danh sách ảnh
4. Với mỗi ảnh: gọi pipeline OCR đầy đủ (giống UC-01)
5. Ghép kết quả các trang theo thứ tự
6. Lưu ra `data/results/<folder_name>.txt`
7. Ghi log thống kê: số file, thời gian, số ký tự

## 2.6. Biểu đồ hoạt động (Activity Diagram)

### Quy trình xử lý một file OCR

```
[START]
   |
   v
[Nhận file từ người dùng]
   |
   v
< File là ảnh hay PDF? >
   |ảnh              |PDF
   v                  v
[Đọc ảnh OpenCV]   [DocumentFile.from_pdf()]
   |                  |
   +--------+---------+
            |
            v
< Preprocessing được bật? >
   |Có                 |Không
   v                    |
[Deskew (MinAreaRect)] |
   |                    |
[Grayscale]            |
   |                    |
[GaussianBlur(3,3)]    |
   |                    |
[AdaptiveThreshold]    |
   |                    |
   +----------+---------+
              |
              v
[Gọi OCR Engine (blackbox)]
DocTR: ocr_predictor(doc)
Paddle: PaddleOCR.ocr(img)
              |
              v
[Extract text theo cấu trúc Line]
              |
              v
[Rule-based: 250+ replacements]
              |
              v
< SymSpell bật? > --Có--> [SymSpellChecker.correct_text()]
              |
              v
< PhoBERT bật? > --Có--> [PhoBERTCorrector.correct_text()]
              |
              v
[vietnamese_text_clean() - Dict lookup]
              |
              v
[Trả về văn bản cuối]
              |
            [END]
```

## 2.7. Biểu đồ trình tự (Sequence Diagram)

### Scenario 1: User upload ảnh qua Web API

```
User          FastAPI          engine_doctr        DocTR          PostProcess
 |               |                 |                |                |
 |--POST /ocr--> |                 |                |                |
 |               |--validate()---->|                |                |
 |               |                 |--load model()->|                |
 |               |                 |<--model ready--|                |
 |               |                 |--preprocess()  |                |
 |               |                 |--ocr(doc)----->|                |
 |               |                 |                |--recognize()---|
 |               |                 |<--raw result---|                |
 |               |                 |--extract_text()|                |
 |               |                 |--post_process()---------------> |
 |               |                 |                |  rule_replace()|
 |               |                 |                |  symspell()    |
 |               |                 |                |  vn_clean()    |
 |               |                 |<--cleaned text------------------|
 |<--200 + text--|<--return text---|                |                |
```

### Scenario 2: PaddleOCR + ProtonX (tích hợp hệ thống thứ 3)

```
User        engine_paddle      PaddleOCR v5      ProtonXCorrector    HuggingFace
 |                |                 |                  |                  |
 |--call-------> |                 |                  |                  |
 |               |--get_ocr()---->|                  |                  |
 |               |--ocr(img)----->|                  |                  |
 |               |                |--PP-OCRv5:        |                  |
 |               |                | detect+recognize  |                  |
 |               |<--result-------|                  |                  |
 |               |--extract()     |                  |                  |
 |               |--correct_protonx()-------------->|                  |
 |               |                |                  |--load_model()--->|
 |               |                |                  |<--weights--------|
 |               |                |                  |--chunk_text()    |
 |               |                |                  |--generate()      |
 |               |<--corrected text------------------|                  |
 |<--final text--|                |                  |                  |
```

## 2.8. Biểu đồ lớp (Class Diagram)

### Nhóm OCR Engines

**engine_doctr (module-level)**
- Thuộc tính: `model: OcrPredictor` (singleton, load một lần)
- Hàm: `extract_text(result, preserve_lines)`, `post_process_vietnamese_enhanced(text)`, `ocr_doctr_image(img_path)`, `ocr_doctr_pdf(pdf_path)`

**engine_paddle (module-level)**
- Thuộc tính: `_paddle_ocr: PaddleOCR` (singleton)
- Hàm: `get_paddle_ocr()`, `extract_text_from_result(result)`, `post_process_vietnamese(text)`, `ocr_paddle_image(image_path)`, `ocr_paddle_image_with_protonx(image_path)`

### Nhóm Post-Processing

```
┌──────────────────────────────────┐
│        SymSpellChecker           │
├──────────────────────────────────┤
│- word_frequency: Dict[str, int]  │
│- deletes: Dict[str, Set[str]]    │
│- max_edit_distance: int          │
├──────────────────────────────────┤
│+ lookup(word, max_candidates)    │
│+ is_correct(word): bool          │
│+ correct_word(word): str         │
│+ correct_text(text): str         │
│- _create_deletes(word)           │
│- _edit_distance(s1, s2): int     │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│       PhoBERTCorrector           │
├──────────────────────────────────┤
│- model: AutoModelForMaskedLM     │
│- tokenizer: AutoTokenizer        │
│- device: str (cuda/cpu)          │
│- dictionary: Set[str]            │
├──────────────────────────────────┤
│+ correct_word(word, sentence,    │
│    word_index): str              │
│+ correct_text(text, use_context) │
│+ predict_with_phobert(sentence,  │
│    word_index): List[str]        │
│+ get_dictionary_candidates(word) │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│       ProtonXCorrector           │
├──────────────────────────────────┤
│- model: AutoModelForSeq2SeqLM    │
│- tokenizer: AutoTokenizer        │
│- device: torch.device            │
│- max_tokens: int (=160)          │
├──────────────────────────────────┤
│+ correct_text(text, num_beams)   │
│+ correct_text_chunked(text,      │
│    preserve_formatting): str     │
│+ correct_batch(texts): List[str] │
│- _chunk_text(text): List[str]    │
│- _split_into_sentences(text)     │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│        preprocess (module)       │
├──────────────────────────────────┤
│+ deskew(image: np.ndarray)       │
│+ preprocess_image(img_or_path)   │
└──────────────────────────────────┘
```

**Quan hệ phụ thuộc:**
- `engine_doctr` → uses → `SymSpellChecker`, `PhoBERTCorrector`, `preprocess`, `vietnamese_text_cleaner`
- `engine_paddle` → uses → `ProtonXCorrector`, `post_process_vietnamese()`
- `FastAPI (web/main.py)` → uses → `engine_doctr`, `engine_paddle`
- `SymSpellChecker` → reads → `data/raw_dict.jsonl` (từ điển JSONL ~4.9MB)
- `PhoBERTCorrector` → loads → `vinai/phobert-base` (HuggingFace)
- `ProtonXCorrector` → loads → `models/protonx-legal-tc/` (local) hoặc HuggingFace

## 2.9. Biểu đồ lớp cơ sở dữ liệu quan hệ

Hệ thống hiện dùng file-based storage. Mô hình logic nếu mở rộng sang RDBMS:

```
Document (id PK, filename, file_type, upload_date, file_size, upload_by)
    |1
    |N
OCRResult (id PK, document_id FK, engine, page_number, raw_text,
           processed_text, confidence, process_time, created_at)
    |1
    |N
PostProcessLog (id PK AUTO, result_id FK, method, corrections_count,
                processing_time)

Configuration (key PK, value, updated_at)
```

**Bảng `OCRResult`** là trung tâm của schema: lưu cả raw text (trước hậu xử lý) và processed text (sau hậu xử lý), cùng confidence score từng dòng, giúp so sánh và đánh giá chất lượng.

## 2.10. Biểu đồ triển khai (Deployment Diagram)

```
┌───────────────────────────────────────────────────────────┐
│              Application Server                            │
│   16GB RAM | Intel i5-12500F | NVIDIA RTX 3050Ti (4GB)   │
│                                                           │
│  ┌─────────────────────────────────────────────────────┐  │
│  │            Python 3.10 + .venv                       │  │
│  │                                                     │  │
│  │  ┌──────────────┐  ┌───────────┐  ┌─────────────┐  │  │
│  │  │ FastAPI      │  │ DocTR     │  │ PaddleOCR   │  │  │
│  │  │ :8000        │  │ Engine    │  │ v5 Engine   │  │  │
│  │  └──────────────┘  └───────────┘  └─────────────┘  │  │
│  │                                                     │  │
│  │  ┌─────────────────────────────────────────────┐   │  │
│  │  │           CUDA / CPU Runtime                │   │  │
│  │  └─────────────────────────────────────────────┘   │  │
│  │                                                     │  │
│  │  ┌─────────────────────────────────────────────┐   │  │
│  │  │         Local Model Storage                 │   │  │
│  │  │  models/protonx-legal-tc/  (Seq2Seq model) │   │  │
│  │  │  .cache/phobert-base/      (BERT model)    │   │  │
│  │  │  data/raw_dict.jsonl       (100K từ VN)    │   │  │
│  │  └─────────────────────────────────────────────┘   │  │
│  └─────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────┘
          │ HTTP REST API (:8000)
          v
┌─────────────────────┐      ┌─────────────────────┐
│ Client Browser /    │      │   HuggingFace Hub   │
│ External App        │      │ (model download)    │
└─────────────────────┘      └─────────────────────┘
```

**Đặc điểm triển khai:**
- Hệ thống chạy hoàn toàn **local**, không cần internet sau khi tải model
- Hỗ trợ cả CPU (development) và GPU CUDA (production)
- Model ProtonX được lưu local tại `models/protonx-legal-tc/snapshots/04d5b406.../` để triển khai offline
- Config tập trung tại `config/config.json` — thay đổi không cần sửa code

## 2.11. Mô hình hóa quy trình nghiệp vụ (Business Process)

Việc áp dụng hệ thống OCR thay đổi hoàn toàn quy trình xử lý tài liệu hành chính tại Đại học Điện Lực (Góc nhìn MIS).

**Quy trình cũ (Thủ công):**
1. Nhận văn bản giấy → 2. Cán bộ phân loại thư mục vật lý → 3. Khi cần dùng, tìm kiếm thủ công trong hộc tủ → 4. Gõ lại văn bản bằng tay nếu muốn trích xuất nội dung (tốn 5-10 phút/trang) → 5. Soạn thảo văn bản mới.

**Quy trình mới (Tự động hóa số hóa):**
1. Nhận văn bản giấy → 2. Máy scan đẩy file (PDF/JPG) vào hệ thống → 3. Hệ thống OCR tự động quét (batch/real-time), trích xuất và hậu xử lý (mất 1-5 giây/trang) → 4. Lưu metadata và toàn văn vào Database → 5. Tìm kiếm keyword và tái sử dụng nội dung ngay lập tức.
