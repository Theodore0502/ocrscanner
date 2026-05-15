TRƯỜNG ĐẠI HỌC ĐIỆN LỰC  
KHOA CÔNG NGHỆ THÔNG TIN

---

# BÁO CÁO THỰC TẬP TỐT NGHIỆP

## MÔN: THỰC TẬP HỆ THỐNG THÔNG TIN QUẢN LÝ

**Đề tài:** HỆ THỐNG NHẬN DẠNG VÀ QUẢN LÝ VĂN BẢN HÀNH CHÍNH TIẾNG VIỆT (Ứng dụng OCR Scanner & File Tools)

**Giảng viên hướng dẫn:** TS. Ngô Ngọc Thành  
**Sinh viên thực hiện:** Nguyễn Hoàng Thanh Tùng  
**Mã sinh viên:** 22810310248  
**Chuyên ngành:** Hệ thống thông tin quản lý

Hà Nội, 2026

 

# QUYẾT ĐỊNH CỬ ĐI THỰC TẬP

_(Sinh viên chèn bản scan/ảnh chụp tờ Quyết định cử đi thực tập của Nhà trường tại trang này)_

 
ĐỀ CƯƠNG THỰC TẬP MÔN
THỰC TẬP HỆ THỐNG THÔNG TIN QUẢN LÝ

1. Tên đề tài: Hệ Thống Nhận diện Và Xử Lý Văn Bản Tiếng Việt
2. Sinh viên thực hiện:
   Họ và tên: Nguyễn Hoàng Thanh Tùng. MSSV: 22810310248.
   Số điện thoại: 0969386663. Email: tung2004nguyen52@gmail.com.
   Vị trí thực tập: Nhân sự Nghiên cứu và Triển khai.
3. Giảng viên hướng dẫn:
   Họ và tên: Ngô Ngọc Thành. Học vị: Tiến sĩ.
   Số điện thoại: 0988216988 Email: thanhnn_cntt @epu.edu.vn.
   Đơn vị công tác: Khoa Công Nghệ Thông Tin trường Đại học Điện Lực.
4. Mô tả tóm tắt đề tài
   Đề tài tập trung xây dựng ứng dụng phần mềm máy tính (Desktop Application) “OCR Scanner & File Tools”, cho phép người dùng tự động hóa quy trình số hóa tài liệu và văn bản hành chính Tiếng Việt một cách nhanh chóng và chính xác. Hệ thống cung cấp các chức năng cơ bản như quét ảnh trích xuất văn bản thô, chia tách/gộp tài liệu PDF (Split/Merge) và chuẩn hóa tên tệp tin hàng loạt (Batch Rename). Bên cạnh đó, hệ thống còn tích hợp giao diện đối chiếu song song (Dual-panel) để người dùng có thể dễ dàng so sánh và chỉnh sửa kết quả nhận diện so với bản gốc.
   Ngoài các chức năng của một phần mềm số hóa thông thường, đề tài còn nghiên cứu áp dụng triệt để kiến trúc "Tích hợp Hệ thống" (System Integration) nhằm nâng cao tỷ lệ nhận diện chính xác văn bản Tiếng Việt - vốn nổi tiếng với hệ thống dấu thanh phức tạp. Thay vì tự huấn luyện một mô hình mới, các mô hình Trí tuệ nhân tạo tiên tiến nhất hiện nay (DocTR [1], PaddleOCR [2]) được đóng gói dưới dạng các "Hộp đen" (Black-box) độc lập. Đặc biệt, hệ thống sử dụng mô hình Học máy kết hợp (Ensemble Model) để gộp chung sức mạnh của nhiều Engine nhận diện, kết hợp cùng siêu mô hình ngôn ngữ ProtonX Nano Legal Text Correction (Seq2Seq) [5] làm tầng hậu xử lý, giúp tự động sửa lỗi chính tả và khôi phục ngữ cảnh chuẩn xác.
   Bên cạnh đó, hệ thống sử dụng thư viện giao diện hiện đại CustomTkinter trên nền tảng Python để xử lý logic ứng dụng, đồng thời ứng dụng các thư viện tính toán cục bộ (PyTorch, PaddlePaddle) để khai thác sức mạnh xử lý song song của nhân đồ họa (GPU), giúp tăng tốc độ phản hồi mà vẫn đảm bảo tính bảo mật dữ liệu nội bộ.
   Việc xây dựng hệ thống OCR Scanner không chỉ mang lại một công cụ đắc lực hỗ trợ nhân sự hành chính tiết kiệm hàng nghìn giờ gõ lại văn bản thủ công, mà còn minh họa thực tế cách tư duy Tích hợp hệ thống có thể phối hợp các luồng dịch vụ AI độc lập thành một giải pháp hoàn chỉnh, góp phần thúc đẩy công cuộc chuyển đổi số tại các cơ quan và doanh nghiệp.
5. Nội dung báo cáo thực tập
   Chương 1. Khảo sát hiện trạng và xác lập dự án
   1.1. Giới thiệu bối cảnh triển khai
   1.2. Khảo sát hiện trạng hoạt động nghiệp vụ
   1.3. Xác lập dự án
   1.4. Phân tích yêu cầu hệ thống
   1.5. Tính ưu việt và giá trị kinh tế của dự án
   Chương 2. Phân tích và thiết kế hệ thống tích hợp
   2.1. Tổng quan kiến trúc hệ thống
   2.2. Các chức năng chính của hệ thống
   2.3. Thiết kế kiến trúc và cấu trúc dữ liệu
   Chương 3. Triển khai tích hợp và xây dựng hệ thống
   3.1. Công nghệ sử dụng
   3.2. Giao diện hệ thống
   3.3. Kết quả thực nghiệm
   Giảng viên hướng dẫn
   (Ký, Ghi rõ họ tên) Sinh viên thực hiện
   (Ký, Ghi rõ họ tên)

ĐÁNH GIÁ ĐỒ ÁN THỰC TẬP THỰC TẬP MÔN….
(Dành cho cán bộ chấm thi)
Tiêu chí đánh giá:
Tiêu chí
đánh giá Yếu (0 - 39%) Trung Bình
(40-54%) Khá (55-69%) Giỏi (70-84%) Xuất sắc
(85-100%) Điểm tối đa CB 1 (Cho lẻ đến 0.25) CB 2 (Cho lẻ đến 0.25)

1. Báo cáo kết quả 3,0
   Nội dung trình bày đầy đủ, thời gian trình bày phù hợp - Không có tài liệu trình bày, nội dung trình bày gần như không có - Có chuẩn bị tài liệu trình bày, tuy nhiên tài liệu còn sơ sài.

- Thời gian trình bày các phần chưa hợp lý - Có chuẩn bị tài liệu, tài liệu bố cục chưa hợp lý
- Thời gian trình bày chưa hợp lý - Có chuẩn bị tài liệu, bố cục tài liệu hợp lý
- Thời gian trình bày phù hợp - Có sáng tạo trong cách thức trình bày kết quả
- Thời gian trình bày được phân bổ hợp lý 1,0
  Kết quả trả lời các câu hỏi phản biện và câu hỏi khác - Không trả lời hoặc nội dung trả lời sai - Trả lời được ít hơn 50% số câu hỏi, kết quả trả lời chưa tốt - Trả lời được ít hơn 70% câu hỏi, kết quả trả lời phù hợp với nội dung câu hỏi - Trả lời được ít hơn 85% câu hỏi, kết quả trả lời tốt so với nội dung câu hỏi - Trả lời được toàn bộ câu hỏi, kết quả trả lời tốt so với nội dung câu hỏi 2,0

2. Đánh giá kết quả thực hiện 6,0
   2.1 Hoàn thành và đảm bảo đầy đủ nội dung theo yêu cầu học phần thực tập tốt nghiệp Hầu hết không hoàn thành và đảm bảo đầy đủ nội dung theo yêu cầu của học phần. Hoàn thành báo cáo thực tập; hầu hết các nội dung thực nghiệm chưa hoàn thành theo yêu cầu của học phần. Hoàn thành báo cáo thực tập; hoàn thành các nội dung cơ bản của thực nghiệm theo yêu cầu của học phần. Một số nội dung chưa hoàn thành và đảm bảo đầy đủ theo yêu cầu của học phần. Hoàn thành và đảm bảo đầy đủ nội dung theo yêu cầu của học phần. 4,0
   2.2 Đảm bảo yêu cầu về hình thức trình bày, bản vẽ, tham khảo, tỉ lệ trùng lặp - Hình thức trình bày, cấu trúc, định dạng không đúng quy định.

- Không trích dẫn tham khảo với các nội dung tham khảo
- Tỉ lệ trùng lặp dưới 20% - Hình thức trình bày, cấu trúc, định dạng … phần lớn không đúng quy định.
- Còn rất nhiều nội dung tham khảo chưa trích dẫn
- Tỉ lệ trùng lặp dưới 20% - Hình thức trình bày, cấu trúc, định dạng, … của nhiều nội dung không đúng quy định.
- Còn nhiều nội dung tham khảo chưa trích dẫn.
- Tỉ lệ trùng lặp dưới 20% - Hình thức trình bày, cấu trúc, định dạng, … của một số nội dung không đúng quy định.
- Còn một số nội dung tham khảo chưa trích dẫn
- Tỉ lệ trùng lặp dưới 20% - Hình thức trình bày, cấu trúc, định dạng, … đúng quy định và thống nhất.
- Các nội dung tham khảo được trích dẫn hết
- Tỉ lệ trùng lặp dưới 20% 2,0

3. Tính khoa học và ứng dụng thực tiễn 1,0
   3.1 Tính mới, tính sáng tạo Đề tài không có tính mới, tính sáng tạo Đề tài có tính sáng tạo, có điểm mới so với các nội dung kế thừa. 0,5
   3.2 Phạm vi và mức độ ứng dụng Không có khả năng áp dụng cũng như không có hướng phát triển cao hơn trong tương lai Có khả năng ứng dụng vào thực tế nhưng khó có khả năng phát triển cao hơn trong tương lai Có khả năng ứng dụng vào thực tế và có thể định hướng phát triển cao hơn trong tương lai 0,5
   TỔNG 10
   Lưu ý: Điểm chấm làm tròn đến một chữ số thập phân
   Ngày tháng năm 20…  
   Cán bộ chấm thi 1
   (Ký và ghi rõ họ tên) Cán bộ chấm thi 2
   (Ký và ghi rõ họ tên)

MỤC LỤC
LỜI NÓI ĐẦU 1
CHƯƠNG 1: KHẢO SÁT HIỆN TRẠNG VÀ XÁC LẬP DỰ ÁN 2
1.1. Giới thiệu về bối cảnh triển khai 2
1.2. Khảo sát hiện trạng hoạt động nghiệp vụ 2
1.3. Xác lập dự án 3
1.4. Phân tích yêu cầu hệ thống 4
1.5. Tính ưu việt và giá trị kinh tế của dự án 5
CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG 6
2.1. Xác định các Actor và Use Case tổng quát 6
2.2. Các chức năng chính của hệ thống 9
2.2.1. Chức năng Nhận dạng và chuyển đổi số văn bản (Core OCR) 9
2.2.1.1. Biểu đồ hoạt động nhận dạng văn bản 11
2.2.1.2. Biểu đồ trình tự nhận dạng văn bản 12
2.2.2. Chức năng Xử lý chuyển đổi số hàng loạt (Batch OCR) 13
2.2.2.1. Biểu đồ hoạt động xử lý chuyển đổi số hàng loạt 14
2.2.2.2. Biểu đồ trình tự xử lý chuyển đổi số hàng loạt 14
2.2.3. Chức năng Tổ chức và quản lý tệp tin (File Tools) 15
2.2.3.1. Biểu đồ hoạt động tổ chức và quản lý tệp tin 16
2.2.3.2. Biểu đồ trình tự tổ chức và quản lý tệp tin 17
2.3. Thiết kế kiến trúc và cấu trúc dữ liệu 18
2.3.1. Biểu đồ triển khai (Deployment Diagram) 18
2.3.2. Biểu đồ Lớp (Class Diagram) 19
2.3.3. Cấu trúc dữ liệu hệ thống (Data Schema) 20
2.3.4. Biểu đồ lớp cơ sở dữ liệu (Database Class Diagram) 23
CHƯƠNG 3: TRIỂN KHAI TÍCH HỢP VÀ XÂY DỰNG HỆ THỐNG 25
3.1. Công nghệ sử dụng 25
3.2. Giao diện hệ thống. 25
3.2.1. Giao diện màn hình OCR tài liệu. 25
3.2.2. Giao diện màn hình đổi tên tài liệu hàng loạt. 26
3.2.3. Giao diện màn hình tách file hàng loạt 26
3.3. Kết quả thực nghiệm 27
3.3.1. Đánh giá Hiệu quả Kinh tế và Tối ưu nguồn lực (ROI): 29
3.3.2. Đánh giá hiệu quả tích hợp hệ thống: 30
KẾT LUẬN 31
TÀI LIỆU THAM KHẢO 33

 
DANH MỤC TỪ VIẾT TẮT

Từ viết tắt Phiên bản đầy đủ Dịch thuật
AI Artificial Intelligence Trí tuệ nhân tạo
API Application Programming Interface Giao diện lập trình ứng dụng
CPU / GPU / RAM Các phần cứng cốt lõi
GUI Graphical User Interface Giao diện người dùng đồ họa
LLM Large Language Model Mô hình ngôn ngữ lớn
NLP Natural Language Processing Xử lý ngôn ngữ tự nhiên
OCR Optical Character Recognition Nhận diện ký tự quang học
PDF Portable Document Format Định dạng tài liệu di động
RPA Robotic Process Automation Tự động hóa quy trình bằng robot
Seq2Seq Sequence-to-Sequence Kiến trúc dịch tự động chuỗi sang chuỗi
UML Unified Modeling Language Ngôn ngữ mô hình hóa thống nhất

 
DANH MỤC HÌNH ẢNH
Hình 2.1. Use case tổng quát 6
Hình 2.2. Biểu đồ hoạt động nhận dạng văn bản 11
Hình 2.3. Biểu đồ trình tự nhận dạng văn bản 12
Hình 2.4. Biểu đồ hoạt động xử lý chuyển đổi số hàng loạt 14
Hình 2.5. Biểu đồ trình tự xử lý chuyển đổi số hàng loạt 15
Hình 2.6. Biểu đồ hoạt động đổi tên tệp tin 16
Hình 2.7. Biểu đồ trình tự luồng đổi tên tệp tin hàng loạt 17
Hình 2.8. Biểu đồ triển khai hệ thống OCR Scanner 19
Hình 2.9. Biểu đồ Lớp (Class Diagram) 20
Hình 2.10. Schema chi tiết file `config.json` 22
Hình 2.11. Cấu trúc một mục từ điển trong `raw_dict.jsonl` 22
Hình 2.12. Biểu đồ lớp cơ sở dữ liệu hệ thống OCR Scanner 23
Hình 3.1. Giao diện đối chiếu kết quả OCR Dual-panel 26
Hình 3.2. Chức năng đổi tên tệp tin hàng loạt (Batch Rename) 26
Hình 3.3. Chức năng chia tách tài liệu PDF hàng loạt 27

 
DANH MỤC BẢNG BIỂU
Bảng 2.1. Mô tả nhiệm vụ của Actor 6
Bảng 2.2. Đặc tả Danh sách các Use Case tổng quát 7
Bảng 2.3. Đặc tả Use Case Nhận dạng văn bản 9
Bảng 2.4. Đặc tả Use Case Xử lý số hóa hàng loạt 13
Bảng 2.5. Đặc tả Use Case Tổ chức tệp tin 15
Bảng 2.6. Bảng cấu trúc dữ liệu vật lý 21
Bảng 2.7. Ánh xạ thực thể dữ liệu sang lưu trữ vật lý 24
Bảng 3.1. Bảng tổng hợp so sánh hiệu năng giữa các cấu hình tích hợp. 28
Bảng 3.2. So sánh chi phí và thời gian giữa phương pháp thủ công và tự động hóa 29

 
LỜI CẢM ƠN
Trong suốt quá trình học tập và thực hiện báo cáo thực tập chuyên ngành "Thực tập Hệ thống Thông tin Quản lý", em đã nhận được sự quan tâm, chỉ bảo và giúp đỡ tận tình từ phía nhà trường, thầy cô và bạn bè.
Trước hết, em xin gửi lời cảm ơn chân thành tới Ban Giám hiệu, cùng toàn thể quý thầy cô Khoa Công nghệ thông tin, Trường Đại học Điện Lực. Các thầy cô đã tận tâm truyền đạt cho em những kiến thức chuyên ngành quý báu, từ nền tảng lập trình cơ bản đến các khái niệm chuyên sâu về phân tích, thiết kế và kiến trúc phần mềm. Đây là hành trang không thể thiếu giúp em tự tin bước vào môi trường thực tế.
Đặc biệt, em xin bày tỏ lòng biết ơn sâu sắc đến Giảng viên hướng dẫn. Thầy/Cô đã dành nhiều thời gian, tâm huyết để trực tiếp hướng dẫn, định hướng đề tài và đóng góp những ý kiến chuyên môn xác đáng, giúp em giải quyết những vướng mắc trong quá trình tích hợp các mô hình Trí tuệ nhân tạo phức tạp vào một hệ thống phần mềm hoàn chỉnh.
Do thời gian thực hiện đồ án và kiến thức thực tế còn hạn chế, báo cáo chắc chắn không tránh khỏi những thiếu sót. Em rất mong nhận được sự góp ý, chỉ bảo thêm từ quý thầy cô để đề tài được hoàn thiện hơn và bản thân em có thêm kinh nghiệm cho công việc sau này.
Em xin chân thành cảm ơn!
Hà Nội, ngày 16 tháng 5 năm 2026
Sinh viên thực hiện

Nguyễn Hoàng Thanh Tùng

LỜI NÓI ĐẦU
Trong bối cảnh cuộc Cách mạng Công nghiệp 4.0 và làn sóng chuyển đổi số đang diễn ra vô cùng mạnh mẽ trên quy mô toàn cầu, Dữ liệu (Data) đã vượt qua giới hạn của những con số đơn thuần để trở thành "nguồn tài nguyên mới", đóng vai trò cốt lõi trong mọi quyết định quản trị chiến lược của các tổ chức, doanh nghiệp. Cùng với xu hướng xây dựng Chính phủ điện tử và văn phòng không giấy tờ (Paperless office), việc số hóa khối lượng khổng lồ các tài liệu, hồ sơ hành chính đang trở thành một nhiệm vụ mang tính sống còn. Tuy nhiên, trong thực tiễn triển khai tại nhiều đơn vị, các Hệ thống thông tin quản lý (MIS) hiện tại mới chỉ dừng lại ở chức năng lưu trữ tĩnh, thiếu đi khả năng tự động trích xuất thông tin, khiến cho quy trình nhập liệu vẫn phụ thuộc nặng nề vào sức người, gây lãng phí nghiêm trọng nguồn lực và tiềm ẩn nhiều rủi ro sai sót.
Từ việc trực tiếp quan sát và trải nghiệm quy trình nghiệp vụ số hóa chuyên nghiệp tại doanh nghiệp trong quá trình thực tập, em nhận thấy nút thắt lớn nhất (bottleneck) không nằm ở các thao tác cơ học, mà nằm ở khâu bóc tách dữ liệu từ file ảnh/PDF sang định dạng văn bản có cấu trúc và công tác chuẩn hóa tên tệp tin trước khi lưu trữ. Xuất phát từ thực tế đầy thách thức đó, cùng với mong muốn vận dụng các kiến thức đã học về phân tích, thiết kế hệ thống và quản trị quy trình, em đã quyết định lựa chọn đề tài: "Hệ Thống Nhận Dạng Và Quản Lý Văn Bản Hành Chính Tiếng Việt" (ứng dụng OCR Scanner & File Tools) làm đồ án môn học thực tập Hệ thống thông tin Quản lý.
Không chỉ dừng lại ở yếu tố kỹ thuật, kiến trúc của hệ thống còn được định hướng chặt chẽ bởi tư duy quản trị: Toàn bộ quá trình xử lý được diễn ra hoàn toàn ngoại tuyến (Offline 100%) nhằm tuân thủ các Thỏa thuận bảo mật thông tin (NDA) khắt khe nhất; giao diện người dùng (UI/UX) được tối ưu hóa theo nguyên tắc công thái học với chế độ xem song song (Dual-panel) giúp giảm thiểu tải lượng nhận thức cho nhân sự. Thông qua đồ án này, em hy vọng mang đến một công cụ thực chiến, góp phần giải quyết bài toán quản trị nhân lực, tối ưu hóa chi phí vận hành (OPEX) và mang lại trải nghiệm làm việc hiện đại, chuyên nghiệp cho đội ngũ nhân sự hành chính tại các doanh nghiệp.

 
CHƯƠNG 1: KHẢO SÁT HIỆN TRẠNG VÀ XÁC LẬP DỰ ÁN
1.1. Giới thiệu về bối cảnh triển khai
Trong xu thế chính phủ điện tử và văn phòng không giấy tờ, nhu cầu số hóa tài liệu tại các cơ quan nhà nước và doanh nghiệp đang tăng vọt. Kéo theo đó là sự phát triển của các Công ty dịch vụ chuyển đổi số, chuyên đóng vai trò làm nhà thầu phụ (B2B) để thực hiện khối lượng công việc số hóa khổng lồ cho các dự án.
Trong thời gian thực tập tại một công ty hoạt động trong lĩnh vực chuyển đổi số và cung cấp dịch vụ số hóa chuyên nghiệp, em đã có cơ hội quan sát và trực tiếp tham gia vào luồng xử lý tài liệu hành chính quy mô lớn.
1.2. Khảo sát hiện trạng hoạt động nghiệp vụ
Quy trình cung cấp dịch vụ số hóa tại công ty hiện đang được thực hiện chủ yếu dựa trên sức người thông qua một chuỗi 11 bước cơ bản như sau:
• Nhận tài liệu giấy từ chủ thầu
• Phân loại tài liệu
• Chia ra chỉnh lý tài liệu
• Kiểm tra sau chỉnh lý
• Đánh số tài liệu
• Scan tài liệu thành File
• Kiểm tra chất lượng File Scan
• Bàn giao tài liệu gốc lại cho chủ thầu
• Nhập thủ công dữ liệu từ File Scan
• Xuất dữ liệu ra file Excel
• Bàn giao File Excel và File Scan cho chủ thầu
Phân tích chi tiết điểm nghẽn (Bottleneck) trong quy trình:
• Nhìn vào chuỗi cung ứng dịch vụ số hóa trên, từ bước 1 đến bước 8 là các thao tác vật lý liên quan đến tài liệu giấy (như chỉnh lý, tháo ghim, làm sạch mặt giấy, đưa vào máy scan công nghiệp). Các thao tác này bắt buộc phải có sự tham gia trực tiếp của con người và máy móc vật lý, khó có thể tự động hóa hoàn toàn bằng phần mềm. Tuy nhiên, điểm nghẽn (bottleneck) lớn nhất gây lãng phí nguồn lực, thời gian và thường xuyên xảy ra sai sót lại nằm ở khâu xử lý dữ liệu sau khi scan, cụ thể là Bước 9 và Bước 10:
o Nhập liệu hoàn toàn thủ công (Bước 9): Sau khi có được file ảnh scan, nhân sự hành chính phải thực hiện thao tác mở từng file PDF/Ảnh bằng trình xem ảnh ở một nửa màn hình, đồng thời mở phần mềm Microsoft Excel ở nửa màn hình còn lại. Nhân viên phải đọc bằng mắt các trường thông tin quan trọng trên văn bản (ví dụ: Tên văn bản, Số/Ký hiệu, Ngày tháng ban hành, Tên cơ quan, Trích yếu nội dung) và gõ phím nhập lại (re-type) toàn bộ vào các cột Excel tương ứng.
o Hậu quả: Việc này tiêu tốn hàng giờ đồng hồ cho mỗi bộ hồ sơ. Trung bình một nhân sự chỉ có thể xử lý khoảng 200 trang tài liệu mỗi ngày. Hơn nữa, việc liên tục chuyển hướng mắt giữa hai nửa màn hình và thao tác gõ phím lặp đi lặp lại khiến nhân sự rơi vào trạng thái mệt mỏi (cognitive load), dẫn đến tỷ lệ sai sót (typo) cực kỳ cao, đặc biệt là với các con số hợp đồng hoặc họ tên người.
o Quản lý và sắp xếp tệp tin lộn xộn (Bước 10): Các máy scan công nghiệp thường tự động lưu tệp tin và sinh ra những cái tên vô nghĩa dựa trên thời gian thực, ví dụ như `SCAN_20260510_1204.pdf`. Để bàn giao được cho chủ thầu, nhân sự lại phải tốn thêm một công đoạn là nhấp chuột (Right-click -> Rename) từng tệp tin hàng ngàn lần để đổi tên chúng theo đúng quy tắc mã hóa hồ sơ (ví dụ: `HĐ_01_Nguyễn_Văn_A.pdf`). Đây là công việc hoàn toàn cơ học, không tạo ra giá trị gia tăng nhưng lại chiếm đến 30% thời gian xử lý.
1.3. Xác lập dự án
Để giải quyết bài toán tối ưu hóa chi phí nhân sự và tăng tốc độ bàn giao dự án (Lead time), dự án phần mềm "OCR Scanner & File Tools" được đề xuất đưa vào quy trình nghiệp vụ của công ty chuyển đổi số.
• Mục tiêu tổng quát: Xây dựng một ứng dụng máy tính cục bộ (Desktop App) giúp tự động hóa hoàn toàn Bước 9 và Bước 10, giải phóng nhân sự khỏi công việc gõ phím nhàm chán.
• Mục tiêu cụ thể:
o Tích hợp động cơ AI (DocTR [1], PaddleOCR [2]) để tự động đọc và trích xuất văn bản từ hàng ngàn File Scan.
o Cung cấp công cụ (File Tools) đổi tên hàng loạt dựa trên quy tắc (Regex/Tiền tố), giúp chuẩn hóa tên file ngay lập tức.
o Tích hợp bộ từ điển tiếng Việt và thuật toán SymSpell [6] để tự động sửa lỗi chính tả sau khi máy tính nhận dạng, đảm bảo dữ liệu đưa ra Excel là chính xác nhất.
1.4. Phân tích yêu cầu hệ thống
Yêu cầu chức năng:
• Quản lý thu thập dữ liệu đầu vào: Nạp tệp tin hình ảnh, PDF đơn lẻ hoặc nguyên một thư mục (Batch OCR).
• Xử lý số hóa văn bản (OCR): Trích xuất văn bản từ hình ảnh/PDF, tự động đổ dữ liệu ra các file text/cấu trúc để dễ dàng chuyển đổi sang Excel.
• Quản lý chất lượng văn bản: Hậu xử lý kiểm tra và sửa lỗi chính tả tự động. Cung cấp giao diện Dual-panel để nhân sự đối chiếu nhanh chóng thay vì gõ lại từ đầu.
• Quản lý và Tổ chức tệp tin: Cung cấp module đổi tên, chia tách tệp PDF hàng loạt nhằm phục vụ bước chuẩn bị hồ sơ bàn giao.
Yêu cầu phi chức năng:
• Tính bảo mật thông tin và tuân thủ NDA (Bắt buộc tuyệt đối): Trong ngành dịch vụ chuyển đổi số B2B, các tài liệu giao nhận thường là hồ sơ mật của doanh nghiệp (Hợp đồng kinh tế, Báo cáo tài chính, Hồ sơ nhân sự). Công ty phải ký kết Thỏa thuận bảo mật thông tin (NDA - Non-Disclosure Agreement) vô cùng khắt khe với chủ thầu. Điều này đồng nghĩa với việc cấm tuyệt đối việc sử dụng các dịch vụ nhận diện API đám mây (như Google Cloud Vision, AWS Textract) vì rủi ro rò rỉ dữ liệu qua đường truyền mạng. Do đó, hệ thống phần mềm phải được thiết kế theo kiến trúc 100% Offline (Local Processing), mọi mô hình AI phải được tải về và chạy cục bộ trên máy tính nội bộ của công ty.
• Hiệu năng và Tối ưu tài nguyên: Phần mềm phải chạy đa luồng (multi-threading) để xử lý ảnh hàng loạt mà không gây hiện tượng tràn RAM (Memory Leak) làm treo máy tính văn phòng. Thuật toán tự động nhận diện và tận dụng GPU cục bộ (NVIDIA CUDA) nếu có để tăng tốc quá trình suy luận, hướng tới mục tiêu xử lý dưới 2 giây/trang A4.
• Yêu cầu về Công thái học UI/UX (Trải nghiệm người dùng): Người dùng phần mềm là các nhân viên nhập liệu làm việc liên tục 8 tiếng/ngày. Phần mềm yêu cầu phải có chế độ nền tối (Dark-mode) để giảm độ chói, chống hội chứng thị giác màn hình (CVS). Giao diện phải tuân thủ triết lý tối giản (Minimalist), các nút bấm phải lớn và rõ ràng, loại bỏ hoàn toàn các cấu hình kỹ thuật phức tạp ra khỏi tầm nhìn của người dùng thông thường.
1.5. Tính ưu việt và giá trị kinh tế của dự án
• Cắt giảm chi phí nhân sự (ROI): Tự động hóa bước 9 giúp giảm thiểu 80-90% thời gian gõ phím. Nhân sự thay vì "người gõ phím" giờ chuyển sang vai trò "người kiểm duyệt".
• Khép kín quy trình: Tích hợp cả tính năng OCR và tính năng đổi tên/cắt file (File Tools) vào chung một giao diện, nhân sự không cần mở 3-4 phần mềm khác nhau.
• Bảo mật tuyệt đối: Đáp ứng tiêu chuẩn cam kết bảo mật thông tin (NDA) khắt khe của các chủ thầu khi không sử dụng Internet.

CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG
2.1. Xác định các Actor và Use Case tổng quát
Bảng 2.1. Mô tả nhiệm vụ của Actor
Actor Mô tả
Quản trị viên (Admin) Người có kiến thức kỹ thuật, chịu trách nhiệm cấu hình và quản trị toàn bộ hệ thống OCR. Admin thực hiện lựa chọn mô hình nhận dạng văn bản như PaddleOCR hoặc DocTR, thiết lập tài nguyên xử lý CPU/GPU, cấu hình tham số tối ưu hiệu năng và quản lý bộ từ điển phục vụ sửa lỗi chính tả sau OCR. Ngoài ra, Admin còn giám sát hoạt động hệ thống, xử lý lỗi kỹ thuật và đảm bảo hệ thống vận hành ổn định.
Nhân viên hành chính (User) Người sử dụng trực tiếp hệ thống để phục vụ công việc nghiệp vụ hằng ngày. User thực hiện các thao tác như nạp ảnh hoặc tài liệu PDF, tiến hành quét OCR để trích xuất văn bản, kiểm duyệt và chỉnh sửa lỗi chính tả sau nhận dạng, đồng thời thực hiện đổi tên hoặc sắp xếp tệp hàng loạt nhằm hỗ trợ quản lý tài liệu nhanh chóng và hiệu quả.

Hình 2.1. Use case tổng quát
Hệ thống được thiết kế với 11 Use Case (ca sử dụng) riêng biệt, được phân rã thành 3 nhóm chức năng chính nhằm bao phủ toàn bộ vòng đời của tài liệu số hóa:
Bảng 2.2. Đặc tả Danh sách các Use Case tổng quát
Nhóm chức năng Tên Use Case Mô tả vai trò và chức năng
Nhóm quản trị hệ thống 1. Cấu hình hệ thống chuyên sâu Cung cấp cho Admin quyền tinh chỉnh các tham số kỹ thuật mức thấp nhằm tối ưu hiệu năng và độ chính xác của hệ thống. Bao gồm bật/tắt tăng tốc GPU, điều chỉnh ngưỡng độ tin cậy (Confidence Threshold), cấu hình thư mục lưu trữ dữ liệu, quản lý tài nguyên CPU/RAM và thiết lập bộ từ điển hậu xử lý chính tả.
Nhóm chức năng tiện ích 2. Đổi tệp tin hàng loạt Hỗ trợ chuẩn hóa tên của số lượng lớn tệp tin theo quy tắc định sẵn như thêm tiền tố, hậu tố, đánh số tự động hoặc áp dụng Regex nhằm đảm bảo tính nhất quán trước khi đưa vào quy trình số hóa tài liệu. 3. Tách/Gộp tài liệu PDF Cho phép người dùng tách một tài liệu PDF nhiều trang thành các file riêng lẻ hoặc gộp nhiều tệp PDF độc lập thành một bộ hồ sơ hoàn chỉnh để thuận tiện lưu trữ và xử lý. 4. Chuyển định dạng PDF sang Word Hỗ trợ chuyển đổi nhanh tài liệu PDF có sẵn lớp văn bản (Text-layer) sang định dạng Word nhằm phục vụ chỉnh sửa nội dung mà không cần thực hiện OCR lại. 5. Đánh số thứ tự tệp tin tự động Tự động sinh mã số tuần tự như 001, 002, 003… và gắn vào tên tệp nhằm hỗ trợ đối chiếu giữa hồ sơ giấy và hồ sơ số hóa một cách khoa học và dễ quản lý.
Nhóm chức năng số hóa 6. Nạp tài liệu ảnh/PDF Cho phép tải lên một hoặc nhiều tài liệu ảnh hoặc PDF vào hệ thống để chuẩn bị cho quá trình nhận dạng ký tự. Chức năng này đóng vai trò điểm khởi đầu của luồng xử lý OCR. (Include: Thực thi nhận dạng tài liệu) 7. Xem đối chiếu kết quả (Dual-panel) Cung cấp giao diện chia đôi màn hình giúp người dùng đồng thời quan sát ảnh gốc và văn bản OCR đầu ra để kiểm tra, chỉnh sửa và xác minh độ chính xác của dữ liệu nhận dạng. 8. Lưu và xuất kết quả văn bản Cho phép lưu nội dung sau khi chỉnh sửa và xuất ra các định dạng mở như .txt hoặc dữ liệu có thể sao chép trực tiếp sang Excel, Word hoặc hệ thống quản lý dữ liệu khác. 9. Thực thi quét tự động hàng loạt Tự động quét OCR cho toàn bộ thư mục tài liệu mà không yêu cầu người dùng thao tác thủ công từng file. Hệ thống sẽ lần lượt tiền xử lý, nhận dạng và lưu kết quả theo luồng tự động hóa hoàn chỉnh. (Include: Thực thi nhận dạng tài liệu) 10. Lựa chọn cấu hình nhận dạng Cho phép người dùng linh hoạt lựa chọn giữa các Engine OCR như PaddleOCR hoặc DocTR, đồng thời thay đổi bộ sửa lỗi chính tả và chế độ hậu xử lý phù hợp với từng loại tài liệu. (Include: Thực thi nhận dạng tài liệu) 11. Thực thi nhận dạng tài liệu (Single) Đây là ca sử dụng trung tâm của hệ thống OCR. Chức năng đảm nhận toàn bộ pipeline gồm tiền xử lý ảnh, tăng cường chất lượng dữ liệu đầu vào, gọi mô hình học sâu để nhận dạng văn bản và hậu xử lý ngôn ngữ nhằm tạo ra kết quả văn bản cuối cùng có độ chính xác cao. Mọi tác vụ quét OCR đều phụ thuộc vào ca sử dụng này.

2.2. Các chức năng chính của hệ thống
2.2.1. Chức năng Nhận dạng và chuyển đổi số văn bản (Core OCR)
Bảng 2.3. Đặc tả Use Case Nhận dạng văn bản
Thành phần Nội dung chi tiết
Tên Use case Nhận dạng và chuyển đổi số văn bản
Mô tả Đây là chức năng trung tâm của hệ thống OCR, thực hiện tự động hóa quá trình trích xuất văn bản từ hình ảnh hoặc tài liệu PDF. Hệ thống tiến hành tiền xử lý ảnh, gọi mô hình nhận dạng ký tự, hậu xử lý sửa lỗi chính tả và hiển thị kết quả theo chế độ đối chiếu song song (Dual-panel) giữa ảnh gốc và văn bản đầu ra nhằm hỗ trợ nhân viên kiểm duyệt và hiệu chỉnh dữ liệu nhanh chóng, chính xác.
Actor Nhân viên hành chính
Tiền điều kiện Phần mềm đã được khởi động thành công; người dùng đã chọn tối thiểu một tệp tin hợp lệ thuộc các định dạng được hỗ trợ như ảnh (.png, .jpg, .jpeg) hoặc tài liệu PDF (.pdf).

Đặc tả chi tiết Luồng sự kiện chính:
• Người dùng thao tác bấm nút "Bắt đầu quét" trên giao diện phần mềm.
• Hệ thống chuyển sang trạng thái "Đang xử lý" và hiện thanh tiến trình. Lớp Core Orchestrator thực hiện tiền xử lý hình ảnh (chuyển sang thang độ xám, giảm nhiễu) bằng bộ công cụ OpenCV.
• Dựa trên file cấu hình `config.json`, Core gọi hàm API tương ứng đến mô hình AI được chỉ định (Ví dụ: DocTR hoặc PaddleOCR) và truyền vào bộ nhớ ma trận ảnh.
• Mô hình AI xử lý chuyên sâu và phản hồi về dữ liệu tọa độ hình học cùng văn bản thô.
• Hệ thống lấy dữ liệu, ráp nối các từ thành câu hoàn chỉnh và thực hiện thuật toán kiểm tra chính tả nội bộ.
• Nếu cấu hình mô hình AI ngôn ngữ (ProtonX Nano) được bật, văn bản thô tiếp tục được gửi sang hệ thống NLP thứ hai để thực hiện suy luận ngữ cảnh theo kiến trúc Seq2Seq, "dịch" câu lỗi thành câu chuẩn và trả về văn bản đã khôi phục.
• Hệ thống tổng hợp kết quả cuối cùng, ra lệnh cho tầng Giao diện cập nhật màn hình hiển thị Dual-panel cho người dùng đối chiếu.

2.2.1.1. Biểu đồ hoạt động nhận dạng văn bản

Hình 2.2. Biểu đồ hoạt động nhận dạng văn bản
2.2.1.2. Biểu đồ trình tự nhận dạng văn bản
Biểu đồ trình tự là một công cụ phân tích quan trọng giúp hiểu rõ sự trao đổi thông điệp (Message passing) theo thời gian giữa các thành phần độc lập trong kiến trúc. Biểu đồ dưới đây minh họa rõ rệt sự phân tách trách nhiệm giữa ba thực thể: Tầng Giao diện (UI), Tầng Điều phối (Core) và Tầng Tích hợp (Black-box). Tầng Giao diện tuyệt đối không liên lạc trực tiếp với các mô hình AI mà mọi mệnh lệnh đều phải thông qua Bộ điều phối.

Hình 2.3. Biểu đồ trình tự nhận dạng văn bản
2.2.2. Chức năng Xử lý chuyển đổi số hàng loạt (Batch OCR)
Bảng 2.4. Đặc tả Use Case Xử lý số hóa hàng loạt
Thành phần Nội dung chi tiết
Tên Use case Xử lý số hóa hàng loạt (Batch OCR)
Mô tả Chức năng cho phép hệ thống tự động thực hiện nhận dạng OCR cho toàn bộ tài liệu trong một thư mục mà không cần người dùng thao tác thủ công trên từng tệp riêng lẻ, giúp tăng tốc quá trình số hóa dữ liệu quy mô lớn.
Actor Nhân viên hành chính
Điều kiện tiên quyết Thư mục đầu vào chứa ít nhất một tệp ảnh hoặc PDF hợp lệ để hệ thống tiến hành xử lý OCR tự động.

Đặc tả chi tiết Luồng sự kiện chính:
• Người dùng chọn thư mục nguồn chứa các tệp tin cần quét và thư mục đích để lưu kết quả.
• Hệ thống quét thư mục, tự động lọc ra danh sách các file có định dạng hỗ trợ hợp lệ (.png, .jpg, .pdf, .bmp, .tiff, .webp).
• Với mỗi file trong danh sách, hệ thống gọi lại toàn bộ luồng xử lý của Use Case Nhận dạng tài liệu: tiền xử lý ảnh → gọi Engine AI → hậu xử lý ngôn ngữ tự nhiên.
• Thanh tiến trình trên giao diện được cập nhật theo thời gian thực, hiển thị file đang xử lý và tỷ lệ hoàn thành (ví dụ: 5/1000 files).
• Kết quả văn bản của mỗi file được tự động lưu thành file `.txt` tương ứng trong thư mục đích ngay lập tức để giải phóng RAM.
• Khi toàn bộ danh sách đã xử lý xong, hệ thống hiển thị bảng tổng kết: Số file thành công, số file lỗi, và tổng thời gian xử lý.
• Luồng ngoại lệ: Nếu một file trong danh sách gặp lỗi (ảnh bị hỏng, file mã hóa), hệ thống tự động ghi nhận lỗi vào log, bỏ qua file đó và tiếp tục xử lý các file còn lại mà không làm treo toàn bộ tiến trình.
2.2.2.1. Biểu đồ hoạt động xử lý chuyển đổi số hàng loạt
Đây là chức năng thể hiện sức mạnh tự động hóa của phần mềm. Thay vì thao tác từng ảnh, luồng này cho phép số hóa toàn bộ thư mục một cách tự động, hoàn toàn không cần sự can thiệp của con người.

Hình 2.4. Biểu đồ hoạt động xử lý chuyển đổi số hàng loạt
2.2.2.2. Biểu đồ trình tự xử lý chuyển đổi số hàng loạt
Biểu đồ trình tự dưới đây minh họa sự trao đổi thông điệp giữa các thành phần hệ thống khi thực thi luồng xử lý số hóa hàng loạt. Điểm nổi bật là cơ chế xử lý lỗi linh hoạt: Khi một file gặp sự cố, hệ thống tự động ghi nhận và bỏ qua, tiếp tục xử lý file tiếp theo mà không làm gián đoạn toàn bộ tiến trình.

Hình 2.5. Biểu đồ trình tự xử lý chuyển đổi số hàng loạt
2.2.3. Chức năng Tổ chức và quản lý tệp tin (File Tools)
Bảng 2.5. Đặc tả Use Case Tổ chức tệp tin
Thành phần Nội dung chi tiết
Tên Use case Quản lý, đổi tên và chia tách tệp tin (File Tools)
Mô tả Chức năng hỗ trợ người dùng thực hiện đổi tên, đánh số thứ tự, tách hoặc gộp tệp tin hàng loạt nhằm chuẩn hóa cấu trúc tài liệu trước khi đưa vào quy trình quét OCR hoặc lưu trữ trong hệ thống quản lý hồ sơ số.
Actor Nhân viên hành chính

Đặc tả chi tiết Luồng sự kiện chính (Tính năng Đổi tên - Rename):
• Người dùng chọn thư mục chứa các tệp tin cần chuẩn hóa tên.
• Hệ thống quét và hiển thị danh sách tên file hiện tại trên giao diện bảng (Table).
• Người dùng thiết lập các quy tắc đổi tên tùy chỉnh: thêm Tiền tố (Prefix), thêm Hậu tố (Suffix), tìm và thay thế chuỗi ký tự (Search & Replace), hoặc đánh số thứ tự tự động theo quy định của dự án thầu.
• Thay vì đổi tên ngay, hệ thống tự động tính toán và hiển thị bản Xem trước (Preview) tên mới ngay bên cạnh tên cũ. Tính năng này giúp nhân sự kiểm soát hoàn toàn kết quả trước khi thực thi.
• Khi nhân sự xác nhận đồng ý, hệ thống gọi các lệnh hệ điều hành cấp thấp (`os.rename`) để thực thi đổi tên hàng loạt trên ổ cứng.
• Luồng ngoại lệ: Nếu tên file mới được thiết lập bị trùng lặp hoặc chứa ký tự cấm của Windows/Linux, hệ thống sẽ cảnh báo bằng màu đỏ và yêu cầu nhân sự điều chỉnh lại quy tắc.
2.2.3.1. Biểu đồ hoạt động tổ chức và quản lý tệp tin
Trong chuyển đổi số, việc chuẩn hóa tên file là bước cực kỳ quan trọng. Chức năng này giúp nhân sự hành chính chuẩn hóa tên hàng ngàn tài liệu lộn xộn trước khi lưu trữ hoặc quét OCR.

Hình 2.6. Biểu đồ hoạt động đổi tên tệp tin
2.2.3.2. Biểu đồ trình tự tổ chức và quản lý tệp tin
Biểu đồ trình tự dưới đây mô tả chi tiết sự tương tác giữa người dùng, giao diện và lớp xử lý nghiệp vụ trong quy trình đổi tên tệp tin hàng loạt. Điểm đặc biệt là cơ chế Preview cho phép người dùng kiểm soát hoàn toàn kết quả trước khi thực thi thay đổi trên ổ cứng.

Hình 2.7. Biểu đồ trình tự luồng đổi tên tệp tin hàng loạt
2.2.4. Phân tích nguyên tắc thiết kế Giao diện và Bảo mật
Bên cạnh các luồng chức năng cốt lõi, việc thiết kế phần mềm tại công ty số hóa không chỉ dừng lại ở việc "chạy được", mà phải tuân thủ nghiêm ngặt các tiêu chí về Công thái học (Ergonomics) và Bảo mật (Security) để đảm bảo hiệu suất nhân sự và uy tín với chủ thầu:
• Nguyên tắc Công thái học Phần mềm trong Giao diện (UI/UX):
o Kiến trúc Dual-panel (Màn hình song song): Trước đây, nhân sự phải dùng một màn hình để mở file PDF và một màn hình khác để gõ Word/Excel, buộc họ phải liên tục quay cổ qua lại. Hệ thống OCR Scanner giải quyết triệt để nút thắt này bằng giao diện Dual-panel: Nửa trái hiển thị ảnh chụp bản gốc đã được nhận diện Bounding-box, nửa phải hiển thị văn bản OCR có thể chỉnh sửa trực tiếp (Rich Text Editor).
o Thiết kế này tuân thủ nguyên lý giảm Tải lượng nhận thức (Cognitive Load), cho phép mắt người dùng dễ dàng đối chiếu song song ở khoảng cách gần, giảm thiểu tối đa hiện tượng gõ sai dòng hoặc rớt từ (typo).
• Quy định Bảo mật Dữ liệu (Data Privacy) và Kiến trúc Offline:
o Trong quá trình xử lý hồ sơ B2B, các tài liệu nhận từ chủ thầu thường mang tính chất bảo mật tuyệt đối (như Hợp đồng kinh tế lớn, Báo cáo tài chính nội bộ, thông tin cá nhân khách hàng). Việc vô tình tải (upload) những dữ liệu này lên các API đám mây (như Google Vision API hay AWS Textract) là hành vi bị nghiêm cấm hoàn toàn, có thể dẫn tới vi phạm hợp đồng NDA (Thỏa thuận bảo mật) gây thiệt hại hàng tỷ đồng.
o Để giải quyết bài toán này, toàn bộ hệ thống trí tuệ nhân tạo (từ DocTR, PaddleOCR cho tới ProtonX Nano) đều được đóng gói và tải trực tiếp các tệp trọng số (pre-trained weights) về máy tính nội bộ. Kiến trúc phần mềm hoạt động 100% Offline (Local Processing). Dữ liệu sau khi xử lý chỉ tồn tại trên thanh RAM vật lý của máy tính và được ghi đè/xóa vĩnh viễn khi tắt phần mềm, đảm bảo dữ liệu không bao giờ rời khỏi hệ thống mạng nội bộ (Intranet) của doanh nghiệp.
2.3. Thiết kế kiến trúc và cấu trúc dữ liệu
Dưới đây là các biểu đồ thiết kế hệ thống theo tiêu chuẩn ngôn ngữ mô hình hóa thống nhất (UML), nhằm minh họa trực quan sự tương tác giữa các thành phần và các luồng xử lý dữ liệu phức tạp bên trong phần mềm.
2.3.1. Biểu đồ triển khai (Deployment Diagram)
Biểu đồ triển khai dưới đây mô tả cách các thành phần phần mềm được bố trí và vận hành trên hạ tầng vật lý thực tế. Do đặc thù là ứng dụng Desktop xử lý cục bộ (Local Processing), toàn bộ hệ thống được triển khai trên một máy tính duy nhất của người dùng, không yêu cầu máy chủ hay kết nối mạng.

Hình 2.8. Biểu đồ triển khai hệ thống OCR Scanner
Điểm đặc biệt của mô hình triển khai này là tính tự chủ hoàn toàn: Không có bất kỳ thành phần nào yêu cầu kết nối tới máy chủ bên ngoài (Cloud Server) hay dịch vụ API trả phí. Mọi quá trình nhận dạng hình ảnh, suy luận ngôn ngữ và kiểm tra chính tả đều diễn ra trong không gian bộ nhớ cục bộ của máy tính người dùng.
Kiến trúc này đảm bảo tuyệt đối tính bảo mật cho các tài liệu hành chính nhạy cảm, đồng thời cho phép phần mềm hoạt động hoàn toàn ở chế độ ngoại tuyến (Offline).
2.3.2. Biểu đồ Lớp (Class Diagram)
Biểu đồ lớp dưới đây thể hiện việc áp dụng Mẫu thiết kế phần mềm (Design Pattern) chuyên nghiệp vào thực tiễn. Thay vì mã hóa cứng (Hard-code) việc gọi trực tiếp đến từng thư viện AI, hệ thống định nghĩa một Lớp trừu tượng `BaseOCREngine`.
Tất cả các mô hình học sâu muốn tích hợp vào hệ thống đều phải tạo ra một Lớp triển khai (Implement) thừa kế từ Lớp trừu tượng này và ghi đè phương thức `extract_text()`. Lớp trung tâm `OCRController` chỉ tương tác với Lớp trừu tượng, nhờ đó đạt được nguyên tắc Mở/Đóng (Open/Closed Principle) trong kỹ nghệ phần mềm: Hệ thống mở rộng dễ dàng (thêm mô hình mới) mà không cần phải chỉnh sửa mã nguồn cốt lõi hiện tại.

Hình 2.9. Biểu đồ Lớp (Class Diagram)
2.3.3. Cấu trúc dữ liệu hệ thống (Data Schema)
Do đặc thù là một ứng dụng Desktop xử lý theo phiên (Session-based), hệ thống không sử dụng các hệ quản trị cơ sở dữ liệu quan hệ (RDBMS) truyền thống như MySQL hay SQL Server. Thay vào đó, chiến lược lưu trữ dữ liệu được thiết kế tối giản theo triết lý "File-based Storage", phù hợp với quy mô và yêu cầu của phần mềm:

Bảng 2.6. Bảng cấu trúc dữ liệu vật lý
Tên file Định dạng Dung lượng Mục đích Thời điểm truy xuất
config.json JSON ~1 KB Lưu trữ cấu hình mặc định của hệ thống như Engine OCR đang sử dụng, trạng thái bật/tắt các tính năng AI, ngưỡng độ tin cậy và đường dẫn thư mục xử lý dữ liệu. Được đọc khi khởi động phần mềm và cập nhật lại khi người dùng thay đổi cấu hình.
raw_dict.jsonl JSONL ~4.9 MB Chứa bộ từ điển tiếng Việt với hơn 100.000 mục từ phục vụ thuật toán sửa lỗi chính tả SymSpell trong giai đoạn hậu xử lý OCR. Được tải lên bộ nhớ RAM ngay khi hệ thống khởi động để tối ưu tốc độ tra cứu.
FileResult In-memory Object Dynamic Lưu trữ tạm thời toàn bộ kết quả OCR của từng tài liệu bao gồm đường dẫn file, Engine nhận dạng, trạng thái xử lý, văn bản thô, văn bản đã sửa lỗi, thời gian xử lý, độ tin cậy và thống kê ký tự. Được khởi tạo mới sau mỗi lần quét OCR và giải phóng khi kết thúc phiên làm việc.
\*.txt Plain Text Dynamic Tệp đầu ra chứa nội dung văn bản đã được nhận dạng và hậu xử lý hoàn chỉnh để phục vụ lưu trữ hoặc sử dụng cho các hệ thống khác. Được ghi ra ổ đĩa sau mỗi lần nhận dạng OCR thành công.

Schema chi tiết file `config.json`:

Hình 2.10. Schema chi tiết file `config.json`
Cấu trúc một mục từ điển trong `raw_dict.jsonl` (mỗi dòng là một JSON object):

Hình 2.11. Cấu trúc một mục từ điển trong `raw_dict.jsonl`
Việc lựa chọn chiến lược lưu trữ bằng File-based thay vì sử dụng các Hệ quản trị Cơ sở dữ liệu quan hệ (RDBMS) lớn như MySQL hay SQL Server là một quyết định kiến trúc mang đậm tính thực tiễn quản trị. Phân tích lợi ích mang lại:
o Giảm thiểu độ phức tạp triển khai (Deployment Complexity): Đối với một ứng dụng Desktop nội bộ, nếu yêu cầu người dùng cuối (thường là nhân viên hành chính) phải tự cài đặt thêm một MySQL Server, cấu hình Port, User/Password là điều bất khả thi. Kiến trúc File-based cho phép phần mềm đạt được trạng thái "Plug-and-play" (Cắm là chạy), chỉ cần giải nén thư mục là ứng dụng đã có thể hoạt động lập tức mà không cần sự hỗ trợ của đội ngũ IT Helpdesk.
o Hiệu năng truy xuất in-memory (O(1)): Hệ thống từ điển sửa lỗi chính tả có tới hơn 100.000 bản ghi. Nếu truy vấn qua RDBMS với lệnh `SELECT` cho mỗi từ, tốc độ sẽ bị giảm đáng kể do độ trễ kết nối (Network Latency) và I/O Disk. Thay vào đó, việc dùng tệp `.jsonl` tĩnh cho phép phần mềm nạp toàn bộ dữ liệu này thẳng lên RAM ngay khi khởi động. Kết hợp với cấu trúc dữ liệu Hash Map (từ điển), thời gian tra cứu từ vựng được giảm xuống mức lý tưởng O(1) – tốc độ chỉ tính bằng micro-giây, đáp ứng hoàn hảo yêu cầu xử lý hàng ngàn từ vựng mỗi trang giấy theo thời gian thực (Real-time).
2.3.4. Biểu đồ lớp cơ sở dữ liệu (Database Class Diagram)
Mặc dù hệ thống sử dụng chiến lược lưu trữ File-based thay vì RDBMS truyền thống (như đã phân tích ở mục 2.3.3), biểu đồ lớp cơ sở dữ liệu dưới đây mô hình hóa cấu trúc dữ liệu logic của hệ thống theo chuẩn UML, thể hiện rõ mối quan hệ giữa các thực thể dữ liệu và cách chúng được ánh xạ sang các file lưu trữ vật lý tương ứng:

Hình 2.12. Biểu đồ lớp cơ sở dữ liệu hệ thống OCR Scanner

 
Bảng 2.7. Ánh xạ thực thể dữ liệu sang lưu trữ vật lý
Thực thể (Entity) Hình thức lưu trữ Ghi chú
CauHinhHeThong File config.json trên ổ cứng Chứa các thông số cấu hình của hệ thống OCR như Engine mặc định, đường dẫn xử lý và trạng thái tính năng AI. Được đọc khi khởi động và cập nhật khi thay đổi cài đặt.
MucTuDien File raw_dict.jsonl (~4.9 MB) Lưu bộ từ điển tiếng Việt phục vụ thuật toán sửa lỗi chính tả SymSpell. Toàn bộ dữ liệu được nạp vào RAM khi hệ thống khởi động để tăng tốc độ tra cứu.
KetQuaFile Đối tượng FileResult trên RAM Lưu kết quả OCR tạm thời của từng tài liệu bao gồm nội dung nhận dạng, trạng thái xử lý, độ tin cậy và thông tin thống kê. Được tạo mới mỗi lần quét OCR.
FileKetXuat File .txt trên ổ cứng Chứa văn bản đầu ra sau khi nhận dạng và hậu xử lý hoàn tất. Được ghi xuống ổ đĩa sau mỗi lần quét thành công.
PhienLamViec Biến trạng thái trên RAM Lưu trạng thái hoạt động hiện tại của người dùng như danh sách file đang xử lý, tiến trình OCR và cấu hình tạm thời. Chỉ tồn tại trong phiên làm việc hiện tại.

 
CHƯƠNG 3: TRIỂN KHAI TÍCH HỢP VÀ XÂY DỰNG HỆ THỐNG
3.1. Công nghệ sử dụng
Hệ thống được phát triển và vận hành dựa trên một hệ sinh thái công nghệ đa dạng, được lựa chọn kỹ lưỡng nhằm đáp ứng yêu cầu xử lý đồ họa, học sâu và thiết kế giao diện trên máy tính để bàn:
• Ngôn ngữ và Môi trường: Python 3.10 được chọn làm ngôn ngữ lập trình chính nhờ sức mạnh vượt trội trong lĩnh vực khoa học dữ liệu và hỗ trợ tốt các thư viện hệ thống. Việc thực nghiệm được chạy trên hệ điều hành Windows 11.
• Nền tảng Phần cứng & Tăng tốc tính toán: Để các mô hình AI có thể hoạt động mượt mà, hệ thống đòi hỏi thiết bị cài đặt hạ tầng NVIDIA CUDA Toolkit (kèm cuDNN) để có thể truy xuất và khai thác sức mạnh tính toán song song của nhân GPU cục bộ.
• Thư viện Giao diện Người dùng: Thư viện `CustomTkinter` được sử dụng để lập trình Giao diện đồ họa (GUI). Thư viện này kế thừa sức mạnh của hệ thống Tkinter truyền thống nhưng mang lại phong cách thiết kế giao diện hiện đại, bóng bẩy và chuyên nghiệp hơn, hỗ trợ tốt các chế độ chủ đề (Dark/Light mode).
• Thư viện AI và Xử lý ảnh: Thư viện mã nguồn mở OpenCV [9] (`cv2`) đảm nhiệm mọi thao tác biến đổi không gian ảnh. Các nền tảng học sâu cốt lõi như PyTorch và PaddlePaddle được cấu hình thành môi trường nền tảng để chạy các Engine tích hợp. Module `transformers` do HuggingFace cung cấp được sử dụng để kết nối và gọi siêu mô hình ngôn ngữ ProtonX Nano Legal Text Correction [5].
3.2. Giao diện hệ thống.
3.2.1. Giao diện màn hình OCR tài liệu.
Giao diện chính phục vụ chức năng cốt lõi của hệ thống, được thiết kế theo dạng đối chiếu song song (Dual-panel). Hệ thống cung cấp các thanh công cụ điều hướng, chọn Engine và bảng nhật ký xử lý chi tiết.

Hình 3.1. Giao diện đối chiếu kết quả OCR Dual-panel
3.2.2. Giao diện màn hình đổi tên tài liệu hàng loạt.
Màn hình này cho phép người dùng chuẩn hóa tên tệp tin số lượng lớn theo các quy tắc định sẵn. Giao diện bao gồm khu vực thiết lập quy tắc (thêm tiền tố, hậu tố, thay thế chuỗi bằng Regex) và bảng danh sách tệp tin hiển thị kết quả xem trước (Preview) tên mới trước khi thực thi, giúp giảm thiểu sai sót trong quá trình quản lý hồ sơ.

Hình 3.2. Chức năng đổi tên tệp tin hàng loạt (Batch Rename)
3.2.3. Giao diện màn hình tách file hàng loạt
Đây là công cụ hỗ trợ xử lý các tệp PDF đa trang. Giao diện tập trung vào sự đơn giản, cho phép người dùng nạp tệp PDF gốc và tự động bóc tách từng trang thành các tệp tin độc lập. Màn hình hiển thị danh sách các trang đã tách kèm theo trạng thái xử lý thành công, phục vụ cho việc số hóa tài liệu lẻ từ các tập hồ sơ lớn.

Hình 3.3. Chức năng chia tách tài liệu PDF hàng loạt
3.3. Kết quả thực nghiệm
Sau một thời gian tích cực lập trình và tinh chỉnh hệ thống, dự án đã triển khai thành công mô hình tích hợp kiến trúc hộp đen và tiến hành thực nghiệm thực tế trên nhiều mẫu văn bản, tài liệu, công văn tiếng Việt khác nhau. Các kết quả thu thập được chứng minh rõ rệt tính ưu việt của phương pháp tiếp cận:
• Trường hợp tích hợp DocTR [1] và Thuật toán SymSpell [6]: Khi hệ thống được cấu hình chạy module DocTR kết hợp xử lý từ điển nội bộ, phần mềm mang lại độ chính xác trung bình đạt 92% trong thời gian phản hồi khoảng 2 giây cho một trang văn bản kích thước tiêu chuẩn A4. Mặc dù tốc độ không phải là nhanh nhất, nhưng phương thức này tiêu thụ lượng RAM đồ họa ở mức vừa phải, chứng tỏ đây là một cấu hình hoàn toàn phù hợp và kinh tế để triển khai cho các máy tính văn phòng có cấu hình trung bình.
• Trường hợp tích hợp cấu hình cao cấp PaddleOCR [2] kết hợp ProtonX Nano [5]: Với các thiết bị máy tính sở hữu card đồ họa mạnh, việc thiết lập phần mềm sử dụng Engine PaddleOCR đem lại một tốc độ xử lý siêu tốc, quét toàn bộ hình ảnh trong thời gian chưa tới 1 giây. Việc xuất hiện hiện tượng rớt dấu của PaddleOCR đã được khắc phục một cách hoàn hảo nhờ module hậu xử lý ProtonX Nano. Khả năng phân tích và hiểu cấu trúc ngữ pháp thông qua kiến trúc Seq2Seq [10] đã giúp mô hình dịch toàn bộ câu văn lỗi thành câu văn đúng chuẩn, khôi phục thành công các dấu câu bị mất, đẩy chỉ số chính xác tổng thể (Overall Accuracy) của toàn bộ hệ thống lên tới mức 95-96%. Kết quả đầu ra là những đoạn văn bản liền mạch, đúng chính tả, ngữ nghĩa trôi chảy và sẵn sàng để lưu trữ ngay lập tức.
• Tích hợp bộ công cụ phụ trợ (File Tools): Bên cạnh chức năng cốt lõi là nhận dạng, tính năng đổi tên tệp tin hàng loạt (Batch Renaming) và chia cắt tài liệu (File Splitting) đã phát huy hiệu quả to lớn trong thực tế. Nó giúp người dùng tổ chức, sắp xếp lại hàng ngàn tài liệu hình ảnh, PDF lộn xộn thành một kho dữ liệu có cấu trúc định dạng chuẩn mực trước khi đưa vào luồng quét OCR, góp phần hoàn thiện một quy trình số hóa khép kín.
• Ngoài ra, hệ thống xử lý thao tác hàng loạt (Batch Processing) vận hành ổn định. Chức năng này cho phép một nhân sự hành chính chỉ cần thực hiện duy nhất một thao tác chọn thư mục nguồn, phần mềm sẽ tự động đẩy hàng loạt ảnh chụp màn hình qua pipeline xử lý của hệ thống tích hợp và lần lượt xuất file kết quả. Theo ước tính, quy trình này giúp giảm thiểu tới 80-90% khối lượng thời gian so với phương pháp gõ phím sao chép văn bản truyền thống.
Bảng 3.1. Bảng tổng hợp so sánh hiệu năng giữa các cấu hình tích hợp.
Cấu hình Engine OCR Hậu xử lý Độ chính xác Thời gian / trang A4 VRAM yêu cầu Đối tượng phù hợp
Cơ bản DocTR SymSpell ~92% ~2 giây ~2 GB Máy văn phòng tầm trung
Nhanh PaddleOCR Fast SymSpell ~88–90% < 1 giây ~1.5 GB Ưu tiên tốc độ xử lý
Cao cấp PaddleOCR ProtonX Nano Seq2Seq ~95–96% ~1 giây OCR + ~2 giây NLP ~4 GB Máy có GPU mạnh
Tối ưu Ensemble DocTR + PaddleOCR ProtonX Nano Seq2Seq ~96–97% ~3–4 giây ~6 GB Ưu tiên chất lượng đầu ra
3.3.1. Đánh giá Hiệu quả Kinh tế và Tối ưu nguồn lực (ROI):
• Dưới góc độ của một doanh nghiệp cung cấp dịch vụ số hóa B2B, bài toán lớn nhất không phải là độ chính xác tuyệt đối của AI, mà là bài toán tối ưu chi phí vận hành (OPEX).
• Để chứng minh giá trị thực tiễn của phần mềm "OCR Scanner & File Tools", một bảng Phân tích Chi phí - Lợi ích (Cost-Benefit Analysis - CBA) đã được thiết lập dựa trên một dự án mẫu: Số hóa 10.000 trang tài liệu hành chính.
Bảng 3.2. So sánh chi phí và thời gian giữa phương pháp thủ công và tự động hóa
Hạng mục đánh giá Phương pháp nhập liệu thủ công (Cũ) Áp dụng OCR Scanner (Mới) Mức độ cải thiện
Số lượng nhân sự cần thiết 5 nhân viên đánh máy 1 nhân viên kiểm duyệt (QC) Giảm 80% nhân sự
Thời gian hoàn thành (Lead time) 7 ngày (tương đương 35 ngày công) 1.5 ngày (~1.5 ngày công) Tốc độ xử lý tăng khoảng 4.6 lần
Tổng số ngày công 35 ngày công (5 người × 7 ngày) 1.5 ngày công (1 người × 1.5 ngày) Tiết kiệm 33.5 ngày công
Chi phí nhân sự ước tính (200.000 VNĐ/ngày công) 7.000.000 VNĐ 300.000 VNĐ Tiết kiệm khoảng 95.7% chi phí
Chi phí máy móc / Hạ tầng Sử dụng 5 PC văn phòng thông thường Sử dụng 1 PC cấu hình cao (GPU) chạy xử lý khoảng 5–6 giờ Giảm số lượng thiết bị vận hành và hao mòn phần cứng

Phân tích Điểm hòa vốn (Break-even Point) và ROI:
• Khi áp dụng phần mềm này vào luồng nghiệp vụ (tại Bước 9 và Bước 10), công ty có thể tiết kiệm được khoảng 6.700.000 VNĐ cho mỗi 10.000 trang tài liệu được số hóa. Đối với một doanh nghiệp số hóa xử lý trung bình 100.000 trang tài liệu mỗi tháng:
o Chi phí tiết kiệm hàng tháng (OPEX Savings): ~67.000.000 VNĐ/tháng.
o Tái đầu tư: Số tiền tiết kiệm được có thể dùng để khấu hao nhanh chóng chi phí trang bị 1 máy tính trạm (Workstation) cấu hình cao (khoảng 30-40 triệu VNĐ) chỉ trong chưa đầy 1 tháng. Điểm hòa vốn (Break-even point) của dự án phần mềm đạt được ngay trong tháng đầu tiên triển khai.
o Tối ưu nguồn lực: 4 nhân sự được giải phóng khỏi công việc đánh máy nhàm chán có thể được luân chuyển sang các khâu chỉnh lý tài liệu giấy (Bước 1-8) hoặc đảm nhận các dự án song song khác. Hiệu suất tổng thể (Productivity) tăng xấp xỉ 350%, giúp công ty có thể nhận số lượng gói thầu gấp 3 lần so với trước đây mà không cần tuyển thêm nhân sự hành chính.
3.3.2. Đánh giá hiệu quả tích hợp hệ thống:
• Kết quả thực nghiệm cho thấy sự khác biệt rõ rệt giữa việc sử dụng các Engine OCR đơn lẻ và việc tích hợp chúng thông qua kiến trúc Orchestrator. Khi chạy PaddleOCR [2] một mình mà không có hậu xử lý, độ chính xác chỉ đạt khoảng 82-85% do hiện tượng mất dấu thanh tiếng Việt. Tuy nhiên, khi tích hợp cùng tầng hậu xử lý ProtonX Nano [5] thông qua pipeline Black-box, chỉ số này được đẩy lên 95-96%, một bước nhảy vọt khoảng 10-13 điểm phần trăm. Điều này minh chứng rằng giá trị cốt lõi của đồ án không nằm ở từng mô hình riêng lẻ, mà nằm ở nghệ thuật tích hợp và điều phối chúng làm việc đồng bộ.
• Đặc biệt, cơ chế Ensemble (chạy song song cả DocTR [1] và PaddleOCR [2], sau đó so sánh Confidence Score để chọn kết quả tốt hơn) đã chứng minh rằng việc kết hợp nhiều chuyên gia AI luôn cho kết quả vượt trội so với việc tin tưởng vào một nguồn duy nhất. Đây chính là ứng dụng thực tiễn của nguyên lý Tích hợp hệ thống mà môn học đề cập.

KẾT LUẬN
Đề tài "Hệ Thống Nhận Dạng Và Quản Lý Văn Bản Hành Chính Tiếng Việt" là một minh chứng rõ nét cho việc vận dụng hiệu quả các nền tảng lý thuyết từ môn học Hệ thống thông tin Quản lý vào việc giải quyết các bài toán thực tiễn của doanh nghiệp. Xuyên suốt quá trình thực tập tại công ty chuyển đổi số, thông qua việc trực tiếp khảo sát và tham gia vào quy trình 11 bước cung cấp dịch vụ số hóa chuyên nghiệp, em đã có cơ hội phân tích tường tận các luồng nghiệp vụ, qua đó phát hiện ra những điểm nghẽn (bottleneck) nghiêm trọng làm suy giảm năng suất tại khâu nhập liệu thủ công và tổ chức lưu trữ tài liệu.
Để khắc phục triệt để vấn đề này, dự án đã thiết kế và hiện thực hóa thành công một hệ thống phần mềm Desktop hoàn chỉnh mang tên "OCR Scanner & File Tools". Hệ thống cung cấp một giải pháp toàn diện, khép kín từ khâu số hóa dữ liệu (tích hợp các Engine OCR tiên tiến như DocTR và PaddleOCR), hậu xử lý sửa lỗi tự động bằng công nghệ AI (ProtonX Nano, SymSpell) phù hợp với đặc thù tiếng Việt, cho đến việc quản lý và chuẩn hóa định dạng file lưu trữ một cách khoa học.
Thông qua đồ án này, em đã đạt được những kết quả đáng kể cả về mặt kiến thức chuyên môn lẫn kinh nghiệm thực tiễn:
Về mặt phân tích và thiết kế: Nắm vững và ứng dụng thành thạo ngôn ngữ mô hình hóa thống nhất (UML) để xây dựng hệ thống tài liệu kỹ thuật chuẩn mực, từ biểu đồ Use Case, Activity Diagram cho đến Class Diagram và Sequence Diagram, giúp mô tả chính xác sự tương tác giữa các thực thể trong hệ thống.
Về mặt kiến trúc phần mềm: Xây dựng thành công kiến trúc Black-box và Orchestrator, kết hợp kiến trúc File-based phù hợp với tính chất của ứng dụng cục bộ (Local App), giúp phần mềm vừa dễ dàng mở rộng (Plug-and-play) vừa đáp ứng các tiêu chuẩn bảo mật thông tin nội bộ (NDA) khắt khe nhất của thị trường B2B.
Về mặt quản trị và hiệu quả kinh tế (ROI): Đưa ra một giải pháp mang lại giá trị định lượng rõ ràng cho doanh nghiệp, giúp cắt giảm hơn 80% thời gian nhập liệu, tăng 350% năng suất làm việc tổng thể và mang lại hiệu quả hoàn vốn chỉ sau một tháng triển khai. Đây là minh chứng cho thấy công nghệ thông tin khi được định hướng đúng đắn bởi tư duy quản trị sẽ tạo ra lợi thế cạnh tranh to lớn.

Mặc dù hệ thống đã đáp ứng tốt các yêu cầu hiện tại, tuy nhiên để sản phẩm ngày càng hoàn thiện và mang lại giá trị cao hơn, trong thời gian tới hệ thống có thể được phát triển theo các hướng sau:
Tối ưu hóa quy trình và mô hình AI: Tiếp tục nghiên cứu và tinh chỉnh (Fine-tuning) các mô hình nhận dạng cũng như mô hình ngôn ngữ lớn chuyên biệt cho các loại tài liệu đặc thù hơn (như hóa đơn tài chính, bản vẽ kỹ thuật) nhằm nâng cao độ chính xác tổng thể.
Đóng gói và thương mại hóa: Áp dụng các công cụ như PyInstaller để đóng gói toàn bộ ứng dụng và môi trường Python thành một tệp thực thi độc lập (.exe), giúp quá trình triển khai trên các thiết bị máy tính trạm của nhân viên dễ dàng hơn, không đòi hỏi phải thiết lập môi trường lập trình phức tạp.
Khả năng tích hợp mở rộng: Xây dựng hệ thống API nội bộ (Local API) nhằm tự động đẩy thẳng dữ liệu đã kết xuất (dưới dạng JSON hoặc Excel) lên hệ thống phần mềm Quản trị nguồn lực doanh nghiệp (ERP) nội bộ hoặc bàn giao tự động lên cổng thông tin của các chủ thầu, tạo nên một dây chuyền số hóa liên tục và hoàn toàn không chạm (Zero-touch processing).

 
TÀI LIỆU THAM KHẢO
[1]. Mindee, "DocTR: Document Text Recognition," 2022, from: <https://github.com/mindee/doctr>.
[2]. PaddlePaddle Team, "PaddleOCR: Awesome multilingual OCR toolkits based on PaddlePaddle," 2023, from: <https://github.com/PaddlePaddle/PaddleOCR>.
[3]. pbcquoc, "VietOCR: A framework for building OCR system for Vietnamese text," 2021, from: <https://github.com/pbcquoc/vietocr>.
[4]. D. Q. Nguyen; A. T. Nguyen, "PhoBERT: Pre-trained language models for Vietnamese. Findings of the Association for Computational Linguistics: EMNLP 2020," 2020.
[5]. ProtonX, "ProtonX Legal Text Correction Model," 2023, from: <https://huggingface.co/protonx/protonx-legal-text-correction>.
[6]. W. Garbe, "SymSpell: 1 million times faster through Symmetric Delete spelling correction algorithm," 2012, from: <https://github.com/wolfgarbe/SymSpell>.
[7]. V. Sanh; L. Debut; J. Chaumond; T. Wolf, "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter," 2019.
[8]. R. Smith, "An overview of the Tesseract OCR engine. Ninth International Conference on Document Analysis and Recognition (ICDAR 2007)," 2007.
[9]. G. Bradski, "The OpenCV Library," Dr. Dobb's Journal of Software Tools, vol. 120, pp. 122-125, 2000.
[10]. Author: J. Devlin; M.-W. Chang; K. Lee; K. Toutanova, "Pre-training of deep bidirectional transformers for language understanding. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies," 2019.
[11]. J. L. Schönberger; J. M. Frahm, "Structure-from-motion revisited. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)," 2016.
[12]. M. T. e. al, "Adapting BERT for named entity recognition in OCR," Computational Linguistics and Intellectual Technologies, vol. 20, 2021.
[13]. Y. Baek; B. Lee; D. Han; S. Yun; H. Lee, "Character region awareness for text detection. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)," 2019.
