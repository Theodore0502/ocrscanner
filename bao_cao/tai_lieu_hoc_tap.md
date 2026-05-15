# TÀI LIỆU ÔN TẬP BẢO VỆ ĐỒ ÁN: KIẾN THỨC CỐT LÕI HỆ THỐNG OCR SCANNER

Tài liệu này được biên soạn để giúp bạn nắm vững các khái niệm kỹ thuật chuyên sâu đằng sau 4 chức năng phức tạp nhất của phần mềm. Hãy đọc kỹ để tự tin trả lời mọi câu hỏi phản biện từ hội đồng giảng viên.

---

## 1. Cơ chế Hậu xử lý Kép (SymSpell và AI ProtonX Nano)

Hệ thống của bạn thiết kế 2 luồng hậu xử lý (Post-processing) hoàn toàn độc lập, cung cấp sự linh hoạt tối đa cho người dùng tùy thuộc vào cấu hình phần cứng.

### Nền tảng kiến thức:
- **Khoảng cách Levenshtein (Levenshtein Distance):** Thuật toán đo lường sự khác biệt giữa hai chuỗi ký tự bằng cách đếm số bước tối thiểu (thêm, sửa, xóa) để biến chuỗi này thành chuỗi kia.
- **Thuật toán SymSpell:** Thuật toán phát triển từ Levenshtein nhưng được tối ưu hóa bằng cách sinh ra trước các biến thể xóa ký tự (deletes). Giúp tốc độ tìm kiếm lỗi chính tả đạt O(1) - siêu tốc.
- **Sequence-to-Sequence (Seq2Seq):** Kiến trúc Trí tuệ nhân tạo (như ProtonX Nano) hoạt động theo cơ chế Encoder-Decoder. Nó đọc toàn bộ một câu sai, mã hóa ngữ cảnh, và sinh ra một câu hoàn toàn mới đúng chuẩn (giống cách Google Translate hoạt động).

### Cách hệ thống của bạn áp dụng:
**Luồng 1: Chế độ Siêu tốc (Dành cho máy yếu / văn phòng)**
- Bạn kết hợp Engine OCR với **SymSpell**. Hệ thống quét lướt qua từng từ trong đoạn văn, dùng khoảng cách Levenshtein để so sánh với từ điển 100.000 từ tiếng Việt tĩnh.
- Ưu điểm: Tốc độ xử lý chớp nhoáng, không tốn GPU.
- Nhược điểm: Không hiểu ngữ cảnh (Ví dụ: OCR quét nhầm "mực" thành "mức", SymSpell bỏ qua vì "mức" vẫn là từ có nghĩa trong từ điển).

**Luồng 2: Chế độ Trí tuệ nhân tạo (Dành cho máy có GPU mạnh)**
- Bạn kết hợp Engine OCR (như PaddleOCR) với **ProtonX Nano Legal Text Correction** (Mô hình Seq2Seq chuyên ngành luật).
- Lúc này, hệ thống bỏ qua hoàn toàn SymSpell. Toàn bộ văn bản OCR thô được bơm thẳng vào ProtonX. Mô hình sẽ phân tích ngữ cảnh của cả câu và tự động viết lại câu đó chuẩn xác 100% về mặt ngữ nghĩa và dấu thanh.
- Ưu điểm: Hiểu ngữ cảnh sâu sắc, sửa chính xác tuyệt đối các từ rớt dấu đặc thù.

---

## 2. Kiến trúc Orchestrator và Plugin Pattern

### Nền tảng kiến thức:
- **Hard-code (Mã hóa cứng):** Là cách code "nghiệp dư", viết thẳng code gọi thư viện PaddleOCR vào trong nút bấm giao diện. Nếu mai mốt muốn đổi sang DocTR, bạn phải xóa code cũ và viết lại toàn bộ.
- **Design Patterns (Mẫu thiết kế phần mềm):** Là những giải pháp đã được chứng minh hiệu quả để giải quyết các vấn đề lập trình phổ biến.
- **Nguyên tắc SOLID (Đặc biệt là Open/Closed Principle):** Một phần mềm tốt phải "Mở cho việc mở rộng, nhưng Đóng cho việc sửa đổi". Tức là muốn thêm tính năng mới thì chỉ cần viết thêm file mới, chứ không được đụng vào sửa file lõi cũ.

### Cách hệ thống của bạn áp dụng:
Bạn sử dụng **Plugin Pattern**.
- Cốt lõi hệ thống định nghĩa một Lớp Trừu Tượng (Abstract Interface) mang tên `BaseOCREngine` với hàm `extract_text()`. Lớp trung tâm (Orchestrator) chỉ gọi hàm này.
- Khi tích hợp PaddleOCR hay DocTR, bạn tạo ra các lớp `PaddleEngine`, `DocTREngine` kế thừa từ `BaseOCREngine`.
- Nhờ cách thiết kế tách bạch này, bạn mới có thể dễ dàng viết thêm một "trùm cuối" là mô hình **Ensemble** (sẽ được nhắc tới ở mục 5) để gộp chung sức mạnh của các Engine lại với nhau.

---

## 3. Cơ chế Quản lý bộ nhớ AI và Fallback phần cứng

### Nền tảng kiến thức:
- **VRAM vs RAM:** Các mô hình AI (Deep Learning) tính toán ma trận khổng lồ nên chúng cần chạy trên Card đồ họa (GPU - dùng VRAM) chứ không phải vi xử lý trung tâm (CPU - dùng RAM). VRAM thường rất ít (chỉ 4GB-8GB).
- **Lỗi Out-Of-Memory (OOM):** Lỗi kinh điển khi code AI. Nếu nạp mô hình vào VRAM quá nhiều lần hoặc ảnh quá to, bộ nhớ sẽ tràn và phần mềm văng (crash) tức thì.
- **Singleton Pattern:** Một Design Pattern đảm bảo rằng một đối tượng (Lớp) chỉ được khởi tạo MỘT LẦN DUY NHẤT trong suốt quá trình phần mềm chạy.

### Cách hệ thống của bạn áp dụng:
1. **Dùng Singleton:** Bạn không load mô hình AI mỗi khi người dùng bấm nút quét (như thế sẽ mất 5-10s mỗi lần quét và gây tràn RAM). Nhờ Singleton, mô hình chỉ được nạp lên GPU đúng 1 lần khi phần mềm vừa mở lên. Các lần bấm quét sau chỉ lấy mô hình đang túc trực sẵn trên GPU ra xài.
2. **Cơ chế Fallback (Kế hoạch dự phòng):** Bạn dùng lệnh `Try... Catch` khép kín. Nếu GPU máy người dùng quá yếu và bị tràn VRAM, thay vì văng app, khối `Catch` sẽ bắt lỗi đó và tự động chuyển luồng thực thi sang chạy bằng CPU (chậm hơn nhưng an toàn), hoặc hiển thị cảnh báo yêu cầu người dùng đổi sang Engine nhẹ hơn.

---

## 4. Tự động hóa Đổi tên bằng Biểu thức chính quy (Regex)

### Nền tảng kiến thức:
- **Biểu thức chính quy (Regular Expressions - Regex):** Là một chuỗi các ký tự dùng để xác định một "mẫu" (pattern) tìm kiếm trong văn bản. Ví dụ: Dùng regex `\d{4}` để tìm bất kỳ đoạn nào có đúng 4 chữ số (để tìm năm sinh).
- **RPA (Robotic Process Automation):** Tự động hóa quy trình bằng robot/phần mềm. Thay thế con người làm các việc lặp đi lặp lại.

### Cách hệ thống của bạn áp dụng:
Thay vì người dùng phải mở từng tệp PDF, đọc số hợp đồng rồi nhấn F2 đổi tên file thành số hợp đồng đó, công cụ **File Tools** của bạn làm tất cả trong 1 nốt nhạc:
1. Phần mềm ngầm chạy OCR lên file PDF để lấy toàn bộ chữ.
2. Dùng quy tắc Regex do người dùng nhập (VD: `HĐ-\d{4}-\d{2}`) để quét đoạn chữ OCR đó.
3. Nếu khớp chữ "HĐ-2026-05", phần mềm tự động lấy chuỗi đó đặt làm tên mới cho tệp PDF.
---

## 5. Mô hình Học máy kết hợp (Ensemble Model)

### Nền tảng kiến thức:
- **Học máy kết hợp (Ensemble Learning):** Là kỹ thuật sử dụng nhiều thuật toán, mô hình học máy khác nhau cùng giải quyết một bài toán. Thay vì tin tưởng tuyệt đối vào 1 người, bạn hỏi ý kiến của một "hội đồng" chuyên gia và chọn ra đáp án được đồng thuận cao nhất hoặc có độ tin cậy (Confidence Score) cao nhất.

### Cách hệ thống của bạn áp dụng:
Đây là **"trùm cuối"** trong dự án của bạn (nằm ở file `scripts/scan_ensemble.py`). Bạn không cam chịu việc chỉ dùng 1 trong 2 công cụ (PaddleOCR hoặc DocTR). Bạn đã tạo ra chế độ **Ensemble OCR**:
1. Khi một bức ảnh được nạp vào, hệ thống chạy **song song** cả 2 engine: DocTR và PaddleOCR.
2. PaddleOCR siêu tốc độ nhưng hay rớt dấu. DocTR bắt tọa độ cực chuẩn nhưng nhận dạng đôi khi bị nhiễu.
3. Hệ thống của bạn thu thập kết quả từ cả 2 nguồn, tự động tính toán **Chỉ số tin cậy (Confidence Score)** cho từng văn bản.
4. Nó tự động ra quyết định chọn văn bản có chất lượng cao nhất để chuyển sang tầng Hậu xử lý (ProtonX Nano).
=> **Bản chất:** Bạn đã tạo ra một "Hội đồng AI" tự chấm điểm lẫn nhau để lấy kết quả hoàn hảo nhất.
