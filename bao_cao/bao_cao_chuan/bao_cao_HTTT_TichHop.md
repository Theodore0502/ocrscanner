 
ĐỀ CƯƠNG THỰC TẬP MÔN
THỰC TẬP HỆ THỐNG THÔNG TIN TÍCH HỢP

1. Tên đề tài: Hệ Thống Nhận dạng Và Xử Lý Văn Bản Tiếng Việt Tích hợp Đa Engine OCR
2. Sinh viên thực hiện:
   Họ và tên: Nguyễn Hoàng Thanh Tùng. MSSV: 22810310248.
   Số điện thoại: 0969386663. Email: tung2004nguyen52@gmail.com.
   Vị trí thực tập: Nhân sự Nghiên cứu và Triển khai.
3. Giảng viên hướng dẫn:
   Họ và tên: Phạm Quang Huy. Học vị: Tiến sĩ.
   Số điện thoại: 0982048668 Email: huypq@epu.edu.vn.
   Đơn vị công tác: Khoa Công Nghệ Thông Tin trường Đại học Điện Lực.
4. Mô tả tóm tắt đề tài
   Đề tài tập trung xây dựng hệ thống cho phép người dùng tự động hóa quy trình số hóa tài liệu và văn bản hành chính Tiếng Việt một cách nhanh chóng và chính xác. Hệ thống cung cấp các chức năng cơ bản như quét ảnh trích xuất văn bản thô, chia tách/gộp tài liệu PDF (Split/Merge) và chuẩn hóa tên tệp tin hàng loạt (Batch Rename). Bên cạnh đó, hệ thống còn tích hợp giao diện đối chiếu song song (Dual-panel) để người dùng có thể dễ dàng so sánh và chỉnh sửa kết quả nhận dạng so với bản gốc.
   Ngoài các chức năng của một phần mềm số hóa thông thường, đề tài còn nghiên cứu áp dụng triệt để kiến trúc "Tích hợp Hệ thống" (System Integration) nhằm nâng cao tỷ lệ nhận dạng chính xác văn bản Tiếng Việt - vốn nổi tiếng với hệ thống dấu thanh phức tạp. Thay vì tự huấn luyện một mô hình mới, các mô hình Trí tuệ nhân tạo tiên tiến nhất hiện nay (DocTR [1], PaddleOCR [2]) được đóng gói dưới dạng các "Hộp đen" (Black-box) độc lập. Đặc biệt, hệ thống sử dụng mô hình Học máy kết hợp (Ensemble Model) để gộp chung sức mạnh của nhiều Engine nhận dạng, kết hợp cùng siêu mô hình ngôn ngữ ProtonX Nano Legal Text Correction (Seq2Seq) [5] làm tầng hậu xử lý, giúp tự động sửa lỗi chính tả và khôi phục ngữ cảnh chuẩn xác.
   Bên cạnh đó, hệ thống sử dụng thư viện giao diện hiện đại CustomTkinter trên nền tảng Python để xử lý logic ứng dụng, đồng thời ứng dụng các thư viện tính toán cục bộ (PyTorch, PaddlePaddle) để khai thác sức mạnh xử lý song song của nhân đồ họa (GPU), giúp tăng tốc độ phản hồi mà vẫn đảm bảo tính bảo mật dữ liệu nội bộ.
5. Nội dung báo cáo thực tập
   Chương 1: Khảo sát hiện trạng và xác lập dự án
   1.1. Giới thiệu về đơn vị thực tập
   1.2. Giới thiệu tổng quan đề tài
   1.3. Khảo sát hiện trạng
   1.4. Xác lập dự án
   1.5. Phân tích yêu cầu hệ thống
   1.6. Cơ sở lý thuyết và công nghệ lõi
   1.7. Công nghệ nền tảng sử dụng
   Chương 2: Phân tích và thiết kế hệ thống 
   2.1. Tổng quan kiến trúc hệ thống
   2.2. Tích hợp hệ thống bên thứ ba
   2.3. Thiết kế hệ thống
   2.4. Cài đặt và hướng dẫn tích hợp hệ thống
   Chương 3: Thực nghiệm và đánh giá
   3.1. Công nghệ sử dụng
   3.2. Giao diện hệ thống
   3.3. Kết quả thực nghiệm
   Kết luận và hướng nghiên cứu trong tương lai
   Những kết quả đạt được
   Những hạn chế và hướng phát triển
   Giảng viên hướng dẫn
   (Ký, Ghi rõ họ tên) Sinh viên thực hiện
   (Ký, Ghi rõ họ tên)

ĐÁNH GIÁ ĐỒ ÁN THỰC TẬP THỰC TẬP MÔN
HỆ THỐNG THÔNG TIN TÍCH HỢP
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
1.1. Giới thiệu về đơn vị thực tập 2
1.2. Giới thiệu tổng quan đề tài 3
1.3. Khảo sát hiện trạng 3
1.4. Xác lập dự án 4
1.4.1. Mục tiêu của hệ thống 4
1.4.2. Phạm vi của dự án 5
1.4.3. Đánh giá tính khả thi của hệ thống 5
1.5. Phân tích yêu cầu hệ thống 5
1.5.1. Yêu cầu chức năng 5
1.5.2. Yêu cầu phi chức năng 6
1.6. Cơ sở lý thuyết và công nghệ lõi 6
1.6.1. Thuật toán khoảng cách Levenshtein (Levenshtein Distance) 7
1.6.2. Thuật toán SymSpell 8
1.6.3. Kiến trúc Transformer và Sequence-to-Sequence (Seq2Seq) 8
1.6.4. Các Engine OCR nền tảng 8
1.7. Công nghệ nền tảng sử dụng 9
CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG 10
2.1. Tổng quan kiến trúc hệ thống 10
2.2. Tích hợp hệ thống bên thứ ba 10
2.2.1 Tích hợp các Engine OCR (DocTR và PaddleOCR). 11
2.2.2 Tích hợp mô hình ngôn ngữ lớn ProtonX Nano [5]. 11
2.2.3 Tích hợp bộ sửa lỗi chính tả SymSpell [6]. 12
2.2.4 Tích hợp cơ chế Ensemble đa Engine. 13
2.2.5 Thách thức trong quá trình tích hợp và giải pháp. 13
2.3. Thiết kế hệ thống 14
2.3.1. Biểu đồ Usecase tổng quát 14
2.3.2. Các biểu đồ hoạt động (Activity Diagrams) 20
2.3.2.1. Luồng chức năng cốt lõi: Nhận dạng và xử lý OCR 21
2.3.2.2. Luồng chức năng: Tiện ích Đổi tên tệp tin hàng loạt (Batch Rename) 23
2.3.2.3. Luồng chức năng: Chia cắt và Gộp tài liệu (Split/Merge PDF) 23
2.3.2.4. Luồng chức năng: Xử lý quét văn bản hàng loạt (Batch Processing OCR) 24
2.3.3. Biểu đồ trình tự (Sequence Diagram) 24
2.3.4. Biểu đồ Lớp (Class Diagram) 25
2.3.5. Biểu đồ triển khai (Deployment Diagram) 27
2.3.6. Cấu trúc dữ liệu hệ thống (Data Schema) 28
2.4. Cài đặt và hướng dẫn tích hợp hệ thống 30
2.4.1. Thiết lập môi trường phát triển 31
2.4.2. Tích hợp từng Engine vào hệ thống 31
2.4.3. Cấu hình tham số tích hợp qua file config.json 33
2.4.4. Quy trình khởi động và kiểm tra tích hợp 33
CHƯƠNG 3: THỰC NGHIỆM VÀ ĐÁNH GIÁ 34
3.1. Công nghệ sử dụng 34
3.2. Giao diện hệ thống 36
3.2.1. Giao diện màn hình OCR tài liệu. 36
3.2.2. Giao diện màn hình đổi tên tài liệu hàng loạt. 36
3.2.3. Giao diện màn hình tách file hàng loạt 37
3.3. Kết quả thực nghiệm 37
KẾT LUẬN 41
TÀI LIỆU THAM KHẢO 42

 
DANH MỤC TỪ VIẾT TẮT

Từ viết tắt Phiên bản đầy đủ Dịch thuật
AI Artificial Intelligence Trí tuệ nhân tạo
API Application Programming Interface Giao diện lập trình ứng dụng
CPU / GPU / RAM Các phần cứng cốt lõi
GUI Graphical User Interface Giao diện người dùng đồ họa
LLM Large Language Model Mô hình ngôn ngữ lớn
NLP Natural Language Processing Xử lý ngôn ngữ tự nhiên
OCR Optical Character Recognition Nhận dạng ký tự quang học
PDF Portable Document Format Định dạng tài liệu di động
RPA Robotic Process Automation Tự động hóa quy trình bằng robot
Seq2Seq Sequence-to-Sequence Kiến trúc dịch tự động chuỗi sang chuỗi
UML Unified Modeling Language Ngôn ngữ mô hình hóa thống nhất

 
DANH MỤC HÌNH ẢNH
Hình 1.1. Logo Công ty Cổ phần Công nghệ Nhật Thiên 2
Hình 1.2. Phương pháp Quy hoạch động (Dynamic Programming) 7
Hình 1.3. Biểu diễn toán học cơ chế Attention mechanism 8
Hình 2.1. Biểu đồ Usecase tổng quát hệ thống 15
Hình 2.2. Biểu đồ minh họa luồng chức năng cốt lõi: Nhận dạng và xử lý OCR 22
Hình 2.3. Biểu đồ minh họa luồng chức năng: Chia cắt và Gộp tài liệu 23
Hình 2.4. Biểu đồ minh họa luồng chức năng: Xử lý quét văn bản hàng loạt 24
Hình 2.5. Biểu đồ trình tự hệ thống OCR Scanner 25
Hình 2.6. Biểu đồ lớp hệ thống OCR Scanner 26
Hình 2.7. Biểu đồ triển khai hệ thống OCR Scanner 28
Hình 2.8. Schema chi tiết file `config.json’ 31
Hình 2.9. Cấu trúc một mục từ điển trong raw_dict.jsonl 31
Hình 3.1. Giao diện đối chiếu kết quả OCR Dual-panel 37
Hình 3.2. Chức năng đổi tên tệp tin hàng loạt (Batch Rename) 37
Hình 3.3. Chức năng chia tách tài liệu PDF hàng loạt 38

 
DANH MỤC BẢNG BIỂU
Bảng 2.1. Bảng cấu trúc dữ liệu vật lý 29
Bảng 3.1. Bảng so sánh hệ thống trước và sau khi tích hợp. 40
Bảng 3.2. Bảng tổng hợp so sánh hiệu năng giữa các cấu hình tích hợp. 41

 
LỜI CẢM ƠN
Trong suốt quá trình học tập và thực hiện báo cáo thực tập chuyên ngành "Hệ thống thông tin tích hợp", em đã nhận được sự quan tâm, chỉ bảo và giúp đỡ tận tình từ phía nhà trường, thầy cô và bạn bè.
Trước hết, em xin gửi lời cảm ơn chân thành tới Ban Giám hiệu, cùng toàn thể quý thầy cô Khoa Công nghệ thông tin, Trường Đại học Điện Lực. Các thầy cô đã tận tâm truyền đạt cho em những kiến thức chuyên ngành quý báu, từ nền tảng lập trình cơ bản đến các khái niệm chuyên sâu về phân tích, thiết kế và kiến trúc phần mềm. Đây là hành trang không thể thiếu giúp em tự tin bước vào môi trường thực tế.
Đặc biệt, em xin bày tỏ lòng biết ơn sâu sắc đến Giảng viên hướng dẫn. Thầy/Cô đã dành nhiều thời gian, tâm huyết để trực tiếp hướng dẫn, định hướng đề tài và đóng góp những ý kiến chuyên môn xác đáng, giúp em giải quyết những vướng mắc trong quá trình tích hợp các mô hình Trí tuệ nhân tạo phức tạp vào một hệ thống phần mềm hoàn chỉnh.
Do thời gian thực hiện đồ án và kiến thức thực tế còn hạn chế, báo cáo chắc chắn không tránh khỏi những thiếu sót. Em rất mong nhận được sự góp ý, chỉ bảo thêm từ quý thầy cô để đề tài được hoàn thiện hơn và bản thân em có thêm kinh nghiệm cho công việc sau này.
Em xin chân thành cảm ơn!
Hà Nội, ngày 16 tháng 5 năm 2026
Sinh viên thực hiện

Nguyễn Hoàng Thanh Tùng

LỜI NÓI ĐẦU
Trong kỷ nguyên Cách mạng công nghiệp 4.0, chuyển đổi số không còn là một lựa chọn mà đã trở thành xu hướng tất yếu đối với mọi cơ quan, tổ chức và doanh nghiệp. Một trong những bước đi đầu tiên và quan trọng nhất của quá trình chuyển đổi số là việc số hóa hệ thống tài liệu, hồ sơ, giấy tờ hành chính đang được lưu trữ dưới dạng vật lý. Việc chuyển đổi các tài liệu này sang định dạng văn bản kỹ thuật số (text) không chỉ giúp tiết kiệm không gian lưu trữ mà còn tối ưu hóa quá trình tìm kiếm, trích xuất thông tin và quản lý tri thức.
Để giải quyết bài toán này, công nghệ Nhận dạng ký tự quang học (OCR - Optical Character Recognition) đã ra đời và phát triển mạnh mẽ. Tuy nhiên, khi áp dụng OCR vào thực tiễn tại Việt Nam, các kỹ sư phần mềm phải đối mặt với một thách thức kỹ thuật đặc thù: Tiếng Việt là một ngôn ngữ có hệ thống dấu thanh vô cùng phức tạp (sắc, huyền, hỏi, ngã, nặng) và các biến thể vị trí đặt dấu (ví dụ: òa, oà, thủy, thuỷ). Chính sự phức tạp này khiến cho hầu hết các giải pháp phần mềm mã nguồn mở của nước ngoài (như Tesseract) thường xuyên nhận dạng sai lệch, làm mất dấu hoặc nhầm lẫn các ký tự có hình dáng tương đồng, dẫn đến kết quả đầu ra không đạt yêu cầu thực tiễn và đòi hỏi con người phải can thiệp chỉnh sửa thủ công rất nhiều.
Xuất phát từ nhu cầu cấp thiết đó, nhóm sinh viên chúng em đã lựa chọn và phát triển đề tài: "Hệ Thống Nhận dạng Và Xử Lý Văn Bản Tiếng Việt Tích hợp Đa Engine OCR". Điểm khác biệt và sáng tạo của đề tài này nằm ở chỗ, thay vì cố gắng tự huấn luyện một mô hình AI từ đầu với chi phí và tài nguyên khổng lồ, chúng em đã áp dụng triệt để tư duy "Tích hợp Hệ thống" (System Integration). Bằng cách coi các mô hình AI tiên tiến nhất hiện nay như các "Hộp đen" (Black-box), hệ thống sẽ đóng vai trò làm trung tâm điều phối, linh hoạt kết hợp sức mạnh nhận dạng tọa độ của DocTR [1], tốc độ đọc văn bản của PaddleOCR [2] và khả năng suy luận, khôi phục ngữ cảnh ngôn ngữ của siêu mô hình ProtonX Nano Legal Text Correction [5].
Mục tiêu cuối cùng của đồ án là mang đến một phần mềm Desktop hoàn chỉnh, thân thiện với người dùng, có khả năng tự động xử lý hàng loạt tài liệu với độ chính xác cao nhất, qua đó minh chứng cho sức mạnh của nghệ thuật Tích hợp hệ thống trong lĩnh vực phát triển phần mềm ứng dụng Trí tuệ nhân tạo.
CHƯƠNG 1: KHẢO SÁT HIỆN TRẠNG VÀ XÁC LẬP DỰ ÁN
1.1. Giới thiệu về đơn vị thực tập

Hình 1.1. Logo Công ty Cổ phần Công nghệ Nhật Thiên
Công ty Cổ phần Công nghệ Nhật Thiên (NHAT THIEN TECHNOLOGY CORPORATION) là doanh nghiệp hoạt động trong lĩnh vực công nghệ thông tin, khoa học và kỹ thuật, được thành lập từ năm 2011 với trụ sở đặt tại quận Cầu Giấy, Hà Nội. Công ty chuyên cung cấp các giải pháp công nghệ, thiết bị máy tính, phần mềm và dịch vụ số hóa dữ liệu phục vụ quá trình chuyển đổi số cho doanh nghiệp và tổ chức.
Trong bối cảnh chuyển đổi số ngày càng phát triển mạnh mẽ, Nhật Thiên tập trung vào các giải pháp số hóa tài liệu và dữ liệu nhằm hỗ trợ doanh nghiệp tối ưu hóa quy trình quản lý thông tin. Dịch vụ số hóa giúp chuyển đổi tài liệu giấy sang định dạng kỹ thuật số nhưng vẫn đảm bảo giữ nguyên nội dung và giá trị dữ liệu gốc. Điều này giúp doanh nghiệp dễ dàng lưu trữ, tra cứu, chia sẻ và bảo vệ dữ liệu một cách an toàn và hiệu quả hơn.
Bên cạnh đó, công ty còn xây dựng quy trình số hóa chuyên nghiệp bao gồm tiếp nhận tài liệu, phân loại, scan, nhập liệu, kiểm tra dữ liệu, chuẩn hóa thông tin và tích hợp ký số trước khi bàn giao nghiệm thu. Quy trình này giúp giảm thiểu sai sót thủ công, nâng cao hiệu suất làm việc và tiết kiệm đáng kể chi phí vận hành cho doanh nghiệp.

Với định hướng phát triển dựa trên công nghệ và tự động hóa, Công ty Cổ phần Công nghệ Nhật Thiên đang từng bước khẳng định vai trò là đơn vị hỗ trợ chuyển đổi số và số hóa dữ liệu cho nhiều tổ chức, doanh nghiệp tại Việt Nam.
1.2. Giới thiệu tổng quan đề tài
Trong những năm gần đây, việc áp dụng công nghệ thông tin vào công tác quản trị hành chính đang được đẩy mạnh tại các trường Đại học cũng như các doanh nghiệp trên cả nước. Tuy nhiên, khối lượng giấy tờ vật lý bao gồm công văn, hợp đồng, quyết định và hồ sơ nhân sự vẫn còn tồn đọng một số lượng khổng lồ. Việc số hóa thủ công bằng cách gõ lại (re-type) văn bản tiêu tốn một lượng lớn thời gian và nhân lực, đồng thời dễ phát sinh sai sót trong quá trình nhập liệu.
Từ thực tế đó, đề tài "Hệ thống Nhận dạng và Xử lý Văn bản Tiếng Việt Tích hợp Đa Engine OCR" được ra đời nhằm mục đích tự động hóa hoàn toàn quy trình này. Hệ thống được xây dựng dưới dạng một ứng dụng Desktop GUI, cho phép người dùng cuối (nhân viên hành chính) có thể dễ dàng tải lên các tệp tin hình ảnh hoặc PDF, và phần mềm sẽ tự động đọc, trích xuất nội dung văn bản bên trong tệp tin đó. Điểm đặc biệt của đề tài là việc áp dụng kiến trúc phần mềm tích hợp, kết nối đa nền tảng. Thay vì sử dụng một công cụ OCR duy nhất, phần mềm cung cấp một hệ thống "plug-and-play" linh hoạt, cho phép tích hợp và chạy song song nhiều mô hình nhận dạng quang học (OCR) cùng các mô hình xử lý ngôn ngữ tự nhiên (NLP) tiên tiến để hỗ trợ nhau bù đắp các khuyết điểm trong việc đọc tiếng Việt. Thông qua đề tài này, mục tiêu đặt ra không chỉ là giải quyết một bài toán ứng dụng thực tiễn mà còn thể hiện năng lực vận dụng kiến trúc phần mềm và kỹ năng giao tiếp API giữa các hệ thống phức tạp.
1.3. Khảo sát hiện trạng
Thị trường hiện nay cung cấp nhiều giải pháp và thư viện phần mềm hỗ trợ nhận dạng chữ viết (OCR). Phổ biến nhất có thể kể đến Tesseract OCR [8] của Google. Mặc dù Tesseract hoàn toàn miễn phí và có cộng đồng hỗ trợ lớn, nhưng kiến trúc của nó đã khá cũ, khả năng nhận dạng các phông chữ tiếng Việt đa dạng hoặc các tài liệu bị mờ, nhiễu là rất kém. Người dùng thường xuyên phải đối mặt với tình trạng văn bản đầu ra bị vỡ chữ, thiếu dấu hoặc sinh ra các ký tự lạ vô nghĩa.
Một nền tảng khác nổi lên gần đây là PaddleOCR [2] do Baidu phát triển. PaddleOCR sở hữu ưu điểm vượt trội về tốc độ xử lý và khả năng nhận dạng các khối văn bản (text block) rất tốt nhờ áp dụng các kiến trúc Deep Learning hiện đại. Tuy nhiên, do mô hình được huấn luyện chủ yếu cho ngôn ngữ tiếng Trung và tiếng Anh, khi áp dụng trực tiếp cho tiếng Việt, PaddleOCR thường xuyên gặp lỗi "rụng dấu" (ví dụ: chữ "Nguyễn" bị nhận nhầm thành "Nguyen" hoặc "Nguyén").
Trong khi đó, thư viện DocTR [1] (do Mindee phát triển) cho thấy khả năng trích xuất tọa độ không gian (Bounding Box) của các từ ngữ trên trang giấy cực kỳ chính xác, hỗ trợ rất tốt cho việc tái tạo lại định dạng layout của đoạn văn. Thế nhưng điểm yếu của DocTR là tốc độ xử lý khá chậm và tiêu tốn nhiều tài nguyên bộ nhớ GPU.
Nhìn chung, hiện trạng các hệ thống OCR đơn lẻ mang lại những ưu điểm và hạn chế đan xen. Bất kỳ một giải pháp độc lập nào cũng không thể xử lý hoàn hảo văn bản tiếng Việt. Do đó, bài toán đặt ra là cần phải có một "nhạc trưởng" (Orchestrator) đứng ra điều phối: Lấy khả năng bắt tọa độ chính xác của DocTR [1] kết hợp với khả năng đọc chữ siêu tốc của PaddleOCR [2], và cuối cùng, đưa toàn bộ văn bản có lỗi đi qua một hệ thống sửa lỗi chính tả theo ngữ cảnh (Sử dụng mô hình ngôn ngữ lớn ProtonX Nano [5]) để khôi phục lại các dấu thanh bị mất. Đây chính là tiền đề dẫn tới giải pháp của dự án.
1.4. Xác lập dự án
1.4.1. Mục tiêu của hệ thống
Mục tiêu tổng quát: Xây dựng một ứng dụng máy tính để bàn (Desktop Application) giúp số hóa văn bản hành chính với tỷ lệ chính xác cao, tự động hóa quy trình hậu xử lý tiếng Việt bằng AI.
Mục tiêu cụ thể:
• Cung cấp giao diện người dùng thân thiện, cho phép tải lên hình ảnh hoặc file PDF trực quan bằng thao tác kéo thả.
• Tích hợp thành công thư viện nhận dạng DocTR và PaddleOCR vào chung một hệ thống phần mềm.
• Tích hợp mô hình ProtonX Nano Legal Text Correction để kiểm tra và sửa lỗi chính tả ngữ nghĩa tự động.
• Thiết kế giao diện đối chiếu song song (Dual-panel) giúp người dùng dễ dàng so sánh văn bản gốc và kết quả nhận dạng.
• Cung cấp tính năng Batch Processing để xử lý hàng loạt tài liệu tự động trong một thư mục.
1.4.2. Phạm vi của dự án
• Về mặt người dùng: Hệ thống hướng tới đối tượng người dùng cuối là nhân viên văn phòng, cán bộ hành chính, những người không yêu cầu kiến thức về lập trình hay thao tác dòng lệnh (Command Line).
• Về mặt môi trường: Phần mềm được triển khai và chạy trực tiếp trên máy tính cá nhân (Local Machine) hệ điều hành Windows. Hệ thống xử lý dữ liệu nội bộ không cần tải tài liệu lên môi trường Internet (Cloud) nhằm đảm bảo tính bảo mật tuyệt đối cho các văn bản quan trọng của tổ chức.
1.4.3. Đánh giá tính khả thi của hệ thống
Dự án "Hệ thống Nhận dạng và Xử lý Văn bản Tiếng Việt Tích hợp Đa Engine OCR" được đánh giá có tính khả thi kỹ thuật rất cao.
Về công nghệ lập trình, hệ sinh thái Python cung cấp đầy đủ các thư viện hỗ trợ xây dựng giao diện Desktop hiện đại (như CustomTkinter), đồng thời Python cũng là ngôn ngữ tiêu chuẩn để làm việc với các hệ thống Trí tuệ nhân tạo.
Về việc tích hợp các mô hình bên thứ ba, toàn bộ các mô hình như DocTR, PaddleOCR, và ProtonX Nano đều được phát hành dưới dạng mã nguồn mở (Open-source) với hệ thống tài liệu API được cung cấp đầy đủ rõ ràng. Việc tải xuống các trọng số mô hình (Pre-trained weights) và nhúng chúng vào hệ thống thông qua các framework như PyTorch hay HuggingFace là hoàn toàn có thể thực hiện được trong phạm vi của một đồ án môn học.
1.5. Phân tích yêu cầu hệ thống
1.5.1. Yêu cầu chức năng
• Nạp và quản lý tài liệu: Hệ thống phải cho phép người dùng chọn tệp tin từ máy tính (hỗ trợ các định dạng .png, .jpg, .jpeg, .pdf).
• Cấu hình linh hoạt: Cho phép người dùng hoặc Quản trị viên truy cập màn hình Cài đặt để lựa chọn Engine OCR muốn sử dụng (chuyển đổi giữa DocTR [1] và PaddleOCR [2]), bật hoặc tắt tính năng sửa lỗi bằng AI (ProtonX Nano [5]).
• Xử lý nhận dạng chữ (Core OCR): Hệ thống phải trích xuất được văn bản từ hình ảnh và phân đoạn đoạn văn bản đúng với thiết kế gốc.
• Hậu xử lý văn bản: Tự động phát hiện các từ nghi ngờ sai chính tả và gợi ý sửa lỗi dựa trên bộ từ điển (SymSpell [6]) hoặc ngữ cảnh (ProtonX Nano [5]).
• Đối chiếu và Xuất tệp: Hiển thị văn bản kết quả bên cạnh hình ảnh gốc; cho phép người dùng chỉnh sửa thủ công và xuất kết quả ra file định dạng txt hoặc json.
• Quản lý và thao tác tệp tin (File Tools): Hệ thống cung cấp bộ công cụ phụ trợ độc lập, cho phép người dùng đổi tên tệp tin hàng loạt theo các quy tắc (Rules) cấu hình trước, đồng thời hỗ trợ chia nhỏ (Split) các tệp PDF lớn thành nhiều trang hoặc gộp (Merge) chúng lại để phục vụ cho luồng công việc số hóa.
1.5.2. Yêu cầu phi chức năng
• Hiệu năng hệ thống: Thời gian xử lý một trang văn bản kích thước tiêu chuẩn (A4) không được vượt quá 5 giây trên máy tính có hỗ trợ GPU, và không quá 15 giây trên máy tính chỉ chạy bằng CPU.
• Tính mở rộng (Scalability): Kiến trúc phần mềm phải được thiết kế dạng module (Plugin). Khi có một công cụ OCR thế hệ mới xuất hiện trên thị trường, lập trình viên có thể dễ dàng lập trình thêm một module mới kết nối vào hệ thống mà không làm ảnh hưởng đến mã nguồn cũ.
• Bảo mật và an toàn: Mọi quá trình xử lý hình ảnh, ma trận và dữ liệu văn bản phải được lưu trữ trên bộ nhớ RAM cục bộ và giải phóng ngay khi kết thúc phiên làm việc, không được phép rò rỉ dữ liệu ra bên ngoài.
• Độ ổn định (Robustness): Khi một Engine AI bên thứ ba gặp lỗi (ví dụ hết bộ nhớ GPU cục bộ), phần mềm không được phép văng (crash) hoàn toàn, mà phải hiển thị hộp thoại cảnh báo và cung cấp giải pháp dự phòng (Fallback qua CPU).
1.6. Cơ sở lý thuyết và công nghệ lõi
Để đáp ứng các yêu cầu phức tạp của hệ thống, dự án đã nghiên cứu và áp dụng các cơ sở lý thuyết khoa học máy tính tiên tiến:
• Khoảng cách Levenshtein (Levenshtein Distance): Thuật toán đo lường sự khác biệt giữa 2 chuỗi ký tự bằng cách đếm số bước thao tác (thêm, xóa, thay thế) tối thiểu để biến đổi chuỗi này thành chuỗi kia. Đây là hạt nhân của bộ kiểm tra lỗi chính tả trong dự án.
• Thuật toán SymSpell: Một sự cải tiến vượt bậc so với thuật toán Levenshtein truyền thống. Bằng cách sinh trước (pre-calculate) các biến thể xóa ký tự và lưu vào cấu trúc từ điển (Dictionary), SymSpell giảm độ phức tạp tìm kiếm xuống O(1), mang lại tốc độ sửa lỗi siêu tốc.
• Mô hình học sâu Sequence-to-Sequence (Seq2Seq): Kiến trúc mạng nơ-ron chuyên dụng cho bài toán sinh ngôn ngữ. Trong đồ án này, kiến trúc Seq2Seq (của mô hình AI ProtonX Nano) được dùng để phân tích và "dịch" một câu tiếng Việt bị sai do máy quét thành một câu tiếng Việt đúng chuẩn hoàn toàn dựa trên ngữ cảnh.
• Mẫu thiết kế Singleton & Plugin Pattern: Các nguyên lý cốt lõi của kỹ nghệ phần mềm. Singleton đảm bảo các mô hình AI đồ sộ chỉ khởi tạo đúng 1 lần trên RAM. Plugin Pattern cho phép trừu tượng hóa các module AI, giúp hệ thống lõi dễ dàng cắm/rút các Engine khác nhau mà không phá vỡ kiến trúc.
• Biểu thức chính quy (Regex): Tập hợp các quy tắc định dạng chuỗi mạnh mẽ, được ứng dụng vào công cụ File Tools để nhận dạng mẫu (ví dụ: mã số hợp đồng, ngày tháng) và tự động hóa việc định danh tệp tin.
1.6.1. Thuật toán khoảng cách Levenshtein (Levenshtein Distance)
Thuật toán Levenshtein đo lường khoảng cách chỉnh sửa giữa hai chuỗi ký tự, được định nghĩa là số lượng tối thiểu các phép biến đổi đơn lẻ (chèn, xóa, hoặc thay thế một ký tự) cần thiết để biến đổi chuỗi này thành chuỗi kia.
Về mặt toán học, khoảng cách Levenshtein giữa hai chuỗi $a$ và $b$ có độ dài tương ứng |a| và |b| được tính bằng hàm chỉ thị thông qua quy hoạch động (Dynamic Programming):

Hình 1.2. Phương pháp Quy hoạch động (Dynamic Programming)
Trong đó, `cost` bằng 0 nếu ký tự i == j và bằng 1 nếu ngược lại. Thuật toán này là nền tảng cốt lõi giúp hệ thống phát hiện các từ tiếng Việt bị nhận dạng sai (ví dụ: "Nguyễn" bị OCR thành "Nguyẻn" - khoảng cách Levenshtein là 1) để từ đó đề xuất từ đúng trong từ điển.
1.6.2. Thuật toán SymSpell
Dù Levenshtein rất hiệu quả, nhưng việc duyệt qua toàn bộ từ điển 100.000 từ để tìm từ có khoảng cách nhỏ nhất yêu cầu độ phức tạp thời gian cực lớn O(n \times m) cho mỗi từ, khiến quá trình số hóa chậm chạp. Đồ án giải quyết bài toán này bằng việc tích hợp thuật toán SymSpell (Symmetric Delete Spelling Correction).
Khác với cây Trie truyền thống, SymSpell áp dụng phương pháp sinh trước (pre-calculation). Thay vì tính khoảng cách giữa từ bị sai và từ điển, SymSpell sinh ra tất cả các biến thể có thể bị xóa đi 1-2 ký tự của các từ trong từ điển và lưu vào bộ nhớ RAM dưới dạng Bảng băm (Hash Table). Khi một từ sai xuất hiện, hệ thống chỉ cần sinh các biến thể xóa của nó và tra cứu Hash Table trong thời gian O(1). Nhờ đó, tốc độ sửa lỗi tăng gấp 1 triệu lần, đảm bảo yêu cầu hậu xử lý theo thời gian thực (Real-time processing).
1.6.3. Kiến trúc Transformer và Sequence-to-Sequence (Seq2Seq)
Hạn chế của SymSpell là chỉ sửa được lỗi từ đơn lẻ mà không hiểu được ngữ cảnh. Để giải quyết, dự án tích hợp siêu mô hình ngôn ngữ ProtonX Nano, được xây dựng dựa trên kiến trúc Transformer (Vaswani et al., 2017).
Trái tim của Transformer là cơ chế Self-Attention (Tự chú ý), cho phép mô hình đánh giá mức độ liên quan của mọi từ trong câu đối với từng từ đang được xem xét. Công thức Attention được biểu diễn:

Hình 1.3. Biểu diễn toán học cơ chế Attention mechanism
Với kiến trúc Seq2Seq, ProtonX Nano đóng vai trò như một bộ dịch thuật: "Dịch" một câu tiếng Việt bị sai dấu do OCR thành một câu tiếng Việt đúng ngữ pháp hoàn chỉnh. Khả năng này dựa trên việc mô hình đã được huấn luyện (Fine-tuning) trên hàng triệu văn bản pháp luật hành chính của Việt Nam.
1.6.4. Các Engine OCR nền tảng
• PaddleOCR (DBNet & CRNN): PaddleOCR sử dụng mô hình DBNet (Differentiable Binarization) cho giai đoạn phát hiện vùng văn bản (Text Detection). Nhờ khả năng nhị phân hóa khác biệt, DBNet có thể bám sát các đường viền văn bản cong hoặc nghiêng. Đối với giai đoạn nhận dạng (Text Recognition), hệ thống sử dụng mạng CRNN (Convolutional Recurrent Neural Network) kết hợp CTC Loss để giải mã chuỗi ký tự.
• DocTR: Được xây dựng trên framework PyTorch, DocTR sử dụng kiến trúc ResNet kết hợp với FPN (Feature Pyramid Network) để trích xuất tọa độ chính xác cao. DocTR xuất ra kết quả dưới dạng cây DOM (Document Object Model), giúp tái tạo lại hoàn hảo bố cục (layout) của văn bản gốc (chia cột, đoạn văn).
1.7. Công nghệ nền tảng sử dụng
Hệ thống được phát triển và vận hành dựa trên một hệ sinh thái công nghệ đa dạng, được lựa chọn kỹ lưỡng nhằm đáp ứng yêu cầu xử lý đồ họa, học sâu và thiết kế giao diện trên máy tính để bàn:
• Ngôn ngữ và Môi trường: Python 3.10 được chọn làm ngôn ngữ lập trình chính nhờ sức mạnh vượt trội trong lĩnh vực khoa học dữ liệu và hỗ trợ tốt các thư viện hệ thống. Việc thực nghiệm được chạy trên hệ điều hành Windows 11.
• Nền tảng Phần cứng & Tăng tốc tính toán: Để các mô hình AI có thể hoạt động mượt mà, hệ thống đòi hỏi thiết bị cài đặt hạ tầng NVIDIA CUDA Toolkit (kèm cuDNN) để có thể truy xuất và khai thác sức mạnh tính toán song song của nhân GPU cục bộ.
• Thư viện Giao diện Người dùng: Thư viện `CustomTkinter` được sử dụng để lập trình Giao diện đồ họa (GUI). Thư viện này kế thừa sức mạnh của hệ thống Tkinter truyền thống nhưng mang lại phong cách thiết kế giao diện hiện đại, bóng bẩy và chuyên nghiệp hơn, hỗ trợ tốt các chế độ chủ đề (Dark/Light mode).
• Thư viện AI và Xử lý ảnh: Thư viện mã nguồn mở OpenCV [9] (`cv2`) đảm nhiệm mọi thao tác biến đổi không gian ảnh. Các nền tảng học sâu cốt lõi như PyTorch và PaddlePaddle được cấu hình thành môi trường nền tảng để chạy các Engine tích hợp. Module `transformers` do HuggingFace cung cấp được sử dụng để kết nối và gọi siêu mô hình ngôn ngữ ProtonX Nano Legal Text Correction [5].

CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG
2.1. Tổng quan kiến trúc hệ thống
Hệ thống được thiết kế dựa trên sự kết hợp giữa mô hình Kiến trúc phân lớp (Layered Architecture) và Mẫu thiết kế Plugin (Plugin Pattern). Việc lựa chọn kiến trúc này bắt nguồn từ bản chất của hệ thống: Đây là một hệ thống mang tính chất Điều phối (Orchestration).
Hệ thống chia làm ba tầng chính:
• Tầng Giao diện (Presentation Layer): Được xây dựng bằng thư viện CustomTkinter. Tầng này chịu trách nhiệm tương tác trực tiếp với người dùng, nhận các tệp tin hình ảnh, tiếp nhận các sự kiện click chuột và hiển thị hình ảnh cùng văn bản đối chiếu. Tầng này hoàn toàn không chứa bất kỳ logic xử lý AI nào.
• Tầng Điều phối cốt lõi (Core Orchestrator Layer): Đây là "bộ não" của hệ thống phần mềm. Tầng này tiếp nhận lệnh từ giao diện, thực hiện các bước tiền xử lý hình ảnh (sử dụng thư viện OpenCV để cắt, xoay, cân bằng sáng). Sau đó, dựa vào file cấu hình (config.json), tầng này sẽ quyết định sẽ đóng gói dữ liệu và gửi yêu cầu (Request) đến Engine AI nào. Khi nhận được kết quả trả về, nó tiến hành ghép nối các đoạn văn bản (text alignment) và áp dụng các thuật toán nội bộ.
• Tầng Dịch vụ Tích hợp Bên thứ ba (Black-box Layer): Đây là nơi chứa các mô hình Học sâu (Deep Learning) nặng nề và phức tạp. Các mô hình này được bọc lại bằng một lớp Giao diện lập trình (Wrapper Interface). Tầng Core Orchestrator chỉ cần gọi một hàm chuẩn duy nhất như `extract_text()`, và Interface này sẽ lo liệu việc giao tiếp phức tạp với các thư viện PyTorch hay Paddle bên dưới.
Đặc điểm của kiến trúc này là sự tách biệt hoàn toàn giữa ứng dụng và mô hình. Cơ sở dữ liệu và các luồng xử lý AI chạy trong không gian bộ nhớ riêng. Việc thiết kế này giúp hệ thống quản lý tài nguyên bộ nhớ hiệu quả, đặc biệt là RAM đồ họa (VRAM), đồng thời giảm thiểu tối đa rủi ro phần mềm ngừng hoạt động do lỗi từ bên thứ ba.
2.2. Tích hợp hệ thống bên thứ ba
Trong phạm vi của dự án, khái niệm "Tích hợp Hộp đen" (Black-box Integration) được áp dụng một cách triệt để. Hệ thống nội bộ không cần hiểu cấu trúc mạng Neural bên trong DocTR hay PaddleOCR có bao nhiêu lớp, không cần tham gia vào quá trình lan truyền ngược (Backpropagation) hay huấn luyện mô hình. Hệ thống chỉ quan tâm đến Dữ liệu Đầu vào (Input) và Dữ liệu Đầu ra (Output).
2.2.1 Tích hợp các Engine OCR (DocTR và PaddleOCR).
Việc tích hợp được thực hiện thông qua việc gọi các thư viện API được cung cấp bởi nhà phát triển.
• Đối với DocTR [1]: Hệ thống Core Orchestrator sau khi chuyển đổi hình ảnh thành một ma trận đa chiều (Numpy Array) sẽ truyền ma trận này vào hàm `Predictor` của DocTR. Khối lượng xử lý khổng lồ sẽ diễn ra bên trong không gian của bộ thư viện này. Kết quả mà hệ thống nhận lại là một cấu trúc dữ liệu dạng cây (JSON/Dictionary) bao gồm các trang (Pages), các khối (Blocks), các dòng (Lines) và cuối cùng là các từ (Words) kèm theo tọa độ (X, Y) của chúng trên ảnh.
• Đối với PaddleOCR [2]: Quá trình tích hợp cũng tương tự. Lớp Wrapper của PaddleOCR sẽ nhận vào đường dẫn hoặc ma trận ảnh và kích hoạt hàm `paddleocr.ocr()`. Phản hồi trả về là một danh sách chứa nội dung văn bản thô (Raw text) cùng với độ tin cậy (Confidence score) của mỗi từ. Core Orchestrator sẽ lấy danh sách này, lọc bỏ các từ có độ tin cậy quá thấp để chuẩn bị cho bước tiếp theo.
2.2.2 Tích hợp mô hình ngôn ngữ lớn ProtonX Nano [5].
Sau khi có được văn bản thô từ tầng nhận dạng hình ảnh, văn bản này thường xuyên gặp các lỗi mất dấu hoặc nhầm lẫn ký tự. Hệ thống tiếp tục quy trình tích hợp hộp đen bằng cách gửi đoạn văn bản này đến mô hình ProtonX Nano Legal Text Correction.
ProtonX Nano được tích hợp thông qua thư viện `Transformers` của HuggingFace. Cơ chế được sử dụng ở đây là Sequence-to-Sequence (Dịch chuỗi sang chuỗi). Toàn bộ đoạn văn bản chứa lỗi sẽ được truyền qua giao thức API nội bộ tới mô hình.
Nhờ vào cấu trúc Transformer đã được huấn luyện trên khối lượng dữ liệu hành chính và pháp luật khổng lồ của tiếng Việt, ProtonX Nano sẽ đóng vai trò như một bộ "dịch thuật", phân tích ngữ cảnh của toàn bộ câu và phản hồi lại cho hệ thống phiên bản văn bản đã được khôi phục dấu và sửa lỗi chính tả chính xác. Quy trình tích hợp tinh vi này giúp hệ thống đạt được sự hoàn thiện về mặt ngữ nghĩa mà một mô hình quang học đơn thuần không bao giờ có thể làm được.
Để tối ưu hiệu suất tích hợp, ProtonX Nano được triển khai theo cơ chế phân đoạn văn bản (Text Chunking). Do giới hạn về số lượng token tối đa mà mô hình Seq2Seq có thể xử lý trong một lần suy luận (thường là 256-512 tokens), hệ thống tự động chia văn bản dài thành các đoạn nhỏ có kích thước phù hợp, gửi lần lượt từng đoạn qua mô hình, sau đó ghép nối kết quả lại thành văn bản hoàn chỉnh. Kỹ thuật này đảm bảo rằng ngay cả các tài liệu dài nhiều trang cũng được xử lý chính xác mà không bị cắt xén hoặc mất thông tin.
2.2.3 Tích hợp bộ sửa lỗi chính tả SymSpell [6].
Bên cạnh mô hình ngôn ngữ nặng ProtonX Nano, hệ thống còn tích hợp một tầng sửa lỗi nhẹ và siêu tốc dựa trên thuật toán SymSpell (Symmetric Delete Spelling Correction). Đây là giải pháp bổ trợ dành cho các máy tính không đủ tài nguyên phần cứng để chạy mô hình Seq2Seq.
Việc tích hợp SymSpell vào hệ thống diễn ra theo hai giai đoạn. Giai đoạn khởi tạo (Initialization): Ngay khi ứng dụng khởi động, module SymSpellChecker đọc toàn bộ tệp từ điển `raw_dict.jsonl` (khoảng 4.9MB, chứa hơn 100.000 mục từ vựng tiếng Việt) và tải lên bộ nhớ RAM. Đồng thời, thuật toán sinh trước (pre-calculate) tất cả các biến thể xóa ký tự (delete variants) với khoảng cách chỉnh sửa tối đa là 2, lưu vào một cấu trúc Bảng băm (Hash Table). Quá trình này chỉ diễn ra duy nhất một lần và mất khoảng 2-3 giây.
Giai đoạn tra cứu (Runtime Lookup): Khi nhận được văn bản thô từ Engine OCR, hệ thống tách văn bản thành từng từ đơn lẻ. Với mỗi từ, SymSpell sinh các biến thể xóa ký tự của từ đó và tra cứu trong Bảng băm đã xây dựng sẵn. Nếu tìm thấy từ ứng viên (candidate) trong từ điển có khoảng cách Levenshtein nhỏ hơn hoặc bằng ngưỡng cho phép, hệ thống sẽ thay thế từ sai bằng từ đúng. Nhờ cơ chế Bảng băm, toàn bộ quá trình tra cứu diễn ra với độ phức tạp thời gian O(1), nhanh hơn hàng triệu lần so với phương pháp duyệt tuần tự truyền thống.
Ngoài ra, để tránh sửa nhầm các từ chuyên ngành, tên riêng hoặc từ viết tắt, hệ thống áp dụng thêm một bộ lọc bảo vệ (Guard Filter): Các từ viết hoa toàn bộ, từ chứa ký tự số, hoặc từ đã tồn tại trong từ điển sẽ được bỏ qua và giữ nguyên.
2.2.4 Tích hợp cơ chế Ensemble đa Engine.
Một trong những đóng góp quan trọng nhất của dự án về mặt tích hợp hệ thống là cơ chế Ensemble (Học máy kết hợp). Thay vì phụ thuộc vào một Engine OCR duy nhất, hệ thống cho phép chạy đồng thời nhiều Engine trên cùng một ảnh đầu vào, sau đó áp dụng chiến lược chọn lọc thông minh để lấy ra kết quả tốt nhất.
Quy trình tích hợp Ensemble được thiết kế theo các bước sau:
• Bước 1 - Hệ thống gửi cùng một ảnh đầu vào tới cả hai Engine: DocTR [1] và PaddleOCR [2]. Mỗi Engine xử lý độc lập trong không gian bộ nhớ riêng và trả về hai bộ kết quả chứa văn bản thô cùng với chỉ số Confidence Score (độ tin cậy trung bình).
• Bước 2 - Lớp Core Orchestrator so sánh Confidence Score giữa hai kết quả. Engine nào có chỉ số tin cậy cao hơn sẽ được chọn làm kết quả chính thức.
• Bước 3 - Kết quả được chọn tiếp tục đi qua pipeline hậu xử lý (SymSpell hoặc ProtonX Nano) để tinh chỉnh lần cuối.
Triết lý đằng sau cơ chế Ensemble là nguyên lý "Trí tuệ tập thể" (Wisdom of Crowds): Mỗi Engine có thế mạnh riêng - DocTR mạnh về trích xuất tọa độ và giữ đúng bố cục, PaddleOCR mạnh về tốc độ và nhận dạng ký tự - việc kết hợp chúng lại cho ra kết quả vượt trội so với bất kỳ Engine đơn lẻ nào. Kết quả thực nghiệm cho thấy cấu hình Ensemble đạt độ chính xác 96-97%, cao hơn 4-5 điểm phần trăm so với khi chạy từng Engine riêng rẽ.
2.2.5 Thách thức trong quá trình tích hợp và giải pháp.
Việc tích hợp đồng thời nhiều hệ thống AI từ các nhà phát triển khác nhau vào chung một ứng dụng Desktop đặt ra nhiều thách thức kỹ thuật phức tạp. Dưới đây là các vấn đề chính mà dự án đã đối mặt và cách giải quyết:
• Thách thức 1: An toàn đa luồng (Thread Safety): Thư viện PaddleOCR không hỗ trợ truy cập đa luồng (thread-safe). Nếu nhiều tiến trình đồng thời gọi vào cùng một instance PaddleOCR, ứng dụng sẽ bị treo hoặc sinh ra kết quả lỗi. Giải pháp: Hệ thống sử dụng cơ chế khóa luồng (`threading.Lock`) để đảm bảo rằng tại bất kỳ thời điểm nào, chỉ có duy nhất một yêu cầu được gửi tới PaddleOCR. Các yêu cầu khác sẽ được xếp hàng (queued) và chờ đến lượt.
• Thách thức 2: Quản lý bộ nhớ GPU (VRAM Management): Các mô hình DocTR, PaddleOCR và ProtonX Nano khi nạp lên GPU chiếm tổng cộng 4-6 GB VRAM. Trên các máy tính có card đồ họa giới hạn (ví dụ: RTX 3050 Ti 4GB), việc nạp đồng thời tất cả các mô hình sẽ gây tràn bộ nhớ (Out of Memory). Giải pháp: Hệ thống áp dụng mẫu thiết kế Singleton (Độc bản) để đảm bảo mỗi mô hình chỉ được khởi tạo duy nhất một lần và dùng chung cho mọi yêu cầu. Đồng thời, cơ chế tải lười (Lazy Loading) chỉ nạp mô hình lên GPU khi người dùng thực sự cần sử dụng, thay vì nạp toàn bộ ngay từ đầu.
• Thách thức 3: Cơ chế dự phòng (Fallback Mechanism): Khi GPU cục bộ không khả dụng (không có card NVIDIA, thiếu driver CUDA), các mô hình AI không thể chạy ở chế độ tăng tốc. Giải pháp: Hệ thống thiết kế cơ chế dự phòng tự động - khi phát hiện GPU không khả dụng, toàn bộ pipeline sẽ tự động chuyển sang chế độ CPU. Mặc dù tốc độ chậm hơn (khoảng 10-15 giây mỗi trang thay vì 1-2 giây), nhưng đảm bảo phần mềm vẫn hoạt động bình thường trên mọi máy tính.
• Thách thức 4: Xung đột phiên bản thư viện (Dependency Conflict): DocTR yêu cầu PyTorch phiên bản mới, trong khi PaddleOCR sử dụng framework PaddlePaddle hoàn toàn riêng biệt. Hai framework này có thể xung đột khi cùng truy cập GPU. Giải pháp: Hệ thống cô lập các Engine trong các module Python riêng biệt, mỗi module tự quản lý việc import thư viện của mình. Lớp Core Orchestrator chỉ giao tiếp thông qua giao diện hàm chuẩn (function interface), không import trực tiếp các thư viện nội bộ của Engine.
2.3. Thiết kế hệ thống
Dưới đây là các biểu đồ thiết kế hệ thống theo tiêu chuẩn ngôn ngữ mô hình hóa thống nhất (UML), nhằm minh họa trực quan sự tương tác giữa các thành phần và các luồng xử lý dữ liệu phức tạp bên trong phần mềm.
2.3.1. Biểu đồ Usecase tổng quát
Biểu đồ Usecase tổng quát dưới đây mô tả toàn bộ các ca sử dụng (Use Case) của hệ thống "Hệ thống Desktop OCR" từ góc nhìn của hai nhóm tác nhân chính. Biểu đồ được tổ chức theo ranh giới hệ thống (System Boundary) và phân rã thành 3 nhóm chức năng (Package) rõ ràng, thể hiện đầy đủ các mối quan hệ kế thừa (Generalization) giữa các tác nhân và quan hệ ràng buộc (Include) giữa các ca sử dụng.

Hình 2.1. Biểu đồ Usecase tổng quát hệ thống
Các Tác nhân (Actors) và Mối quan hệ:
• User (Người dùng cuối): Là nhân viên văn phòng, chuyên viên hành chính sử dụng phần mềm để thực hiện các nghiệp vụ số hóa và xử lý tài liệu hàng ngày. User có quyền truy cập vào các nhóm chức năng thao tác tệp tin và nhận dạng OCR cơ bản.
• Quản trị viên: Là người có kiến thức về kỹ thuật hoặc được phân quyền quản lý phần mềm. Quản trị viên có mũi tên quan hệ Kế thừa (Generalization) trỏ về phía User. Điều này có nghĩa là Quản trị viên kế thừa toàn bộ các quyền hạn, chức năng của User, đồng thời có thêm quyền truy cập vào các chức năng cấu hình hệ thống chuyên sâu.
Các Nhóm chức năng (Use Cases) phân rã theo System Boundary. Hệ thống được chia thành 3 nhóm chức năng (Packages) chính để dễ quản lý:
• Nhóm quản trị hệ thống: Cấu hình hệ thống chuyên sâu: Chức năng độc quyền của Quản trị viên, cho phép can thiệp vào các file cài đặt (`config.json`), thay đổi thông số phần cứng (VRAM) hoặc cấu hình các mô hình trí tuệ nhân tạo bên dưới lõi phần mềm.
• Nhóm chức năng tiện ích: Cung cấp bộ công cụ mạnh mẽ hỗ trợ User xử lý tệp tin trước và sau khi OCR. Bao gồm:
o Đổi tệp tin hàng loạt: Chuẩn hóa tên file theo quy tắc Regex, thêm tiền
o Tách/Gộp tài liệu PDF: Phục vụ xử lý hồ sơ dung lượng lớn bằng thư viện PyPDF2.
o Chuyển định dạng PDF sang Word: Hỗ trợ chuyển đổi định dạng phục vụ chỉnh sửa.
o Đánh số thứ tự tệp tin tự động: Tổ chức lại danh mục tệp tin theo trình tự logic.
• Nhóm chức năng số hóa (Core OCR):
o Đây là phân hệ quan trọng nhất của ứng dụng, nơi User thực hiện nghiệp vụ trích xuất văn bản. Bao gồm:
o Nạp tài liệu ảnh/PDF: Tải tệp tin vào hệ thống qua kéo thả hoặc hộp thoại chọn file.
o Xem đối chiếu kết quả (Dual-panel): So sánh văn bản đầu ra với ảnh gốc song song.
o Lưu và xuất kết quả văn bản: Xuất file .txt hoặc copy kết quả vào clipboard.
o Thực thi nhận dạng tài liệu (Single): Gọi Engine AI để nhận dạng một tài liệu đơn lẻ.
o Lựa chọn cấu hình nhận dạng: Chọn Engine OCR (DocTR / PaddleOCR / Ensemble / EraX) và chế độ hậu xử lý (SymSpell / ProtonX Nano).
o Thực thi quét tự động hàng loạt: Tự động lặp quét toàn bộ tài liệu trong một thư mục.
Các Mối quan hệ ràng buộc (Include) giữa các Use Case:
• Biểu đồ chỉ ra luồng ràng buộc logic trong nghiệp vụ chuyển đổi số:
• Nạp tài liệu ảnh/PDF «include» Thực thi nhận dạng tài liệu: Để hệ thống có thể chạy AI trích xuất chữ, điều kiện tiên quyết và bắt buộc là User phải nạp tài liệu vào phần mềm thành công.
• Lựa chọn cấu hình nhận dạng «include» Thực thi nhận dạng tài liệu: Việc thiết lập cấu hình nhận dạng (chọn Engine nào, có dùng Hậu xử lý hay không) được đính kèm và tích hợp trực tiếp vào quá trình thực thi OCR.
• Thực thi quét tự động hàng loạt «include» Thực thi nhận dạng tài liệu: Bản chất của tính năng quét hàng loạt (Batch Processing) là vòng lặp gọi lại luồng xử lý của việc quét một tài liệu đơn lẻ nhiều lần liên tiếp.
Đặc tả chi tiết ca sử dụng UC01 - Nạp và tiền xử lý ảnh/PDF:
• Tên ca sử dụng: Tải tài liệu vào hệ thống và tiền xử lý.
• Tác nhân: Người dùng cuối.
• Luồng sự kiện chính:
o Người dùng kéo thả file hoặc chọn qua hộp thoại.
o Nếu là file PDF, hệ thống gọi thư viện PyMuPDF (`fitz`) để render PDF thành các trang ảnh độ phân giải cao (300 DPI) đưa vào bộ nhớ RAM.
o Hệ thống gọi module OpenCV để tiền xử lý:
o Grayscaling: Chuyển ảnh sang đen trắng để loại bỏ nhiễu màu.
o Binarization (Adaptive Gaussian Thresholding): Nhị phân hóa ảnh, làm nổi bật chữ đen trên nền trắng.
o Deskewing: Áp dụng phép tính minAreaRect (OpenCV) để tự động phát hiện góc nghiêng của giấy và xoay ảnh lại cho thẳng (Angle correction).
Đặc tả chi tiết ca sử dụng UC03 - Xem đối chiếu Dual-panel:
• Tên ca sử dụng: Đối chiếu và chỉnh sửa kết quả.
• Tác nhân: Người dùng cuối.
• Luồng sự kiện chính:
o Sau khi OCR, màn hình tự động tách làm hai nửa (Split-view).
o Nửa trái hiển thị ảnh gốc, tích hợp công cụ zoom (phóng to/thu nhỏ) và kéo rê (pan) để đọc các chữ nhỏ.
o Nửa phải hiển thị Textbox chứa kết quả. Bất kỳ sự thay đổi nào của người dùng trên Textbox đều được lưu tạm vào bộ đệm (Memory Buffer).
Đặc tả chi tiết ca sử dụng UC08 - Chia cắt/Gộp tài liệu PDF:
• Mô tả: Tiện ích xử lý tiền kỳ cho các tệp hồ sơ dung lượng lớn (có thể lên tới hàng ngàn trang).
• Luồng sự kiện:
o Chế độ Split: Người dùng nhập khoảng trang (Ví dụ: 1-5, 8). Hệ thống sử dụng thư viện `PyPDF2` để đọc luồng byte tĩnh (Stream) mà không nạp toàn bộ file vào RAM, cắt các trang tương ứng và ghi ra đĩa cứng.
o Chế độ Merge: Người dùng nạp nhiều tệp PDF. Hệ thống hợp nhất các luồng byte theo thứ tự và tạo ra mục lục (Bookmarks) tự động.
Đặc tả chi tiết ca sử dụng UC02 - Nhận dạng tài liệu (Gọi AI):
• Tên ca sử dụng: Thực thi quy trình nhận dạng tài liệu thông qua việc gọi hệ thống tích hợp bên thứ ba.
• Tác nhân: Người dùng cuối, Các Engine Blackbox.
• Mô tả: Đây là chức năng cốt lõi của phần mềm, nơi hệ thống khởi động quy trình pipeline, cắt nhỏ ảnh, đóng gói dữ liệu và liên lạc với các thư viện AI thông qua lớp Wrapper.
• Luồng sự kiện chính:
o Người dùng thao tác bấm nút "Bắt đầu quét" trên giao diện phần mềm.
o Hệ thống chuyển sang trạng thái "Đang xử lý" và hiện thanh tiến trình. Lớp Core Orchestrator thực hiện tiền xử lý hình ảnh (chuyển sang thang độ xám, giảm nhiễu) bằng bộ công cụ OpenCV [9].
o Dựa trên file cấu hình, Core gọi hàm API tương ứng đến Blackbox được chỉ định (Ví dụ: DocTR [1]) và truyền vào bộ nhớ ma trận ảnh.
o Hệ thống Blackbox xử lý chuyên sâu và phản hồi về dữ liệu tọa độ hình học cùng văn bản thô.
o Core Orchestrator lấy dữ liệu, ráp nối các từ thành câu hoàn chỉnh và thực hiện thuật toán kiểm tra chính tả.
o Nếu cấu hình ProtonX Nano [5] được bật, Core gửi toàn bộ văn bản thô sang API của hệ thống NLP Blackbox thứ hai (ProtonX Nano).
o ProtonX Nano [5] thực hiện suy luận ngữ cảnh theo kiến trúc Seq2Seq, "dịch" câu lỗi thành câu chuẩn và trả về văn bản đã khôi phục. Core ghi đè kết quả này.
o Hệ thống tổng hợp kết quả cuối cùng, ra lệnh cho tầng Giao diện cập nhật màn hình hiển thị Dual-panel cho người dùng.
Đặc tả chi tiết ca sử dụng UC11 - Xử lý quét văn bản hàng loạt (Batch Processing):
• Tên ca sử dụng: Tự động hóa quy trình nhận dạng toàn bộ tài liệu trong một thư mục.
• Tác nhân: Người dùng cuối, Các Engine Blackbox.
• Mô tả: Thay vì thao tác từng file đơn lẻ, người dùng chỉ định một thư mục đầu vào và thư mục đầu ra, hệ thống sẽ tự động lặp qua tất cả các tệp tin hợp lệ, lần lượt gọi pipeline OCR tích hợp cho từng file và xuất kết quả.
• Điều kiện tiên quyết: Thư mục đầu vào chứa ít nhất 1 file ảnh hoặc PDF hợp lệ.
• Luồng sự kiện chính:
o Người dùng chọn thư mục nguồn chứa các tệp tin cần quét và thư mục đích để lưu kết quả.
o Hệ thống quét thư mục, lọc ra danh sách các file có định dạng hỗ trợ (.png, .jpg, .pdf, .bmp, .tiff, .webp).
o Với mỗi file trong danh sách, hệ thống gọi lại toàn bộ pipeline của UC02 (Nhận dạng tài liệu): tiền xử lý → gọi Engine Blackbox → hậu xử lý.
o Thanh tiến trình trên giao diện được cập nhật theo thời gian thực, hiển thị file đang xử lý và tỷ lệ hoàn thành (ví dụ: 5/20 files).
o Kết quả văn bản của mỗi file được tự động lưu thành file .txt tương ứng trong thư mục đích.
o Khi toàn bộ danh sách đã xử lý xong, hệ thống hiển thị bảng tổng kết: Số file thành công, số file lỗi, tổng thời gian xử lý.
o Luồng ngoại lệ: Nếu một file trong danh sách gặp lỗi (ảnh bị hỏng, Engine trả về rỗng), hệ thống ghi nhận lỗi, bỏ qua file đó và tiếp tục xử lý các file còn lại mà không dừng toàn bộ tiến trình.
Đặc tả chi tiết ca sử dụng UC07 - Đổi tên tệp tin hàng loạt (Batch Rename):
• Tên ca sử dụng: Tự động hóa chuẩn hóa tên tệp tin theo quy tắc do người dùng định nghĩa.
• Tác nhân: Người dùng cuối.
• Mô tả: Cho phép người dùng nạp danh sách tệp tin, thiết lập các quy tắc đổi tên (thêm tiền tố, hậu tố, tìm và thay thế bằng Regex, đánh số thứ tự) và thực thi đổi tên hàng loạt trên ổ cứng.
• Điều kiện tiên quyết: Thư mục chứa ít nhất 1 tệp tin cần đổi tên.
• Luồng sự kiện chính:
o Người dùng chọn thư mục chứa các tệp tin cần đổi tên.
o Hệ thống quét và hiển thị danh sách tên file hiện tại trên giao diện.
o Người dùng thiết lập quy tắc đổi tên: thêm Tiền tố (Prefix), Hậu tố (Suffix), tìm và thay thế chuỗi (Search & Replace bằng Regex), hoặc đánh số thứ tự tự động.
o Hệ thống tự động tính toán và hiển thị bản Preview tên mới bên cạnh tên cũ, cho phép người dùng xem trước kết quả trước khi thực thi.
o Nếu người dùng đồng ý, bấm nút "Thực thi" để hệ thống thực hiện đổi tên trên ổ cứng (sử dụng hàm `os.rename()`).
o Hệ thống hiển thị thông báo hoàn tất kèm số lượng file đã đổi tên thành công.
o Luồng ngoại lệ: Nếu tên file mới bị trùng lặp hoặc chứa ký tự không hợp lệ, hệ thống cảnh báo và yêu cầu người dùng điều chỉnh quy tắc.
2.3.2. Các biểu đồ hoạt động (Activity Diagrams)
Hệ thống bao gồm nhiều luồng chức năng hỗ trợ toàn diện cho quy trình chuyển đổi số văn bản. Thay vì chỉ nhận dạng đơn thuần, phần mềm được trang bị đầy đủ các công cụ để xử lý vòng đời của một tài liệu. Dưới đây là các biểu đồ hoạt động chi tiết:
2.3.2.1. Luồng chức năng cốt lõi: Nhận dạng và xử lý OCR
Biểu đồ mô tả chi tiết luồng điều khiển và quá trình ra quyết định của hệ thống, bắt đầu từ thời điểm người dùng nạp dữ liệu đầu vào cho đến khi kết quả cuối cùng được hiển thị trên giao diện ứng dụng. Toàn bộ quá trình xử lý được tổ chức theo dạng pipeline nhiều tầng, trong đó mỗi thành phần đảm nhận một nhiệm vụ chuyên biệt nhằm bảo đảm dữ liệu được xử lý tuần tự, chính xác và tối ưu hiệu năng.
Các nhánh xử lý trong biểu đồ thể hiện khả năng điều phối linh hoạt của hệ thống khi lựa chọn OCR Engine dựa trên cấu hình mà người dùng thiết lập. Nhờ cơ chế này, hệ thống có thể chuyển đổi giữa nhiều engine nhận dạng khác nhau nhằm đáp ứng các tình huống sử dụng riêng biệt như ưu tiên tốc độ, độ chính xác hoặc khả năng xử lý tiếng Việt có dấu. Đồng thời, cấu trúc phân tầng giúp pipeline dễ mở rộng, dễ bảo trì và thuận lợi trong việc nâng cấp hoặc tích hợp thêm các mô hình AI trong tương lai.
Thông qua kiến trúc pipeline phân tầng này, hệ thống không chỉ đảm bảo khả năng xử lý ổn định mà còn tạo nền tảng thuận lợi cho việc mở rộng thêm các công nghệ OCR và AI mới trong tương lai.

Hình 2.2. Biểu đồ minh họa luồng chức năng cốt lõi: Nhận dạng và xử lý OCR
2.3.2.2. Luồng chức năng: Tiện ích Đổi tên tệp tin hàng loạt (Batch Rename)
Trong chuyển đổi số, việc chuẩn hóa tên file là bước cực kỳ quan trọng. Chức năng này giúp nhân sự hành chính chuẩn hóa tên hàng ngàn tài liệu lộn xộn trước khi lưu trữ hoặc quét OCR.
2.3.2.3. Luồng chức năng: Chia cắt và Gộp tài liệu (Split/Merge PDF)
Công cụ đắc lực để xử lý các tệp công văn nhiều trang. Nhân viên có thể bóc tách lấy 1 trang cần thiết để OCR thay vì quét cả tệp nặng nề.

Hình 2.3. Biểu đồ minh họa luồng chức năng: Chia cắt và Gộp tài liệu
2.3.2.4. Luồng chức năng: Xử lý quét văn bản hàng loạt (Batch Processing OCR)
Đây là chức năng thể hiện sức mạnh tự động hóa của phần mềm. Thay vì thao tác từng ảnh, luồng này cho phép số hóa toàn bộ thư mục một cách tự động, hoàn toàn không cần sự can thiệp của con người.

Hình 2.4. Biểu đồ minh họa luồng chức năng: Xử lý quét văn bản hàng loạt
2.3.3. Biểu đồ trình tự (Sequence Diagram)
Biểu đồ trình tự là một công cụ phân tích quan trọng giúp hiểu rõ sự trao đổi thông điệp (Message passing) theo thời gian giữa các thành phần độc lập trong kiến trúc. Biểu đồ dưới đây minh họa rõ rệt sự phân tách trách nhiệm giữa ba thực thể: Tầng Giao diện (UI), Tầng Điều phối (Core) và Tầng Tích hợp (Black-box). Tầng Giao diện tuyệt đối không liên lạc trực tiếp với các mô hình AI mà mọi mệnh lệnh đều phải thông qua Bộ điều phối.

Hình 2.5. Biểu đồ trình tự hệ thống OCR Scanner
2.3.4. Biểu đồ Lớp (Class Diagram)
Biểu đồ lớp dưới đây thể hiện việc áp dụng Mẫu thiết kế phần mềm (Design Pattern) chuyên nghiệp vào thực tiễn. Thay vì mã hóa cứng (Hard-code) việc gọi trực tiếp đến từng thư viện AI, hệ thống định nghĩa một Lớp trừu tượng `BaseOCREngine`.
Tất cả các mô hình học sâu muốn tích hợp vào hệ thống đều phải tạo ra một Lớp triển khai (Implement) thừa kế từ Lớp trừu tượng này và ghi đè phương thức `extract_text()`. Lớp trung tâm `OCRController` chỉ tương tác với Lớp trừu tượng, nhờ đó đạt được nguyên tắc Mở/Đóng (Open/Closed Principle) trong kỹ nghệ phần mềm: Hệ thống mở rộng dễ dàng (thêm mô hình mới) mà không cần phải chỉnh sửa mã nguồn cốt lõi hiện tại.

Hình 2.6. Biểu đồ lớp hệ thống OCR Scanner
Sự hoàn thiện của kiến trúc phần mềm này được minh chứng qua việc áp dụng triệt để các Mẫu thiết kế (Design Patterns) tiêu chuẩn công nghiệp phục vụ cho việc tích hợp:
• Mẫu Strategy (Chiến lược): Trong lớp OCRWorker, hệ thống không sử dụng các câu lệnh điều kiện dài dòng để gọi mô hình. Thay vào đó, một interface BaseOCREngine được định nghĩa. PaddleOCR và DocTR là các "Chiến lược" cụ thể được tiêm (Inject) vào Worker lúc chạy (Runtime), dựa trên tham số cấu hình trong file `config.json`. Điều này tuân thủ nguyên lý Đóng-Mở (Open/Closed Principle) — khi cần tích hợp thêm một Engine mới (ví dụ: Google Cloud Vision API), lập trình viên chỉ cần tạo thêm một lớp mới triển khai interface mà không phải sửa đổi bất kỳ mã nguồn cũ nào.
• Mẫu Observer (Người quan sát): Thách thức lớn nhất trong lập trình ứng dụng Desktop tích hợp AI là hiện tượng "Đóng băng giao diện" (UI Freeze) khi xử lý tác vụ nặng. Hệ thống giải quyết bằng Observer Pattern kết hợp đa luồng (Multi-threading). Lớp GUI đóng vai trò là Người quan sát, lớp Worker đóng vai trò Chủ thể. Worker chạy ngầm trên một luồng riêng biệt (Background Thread) và phát đi các sự kiện báo cáo tiến độ. Lớp GUI lắng nghe thông qua hàng đợi an toàn luồng (Thread-safe Queue) với chu kỳ 50ms để cập nhật thanh tiến trình và kết quả mượt mà mà không làm đóng băng giao diện.
• Mẫu Singleton (Độc bản): Các mô hình AI như ProtonX Nano hay PaddleOCR thường chiếm tới 2GB-4GB RAM khi khởi tạo. Việc khởi tạo nhiều lần sẽ dẫn đến tràn bộ nhớ. Mẫu Singleton đảm bảo rằng các Class quản lý mô hình (ProtonXCorrector, SymSpellChecker) chỉ có một phiên bản duy nhất tồn tại trong suốt vòng đời ứng dụng. Dữ liệu từ điển 4.9MB được nạp một lần duy nhất và chia sẻ (Shared Memory) cho mọi yêu cầu OCR tiếp theo.
2.3.5. Biểu đồ triển khai (Deployment Diagram)
Biểu đồ triển khai dưới đây mô tả cách các thành phần phần mềm được bố trí và vận hành trên hạ tầng vật lý thực tế. Do đặc thù là ứng dụng Desktop xử lý cục bộ (Local Processing), toàn bộ hệ thống được triển khai trên một máy tính duy nhất của người dùng, không yêu cầu máy chủ hay kết nối mạng. Trong kiến trúc này, toàn bộ các module chức năng như giao diện người dùng, bộ xử lý OCR, mô hình AI/NLP hậu xử lý, bộ từ điển kiểm lỗi, cơ sở dữ liệu nội bộ và các thành phần điều phối xử lý đều được triển khai tập trung trên cùng một thiết bị vật lý. Điều này giúp hệ thống hoạt động độc lập, giảm độ trễ xử lý, tăng tốc độ phản hồi và đảm bảo khả năng vận hành ngay cả khi không có kết nối Internet. Ngoài ra, việc triển khai theo mô hình cục bộ còn giúp tăng cường tính bảo mật và quyền riêng tư của dữ liệu, vì toàn bộ hình ảnh và nội dung văn bản được xử lý trực tiếp trên máy người dùng thay vì gửi lên máy chủ từ xa. Kiến trúc này đặc biệt phù hợp với các bài toán OCR tài liệu nội bộ, xử lý dữ liệu nhạy cảm hoặc các môi trường yêu cầu khả năng hoạt động offline ổn định. Bên cạnh đó, do không cần xây dựng hạ tầng server hay hệ thống phân tán, chi phí triển khai và bảo trì hệ thống cũng được tối ưu đáng kể, giúp việc cài đặt và sử dụng trở nên đơn giản hơn đối với người dùng cuối.

Hình 2.7. Biểu đồ triển khai hệ thống OCR Scanner
Điểm đặc biệt của mô hình triển khai này là tính tự chủ hoàn toàn: Không có bất kỳ thành phần nào yêu cầu kết nối tới máy chủ bên ngoài (Cloud Server) hay dịch vụ API trả phí. Mọi quá trình nhận dạng hình ảnh, suy luận ngôn ngữ và kiểm tra chính tả đều diễn ra trong không gian bộ nhớ cục bộ của máy tính người dùng.
2.3.6. Cấu trúc dữ liệu hệ thống (Data Schema)
Do đặc thù là một ứng dụng Desktop xử lý theo phiên (Session-based), hệ thống không sử dụng các hệ quản trị cơ sở dữ liệu quan hệ (RDBMS) truyền thống như MySQL hay SQL Server. Thay vào đó, chiến lược lưu trữ dữ liệu được thiết kế tối giản theo triết lý "File-based Storage", phù hợp với quy mô và yêu cầu của phần mềm. Quyết định thiết kế này được đưa ra dựa trên ba phân tích cụ thể: Thứ nhất, về bản chất nghiệp vụ, phần mềm OCR Scanner xử lý dữ liệu theo từng phiên làm việc độc lập - mỗi lần người dùng nạp tài liệu, hệ thống xử lý và trả về kết quả, không có nhu cầu lưu trữ dài hạn hay truy vấn phức tạp giữa các phiên. Thứ hai, về đối tượng người dùng, nhân viên văn phòng không có kiến thức cài đặt và quản trị cơ sở dữ liệu - việc yêu cầu cài MySQL Server sẽ tạo ra rào cản triển khai không cần thiết. Thứ ba, về hiệu năng, các file cấu hình JSON có dung lượng cực nhỏ (dưới 1KB), việc đọc/ghi trực tiếp trên hệ thống file nhanh hơn đáng kể so với việc khởi tạo kết nối, mở transaction và thực thi câu lệnh SQL. Mô hình xử lý dữ liệu của hệ thống tuân theo nguyên tắc "Xử lý trên bộ nhớ, lưu trữ trên ổ đĩa" (Process in Memory, Persist on Disk). Cụ thể, khi người dùng thực hiện quét OCR, toàn bộ dữ liệu trung gian (ảnh đã tiền xử lý, ma trận pixel, văn bản thô từ Engine, văn bản đã hậu xử lý) đều được xử lý hoàn toàn trong không gian bộ nhớ RAM. Chỉ khi kết quả cuối cùng đã hoàn chỉnh, hệ thống mới ghi xuống ổ cứng dưới dạng file văn bản thuần (.txt). Cơ chế này đảm bảo tốc độ xử lý tối đa đồng thời giảm thiểu số lần truy xuất ổ đĩa (I/O operations).
Bảng 2.1. Bảng cấu trúc dữ liệu vật lý
Tên file / Đối tượng Định dạng Dung lượng Mục đích sử dụng Thời điểm truy xuất
config.json JSON ~1 KB Lưu cấu hình mặc định của hệ thống: Engine OCR, trạng thái AI, thư mục lưu trữ, tham số xử lý Đọc khi khởi động, ghi khi thay đổi cấu hình
raw_dict.jsonl JSONL ~4.9 MB Từ điển Tiếng Việt gồm hơn 100.000 từ phục vụ thuật toán sửa lỗi SymSpell Nạp toàn bộ vào RAM khi khởi động hệ thống
FileResult In-memory Object Dynamic Lưu kết quả OCR của từng file: đường dẫn, engine sử dụng, trạng thái, văn bản gốc, văn bản hậu xử lý, thời gian xử lý, độ tin cậy, số dòng, số ký tự Khởi tạo trong mỗi phiên quét và giải phóng khi kết thúc
\*.txt Plain Text Dynamic Lưu văn bản đầu ra sau khi OCR và hậu xử lý hoàn tất Ghi xuống ổ cứng sau khi xử lý thành công

Schema chi tiết file `config.json`:

Hình 2.8. Schema chi tiết file `config.json’
Cấu trúc một mục từ điển trong raw_dict.jsonl (mỗi dòng là một JSON object):

Hình 2.9. Cấu trúc một mục từ điển trong raw_dict.jsonl
Việc lựa chọn chiến lược File-based thay vì RDBMS mang lại hai lợi ích thiết thực: Thứ nhất, giảm thiểu hoàn toàn độ phức tạp cài đặt cho người dùng cuối (không cần cài đặt MySQL Server). Thứ hai, tốc độ truy xuất cấu hình nhanh chóng (đọc file JSON nhỏ nhanh hơn nhiều so với khởi tạo kết nối tới database server).
2.4. Cài đặt và hướng dẫn tích hợp hệ thống
Mục này trình bày quy trình cài đặt thực tế và các bước tích hợp từng thành phần bên thứ ba vào hệ thống phần mềm OCR Scanner. Quy trình được chia thành 4 giai đoạn tuần tự, mỗi giai đoạn phải hoàn tất trước khi chuyển sang giai đoạn tiếp theo.
2.4.1. Thiết lập môi trường phát triển
Bước đầu tiên trong quá trình tích hợp là chuẩn bị môi trường hệ thống nền tảng. Hệ thống yêu cầu cài đặt Python phiên bản 3.10 trở lên làm trình thông dịch chính. Để cô lập các thư viện của dự án khỏi hệ thống Python toàn cục (tránh xung đột phiên bản), một môi trường ảo (Virtual Environment) được tạo riêng cho dự án bằng lệnh python -m venv .venv. Toàn bộ các thư viện phụ thuộc sau đó sẽ được cài đặt vào trong môi trường ảo này.
Đối với tăng tốc phần cứng GPU, người dùng cần cài đặt bộ công cụ NVIDIA CUDA Toolkit (phiên bản 11.8 hoặc 12.x) và thư viện cuDNN tương thích trên máy tính. Đây là điều kiện tiên quyết để các framework học sâu PyTorch và PaddlePaddle có thể khai thác sức mạnh tính toán song song của card đồ họa NVIDIA. Nếu máy tính không có GPU NVIDIA, hệ thống vẫn hoạt động bình thường ở chế độ CPU với tốc độ xử lý chậm hơn.
2.4.2. Tích hợp từng Engine vào hệ thống
Sau khi môi trường nền tảng đã sẵn sàng, quá trình tích hợp từng Engine AI được thực hiện theo thứ tự ưu tiên:
• Tích hợp Engine DocTR [1]:
o Thư viện DocTR được cài đặt thông qua trình quản lý gói pip cùng với các phụ thuộc PyTorch.
o Khi cài đặt lần đầu, hệ thống tự động tải xuống các trọng số mô hình tiền huấn luyện (Pre-trained weights) từ kho HuggingFace Hub và lưu vào thư mục cache cục bộ.
o Lớp Wrapper engine_doctr.py được xây dựng để đóng gói toàn bộ logic gọi DocTR, cung cấp cho hệ thống lõi một hàm duy nhất ocr_doctr_image(image_path) trả về chuỗi văn bản đã trích xuất.
o Bên trong lớp Wrapper, quá trình chuyển đổi dữ liệu giữa định dạng ảnh OpenCV (numpy array) sang định dạng đầu vào của DocTR (DocumentFile) được xử lý tự động và trong suốt đối với lớp gọi.
• Tích hợp Engine PaddleOCR [2]:
o PaddleOCR yêu cầu cài đặt riêng framework PaddlePaddle (phiên bản GPU hoặc CPU tùy cấu hình phần cứng).
o Do PaddlePaddle và PyTorch là hai framework độc lập, cần đặc biệt chú ý đến thứ tự cài đặt và phiên bản CUDA tương thích để tránh xung đột.
o Lớp Wrapper engine_paddle.py cung cấp hai chế độ hoạt động: chế độ đầy đủ (Full) bật tính năng unwarping giúp nhận dạng chính xác hơn nhưng chậm hơn, và chế độ nhanh (Fast) tắt unwarping để tăng tốc độ lên 3-5 lần.
o Cả hai chế độ đều được truy cập thông qua cùng một giao diện hàm chuẩn, giúp lớp Core Orchestrator không cần quan tâm đến chi tiết bên trong.
• Tích hợp mô hình ProtonX Nano [5]:
o Mô hình Seq2Seq của ProtonX được tích hợp thông qua thư viện transformers của HuggingFace.
o Quá trình cài đặt bao gồm việc tải xuống hai thành phần: Tokenizer (bộ phân tích từ vựng) và Model (trọng số mô hình), tổng dung lượng khoảng 500MB-1GB.
o Lớp Wrapper engine_protonx_correction.py đóng gói toàn bộ logic tokenize, suy luận (inference) và giải mã (decode) thành một hàm duy nhất correct_text(text).
o Đặc biệt, module này cài đặt cơ chế phân đoạn văn bản (Chunking) để xử lý các tài liệu dài vượt quá giới hạn token tối đa của mô hình.
• Tích hợp SymSpell [6]:
o Thuật toán SymSpell không yêu cầu cài đặt thư viện bên ngoài phức tạp mà được triển khai trực tiếp trong module symspell_checker.py bằng mã nguồn Python thuần.
o Quá trình tích hợp chủ yếu tập trung vào việc chuẩn bị bộ từ điển: Tệp raw_dict.jsonl chứa hơn 100.000 mục từ vựng tiếng Việt được thu thập, làm sạch và định dạng chuẩn JSON Lines.
o Khi ứng dụng khởi động, module tự động đọc tệp từ điển và xây dựng bảng băm trong bộ nhớ RAM.
2.4.3. Cấu hình tham số tích hợp qua file config.json
Toàn bộ các tham số điều khiển quá trình tích hợp được tập trung quản lý trong một tệp cấu hình duy nhất config.json, đặt tại thư mục gốc của dự án. Tệp này đóng vai trò như một Bảng điều khiển trung tâm cho phép Quản trị viên thay đổi hành vi của hệ thống mà không cần chỉnh sửa mã nguồn.
Các tham số cấu hình chính bao gồm: Tham số default_engine quy định Engine OCR mặc định khi khởi động (có thể là doctr, paddle, paddle_fast hoặc ensemble).
Tham số use_postprocess bật/tắt pipeline hậu xử lý. Tham số use_protonx kích hoạt mô hình ProtonX Nano Seq2Seq cho sửa lỗi ngữ cảnh sâu. Tham số use_spellcheck bật chế độ sửa lỗi chính tả SymSpell nhẹ. Ngoài ra, khối preprocessing cho phép bật/tắt các bước tiền xử lý ảnh (deskew, denoise) tùy theo chất lượng tài liệu đầu vào.
Cơ chế hoạt động: Khi ứng dụng khởi động, lớp Core Orchestrator đọc file config.json một lần duy nhất và lưu vào bộ nhớ. Khi người dùng thay đổi cài đặt thông qua giao diện (ví dụ: chuyển từ DocTR sang PaddleOCR), hệ thống ghi đè giá trị mới vào file JSON và tải lại cấu hình. Thiết kế này cho phép cấu hình hệ thống được bảo toàn giữa các lần khởi động ứng dụng.
2.4.4. Quy trình khởi động và kiểm tra tích hợp
Khi người dùng khởi động ứng dụng Desktop, hệ thống thực hiện quy trình khởi tạo theo trình tự sau: (1) Đọc file config.json để xác định cấu hình mặc định; (2) Khởi tạo module SymSpellChecker — nạp toàn bộ từ điển 4.9MB vào RAM và xây dựng bảng băm, quá trình này mất khoảng 2-3 giây; (3) Hiển thị giao diện chính cho người dùng; (4) Khi người dùng bấm nút OCR lần đầu tiên, hệ thống mới thực sự nạp mô hình Engine (DocTR hoặc PaddleOCR) lên GPU theo cơ chế tải lười (Lazy Loading), quá trình này mất 5-10 giây tùy thuộc tốc độ ổ cứng và dung lượng VRAM.
Để kiểm tra tính toàn vẹn của quá trình tích hợp, hệ thống cung cấp cơ chế kiểm tra tự động (Self-check): Trước khi gọi bất kỳ Engine nào, lớp Wrapper kiểm tra xem mô hình đã được tải thành công chưa, CUDA có khả dụng không, và các tệp trọng số có tồn tại trong thư mục cache không. Nếu phát hiện lỗi, hệ thống hiển thị thông báo cụ thể cho người dùng (ví dụ: CUDA không khả dụng, chuyển sang CPU mode) và tự động kích hoạt cơ chế dự phòng (Fallback) thay vì để ứng dụng bị treo.
CHƯƠNG 3: THỰC NGHIỆM VÀ ĐÁNH GIÁ
3.1. Công nghệ sử dụng
Hệ thống được phát triển và vận hành dựa trên một hệ sinh thái công nghệ đa dạng, được lựa chọn kỹ lưỡng nhằm đáp ứng yêu cầu xử lý đồ họa, học sâu và thiết kế giao diện trên máy tính để bàn:
• Ngôn ngữ và Môi trường: Python 3.10 được chọn làm ngôn ngữ lập trình chính nhờ sức mạnh vượt trội trong lĩnh vực khoa học dữ liệu và hỗ trợ tốt các thư viện hệ thống. Việc thực nghiệm được chạy trên hệ điều hành Windows 11.
• Nền tảng Phần cứng & Tăng tốc tính toán: Để các mô hình AI có thể hoạt động mượt mà, hệ thống đòi hỏi thiết bị cài đặt hạ tầng NVIDIA CUDA Toolkit (kèm cuDNN) để có thể truy xuất và khai thác sức mạnh tính toán song song của nhân GPU cục bộ.
• Thư viện Giao diện Người dùng: Thư viện `CustomTkinter` được sử dụng để lập trình Giao diện đồ họa (GUI). Thư viện này kế thừa sức mạnh của hệ thống Tkinter truyền thống nhưng mang lại phong cách thiết kế giao diện hiện đại, bóng bẩy và chuyên nghiệp hơn, hỗ trợ tốt các chế độ chủ đề (Dark/Light mode).
• Thư viện AI và Xử lý ảnh: Thư viện mã nguồn mở OpenCV [9] (`cv2`) đảm nhiệm mọi thao tác biến đổi không gian ảnh. Các nền tảng học sâu cốt lõi như PyTorch và PaddlePaddle được cấu hình thành môi trường nền tảng để chạy các Engine tích hợp. Module `transformers` do HuggingFace cung cấp được sử dụng để kết nối và gọi siêu mô hình ngôn ngữ ProtonX Nano Legal Text Correction [5].
• Xử lý tài liệu PDF: Thư viện PyMuPDF (`fitz`) được sử dụng để render các trang PDF thành hình ảnh với độ phân giải cao, phục vụ cho quy trình OCR trên tài liệu đa trang. Ngoài ra, thư viện PyPDF2 đảm nhiệm chức năng chia tách (split) và ghép nối (merge) các tệp PDF trong module File Tools.
• Kiểm tra chính tả và xử lý ngôn ngữ: Thuật toán SymSpell được triển khai nội bộ kết hợp với bộ từ điển tiếng Việt tự xây dựng (hơn 100.000 mục từ vựng, định dạng JSONL) để phục vụ sửa lỗi chính tả ở tốc độ cao. Thư viện `re` (Regular Expression) được sử dụng rộng rãi trong module FIX_MAP để xử lý các mẫu lỗi lặp.
• Quản lý tệp tin và hệ thống: Module `os`, `shutil` và `pathlib` của Python Standard Library được sử dụng để thực hiện các thao tác đổi tên hàng loạt (Batch Rename), di chuyển tệp và quản lý cấu trúc thư mục. Module `threading` và `concurrent.futures` đảm nhiệm việc xử lý đa luồng để tránh đóng băng giao diện.
Tổng hợp các thư viện và công nghệ chính được sử dụng trong hệ thống:
• Python 3.10: Ngôn ngữ lập trình chính, đóng vai trò nền tảng phát triển toàn bộ hệ thống.
• PyTorch 2.x: Framework học sâu phục vụ chạy Engine DocTR.
• PaddlePaddle 2.x: Framework học sâu phục vụ chạy Engine PaddleOCR.
• NVIDIA CUDA Toolkit 11.8/12.x: Hạ tầng tính toán song song trên GPU, tăng tốc suy luận mô hình AI.
• OpenCV (cv2) 4.x: Thư viện xử lý ảnh, đảm nhiệm tiền xử lý và biến đổi không gian ảnh.
• DocTR 0.8+: Engine OCR nhận dạng văn bản từ ảnh, trả về cấu trúc dạng cây.
• PaddleOCR 2.7+: Engine OCR nhận dạng văn bản tốc độ cao, hỗ trợ đa ngôn ngữ.
• ProtonX Nano (transformers): Mô hình ngôn ngữ Seq2Seq phục vụ khôi phục dấu và sửa lỗi ngữ cảnh.
• CustomTkinter 5.x: Thư viện giao diện người dùng hiện đại, hỗ trợ Dark/Light mode.
• PyMuPDF (fitz) 1.23+: Thư viện render PDF thành ảnh và tách trang tài liệu.
3.2. Giao diện hệ thống
3.2.1. Giao diện màn hình OCR tài liệu.

Hình 3.1. Giao diện đối chiếu kết quả OCR Dual-panel
Giao diện chính phục vụ chức năng cốt lõi của hệ thống, được thiết kế theo dạng đối chiếu song song (Dual-panel). Hệ thống cung cấp các thanh công cụ điều hướng, chọn Engine và bảng nhật ký xử lý chi tiết.
3.2.2. Giao diện màn hình đổi tên tài liệu hàng loạt.

Hình 3.2. Chức năng đổi tên tệp tin hàng loạt (Batch Rename)
Màn hình này cho phép người dùng chuẩn hóa tên tệp tin số lượng lớn theo các quy tắc định sẵn. Giao diện bao gồm khu vực thiết lập quy tắc (thêm tiền tố, hậu tố, thay thế chuỗi bằng Regex) và bảng danh sách tệp tin hiển thị kết quả xem trước (Preview) tên mới trước khi thực thi, giúp giảm thiểu sai sót trong quá trình quản lý hồ sơ.
3.2.3. Giao diện màn hình tách file hàng loạt

Hình 3.3. Chức năng chia tách tài liệu PDF hàng loạt
Đây là công cụ hỗ trợ xử lý các tệp PDF đa trang. Giao diện tập trung vào sự đơn giản, cho phép người dùng nạp tệp PDF gốc và tự động bóc tách từng trang thành các tệp tin độc lập. Màn hình hiển thị danh sách các trang đã tách kèm theo trạng thái xử lý thành công, phục vụ cho việc số hóa tài liệu lẻ từ các tập hồ sơ lớn.
3.3. Kết quả thực nghiệm
Mục đích cốt lõi của môn học "Hệ thống thông tin tích hợp" là chứng minh rằng tổng thể hệ thống sau khi tích hợp có giá trị lớn hơn tổng rời rạc của các bộ phận cấu thành. Để minh chứng, dự án đã xây dựng một bộ tiêu chuẩn đánh giá khắt khe.
Sau một thời gian tích cực lập trình và tinh chỉnh hệ thống, dự án đã triển khai thành công mô hình tích hợp kiến trúc hộp đen và tiến hành thực nghiệm thực tế trên nhiều mẫu văn bản, tài liệu, công văn tiếng Việt khác nhau. Các kết quả thu thập được chứng minh rõ rệt tính ưu việt của phương pháp tiếp cận:
• Trường hợp tích hợp DocTR [1] và Thuật toán SymSpell [6]: Khi hệ thống được cấu hình chạy module DocTR kết hợp xử lý từ điển nội bộ, phần mềm mang lại độ chính xác trung bình đạt 92% trong thời gian phản hồi khoảng 2 giây cho một trang văn bản kích thước tiêu chuẩn A4. Mặc dù tốc độ không phải là nhanh nhất, nhưng phương thức này tiêu thụ lượng RAM đồ họa ở mức vừa phải, chứng tỏ đây là một cấu hình hoàn toàn phù hợp và kinh tế để triển khai cho các máy tính văn phòng có cấu hình trung bình.
• Trường hợp tích hợp cấu hình cao cấp PaddleOCR [2] kết hợp ProtonX Nano [5]: Với các thiết bị máy tính sở hữu card đồ họa mạnh, việc thiết lập phần mềm sử dụng Engine PaddleOCR đem lại một tốc độ xử lý siêu tốc, quét toàn bộ hình ảnh trong thời gian chưa tới 1 giây. Việc xuất hiện hiện tượng rớt dấu của PaddleOCR đã được khắc phục một cách hoàn hảo nhờ module hậu xử lý ProtonX Nano. Khả năng phân tích và hiểu cấu trúc ngữ pháp thông qua kiến trúc Seq2Seq [10] đã giúp mô hình dịch toàn bộ câu văn lỗi thành câu văn đúng chuẩn, khôi phục thành công các dấu câu bị mất, đẩy chỉ số chính xác tổng thể (Overall Accuracy) của toàn bộ hệ thống lên tới mức 95-96%. Kết quả đầu ra là những đoạn văn bản liền mạch, đúng chính tả, ngữ nghĩa trôi chảy và sẵn sàng để lưu trữ ngay lập tức.
• Tích hợp bộ công cụ phụ trợ (File Tools): Bên cạnh chức năng cốt lõi là nhận dạng, tính năng đổi tên tệp tin hàng loạt (Batch Renaming) và chia cắt tài liệu (File Splitting) đã phát huy hiệu quả to lớn trong thực tế. Nó giúp người dùng tổ chức, sắp xếp lại hàng ngàn tài liệu hình ảnh, PDF lộn xộn thành một kho dữ liệu có cấu trúc định dạng chuẩn mực trước khi đưa vào luồng quét OCR, góp phần hoàn thiện một quy trình số hóa khép kín.
• Ngoài ra, hệ thống xử lý thao tác hàng loạt (Batch Processing) vận hành ổn định. Chức năng này cho phép một nhân sự hành chính chỉ cần thực hiện duy nhất một thao tác chọn thư mục nguồn, phần mềm sẽ tự động đẩy hàng loạt ảnh chụp màn hình qua pipeline xử lý của hệ thống tích hợp và lần lượt xuất file kết quả. Theo ước tính, quy trình này giúp giảm thiểu tới 80-90% khối lượng thời gian so với phương pháp gõ phím sao chép văn bản truyền thống.
Đánh giá hiệu quả tích hợp hệ thống:
• Kết quả thực nghiệm cho thấy sự khác biệt rõ rệt giữa việc sử dụng các Engine OCR đơn lẻ và việc tích hợp chúng thông qua kiến trúc Orchestrator. Khi chạy PaddleOCR [2] một mình mà không có hậu xử lý, độ chính xác chỉ đạt khoảng 82-85% do hiện tượng mất dấu thanh tiếng Việt.
• Tuy nhiên, khi tích hợp cùng tầng hậu xử lý ProtonX Nano [5] thông qua pipeline Black-box, chỉ số này được đẩy lên 95-96%, một bước nhảy vọt khoảng 10-13 điểm phần trăm. Điều này minh chứng rằng giá trị cốt lõi của đồ án không nằm ở từng mô hình riêng lẻ, mà nằm ở nghệ thuật tích hợp và điều phối chúng làm việc đồng bộ.
• Đặc biệt, cơ chế Ensemble (chạy song song cả DocTR [1] và PaddleOCR [2], sau đó so sánh Confidence Score để chọn kết quả tốt hơn) đã chứng minh rằng việc kết hợp nhiều chuyên gia AI luôn cho kết quả vượt trội so với việc tin tưởng vào một nguồn duy nhất. Đây chính là ứng dụng thực tiễn của nguyên lý Tích hợp hệ thống mà môn học đề cập.
So sánh trước và sau tích hợp: Để minh họa rõ ràng hơn giá trị mà kiến trúc tích hợp hệ thống mang lại, bảng dưới đây so sánh trực tiếp giữa hai trạng thái: hệ thống chạy Engine OCR đơn lẻ (trước tích hợp) và hệ thống hoàn chỉnh sau khi áp dụng pipeline tích hợp đa tầng (sau tích hợp).
Bảng 3.1. Bảng so sánh hệ thống trước và sau khi tích hợp.
Tiêu chí đánh giá Trước tích hợp (Engine đơn lẻ) Sau tích hợp (Pipeline đầy đủ)
Độ chính xác nhận dạng ~82–85% (PaddleOCR đơn lẻ), ~88–90% (DocTR đơn lẻ) ~95–97% (Ensemble + ProtonX Nano)
Khả năng xử lý dấu thanh tiếng Việt Thường xuyên mất dấu, nhầm dấu (ví dụ: “Nguyễn” → “Nguyẻn”, “quyết định” → “quyêt đinh”) Khôi phục chính xác nhờ mô hình Seq2Seq hiểu ngữ cảnh toàn câu
Cơ chế chọn Engine Cố định một Engine duy nhất, không có khả năng tự điều chỉnh Tự động chọn Engine tốt nhất qua Confidence Score (Ensemble)
Khả năng sửa lỗi chính tả Không có — văn bản thô chứa nhiều lỗi, phải chỉnh sửa thủ công Hai tầng sửa lỗi: SymSpell (từ đơn, siêu nhanh) + ProtonX Nano (ngữ cảnh, chính xác cao)
Khả năng chịu lỗi phần cứng Phụ thuộc hoàn toàn vào GPU; nếu GPU không khả dụng thì không hoạt động Cơ chế Fallback tự động: GPU → CPU, đảm bảo hoạt động trên mọi cấu hình
Khả năng mở rộng Thêm Engine mới yêu cầu viết lại mã nguồn lõi Kiến trúc Plugin + Strategy Pattern: chỉ cần tạo Wrapper mới, không sửa mã cũ

Kết quả so sánh cho thấy một sự cải thiện toàn diện trên mọi tiêu chí sau khi áp dụng kiến trúc tích hợp. Đặc biệt, bước nhảy vọt 10-15 điểm phần trăm về độ chính xác (từ ~82% lên ~97%) minh chứng rằng giá trị thực sự không nằm ở từng mô hình riêng lẻ, mà nằm ở nghệ thuật điều phối và phối hợp chúng thành một pipeline xử lý thống nhất. Đây chính là bản chất cốt lõi của môn học "Hệ thống thông tin tích hợp" được ứng dụng vào thực tiễn.
Bảng 3.2. Bảng tổng hợp so sánh hiệu năng giữa các cấu hình tích hợp.
Cấu hình Engine OCR Hậu xử lý Độ chính xác Thời gian / trang A4 VRAM yêu cầu Đối tượng phù hợp
Cơ bản DocTR SymSpell ~92% ~2 giây ~2 GB Máy văn phòng tầm trung
Nhanh PaddleOCR Fast SymSpell ~88–90% < 1 giây ~1.6 GB Ưu tiên tốc độ xử lý
Cao cấp PaddleOCR ProtonX Nano Seq2Seq ~95–96% ~1 giây OCR + ~2 giây NLP ~4 GB Máy có GPU mạnh
Tối ưu Ensemble DocTR + PaddleOCR ProtonX Nano Seq2Seq ~96–97% ~3–4 giây ~6 GB Ưu tiên chất lượng đầu ra

 
KẾT LUẬN
Qua thời gian nghiêm túc nghiên cứu, xây dựng và thực nghiệm phần mềm, đồ án "Hệ thống Nhận dạng và Xử lý Văn bản Tiếng Việt Tích hợp Đa Engine OCR" đã hoàn thành xuất sắc các mục tiêu và nhiệm vụ đặt ra từ đầu. Vượt ra khỏi giới hạn của một phần mềm trích xuất ký tự đơn thuần, đồ án đã chứng minh một minh chứng sống động cho khả năng ứng dụng tri thức môn học "Hệ thống thông tin tích hợp" vào giải quyết các bài toán hiện đại.
Thành công lớn nhất của đề tài không nằm ở việc phát minh ra một trí tuệ nhân tạo mới, mà nằm ở việc xây dựng thành công một bộ khung kiến trúc phần mềm linh hoạt, có khả năng kết nối, gọi và điều phối các "Hộp đen" AI khổng lồ (DocTR [1], Paddle [2], ProtonX Nano [5]) làm việc đồng bộ với nhau một cách nhịp nhàng. Cơ chế "Lớp vỏ bọc" (Wrapper Interface) đã bảo vệ phần mềm ứng dụng lõi khỏi mọi nguy cơ sụp đổ từ bên thứ ba. Nhờ đó, tính ổn định và khả năng dễ dàng nâng cấp mô hình trong tương lai được đảm bảo tuyệt đối.
Mặc dù đã đem lại những kết quả tích cực về mặt nhận dạng và xử lý ngôn ngữ, đồ án vẫn còn một số điểm giới hạn. Do phụ thuộc vào môi trường cài đặt Python và các trình điều khiển card đồ họa phức tạp, phần mềm hiện tại yêu cầu quá trình thiết lập thủ công khá mất thời gian, chưa được đóng gói hoàn chỉnh thành một tệp tin thực thi độc lập (ví dụ: file .exe hay .msi) để có thể phát hành đại trà cho người dùng thông thường. Đồng thời, mô hình ngôn ngữ lớn ProtonX Nano [5] yêu cầu nhiều tài nguyên tính toán khiến các máy tính chỉ có cấu hình văn phòng cơ bản gặp khó khăn khi xử lý luồng tích hợp nâng cao.
Trong tương lai, hướng phát triển và hoàn thiện tiếp theo của dự án sẽ tập trung vào việc áp dụng các công cụ biên dịch (như PyInstaller) kết hợp với các công nghệ đóng gói môi trường tiên tiến (Docker) nhằm tự động hóa hoàn toàn khâu cài đặt cho người dùng cuối. Bên cạnh đó, việc nghiên cứu các kỹ thuật tối ưu hóa và giảm kích thước mô hình trí tuệ nhân tạo (Model Quantization) sẽ được triển khai, giúp hệ thống hoạt động nhẹ nhàng hơn, phản hồi nhanh hơn và thân thiện với phần cứng máy tính hơn, hướng tới xây dựng một hệ thống văn phòng số hóa toàn diện và độc lập.

 
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
[10]. J. Devlin; M.-W. Chang; K. Lee; K. Toutanova, "Pre-training of deep bidirectional transformers for language understanding. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies," 2019.
[11]. J. L. Schönberger; J. M. Frahm, "Structure-from-motion revisited. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)," 2016.
[12]. M. T. e. al, "Adapting BERT for named entity recognition in OCR," Computational Linguistics and Intellectual Technologies, vol. 20, 2021.
[13]. Y. Baek; B. Lee; D. Han; S. Yun; H. Lee, "Character region awareness for text detection. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)," 2019.
