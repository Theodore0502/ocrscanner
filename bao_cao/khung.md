CHƯƠNG 1. GIỚI THIỆU DỰ ÁN

Chương này phải ngắn gọn, đi thẳng vào bài toán thực tiễn.
Không sa đà vào AI theory.

1.1. Giới thiệu đơn vị thực tập
1.1.1. Giới thiệu tổng quan đơn vị
1.1.2. Lĩnh vực hoạt động
1.1.3. Vai trò của CNTT trong doanh nghiệp
1.2. Tổng quan bài toán
1.2.1. Thực trạng số hóa tài liệu hiện nay
Hồ sơ giấy số lượng lớn
Nhập liệu thủ công
Sai sót dữ liệu
Chi phí nhân lực cao
1.2.2. Những khó khăn trong OCR tiếng Việt
Mất dấu
OCR sai ký tự
PDF scan mờ
Chất lượng ảnh không đồng đều
1.2.3. Nhu cầu xây dựng hệ thống OCR Scanner
Tự động hóa
Giảm thời gian xử lý
Chuẩn hóa tài liệu
1.3. Mục tiêu dự án
1.3.1. Mục tiêu tổng quát

Xây dựng hệ thống OCR Scanner hỗ trợ nhận dạng và xử lý văn bản tiếng Việt.

1.3.2. Mục tiêu cụ thể
OCR tài liệu ảnh/PDF
Batch OCR
Batch Rename
PDF Split
Hậu xử lý tiếng Việt
1.4. Phạm vi dự án
1.4.1. Phạm vi chức năng
OCR
Batch Processing
File Tools
1.4.2. Đối tượng sử dụng
Nhân viên hành chính
Văn phòng
Sinh viên
1.4.3. Giới hạn hệ thống
Chạy local
Chưa hỗ trợ cloud
Chưa hỗ trợ mobile
1.5. Phân tích yêu cầu hệ thống
1.5.1. Yêu cầu chức năng
ID Chức năng
FR-01 OCR ảnh
FR-02 OCR PDF
FR-03 Batch OCR
FR-04 Batch Rename
FR-05 Split PDF
1.5.2. Yêu cầu phi chức năng
ID Yêu cầu
NFR-01 Tốc độ xử lý nhanh
NFR-02 Giao diện thân thiện
NFR-03 Dễ mở rộng
NFR-04 Hoạt động ổn định
CHƯƠNG 2. QUẢN LÝ DỰ ÁN

Đây là chương quan trọng nhất.
Phải mang “mùi quản trị dự án” thật rõ.

PHẦN A. QUẢN TRỊ DỰ ÁN
2.1. Mô hình phát triển phần mềm
2.1.1. Giới thiệu mô hình phát triển
Incremental Model
Agile mindset
Phát triển theo từng giai đoạn
2.1.2. Lý do lựa chọn mô hình
Giảm rủi ro
Kiểm thử sớm
Dễ tích hợp AI
Dễ mở rộng
2.1.3. Quy trình triển khai dự án
Khảo sát
Phân tích
Thiết kế
Xây dựng
Kiểm thử
Bàn giao
2.2. Kế hoạch thực hiện dự án
2.2.1. Các mốc thời gian chính (Milestones)
Giai đoạn Nội dung Thời gian
GĐ1 Khảo sát & Phân tích Tuần 1
GĐ2 Thiết kế hệ thống Tuần 2
GĐ3 Xây dựng GUI Tuần 3-4
GĐ4 Tích hợp OCR & NLP Tuần 5-6
GĐ5 Kiểm thử Tuần 7
GĐ6 Hoàn thiện báo cáo Tuần 8
2.2.2. Ước lượng thời gian theo PERT
Công thức:

EST=
6
O+4M+P
​

Bảng PERT
Mã CV Công việc O M P EST
KS.1 Khảo sát hiện trạng 2 3 5 3.17
KS.2 Phân tích yêu cầu 2 4 6 4
TK.1 Thiết kế UI 3 5 7 5
XD.1 Xây dựng GUI 5 7 10 7.17
2.2.3. Cấu trúc phân rã công việc (WBS)
Bảng WBS
STT Giai đoạn Công việc Mã CV CV trước
1 Khảo sát Khảo sát OCR KS.1 -
2 Phân tích Phân tích yêu cầu KS.2 KS.1
3 Thiết kế Thiết kế UI TK.1 KS.2
4 Thiết kế Thiết kế kiến trúc TK.2 TK.1
5 Xây dựng Core GUI XD.1 TK.2
2.2.4. Biểu đồ Gantt
Nội dung:
Timeline 8 tuần
Dependencies
Milestones
Song song task
2.3. Ước lượng chi phí
2.3.1. Chi phí nhân công
Vai trò SL Chi phí
Dev/PM 1 30.000.000
2.3.2. Chi phí hạ tầng
Hạng mục Chi phí
GPU RTX 3060 1.000.000
Cloud Storage 500.000
2.3.3. Tổng mức đầu tư
Hạng mục Tổng
Nhân công 30.000.000
Hạ tầng 1.500.000
Dự phòng 3.150.000
Tổng cộng 34.650.000
2.4. Ước lượng rủi ro
2.4.1. Nhận diện rủi ro
ID Rủi ro
R1 GPU OOM
R2 OCR mất dấu
R3 Conflict CUDA
R4 PDF crash
2.4.2. Đánh giá rủi ro
ID Ảnh hưởng Xác suất Điểm
R1 5 4 20
R2 5 3 15
2.4.3. Phương án phòng ngừa và xử lý
Rủi ro Giải pháp
OOM GPU Fallback CPU
OCR sai dấu ProtonX + SymSpell
Freeze GUI Multi-threading
2.5. Quản lý chất lượng phần mềm

Phần này rất quan trọng trong QTDA.

2.5.1. Mục tiêu chất lượng
OCR accuracy ≥ 90%
Không crash khi batch
GUI phản hồi ổn định
2.5.2. Quy trình đảm bảo chất lượng
Unit Testing
Functional Testing
Performance Testing
2.5.3. Quy trình kiểm soát thay đổi
Quản lý version
Backup source
Theo dõi bug
PHẦN B. GIẢI PHÁP KỸ THUẬT

Viết ngắn gọn hơn báo cáo HTTT Tích Hợp.

2.6. Công nghệ sử dụng
Công nghệ Vai trò
Python Core
CustomTkinter GUI
OpenCV Xử lý ảnh
DocTR OCR
PaddleOCR OCR
Transformers NLP
2.7. Tổng quan kiến trúc hệ thống
2.7.1. Kiến trúc phân lớp
GUI Layer
Core Layer
AI Layer
2.7.2. Luồng xử lý dữ liệu
Input
OCR
NLP
Export
2.8. Phân tích thiết kế hệ thống
2.8.1. Biểu đồ Use Case tổng quát

Actors:

User
Admin

Use Cases:

OCR
Batch OCR
Rename
Split PDF
2.8.2. Phân tích chức năng OCR
Đặc tả Use Case
Biểu đồ hoạt động
Biểu đồ trình tự
2.8.3. Phân tích chức năng Batch Processing
Đặc tả Use Case
Biểu đồ hoạt động
Biểu đồ trình tự
CHƯƠNG 3. TRIỂN KHAI CHƯƠNG TRÌNH

Chương này phải đánh mạnh vào TESTING + QUALITY.

3.1. Kiểm thử hệ thống
3.1.1. Kế hoạch kiểm thử
Mục tiêu kiểm thử
Phạm vi kiểm thử
Chiến lược kiểm thử
3.1.2. Kiểm thử chức năng OCR
a. Kiểm thử giao diện (UI Testing)
ID Thành phần Kết quả mong đợi Trạng thái
UI-01 Upload File Hiển thị đúng Pass
b. Kiểm thử chức năng (Functional Testing)
ID Kịch bản Kết quả mong đợi Trạng thái
FT-01 OCR ảnh rõ nét Accuracy ≥ 90% Pass
FT-02 PDF scan mờ Cảnh báo lỗi Failed
c. Kiểm thử hiệu năng (Performance Testing)
ID Kịch bản Kết quả Trạng thái
PF-01 OCR 100 ảnh < 5 phút Pass
3.1.3. Kiểm thử Batch Processing
UI Test
Functional Test
Performance Test
3.1.4. Phân tích sai lệch và hướng khắc phục
ID Lỗi Giải pháp
FT-02 PDF corrupt try-except
PF-03 RAM tăng cao Queue processing
3.1.5. Kết quả kiểm thử và đánh giá chất lượng hệ thống
a. Tổng hợp kết quả kiểm thử
Nhóm test Tổng Pass Fail
UI Testing 8 8 0
Functional Testing 15 13 2
Performance Testing 6 5 1
b. Đánh giá độ ổn định hệ thống
Tiêu chí Kết quả
OCR Accuracy 95-96%
Thời gian OCR ~1.8s/trang
Batch OCR 96/100 file
c. Đánh giá chất lượng phần mềm
Tính ổn định
Tính mở rộng
Tính bảo trì
Tính hiệu năng
3.2. Cài đặt hệ thống
3.2.1. Yêu cầu phần cứng
Thành phần Yêu cầu
CPU Intel i5
RAM 8GB
GPU RTX 3060
3.2.2. Yêu cầu phần mềm
Phần mềm Phiên bản
Python 3.10
CUDA 11.8
3.2.3. Quy trình cài đặt
Clone source
pip install
Configure
Run
3.3. Kết quả demo hệ thống
3.3.1. Giao diện OCR
3.3.2. Giao diện Batch Rename
3.3.3. Giao diện Split PDF
3.3.4. Kết quả thực nghiệm
KẾT LUẬN VÀ HƯỚNG NGHIÊN CỨU TRONG TƯƠNG LAI

1. Kết quả đạt được
   Hoàn thành hệ thống OCR
   Tích hợp AI thành công
   Đạt accuracy cao
   Hệ thống hoạt động ổn định
2. Hạn chế
   Chưa đóng gói EXE
   Tốn VRAM
   Cài đặt phức tạp
3. Hướng phát triển
   Docker
   OCR Cloud
   Quantization
   Auto Deployment
