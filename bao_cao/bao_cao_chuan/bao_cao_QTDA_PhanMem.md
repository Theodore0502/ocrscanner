 

MỤC LỤC
CHƯƠNG 1: KHẢO SÁT HIỆN TRẠNG VÀ XÁC LẬP DỰ ÁN 2
CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG 7
CHƯƠNG 3: THỰC NGHIỆM VÀ ĐÁNH GIÁ
CHƯƠNG 1: GIỚI THIỆU DỰ ÁN
CHƯƠNG 2: QUẢN LÝ DỰ ÁN
CHƯƠNG 3: TRIỂN KHAI CHƯƠNG TRÌNH
CHƯƠNG 1: GIỚI THIỆU DỰ ÁN
1.1. Giới thiệu về đơn vị thực tập
1.1.1. Giới thiệu tổng quan đơn vị
1.1.2. Lĩnh vực hoạt động
1.1.3. Vai trò của công nghệ thông tin trong doanh nghiệp
1.2. Tổng quan bài toán (Vấn đề thực tiễn số hóa tài liệu)
1.2.1. Thực trạng số hóa tài liệu hiện nay
1.2.2. Những khó khăn trong OCR tiếng Việt
1.2.3. Nhu cầu xây dựng hệ thống OCR Scanner
1.3. Xác lập dự án
1.3.1. Mục tiêu của hệ thống
1.3.2. Phạm vi của dự án
1.3.3. Đánh giá tính khả thi của hệ thống
1.4. Phân tích yêu cầu hệ thống
1.4.1. Yêu cầu chức năng
1.4.2. Yêu cầu phi chức năng
1.5. Cơ sở lý thuyết và công nghệ lõi
1.5.1. Khoảng cách Levenshtein
1.5.2. Thuật toán SymSpell
1.5.3. Mô hình Seq2Seq trong xử lý ngôn ngữ
1.5.4. Kiến trúc Plugin và Singleton
1.5.5. Biểu thức chính quy (Regex)
CHƯƠNG 2: QUẢN LÝ DỰ ÁN
2.1. Mô hình phát triển phần mềm
2.1.1. Giới thiệu mô hình Scrum
2.1.2. Lý do lựa chọn Scrum cho dự án OCR Scanner
2.1.3. Vai trò Scrum trong dự án
2.1.4. Product Backlog của dự án
2.2. Kế hoạch thực hiện dự án theo Sprint
2.2.1. Các mốc thời gian chính
2.2.2. Sprint Backlog và kế hoạch thực hiện
2.2.3. Sprint Review và Sprint Retrospective
2.2.4. Biểu đồ Gantt
2.3. Cấu trúc phân rã công việc và ước lượng thời gian
2.3.1. Bảng phân rã công việc WBS
2.3.2. Ước lượng thời gian theo PERT
2.4. Dự toán chi phí xây dựng dự án
2.4.1. Chi phí nhân công
2.4.2. Chi phí hạ tầng và thiết bị
2.4.3. Chi phí phần mềm, thư viện và công cụ
2.4.4. Tổng mức đầu tư dự kiến
2.5. Ước lượng rủi ro
2.5.1. Nhận diện và đánh giá rủi ro
2.5.2. Kế hoạch phòng ngừa và xử lý
2.6. Quản lý chất lượng phần mềm
2.6.1. Mục tiêu chất lượng
2.6.2. Quy trình đảm bảo chất lượng
2.6.3. Quy trình kiểm soát thay đổi
CHƯƠNG 3: TRIỂN KHAI CHƯƠNG TRÌNH

DANH MỤC TỪ VIẾT TẮT

Từ viết tắt Tên đầy đủ Dịch thuật
AI Artificial Intelligence Trí tuệ nhân tạo
API Application Programming Interface Giao diện lập trình ứng dụng
CPU / GPU / RAM | Central/Graphics Processing Unit / Random Access Memory | Các phần cứng máy tính cốt lõi
GUI Graphical User Interface Giao diện người dùng đồ họa
LLM Large Language Model Mô hình ngôn ngữ lớn
NLP Natural Language Processing Xử lý ngôn ngữ tự nhiên
OCR Optical Character Recognition Nhận diện ký tự quang học
PDF Portable Document Format Định dạng tài liệu di động
RPA Robotic Process Automation Tự động hóa quy trình bằng robot
Seq2Seq Sequence-to-Sequence Kiến trúc dịch tự động chuỗi sang chuỗi
UML Unified Modeling Language Ngôn ngữ mô hình hóa thống nhất

DANH MỤC HÌNH ẢNH
Hình 3.1. Biểu đồ Usecase tổng quát
Hình 3.2. Biểu đồ minh họa luồng chức năng cốt lõi: Nhận diện và xử lý OCR
Hình 3.3. Biểu đồ minh họa luồng chức năng: Chia cắt tài liệu PDF
Hình 3.4. Biểu đồ minh họa luồng chức năng: Xử lý quét văn bản hàng loạt
Hình 3.5. Biểu đồ trình tự hệ thống OCR Scanner
Hình 3.6. Biểu đồ lớp hệ thống OCR Scanner
Hình 3.7. Biểu đồ triển khai hệ thống OCR Scanner
Hình 3.8. Schema chi tiết file `config.json`
Hình 3.9. Cấu trúc một mục từ điển trong raw_dict.jsonl
Hình 3.10. Biểu đồ Usecase tổng quát 9
Hình 3.11. Biểu đồ minh họa luồng chức năng cốt lõi: Nhận diện và xử lý OCR 12
Hình 3.12. Biểu đồ minh họa luồng chức năng: Chia cắt và Gộp tài liệu 13
Hình 3.13. Biểu đồ minh họa luồng chức năng: Xử lý quét văn bản hàng loạt 14
Hình 3.14. Biểu đồ trình tự hệ thống OCR Scanner 15
Hình 3.15. Biểu đồ lớp hệ thống OCR Scanner 16
Hình 3.16. Biểu đồ triển khai hệ thống OCR Scanner 17
Hình 3.17. Schema chi tiết file `config.json’ 19
Hình 3.18. Cấu trúc một mục từ điển trong raw_dict.jsonl 19
Hình 3.19. Giao diện đối chiếu kết quả OCR Dual-panel 23
Hình 3.20. Chức năng đổi tên tệp tin hàng loạt (Batch Rename) 24
Hình 3.21. Chức năng chia tách tài liệu PDF hàng loạt 24
Hình 3.22. Logo Công ty Cổ phần Công nghệ Nhật Thiên
Hình 3.23. Công thức khoảng cách Levenshtein
Hình 3.24. Biểu đồ Gantt kế hoạch phát triển dự án OCR Scanner theo Scrum
Hình 1.1. Logo Công ty Cổ phần Công nghệ Nhật Thiên
Hình 1.2. Công thức khoảng cách Levenshtein
Hình 2.1. Biểu đồ Gantt kế hoạch phát triển dự án OCR Scanner theo Scrum

DANH MỤC BẢNG BIỂU
Bảng 3.1. Bảng cấu trúc dữ liệu vật lý
Bảng 3.2. Bảng cấu trúc dữ liệu vật lý 18
Bảng 3.3. Bảng tổng hợp so sánh hiệu năng giữa các cấu hình tích hợp. 22
Bảng 3.4. Yêu cầu chức năng
Bảng 3.5. Yêu cầu phi chức năng
Bảng dưới đây thể hiện lịch trình tổng quát của dự án theo 4 Sprint trong 8 tuần.
Bảng 3.6. Bảng phân rã công việc WBS
Bảng 3.7. Ma trận đánh giá rủi ro
Bảng 1.1. Yêu cầu chức năng
Bảng 1.2. Yêu cầu phi chức năng
Bảng dưới đây thể hiện lịch trình tổng quát của dự án theo 4 Sprint trong 8 tuần.
Bảng 2.1. Bảng phân rã công việc WBS
Bảng 2.2. Ma trận đánh giá rủi ro

LỜI CẢM ƠN
Trong suốt quá trình học tập và thực hiện báo cáo thực tập chuyên ngành "Quản trị dự án phần mềm", em đã nhận được sự quan tâm, chỉ bảo và giúp đỡ tận tình từ phía nhà trường, thầy cô và bạn bè.
Trước hết, em xin gửi lời cảm ơn chân thành tới Ban Giám hiệu, cùng toàn thể quý thầy cô Khoa Công nghệ thông tin, Trường Đại học Điện Lực. Các thầy cô đã tận tâm truyền đạt cho em những kiến thức chuyên ngành quý báu, từ nền tảng quản trị đến các khái niệm chuyên sâu về lập kế hoạch, ước lượng và quản lý chất lượng phần mềm. Đây là hành trang không thể thiếu giúp em tự tin bước vào môi trường thực tế.
Đặc biệt, em xin bày tỏ lòng biết ơn sâu sắc đến TS. Phạm Đức Hồng. Thầy đã dành nhiều thời gian, tâm huyết để trực tiếp hướng dẫn, định hướng đề tài và đóng góp những ý kiến chuyên môn xác đáng, giúp em không chỉ hoàn thiện về mặt kỹ thuật mà còn nắm vững tư duy quản trị dự án để đảm bảo dự án OCR Scanner vận hành đúng tiến độ và đạt chất lượng cao nhất.
Do thời gian thực hiện đồ án và kiến thức thực tế còn hạn chế, báo cáo chắc chắn không tránh khỏi những thiếu sót. Em rất mong nhận được sự góp ý, chỉ bảo thêm từ quý thầy cô để đề tài được hoàn thiện hơn và bản thân em có thêm kinh nghiệm cho công việc sau này.
Em xin chân thành cảm ơn!
Hà Nội, tháng 5 năm 2026
Sinh viên thực hiện

Nguyễn Hoàng Thanh Tùng

LỜI NÓI ĐẦU
Trong kỷ nguyên Cách mạng công nghiệp 4.0, chuyển đổi số không còn là một lựa chọn mà đã trở thành xu hướng tất yếu đối với mọi cơ quan, tổ chức và doanh nghiệp. Một trong những bước đi đầu tiên và quan trọng nhất của quá trình chuyển đổi số là việc số hóa hệ thống tài liệu, hồ sơ, giấy tờ hành chính đang được lưu trữ dưới dạng vật lý. Việc chuyển đổi các tài liệu này sang định dạng văn bản kỹ thuật số (text) không chỉ giúp tiết kiệm không gian lưu trữ mà còn tối ưu hóa quá trình tìm kiếm, trích xuất thông tin và quản lý tri thức.
Để giải quyết bài toán này, công nghệ Nhận dạng ký tự quang học (OCR - Optical Character Recognition) đã ra đời và phát triển mạnh mẽ. Tuy nhiên, việc triển khai một dự án phần mềm ứng dụng AI như OCR Scanner không chỉ đòi hỏi sự am hiểu về kỹ thuật mà còn yêu cầu một quy trình Quản trị dự án (Software Project Management) chặt chẽ. Việc điều phối các nguồn lực, lập kế hoạch chi tiết cho các giai đoạn phát triển, ước lượng chi phí hạ tầng GPU đắt đỏ và quản trị các rủi ro về độ chính xác của mô hình là những yếu tố quyết định sự thành bại của dự án.
Xuất phát từ nhu cầu cấp thiết đó, báo cáo thực tập tập trung vào đề tài: "Quản trị dự án xây dựng Hệ Thống Nhận dạng Và Xử Lý Văn Bản Tiếng Việt". Thay vì chỉ tập trung vào các thuật toán AI đơn thuần, báo cáo này hướng tới việc trình bày cách thức tổ chức và vận hành dự án theo một quy trình khoa học. Hệ thống OCR Scanner được xây dựng dựa trên sự tích hợp linh hoạt giữa các "Hộp đen" công nghệ (DocTR, PaddleOCR, ProtonX Nano) nhằm tối ưu hóa hiệu quả nhận dạng tiếng Việt, đồng thời được quản lý dưới các công cụ quản trị dự án chuyên nghiệp như WBS, PERT và Gantt Chart.
Mục tiêu cuối cùng của báo cáo là minh chứng cho khả năng áp dụng các kiến thức quản trị dự án vào thực tiễn, đảm bảo sản phẩm phần mềm không chỉ hoạt động tốt về mặt kỹ thuật mà còn được hoàn thành đúng thời hạn, tối ưu hóa ngân sách và đáp ứng đầy đủ các tiêu chuẩn chất lượng đặt ra.

CHƯƠNG 1: GIỚI THIỆU DỰ ÁN
1.1. Giới thiệu về đơn vị thực tập
1.1.1. Giới thiệu tổng quan đơn vị

Hình 1.1. Logo Công ty Cổ phần Công nghệ Nhật Thiên
Công ty Cổ phần Công nghệ Nhật Thiên là doanh nghiệp hoạt động trong lĩnh vực công nghệ thông tin, khoa học kỹ thuật và giải pháp chuyển đổi số, được thành lập từ năm 2011 với trụ sở đặt tại Hà Nội. Công ty tập trung phát triển các giải pháp phần mềm, hệ thống quản lý dữ liệu, thiết bị công nghệ và các dịch vụ số hóa phục vụ cho doanh nghiệp, tổ chức và cơ quan hành chính.
Trong bối cảnh chuyển đổi số đang diễn ra mạnh mẽ tại Việt Nam, Nhật Thiên định hướng phát triển các giải pháp tự động hóa quy trình xử lý tài liệu nhằm giảm sự phụ thuộc vào thao tác thủ công. Một trong những lĩnh vực được công ty chú trọng là số hóa văn bản và quản lý dữ liệu điện tử, hỗ trợ doanh nghiệp chuyển đổi từ mô hình lưu trữ giấy truyền thống sang môi trường số hiện đại.
Bên cạnh việc cung cấp các giải pháp phần mềm, công ty còn triển khai các quy trình xử lý tài liệu chuyên nghiệp bao gồm tiếp nhận hồ sơ, phân loại tài liệu, scan dữ liệu, nhập liệu, kiểm tra tính chính xác và chuẩn hóa thông tin trước khi lưu trữ hoặc bàn giao cho khách hàng. Quy trình này giúp tăng tốc độ xử lý dữ liệu, hạn chế sai sót và tiết kiệm đáng kể chi phí vận hành cho doanh nghiệp.
Với định hướng phát triển dựa trên công nghệ trí tuệ nhân tạo và tự động hóa, Công ty Cổ phần Công nghệ Nhật Thiên đang từng bước khẳng định vai trò là đơn vị hỗ trợ chuyển đổi số và số hóa dữ liệu cho nhiều tổ chức và doanh nghiệp tại Việt Nam.
1.1.2. Lĩnh vực hoạt động
Công ty hoạt động chủ yếu trong các lĩnh vực sau:
• Phát triển phần mềm quản lý doanh nghiệp.
• Cung cấp giải pháp số hóa tài liệu và dữ liệu.
• Triển khai hệ thống lưu trữ và quản lý hồ sơ điện tử.
• Cung cấp thiết bị công nghệ thông tin và giải pháp hạ tầng mạng.
• Tư vấn và triển khai giải pháp chuyển đổi số cho doanh nghiệp.
• Xây dựng các hệ thống ứng dụng tích hợp trí tuệ nhân tạo trong xử lý dữ liệu.
Trong đó, lĩnh vực số hóa tài liệu và xử lý dữ liệu bằng AI đang là một trong những hướng phát triển trọng tâm của công ty nhằm đáp ứng nhu cầu thực tiễn ngày càng lớn từ doanh nghiệp và tổ chức hành chính.
1.1.3. Vai trò của công nghệ thông tin trong doanh nghiệp
Công nghệ thông tin đóng vai trò cốt lõi trong hoạt động vận hành và phát triển của doanh nghiệp. Việc ứng dụng CNTT giúp doanh nghiệp:
• Tự động hóa các quy trình xử lý dữ liệu.
• Tăng tốc độ lưu trữ và truy xuất thông tin.
• Giảm chi phí nhân sự và chi phí vận hành.
• Nâng cao độ chính xác trong quản lý hồ sơ.
• Hỗ trợ bảo mật và sao lưu dữ liệu hiệu quả.
• Tăng khả năng tích hợp và chia sẻ dữ liệu giữa các hệ thống.
Đặc biệt, trong lĩnh vực số hóa tài liệu, công nghệ OCR kết hợp AI giúp doanh nghiệp giảm đáng kể thời gian nhập liệu thủ công, đồng thời nâng cao hiệu quả quản lý thông tin trong môi trường số.
1.2. Tổng quan bài toán (Vấn đề thực tiễn số hóa tài liệu)
1.2.1. Thực trạng số hóa tài liệu hiện nay
Trong quá trình chuyển đổi số hiện nay, nhiều doanh nghiệp và tổ chức vẫn đang lưu trữ khối lượng lớn tài liệu dưới dạng giấy như hợp đồng, hồ sơ nhân sự, hóa đơn, công văn và biểu mẫu hành chính. Việc quản lý dữ liệu theo phương pháp truyền thống gây ra nhiều khó khăn trong quá trình lưu trữ, tra cứu và xử lý thông tin.
Hiện nay, phần lớn dữ liệu giấy vẫn được nhập liệu bằng phương pháp thủ công. Nhân viên phải đọc nội dung từ tài liệu scan hoặc ảnh chụp rồi nhập lại bằng tay vào hệ thống quản lý. Quy trình này tồn tại nhiều hạn chế như:
• Tốn nhiều thời gian xử lý.
• Chi phí nhân lực cao.
• Dễ phát sinh sai sót dữ liệu.
• Khó kiểm soát tính đồng nhất của thông tin.
• Hiệu suất thấp khi xử lý số lượng lớn tài liệu.
Đối với các doanh nghiệp có hàng nghìn hồ sơ cần số hóa mỗi ngày, phương pháp nhập liệu thủ công gần như không còn phù hợp do tốc độ xử lý chậm và khó mở rộng quy mô.
1.2.2. Những khó khăn trong OCR tiếng Việt
Mặc dù công nghệ OCR hiện nay đã phát triển mạnh, tuy nhiên việc nhận diện văn bản tiếng Việt vẫn còn gặp nhiều thách thức do đặc thù ngôn ngữ có dấu và cấu trúc ký tự phức tạp.
• Một số vấn đề phổ biến trong OCR tiếng Việt gồm:
• Nhận diện sai dấu tiếng Việt.
• Mất dấu hoặc nhầm dấu thanh.
• Nhầm lẫn giữa các ký tự tương đồng như “0/O”, “1/l/I”.
• Khó xử lý tài liệu scan mờ hoặc bị nhiễu.
• Chất lượng ảnh đầu vào không đồng đều.
• Sai lệch bố cục văn bản khi OCR PDF nhiều cột hoặc biểu mẫu.
Ngoài ra, các hệ thống OCR thông thường chủ yếu tập trung vào nhận diện ký tự mà chưa xử lý tốt ngữ cảnh tiếng Việt. Điều này dẫn đến việc văn bản đầu ra dù đọc được nhưng vẫn chứa nhiều lỗi chính tả hoặc sai nghĩa, gây khó khăn cho quá trình sử dụng thực tế.
1.2.3. Nhu cầu xây dựng hệ thống OCR Scanner
Từ những vấn đề thực tiễn trên, nhu cầu xây dựng một hệ thống OCR Scanner hỗ trợ tiếng Việt có khả năng tự động hóa cao là rất cần thiết.
• Hệ thống cần đáp ứng các yêu cầu như:
• Tự động nhận diện văn bản từ ảnh và PDF.
• Hỗ trợ xử lý hàng loạt tài liệu.
• Tăng độ chính xác cho OCR tiếng Việt.
• Giảm thời gian xử lý dữ liệu.
• Chuẩn hóa và lưu trữ tài liệu điện tử.
• Hỗ trợ hậu xử lý và sửa lỗi chính tả bằng AI.
• Tăng hiệu quả làm việc cho doanh nghiệp và nhân viên hành chính.
Từ đó, đề tài “Hệ thống Nhận diện và Xử lý Văn bản Tiếng Việt Tích hợp Đa Engine OCR” được xây dựng nhằm giải quyết bài toán số hóa tài liệu trong môi trường thực tế.
1.3. Xác lập dự án
1.3.1. Mục tiêu của hệ thống
Xây dựng một ứng dụng Desktop hỗ trợ số hóa tài liệu tiếng Việt bằng công nghệ OCR kết hợp AI nhằm nâng cao độ chính xác nhận diện văn bản và tự động hóa quy trình xử lý dữ liệu.
Mục tiêu cụ thể:
• Xây dựng giao diện người dùng trực quan và dễ sử dụng.
• Hỗ trợ OCR cho hình ảnh và tài liệu PDF.
• Tích hợp đồng thời nhiều OCR Engine như DocTR và PaddleOCR.
• Tích hợp mô hình AI hỗ trợ sửa lỗi tiếng Việt theo ngữ cảnh.
• Xây dựng chức năng Batch OCR xử lý hàng loạt tài liệu.
• Phát triển công cụ Batch Rename hỗ trợ đổi tên file tự động.
• Hỗ trợ tách và xử lý PDF nhiều trang.
• Thiết kế giao diện đối chiếu giữa tài liệu gốc và kết quả OCR.
• Tăng khả năng mở rộng và tích hợp thêm AI Engine trong tương lai.
1.3.2. Phạm vi của dự án
• Hệ thống tập trung phát triển các chức năng chính gồm:
o OCR tài liệu ảnh.
o OCR file PDF.
o Batch Processing.
o Batch Rename.
o PDF Split.
o Hậu xử lý tiếng Việt bằng AI.
o Xuất dữ liệu kết quả ra file.
• Hệ thống hướng tới các nhóm người dùng như:
o Nhân viên hành chính.
o Nhân viên văn phòng.
o Sinh viên và giảng viên.
o Doanh nghiệp có nhu cầu số hóa tài liệu.
Người dùng không cần kiến thức lập trình vẫn có thể sử dụng hệ thống thông qua giao diện trực quan.
1.3.3. Đánh giá tính khả thi của hệ thống
Dự án được đánh giá có tính khả thi cao cả về công nghệ lẫn khả năng triển khai thực tế.
Về công nghệ, hệ sinh thái Python hiện nay cung cấp đầy đủ các thư viện phục vụ cho xử lý ảnh, OCR, AI và xây dựng giao diện Desktop. Các thư viện như OpenCV, PaddleOCR, DocTR, Transformers và CustomTkinter đều được phát triển mạnh và có tài liệu hỗ trợ đầy đủ.
Về mặt kỹ thuật, các mô hình OCR và NLP hiện nay đều được phát hành dưới dạng mã nguồn mở, cho phép tích hợp trực tiếp vào hệ thống thông qua PyTorch hoặc HuggingFace. Điều này giúp giảm đáng kể chi phí triển khai và phù hợp với phạm vi của một đồ án thực tế.
Ngoài ra, hệ thống được thiết kế theo kiến trúc module hóa giúp dễ dàng mở rộng thêm OCR Engine hoặc AI Model mới trong tương lai mà không làm ảnh hưởng đến kiến trúc tổng thể của chương trình.
1.4. Phân tích yêu cầu hệ thống
1.4.1. Yêu cầu chức năng
Bảng 1.1. Yêu cầu chức năng
ID Chức năng Mô tả
FR-01 OCR ảnh Nhận diện văn bản từ ảnh
FR-02 OCR PDF Trích xuất văn bản từ file PDF
FR-03 Batch OCR Xử lý OCR hàng loạt
FR-04 Batch Rename Đổi tên file tự động
FR-05 Split PDF Tách file PDF
FR-06 AI Correction Sửa lỗi tiếng Việt bằng AI
FR-07 Export File Xuất kết quả ra TXT/JSON

Ngoài ra, hệ thống còn phải hỗ trợ:
• Hiển thị kết quả OCR song song với tài liệu gốc.
• Cho phép chỉnh sửa văn bản thủ công.
• Hỗ trợ lựa chọn OCR Engine phù hợp.
1.4.2. Yêu cầu phi chức năng
Bảng 1.2. Yêu cầu phi chức năng
ID Yêu cầu Mô tả
NFR-01 Hiệu năng OCR xử lý nhanh và ổn định
NFR-02 Giao diện Dễ sử dụng, trực quan
NFR-03 Khả năng mở rộng Dễ tích hợp module mới
NFR-04 Độ ổn định Không crash khi xử lý batch
NFR-05 Bảo mật Dữ liệu xử lý nội bộ
NFR-06 Khả năng bảo trì Dễ nâng cấp và sửa lỗi

Hệ thống cần đảm bảo thời gian xử lý phù hợp, hạn chế treo giao diện và có khả năng xử lý lỗi khi các OCR Engine gặp sự cố.
1.5. Cơ sở lý thuyết và công nghệ lõi
Để xây dựng hệ thống OCR Scanner tiếng Việt có độ chính xác cao, dự án áp dụng nhiều cơ sở lý thuyết và công nghệ quan trọng.
1.5.1. Khoảng cách Levenshtein

Hình 1.2. Công thức khoảng cách Levenshtein
Thuật toán Levenshtein Distance dùng để đo mức độ khác biệt giữa hai chuỗi ký tự bằng số phép biến đổi tối thiểu gồm thêm, xóa hoặc thay thế ký tự. Đây là nền tảng quan trọng cho hệ thống kiểm tra và sửa lỗi chính tả tiếng Việt.
1.5.2. Thuật toán SymSpell
Thuật toán SymSpell là phiên bản tối ưu của phương pháp sửa lỗi dựa trên khoảng cách Levenshtein. Thay vì tìm kiếm toàn bộ từ điển, SymSpell sinh trước các biến thể xóa ký tự để giảm đáng kể thời gian tìm kiếm và tăng tốc độ xử lý văn bản.
Thuật toán này phù hợp với hệ thống OCR do có khả năng sửa lỗi nhanh khi xử lý số lượng lớn tài liệu.
1.5.3. Mô hình Seq2Seq trong xử lý ngôn ngữ
Mô hình Sequence-to-Sequence (Seq2Seq) là kiến trúc học sâu được sử dụng trong xử lý ngôn ngữ tự nhiên.
Mô hình có khả năng:
• Phân tích ngữ cảnh câu.
• Sửa lỗi chính tả theo ngữ nghĩa.
• Khôi phục câu tiếng Việt hoàn chỉnh từ dữ liệu OCR bị lỗi.
Trong hệ thống, mô hình AI ProtonX Nano được sử dụng để cải thiện chất lượng văn bản đầu ra sau OCR.
1.5.4. Kiến trúc Plugin và Singleton
Hệ thống áp dụng:
• Singleton Pattern để đảm bảo các mô hình AI chỉ khởi tạo một lần nhằm tiết kiệm RAM và VRAM.
• Plugin Pattern để module hóa các OCR Engine, giúp dễ dàng tích hợp thêm công nghệ mới trong tương lai.
Kiến trúc này giúp hệ thống tăng khả năng mở rộng và giảm phụ thuộc giữa các module.
1.5.5. Biểu thức chính quy (Regex)
Regex được sử dụng để:
• Kiểm tra định dạng chuỗi.
• Trích xuất dữ liệu từ văn bản.
• Xử lý Batch Rename.
• Nhận diện mẫu mã hồ sơ, ngày tháng và ký hiệu tài liệu.
Regex đóng vai trò quan trọng trong các công cụ xử lý file và chuẩn hóa dữ liệu của hệ thống.  
CHƯƠNG 2: QUẢN LÝ DỰ ÁN
THIẾT KẾ HỆ THỐNG
2.1. Mô hình phát triển phần mềm
2.1.1. Giới thiệu mô hình Scrum
Dự án OCR Scanner được quản lý theo mô hình Scrum, một khung làm việc thuộc nhóm Agile, phù hợp với các dự án phần mềm có yêu cầu thay đổi linh hoạt và cần kiểm thử thường xuyên. Scrum chia quá trình phát triển thành các vòng lặp ngắn gọi là Sprint. Mỗi Sprint tập trung hoàn thành một nhóm chức năng cụ thể, sau đó tiến hành kiểm thử, đánh giá kết quả và điều chỉnh kế hoạch cho Sprint tiếp theo.
Đối với hệ thống nhận dạng và xử lý văn bản tiếng Việt, việc áp dụng Scrum giúp giảm rủi ro trong quá trình tích hợp các công nghệ AI như DocTR, PaddleOCR và ProtonX Nano. Các module như OCR ảnh, OCR PDF, Batch Rename, Split PDF, PDF to Word, đánh số tệp tin và hậu xử lý tiếng Việt bằng AI có thể được chia nhỏ để phát triển, kiểm thử và tích hợp theo từng Sprint.
2.1.2. Lý do lựa chọn Scrum cho dự án OCR Scanner
Việc lựa chọn mô hình Incremental kết hợp Agile xuất phát từ các nguyên nhân sau:
• Giảm thiểu rủi ro kỹ thuật: Các thư viện AI như DocTR, PaddleOCR hay ProtonX Nano đều có khả năng phát sinh lỗi tương thích GPU, CUDA hoặc xung đột môi trường. Việc phát triển theo từng giai đoạn giúp phát hiện lỗi sớm và cô lập lỗi hiệu quả hơn.
• Kiểm thử liên tục: Hệ thống có thể kiểm thử từng module ngay khi hoàn thành thay vì chờ toàn bộ dự án kết thúc. Điều này giúp:
o Phát hiện bug sớm.
o Giảm chi phí sửa lỗi.
o Tăng độ ổn định của phần mềm.
• Dễ mở rộng hệ thống: Kiến trúc Incremental giúp dễ dàng tích hợp thêm:
o OCR Engine mới.
o AI Model mới.
o Các công cụ File Tools mới.
o Module xử lý dữ liệu mới.
o Mà không ảnh hưởng đến kiến trúc tổng thể.
• Quản lý tiến độ linh hoạt: Một số module như:
o Batch Rename.
o PDF Split.
o Core GUI.
Có thể phát triển song song với quá trình tinh chỉnh AI OCR, giúp tối ưu thời gian triển khai dự án.
2.1.3. Vai trò Scrum trong dự án
Vai trò Scrum Người đảm nhiệm Trách nhiệm
Product Owner Đại diện yêu cầu nghiệp vụ / đơn vị thực tập Xác định nhu cầu số hóa tài liệu, ưu tiên chức năng và đánh giá sản phẩm sau mỗi Sprint.
Scrum Master Sinh viên thực hiện Lập kế hoạch Sprint, theo dõi tiến độ, ghi nhận rủi ro và điều phối quá trình thực hiện.
Development Team Sinh viên thực hiện Phân tích yêu cầu, thiết kế, lập trình, tích hợp OCR/AI, kiểm thử và hoàn thiện báo cáo.

2.1.4. Product Backlog của dự án
Mã User Story / Chức năng Độ ưu tiên Ghi chú
PB01 Là người dùng, tôi muốn OCR ảnh để trích xuất văn bản từ tài liệu scan. Cao Chức năng lõi
PB02 Là người dùng, tôi muốn OCR file PDF để xử lý tài liệu nhiều trang. Cao Chức năng lõi
PB03 Là người dùng, tôi muốn xử lý OCR hàng loạt để tiết kiệm thời gian. Cao Batch OCR
PB04 Là người dùng, tôi muốn sửa lỗi tiếng Việt bằng AI để tăng độ chính xác văn bản. Cao ProtonX / SymSpell
PB05 Là người dùng, tôi muốn xem đối chiếu kết quả OCR với tài liệu gốc. Cao Dual-panel
PB06 Là người dùng, tôi muốn đổi tên tệp hàng loạt để chuẩn hóa hồ sơ. Trung bình Batch Rename
PB07 Là người dùng, tôi muốn tách file PDF để xử lý từng phần tài liệu. Trung bình Split PDF
PB08 Là người dùng, tôi muốn chuyển PDF sang Word để chỉnh sửa nội dung. Trung bình PDF to Word
PB09 Là người dùng, tôi muốn đánh số thứ tự file để quản lý tài liệu theo lô. Trung bình Numbering
PB10 Là quản trị viên, tôi muốn cấu hình OCR Engine và tham số hệ thống. Trung bình config.json
PB11 Là người dùng, tôi muốn xuất kết quả ra TXT/JSON để lưu trữ và sử dụng lại. Trung bình Export
PB12 Là người dùng, tôi muốn hệ thống không bị treo khi xử lý file lớn. Cao Yêu cầu chất lượng

2.2. Kế hoạch thực hiện dự án theo Sprint
2.2.1. Các mốc thời gian chính
Dự án được lên kế hoạch thực hiện trong 8 tuần, chia thành 4 Sprint. Mỗi Sprint kéo dài 2 tuần, tập trung vào một nhóm chức năng cụ thể và kết thúc bằng hoạt động kiểm thử, đánh giá kết quả bàn giao.
2.2.2. Sprint Backlog và kế hoạch thực hiện
Sprint Thời gian Mục tiêu Sprint Kết quả cần đạt
Sprint 1 Tuần 1-2 Khảo sát, xác định yêu cầu, thiết kế kiến trúc và lập Product Backlog. Tài liệu yêu cầu, phạm vi dự án, kiến trúc tổng quan, Product Backlog.
Sprint 2 Tuần 3-4 Xây dựng giao diện Desktop và module File Tools cơ bản. Core GUI, Batch Rename, Split PDF, PDF to Word, Numbering.
Sprint 3 Tuần 5-6 Tích hợp OCR Engine và AI hậu xử lý tiếng Việt. DocTR, PaddleOCR, fast_spell_checker.py, ProtonX Nano, cấu hình config.json.
Sprint 4 Tuần 7-8 Kiểm thử, tối ưu hiệu năng, đóng gói và hoàn thiện báo cáo. Bộ test, kết quả thực nghiệm, bản đóng gói ứng dụng, báo cáo hoàn chỉnh.

2.2.3. Sprint Review và Sprint Retrospective
Sprint Kết quả đạt được Vấn đề phát sinh Điều chỉnh sau Sprint
Sprint 1 Hoàn thành khảo sát, mục tiêu, phạm vi và kiến trúc sơ bộ. Phạm vi ban đầu có chức năng chưa triển khai trong code. Điều chỉnh phạm vi chính thức, chỉ giữ Split PDF đúng với code thực tế.
Sprint 2 Hoàn thành giao diện và các công cụ file cơ bản. Cần bổ sung mô tả PDF to Word và Numbering trong báo cáo. Bổ sung mô tả ở Chương 3 để phản ánh đúng chức năng thực tế.
Sprint 3 Tích hợp OCR Engine và hậu xử lý tiếng Việt. Tên module SymSpell trong báo cáo chưa đúng với code. Sửa thành fast_spell_checker.py và cập nhật đường dẫn.
Sprint 4 Hoàn thành kiểm thử, tối ưu và báo cáo. Một số mục lục, hình ảnh, đường dẫn config chưa thống nhất. Cập nhật mục lục, sửa đường dẫn config.json và đánh lại số hình/bảng.

2.2.4. Biểu đồ Gantt
Bảng dưới đây thể hiện lịch trình tổng quát của dự án theo 4 Sprint trong 8 tuần.

Hình 2.1. Biểu đồ Gantt kế hoạch phát triển dự án OCR Scanner theo Scrum
2.3. Cấu trúc phân rã công việc và ước lượng thời gian
2.3.1. Bảng phân rã công việc WBS
Bảng 2.1. Bảng phân rã công việc WBS
STT Giai đoạn Công việc Mã CV Công việc trước
1 Khảo sát Khảo sát OCR tiếng Việt KS.1 -
2 Khảo sát Phân tích yêu cầu hệ thống KS.2 KS.1
3 Thiết kế Thiết kế UI/UX TK.1 KS.2
4 Thiết kế Thiết kế kiến trúc Plugin AI TK.2 TK.1
5 Xây dựng Phát triển Core GUI XD.1 TK.2
6 Xây dựng Tích hợp DocTR và PaddleOCR XD.2 XD.1
7 Xây dựng Tích hợp SymSpell và ProtonX XD.3 XD.2
8 Xây dựng Xây dựng Batch Rename, Split PDF, PDF to Word, Numbering XD.4 TK.2
9 Kiểm thử Functional Testing KT.1 XD.3, XD.4
10 Kiểm thử Performance Testing KT.2 KT.1
11 Bàn giao Đóng gói và hoàn thiện báo cáo BG.1 KT.2

2.3.2. Ước lượng thời gian theo PERT
Dự án sử dụng kỹ thuật PERT để ước lượng thời gian thực hiện công việc theo công thức EST = (O + 4M + P) / 6, trong đó O là thời gian lạc quan, M là thời gian khả thi nhất và P là thời gian bi quan.
Mã CV O M P EST (ngày)
KS.1 2 3 5 3.17
KS.2 2 4 6 4.00
TK.1 3 5 7 5.00
TK.2 4 6 8 6.00
XD.1 5 7 10 7.17
XD.2 7 10 14 10.17
XD.3 6 9 12 9.00
XD.4 4 5 8 5.33
KT.1 4 6 9 6.17
KT.2 3 5 7 5.00
BG.1 2 3 5 3.17
Tổng ~64 ngày
2.4. Dự toán chi phí xây dựng dự án
Dự toán chi phí được xây dựng nhằm xác định nguồn lực cần thiết để triển khai hệ thống OCR Scanner trong phạm vi 8 tuần. Chi phí bao gồm chi phí nhân công, chi phí thiết bị/hạ tầng, chi phí công cụ phần mềm và chi phí dự phòng rủi ro.
2.4.1. Chi phí nhân công
Chi phí nhân công
Hạng mục Số lượng Đơn giá Thời gian Thành tiền
Phân tích yêu cầu và thiết kế hệ thống 1 150.000 VNĐ/giờ 40 giờ 6.000.000 VNĐ
Lập trình giao diện Desktop 1 150.000 VNĐ/giờ 45 giờ 6.750.000 VNĐ
Tích hợp OCR Engine 1 150.000 VNĐ/giờ 50 giờ 7.500.000 VNĐ
Tích hợp AI hậu xử lý tiếng Việt 1 150.000 VNĐ/giờ 40 giờ 6.000.000 VNĐ
Xây dựng File Tools 1 150.000 VNĐ/giờ 30 giờ 4.500.000 VNĐ
Kiểm thử và tối ưu hiệu năng 1 150.000 VNĐ/giờ 30 giờ 4.500.000 VNĐ
Viết tài liệu và hoàn thiện báo cáo 1 150.000 VNĐ/giờ 25 giờ 3.750.000 VNĐ
Tổng chi phí nhân công 260 giờ 39.000.000 VNĐ

2.4.2. Chi phí hạ tầng và thiết bị
Chi phí hạ tầng và thiết bị
Hạng mục Số lượng Chi phí dự kiến Ghi chú
Máy tính/Workstation có GPU 1 2.000.000 VNĐ Chi phí khấu hao trong thời gian dự án
Dung lượng lưu trữ tài liệu thử nghiệm 1 300.000 VNĐ Lưu file ảnh/PDF test
Chi phí điện năng vận hành thử nghiệm 1 300.000 VNĐ Chạy OCR/AI cục bộ
Thiết bị scan/tạo dữ liệu đầu vào 1 500.000 VNĐ Khấu hao/thuê/mượn thiết bị
Tổng chi phí hạ tầng 3.100.000 VNĐ

2.4.3. Chi phí phần mềm, thư viện và công cụ
Chi phí phần mềm, thư viện và công cụ
Hạng mục Chi phí Ghi chú
Python 0 VNĐ Mã nguồn mở
CustomTkinter 0 VNĐ Mã nguồn mở
PyTorch 0 VNĐ Mã nguồn mở
PaddleOCR / PaddlePaddle 0 VNĐ Mã nguồn mở
DocTR 0 VNĐ Mã nguồn mở
Transformers / HuggingFace 0 VNĐ Mã nguồn mở
Git / GitHub 0 VNĐ Quản lý mã nguồn
Công cụ đóng gói ứng dụng 0 VNĐ Có thể dùng PyInstaller
Tổng chi phí phần mềm 0 VNĐ

2.4.4. Tổng mức đầu tư dự kiến
Tổng mức đầu tư dự kiến
Nhóm chi phí Thành tiền
Chi phí nhân công 39.000.000 VNĐ
Chi phí hạ tầng và thiết bị 3.100.000 VNĐ
Chi phí phần mềm và công cụ 0 VNĐ
Chi phí dự phòng 10% 4.210.000 VNĐ
Tổng dự toán 46.310.000 VNĐ

Tổng chi phí dự kiến để xây dựng hệ thống OCR Scanner là 46.310.000 VNĐ. Trong đó, chi phí nhân công chiếm tỷ trọng lớn nhất do dự án yêu cầu phân tích, lập trình, tích hợp và kiểm thử nhiều module AI/OCR. Các thư viện phần mềm sử dụng chủ yếu là mã nguồn mở nên giúp giảm đáng kể chi phí bản quyền. Chi phí dự phòng 10% được bổ sung nhằm xử lý các rủi ro phát sinh như lỗi tương thích thư viện, yêu cầu tối ưu GPU hoặc kéo dài thời gian kiểm thử.
2.5. Ước lượng rủi ro
2.5.1. Nhận diện và đánh giá rủi ro
Bảng 2.2. Ma trận đánh giá rủi ro
ID Rủi ro Ảnh hưởng Xác suất Điểm Phân loại
R1 GPU OOM khi load AI 5 4 20 Cao
R2 OCR mất dấu tiếng Việt 5 3 15 Cao
R3 Conflict thư viện AI 4 4 16 Cao
R4 Freeze GUI khi xử lý file lớn 4 3 12 Trung bình
R5 Chậm tiến độ nghiên cứu AI 3 3 9 Trung bình

2.5.2. Kế hoạch phòng ngừa và xử lý
• GPU OOM: Fallback CPU + Singleton Pattern.
• OCR mất dấu: ProtonX Nano + SymSpell.
• Conflict thư viện: Virtual Environment.
• Freeze GUI: Multi-threading.
• Chậm tiến độ: Chia Increment nhỏ để kiểm thử sớm.
Quản trị rủi ro được thực hiện xuyên suốt vòng đời dự án nhằm giảm thiểu ảnh hưởng đến tiến độ và chất lượng hệ thống.
2.6. Quản lý chất lượng phần mềm
2.6.1. Mục tiêu chất lượng
Hệ thống hướng tới các tiêu chí chất lượng sau:
• OCR Accuracy ≥ 90%.
• Không crash khi xử lý Batch OCR.
• Giao diện phản hồi ổn định.
• Tốc độ OCR dưới 5 giây/trang khi dùng GPU.
• Đảm bảo tính toàn vẹn dữ liệu đầu ra.
2.6.2. Quy trình đảm bảo chất lượng
Quy trình QA của dự án bao gồm:
• Unit Testing: Kiểm thử từng module độc lập:
o OCR Engine.
o File Tools.
o AI Correction.
o PDF Processing.
• Functional Testing: Kiểm tra:
o Luồng xử lý OCR.
o Kết quả Batch Processing.
o Chức năng Rename/Split PDF.
o Export dữ liệu.
• Performance Testing: Đánh giá:
o Tốc độ OCR.
o Mức sử dụng RAM/VRAM.
o Khả năng xử lý nhiều file liên tục.
2.6.3. Quy trình kiểm soát thay đổi
Dự án áp dụng các phương pháp kiểm soát thay đổi gồm:
• Quản lý source code bằng Git.
• Backup source định kỳ.
• Theo dõi bug theo từng phiên bản.
• Tách branch riêng cho từng tính năng.
• Kiểm thử trước khi merge source.
Quy trình này giúp hạn chế lỗi phát sinh khi cập nhật hệ thống và tăng khả năng bảo trì phần mềm.

CHƯƠNG 3: TRIỂN KHAI CHƯƠNG TRÌNH
