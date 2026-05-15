BỘ CÔNG THƯƠNG
TRƯỜNG ĐẠI HỌC ĐIỆN LỰC
KHOA CÔNG NGHỆ THÔNG TIN

THỰC TẬP HỆ THỐNG THÔNG TIN TÍCH HỢP
TÍCH HỢP HỆ THỐNG THÔNG BÁO QUA EMAIL BREVO VÀ TELEGRAM BOT CHO HỆ THỐNG QUẢN TRỊ DOANH NGHIỆP ERP INNOVISION
Giảng viên hướng dẫn : PHẠM QUANG HUY
Sinh viên thực hiện : CẤN ANH QUÂN
Ngành : CÔNG NGHỆ THÔNG TIN
Chuyên ngành : CÔNG NGHỆ PHẦN MỀM
Lớp : D17CNPM4
Khóa : 2022-2027

ĐỀ CƯƠNG THỰC TẬP MÔN
THỰC TẬP HỆ THỐNG THÔNG TIN TÍCH HỢP

1. Tên đề tài: Tích Hợp Hệ Thống Thông Báo Qua Email (Brevo) Và Telegram Bot Cho Nền Tảng Quản Trị Doanh Nghiệp Erp Innovision
2. Sinh viên thực hiện:
   Họ và tên: Cấn Anh Quân MSSV: 22810310260
   Số điện thoại: 0373089951 Email: phimanhh85@gmail.com
   Vị trí thực tập: Full stack developer
3. Giảng viên hướng dẫn:
   Họ và tên: Phạm Quang Huy Học vị:
   Số điện thoại: Email:
   Đơn vị công tác: Khoa Công Nghệ Thông Tin trường Đại học Điện Lực.
4. Mô tả tóm tắt đề tài
   Đề tài tập trung nghiên cứu và triển khai tích hợp hai hệ thống thông báo bên thứ ba vào nền tảng ERP Innovision: (1) Brevo (Sendinblue) để gửi email giao dịch và thông báo sự kiện, và (2) Telegram Bot API để gửi thông báo tức thời. Mỗi hệ thống tích hợp được coi là một black-box – hệ thống chỉ tương tác thông qua giao thức HTTPS và API chuẩn được công bố, không can thiệp vào cơ sở hạ tầng nội bộ của chúng. Trong đó, tích hợp Brevo là trọng tâm chính của đề tài với phạm vi ứng dụng rộng nhất trong hệ thống.
5. Nội dung báo cáo thực tập:
   Chương 1. TỔNG QUAN VÀ KHẢO SÁT DỰ ÁN
   1.1. Vấn đề cần giải quyết
   • Hệ thống thông báo hiện tại lạc hậu: ERP Innovision trước đó sử dụng SMTP (Nodemailer) truyền thống, dẫn đến tỷ lệ email bị rơi vào hòm thư rác (spam) cao và không thể theo dõi trạng thái gửi.
   • Thiếu kênh tương tác thời gian thực: Người dùng phải chủ động truy cập website để kiểm tra tiến độ công việc (duyệt phép, task mới), gây chậm trễ trong quy trình vận hành doanh nghiệp.
   • Người dùng bị làm phiền: Hệ thống gửi thông báo tràn lan mà không có cơ chế cho phép nhân viên tự bật/tắt các loại thông báo theo nhu cầu cá nhân.
   1.2. Tại sao cần giải quyết?
   • Nâng cao tính chuyên nghiệp: Sử dụng email template chuẩn HTML giúp tăng uy tín thương hiệu.
   • Tối ưu hóa vận hành: Thông báo Telegram giúp nhân viên nhận tin tức ngay lập tức trên điện thoại, giảm thời gian phản hồi.
   • Tuân thủ trải nghiệm người dùng (UX): Cung cấp quyền kiểm soát thông báo giúp giảm tỷ lệ "ô nhiễm" thông tin cho nhân viên.
   1.3. Tổng quan giải pháp
   • Tiếp cận tích hợp Black-box: Coi Brevo và Telegram là các hệ thống độc lập, tương tác thuần túy qua giao thức HTTPS/REST API.
   • Kiến trúc Module hóa: Xây dựng các Service chuyên biệt (brevo.service.js, telegram.service.js) và một bộ điều phối trung tâm (notifications.service.js) để quản lý logic.
   Chương 2. PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG
   2.1. Cơ sở kiến thức liên quan
   • RESTful API & HTTPS: Nền tảng giao tiếp giữa ERP và các dịch vụ bên thứ ba.
   • Mô hình Black-box Integration: Giúp hệ thống không phụ thuộc vào cấu trúc bên trong của đối tác, dễ dàng bảo trì và thay thế.
   • Node.js & Express: Môi trường runtime và framework xử lý logic phía Backend.
   2.2. Chi tiết giải pháp kỹ thuật
   • Tích hợp Brevo Email API:
   o Sử dụng API Key để xác thực.
   o Hàm sendEmail xây dựng nội dung từ Template HTML với inline CSS để đảm bảo hiển thị chuẩn trên mọi thiết bị.
   • Tích hợp Telegram Bot API:
   o Cơ chế kết nối tài khoản qua Deep Link (/start {token}) giúp định danh người dùng ERP trên Telegram một cách an toàn.
   o Sử dụng Webhook để nhận phản hồi từ người dùng về server ERP.
   • Hệ thống Dispatcher & Filter:
   o Kiểm tra bảng UserEmailNotificationSetting và UserTelegramSetting trước khi gửi.
   o Sử dụng cơ chế Fire-and-forget để việc gửi thông báo không làm chậm tiến trình nghiệp vụ chính của người dùng.
   Chương 3. XÂY DỰNG HỆ THỐNG
   3.1. Cài đặt hệ thống
   • Môi trường: Cấu hình biến môi trường trong file .env (API Keys, Bot Token, Webhook Secret).
   • Database: Thực hiện migration Prisma để tạo các bảng lưu trữ cài đặt thông báo cá nhân.
   • Frontend: Xây dựng giao diện Toggle trên React để người dùng tùy chỉnh 19 loại sự kiện thông báo.
   3.2. Demo kết quả
   • Kịch bản 1: Quản trị viên tạo tài khoản mới -> Hệ thống gửi email thiết lập mật khẩu qua Brevo thành công.
   • Kịch bản 2: Nhân viên nhấn link kết nối Telegram -> Bot xác nhận và bắt đầu gửi thông báo duyệt phép.
   • Kịch bản 3: Người dùng tắt thông báo "Tăng ca" trên Email nhưng vẫn giữ trên Telegram -> Hệ thống thực hiện đúng bộ lọc đã cài đặt.
   Kết luận và hướng nghiên cứu
6. Những kết quả đạt được
   • Hoàn thành tích hợp đa kênh (Email & Telegram) vào nền tảng ERP.
   • Giải quyết triệt để vấn đề email bị spam và thiếu thông báo tức thời.
   • Hệ thống có khả năng mở rộng cao (dễ dàng thêm kênh Zalo, SMS trong tương lai).
7. Những hạn chế và hướng phát triển
   • Hạn chế: Chưa có cơ chế xử lý hàng đợi (Queue) khi gửi số lượng lớn email cùng lúc; chưa theo dõi được tỷ lệ mở email (Open rate) ngay trên ERP.
   • Hướng phát triển:
   o Tích hợp BullMQ hoặc RabbitMQ để quản lý hàng đợi gửi tin chuyên nghiệp hơn.
   o Xây dựng Dashboard thống kê hiệu quả thông báo (tỷ lệ thành công, tỷ lệ phản hồi từ người dùng).
   Giảng viên hướng dẫn
   (Ký, Ghi rõ họ tên) Sinh viên thực hiện
   (Ký, Ghi rõ họ tên)

ĐÁNH GIÁ ĐỒ ÁN THỰC TẬP MÔN HỆ THỐNG THÔNG TIN TÍCH HỢP
(Dành cho cán bộ hướng dẫn tại doanh nghiệp)

Họ và tên cán bộ hướng dẫn: …………………………………………………………
Đơn vị công tác: ..……………………………………………………………………..
Họ và tên sinh viên: …………………………………………………………………..
Mã sinh viên: ……………………… Lớp: …………………
Thời gian: Từ ….. đến …….
Tiêu chí đánh giá:
Tiêu chí
đánh giá Yếu (0 - 39%) Trung Bình (40 - 54%) Khá (55 - 69%) Giỏi (70 - 84%) Xuất sắc (85 - 100%) Điểm tối đa Điểm (lẻ đến 0.25)

1.  Ý thức, thái độ 5.0
    1.1 Chấp hành nội quy của đơn vị Không chấp hành các nội quy, quy chế của đơn vị Thường xuyên vi phạm nội quy, quy chế của đơn vị Có vi phạm một vài nội quy, quy chế của đơn vị Chấp hành nội quy, quy chế của đơn vị Chấp hành tốt nội quy, quy chế của đơn vị 1.0
    1.2 Thái độ làm việc Rất thụ động với công việc được giao Thụ động với công việc được giao Hoàn thành công việc được giao Tích cực đối với công việc được giao Rất tích cực đối với công việc được giao 1.0
    1.3 Ý thức học hỏi Không có thái độ học hỏi Rất ít học hỏi và tiếp thu thêm kiến thức mới Có thái độ học hỏi và tiếp thu thêm kiến thức mới Tích cực học hỏi, tiếp thu thêm kiến thức Rất tích cực học hỏi, tiếp thu thêm các kiến thức mới 1.0
    1.4 Tinh thần đồng đội Không có thái độ hợp tác trong làm việc nhóm Có thái độ chưa tích cực trong các hoạt động nhóm Hoàn thành các công việc trong nhóm Hoàn thành tốt vai trò trong nhóm Luôn sẵn sàng phối hợp và hỗ trợ trong công việc nhóm 1.0
    1.5 Kiến thức và kỹ năng thu nhận Thu nhận kém kiến thức và kỹ năng được yêu cầu. Thu nhận một phần các kiến thức cơ bản và kỹ năng được yêu cầu Thu nhận ở mức cơ bản kiến thức và kỹ năng được yêu cầu. Thu nhận đầy đủ kiến thức và kỹ năng được yêu cầu. Thu nhận rất tốt kiến thức và kỹ năng được yêu cầu. 1.0
2.  Đánh giá kết quả thực hiện 5.0
    Hoàn thành và đảm bảo đầy đủ nội dung theo yêu cầu đặt ra Hầu hết không hoàn thành và đảm bảo đầy đủ nội dung theo yêu cầu đặt ra Hoàn thành báo cáo thực tập; hầu hết các nội dung thực nghiệm chưa hoàn thành theo yêu cầu Hoàn thành báo cáo thực tập; hoàn thành các nội dung cơ bản của thực nghiệm theo yêu cầu. Một số nội dung chưa hoàn thành và đảm bảo đầy đủ theo yêu cầu Hoàn thành và đảm bảo đầy đủ nội dung theo yêu cầu 5.0
    Nhận xét:

        Cán bộ hướng dẫn tại đơn vị

    (Ký và ghi rõ họ tên)
    ĐÁNH GIÁ ĐỒ ÁN THỰC TẬP MÔN HỆ THỐNG THÔNG TIN TÍCH HỢP
    (Dành cho cán bộ chấm thi)
    Tiêu chí đánh giá:
    Tiêu chí
    đánh giá Yếu (0 - 39%) Trung Bình
    (40-54%) Khá (55-69%) Giỏi (70-84%) Xuất sắc
    (85-100%) Điểm tối đa CB 1 (Cho lẻ đến 0.25) CB 2 (Cho lẻ đến 0.25)

3.  Báo cáo kết quả 3,0
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
   Ngày tháng năm 20…
   Cán bộ chấm thi 1
   (Ký và ghi rõ họ tên) Cán bộ chấm thi 2
   (Ký và ghi rõ họ tên)

MỤC LỤC
LỜI NÓI ĐẦU 1
CHƯƠNG 1 : TỔNG QUAN VÀ KHẢO SÁT DỰ ÁN 2
1.1. Mô tả yêu cầu hệ thống 2
1.1.1 Giới thiệu sơ lược về ERP Innovision 2
1.1.2 Phạm vi chức năng tích hợp 2
1.1.3 Các yêu cầu chức năng tổng hợp 4
1.1.4 Kết luận 5
1.2 Khảo sát và đánh giá hiện trạng 5
1.2.1 Phương pháp khảo sát 5
1.2.2 Kết quả khảo sát 5
1.2.3 Kết luận khảo sát 7
1.2.4. Đánh giá tính khả thi và rủi ro 9
1.2.5. Phương án thực hiện 11
CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG 15
2.1. Tổng quan giải pháp tích hợp 15
2.1.1 Kiến trúc tổng thể tích hợp 15
2.1.2. Lợi ích của giải pháp tích hợp 16
2.1.3. Các yếu tố cần thiết để tích hợp 16
2.1.4. Các bước thực hiện tích hợp tổng quan 16
2.2. Đặc tả các ca sử dụng 17
2.2.1. Chức năng gửi email qua Brevo 17
2.2.2. Chức năng thông báo qua Telegram Bot 23
CHƯƠNG 3. XÂY DỰNG HỆ THỐNG 27
3.1. Công cụ và nền tảng phát triển 27
3.1.1. Môi trường lập trình 27
3.1.2. Ngôn ngữ và Framework 27
3.1.3. Hệ quản trị cơ sở dữ liệu và ORM 27
3.1.4. Các dịch vụ bên thứ ba tích hợp 28
3.2. Thiết kế giao diện 29
3.2.1. Giao diện cài đặt thông báo Email (Brevo) 29
3.2.3. Ví dụ email gửi qua Brevo 31
3.2.4. Ví dụ tin nhắn Telegram 31
KẾT LUẬN 32
TÀI LIỆU THAM KHẢO 35

MỤC LỤC HÌNH ẢNH
Hình 2.1: Kiến trúc tổng thể tích hợp hệ thống 15
Hình 2.2: Biểu đồ use case chức năng gửi email qua Brevo 19
Hình 2.3: Biểu đồ hoạt động chức năng gửi email giao dịch qua Brevo 20
Hình 2.4: Biểu đồ trình tự chức năng gửi email giao dịch qua Brevo 21
Hình 2.5: Biểu đồ trình tự chức năng gửi email thông báo sự kiện 23
Hình 2.6: Biểu đồ use case chức năng thông báo Telegram 25
Hình 2.7: Biểu đồ trình tự chức năng thông báo Telegram 26
Hình 3.1: Giao diện cài đặt thông báo Email trong phần Cài đặt cá nhân 29
Hình 3.2: Giao diện kết nối tài khoản Telegram 30
Hình 3.3: Giao diện email thiết lập tài khoản được gửi qua Brevo 31
Hình 3.4: Tin nhắn thông báo sự kiện gửi từ Telegram Bot 31 
MỤC LỤC BẢNG
Bảng 1.1: Các yêu cầu chức năng của các module tích hợp bên thứ ba 4
Bảng 1.2: Yêu cầu nghiệp vụ của các module tích hợp bên thứ ba 8
Bảng 1.3: Đánh giá tính khả thi các module tích hợp 9
Bảng 1.4: Yếu tố rủi ro của các module tích hợp 10
Bảng 1.5: Mốc thời gian triển khai các module tích hợp 13
Bảng 2.1 Yếu tố để tích hợp 16
Bảng 3.1: Thông tin kỹ thuật các dịch vụ tích hợp 28

 
LỜI CẢM ƠN
Hà Nội, ngày 16 tháng 12 năm 2025
Sinh viên thực hiện

Nguyễn Văn A

LỜI NÓI ĐẦU
Trong kỷ nguyên chuyển đổi số, các hệ thống ERP (Enterprise Resource Planning) ngày càng đóng vai trò quan trọng trong việc số hóa và tự động hóa quy trình quản trị doanh nghiệp. Một trong những thách thức lớn khi xây dựng hệ thống ERP hiện đại là khả năng tích hợp liền mạch với các dịch vụ bên thứ ba đặc biệt là các kênh truyền thông và thông báo sự kiện đến người dùng.
Dự án ERP Innovision là một nền tảng quản lý nhân sự toàn diện, được xây dựng trên nền tảng Node.js/Express với cơ sở dữ liệu MySQL. Để nâng cao trải nghiệm người dùng và hiệu quả vận hành, hệ thống cần được bổ sung thêm hai kênh thông báo quan trọng:
Gửi email giao dịch qua Brevo: Đảm bảo truyền thông chính thức, theo dõi lịch sử và tỷ lệ gửi email, phục vụ các luồng nghiệp vụ như kích hoạt tài khoản, đặt lại mật khẩu và thông báo sự kiện.
Thông báo tức thời qua Telegram Bot: Giúp người dùng nhận cảnh báo và cập nhật sự kiện theo thời gian thực ngay trên ứng dụng Telegram.
Vì vậy, em chọn đề tài:"Tích hợp hệ thống thông báo cho nền tảng ERP Innovision" làm báo cáo kết thúc học phần Thực tập Hệ thống thông tin tích hợp.

 
CHƯƠNG 1 : TỔNG QUAN VÀ KHẢO SÁT DỰ ÁN
1.1. Mô tả yêu cầu hệ thống
1.1.1 Giới thiệu sơ lược về ERP Innovision
ERP Innovision là một nền tảng quản trị nhân sự doanh nghiệp được xây dựng nhằm hỗ trợ các tổ chức trong việc số hóa quy trình vận hành. Hệ thống bao gồm các module cốt lõi như: quản lý nhân sự, chấm công, nghỉ phép, tăng ca, bảng lương, quản lý dự án và nhiệm vụ.
Hệ thống hoạt động trên nền tảng web với backend được xây dựng bằng Node.js/Express.js, sử dụng Prisma ORM để giao tiếp với cơ sở dữ liệu MySQL/MariaDB, và frontend sử dụng React (Vite). Hệ thống đã vận hành ổn định nhưng còn thiếu các kênh giao tiếp chủ động đến người dùng.Để đáp ứng nhu cầu thực tiễn của doanh nghiệp, ERP Innovision có định hướng tích hợp hai hệ thống thông báo bên thứ ba sau:
Brevo (Sendinblue) Email API – Gửi email thông báo giao dịch (kích hoạt tài khoản, đặt lại mật khẩu, thông báo sự kiện nghiệp vụ).
Telegram Bot API – Gửi thông báo tức thời đến người dùng hoặc nhóm quản lý.
1.1.2 Phạm vi chức năng tích hợp
\*Mục tiêu của các chức năng tích hợp:

- Tự động gửi email xác nhận, thông báo kích hoạt tài khoản, nhắc nhở reset mật khẩu qua Brevo với khả năng theo dõi trạng thái gửi.
- Tự động gửi email thông báo cho người dùng khi có sự kiện nghiệp vụ quan trọng (phê duyệt nghỉ phép, phân công nhiệm vụ, cảnh báo số dư phép, v.v.) theo cài đặt của từng người.
- Hỗ trợ người dùng và quản trị viên nhận cảnh báo ngay trên ứng dụng Telegram mà không cần mở trình duyệt.
- Đảm bảo tính an toàn, bảo mật và không phụ thuộc sâu vào nội bộ của các hệ thống bên thứ ba (tiếp cận black-box).
  \*Tình huống sử dụng thực tế:
- Khi quản trị viên tạo tài khoản nhân viên mới, hệ thống tự động gửi email chứa link thiết lập mật khẩu qua Brevo đến địa chỉ email của nhân viên.
- Khi nhân viên yêu cầu đặt lại mật khẩu, hệ thống gửi email chứa link reset (có thời hạn) qua Brevo.
- Khi đơn xin nghỉ phép được phê duyệt hoặc từ chối, hệ thống gửi thông báo đến người dùng qua email (Brevo) và/hoặc Telegram tùy theo cài đặt cá nhân.
- Người dùng có thể kết nối tài khoản Telegram cá nhân với hệ thống qua deep link để nhận thông báo tức thì.

   
  1.1.3 Các yêu cầu chức năng tổng hợp
  Bảng 1.1: Các yêu cầu chức năng của các module tích hợp bên thứ ba
  Loại yêu cầu Mô tả
  Yêu cầu nghiệp vụ Hệ thống phải hỗ trợ gửi thông báo đa kênh (Email qua Brevo, Telegram) cho các sự kiện nghiệp vụ quan trọng theo cài đặt của từng người dùng.
  Yêu cầu kỹ thuật Tích hợp thông qua REST API/HTTPS với các hệ thống bên thứ ba; xử lý lỗi gracefully khi API bên ngoài không phản hồi.
  Yêu cầu giao diện Cung cấp giao diện cài đặt thông báo cá nhân để bật/tắt từng loại thông báo cho cả hai kênh Email và Telegram.
  Yêu cầu bảo mật Không lưu trữ API Key hay Bot Token dưới dạng plain-text trong database hay source code; sử dụng biến môi trường (.env) để quản lý credentials.
  Yêu cầu khả năng mở rộng Thiết kế theo kiến trúc module hóa, dùng chung một hệ thống map sự kiện để có thể bổ sung thêm kênh thông báo khác trong tương lai.

   
  1.1.4 Kết luận
  Hai chức năng tích hợp Email API và Telegram Bot API – là các thành phần thiết yếu giúp nâng cao trải nghiệm người dùng và hiệu quả vận hành của ERP Innovision. Việc tiếp cận theo hướng black-box (chỉ tương tác qua API chuẩn, không can thiệp vào nội bộ) đảm bảo tính ổn định, dễ bảo trì và linh hoạt trong việc thay thế hoặc nâng cấp dịch vụ bên thứ ba.
  1.2 Khảo sát và đánh giá hiện trạng
  1.2.1 Phương pháp khảo sát
  Để đánh giá hiện trạng xác định nhu cầu tích hợp, nhóm thực tập đã thực hiện:

- Phân tích codebase hiện tại của dự án ERP Innovision (source code trên repository).
- Phỏng vấn trực tiếp người dùng và quản trị viên hệ thống về nhu cầu thông báo sự kiện.
- Nghiên cứu tài liệu kỹ thuật của Brevo REST API và Telegram Bot API.
- Đánh giá các điểm trong hệ thống cần được bổ sung tính năng thông báo.
  1.2.2 Kết quả khảo sát

* Hệ thống ERP Innovision hiện tại

- Có hệ thống gửi email qua SMTP (Nodemailer) nhưng thiếu template chuyên nghiệp, không có khả năng theo dõi trạng thái gửi và hay bị lọc spam.
- Chưa có kênh thông báo tức thời: người dùng phải chủ động truy cập hệ thống để kiểm tra trạng thái đơn nghỉ phép, nhiệm vụ được giao, v.v.
- Chưa có hệ thống cài đặt thông báo cá nhân, chưa có log lịch sử thông báo.

 
\*Các vấn đề đang gặp phải

- Email không đáng tin cậy: Gửi email qua SMTP trực tiếp bằng Nodemailer thường bị rơi vào spam, không có khả năng theo dõi tỷ lệ gửi, tỷ lệ mở hay bounce.
- Thiếu thông báo thời gian thực: Người dùng không nhận được cảnh báo kịp thời khi có sự kiện quan trọng liên quan đến mình (đơn xin phép được duyệt, nhiệm vụ sắp đến hạn, v.v.).
- Trải nghiệm kém chủ động: Nhân viên phải liên tục đăng nhập để biết trạng thái công việc, không có cơ chế push notification.
- Khó mở rộng: Kiến trúc email hiện tại không có khả năng mở rộng linh hoạt, thêm template hay kênh mới rất khó.

* Nhu cầu nâng cấp

- Tích hợp Brevo REST API để gửi email chuyên nghiệp với template HTML chuẩn và khả năng tracking.
- Tích hợp Telegram Bot API để gửi thông báo push tức thì đến từng người dùng theo cài đặt cá nhân.
- Xây dựng hệ thống cài đặt thông báo cá nhân cho phép từng người dùng tự quản lý các loại thông báo muốn nhận qua từng kênh.
   
  1.2.3 Kết luận khảo sát
  Hệ thống ERP Innovision đang thiếu các kênh giao tiếp chủ động và đáng tin cậy với người dùng. Việc tích hợp Brevo và Telegram Bot sẽ giải quyết triệt để các bất cập hiện tại, nâng cao tính chuyên nghiệp và trải nghiệm người dùng của nền tảng.

* Đối với Brevo Email API:

- Tích hợp qua Brevo REST API (HTTPS) sử dụng `api-key` trong request header.
- Endpoint sử dụng: `POST https://api.brevo.com/v3/smtp/email`.
- Hỗ trợ gửi email tới người dùng với nội dung HTML tùy chỉnh (inline CSS để tương thích email client).
- Hỗ trợ theo dõi trạng thái gửi thông qua `messageId` trả về từ Brevo.
- Người dùng có thể bật/tắt từng loại thông báo email mong muốn trong phần cài đặt cá nhân.
  \*Đối với Telegram Bot API:
- Tích hợp qua Telegram Bot API (HTTPS) sử dụng `BOT_TOKEN` trong URL.
- Hỗ trợ định dạng tin nhắn HTML (`parse_mode: "HTML"`), gửi link hành động.
- Người dùng kết nối tài khoản Telegram cá nhân với hệ thống qua deep link, không cần can thiệp thủ công vào cấu hình bot.

- Yêu cầu nghiệp vụ
  Bảng 1.2: Yêu cầu nghiệp vụ của các module tích hợp bên thứ ba
  Yêu cầu Mô tả chi tiết
  Cài đặt cá nhân theo kênh Mỗi người dùng có bảng cài đặt riêng cho kênh Email (UserEmailNotificationSetting) và Telegram (UserTelegramSetting).
  Định danh sự kiện Mỗi loại sự kiện nghiệp vụ (nghỉ phép, tăng ca, nhiệm vụ, lương, v.v.) được ánh xạ sang trường cài đặt cụ thể qua EMAIL_SETTING_MAP và TELEGRAM_SETTING_MAP.
  Tự động gửi khi sự kiện xảy ra Khi có sự kiện nghiệp vụ, hệ thống kiểm tra cài đặt của từng người liên quan rồi quyết định gửi hay không gửi qua từng kênh.
  Bảo mật thông tin BREVO_API_KEY và TELEGRAM_BOT_TOKEN được lưu trong biến môi trường (.env), không lưu trong database hay source code.
  Xử lý lỗi Nếu API bên thứ ba không phản hồi, hệ thống phải xử lý lỗi gracefully (log lỗi, không crash ứng dụng chính).
  Email giao dịch cốt lõi Các email thiết lập tài khoản và reset mật khẩu phải được gửi qua Brevo bất kể cài đặt thông báo cá nhân của người dùng.

   
  1.2.4. Đánh giá tính khả thi và rủi ro

- Tính khả thi
  Bảng 1.3: Đánh giá tính khả thi các module tích hợp
  Yếu tố Đánh giá
  Hạ tầng kỹ thuật hiện tại ERP Innovision đã có kiến trúc backend Node.js/Express với hỗ trợ native fetch API để gọi HTTP – phù hợp để tích hợp các REST API bên thứ ba mà không cần thêm thư viện HTTP client.
  Tài liệu và SDK Brevo REST API v3 và Telegram Bot API đều có tài liệu chính thức đầy đủ, phản hồi JSON chuẩn và cộng đồng hỗ trợ lớn.
  Chi phí Brevo cung cấp gói miễn phí 300 email/ngày, đủ cho môi trường phát triển và thử nghiệm. Telegram Bot API hoàn toàn miễn phí.
  Đội ngũ phát triển Đội ngũ có kinh nghiệm với Node.js và REST API, đủ năng lực triển khai các tích hợp theo tài liệu kỹ thuật chính thức.
  Tính pháp lý Cả hai dịch vụ đều hợp pháp, tuân thủ GDPR và các tiêu chuẩn bảo mật quốc tế.

 
\*Các rủi ro có thể xảy ra
Bảng 1.4: Yếu tố rủi ro của các module tích hợp
Loại rủi ro Mô tả
Phụ thuộc vào dịch vụ bên thứ ba Nếu API của Brevo hoặc Telegram gặp sự cố, các chức năng thông báo liên quan sẽ bị ảnh hưởng.
Thay đổi API Nhà cung cấp có thể thay đổi API (version mới, deprecated endpoint) mà không báo trước.
Giới hạn tốc độ (Rate Limit) Brevo và Telegram đều có giới hạn số lượng request; vượt quá ngưỡng sẽ bị từ chối hoặc tạm khóa.
Bảo mật credentials Nếu BREVO_API_KEY hay TELEGRAM_BOT_TOKEN bị lộ, kẻ tấn công có thể lạm dụng dịch vụ.
Webhook Telegram yêu cầu HTTPS Server cần có domain và chứng chỉ SSL hợp lệ để Telegram gọi webhook về, khó thực hiện trên môi trường development local.
Giới hạn gói miễn phí Brevo 300 email/ngày đủ cho development, nhưng cần nâng cấp gói khi triển khai production với lượng người dùng lớn.

 
\*Giải pháp phòng ngừa:

- Xử lý tất cả lời gọi API bên thứ ba trong `try/catch`, log lỗi và không để lỗi crash ứng dụng chính (fire-and-forget cho thông báo không quan trọng).
- Lưu credentials trong file `.env`, không commit lên repository (đã có `.gitignore`).
- Với Telegram webhook: hỗ trợ cả chế độ polling trong development khi chưa có HTTPS.
- Theo dõi phiên bản API và cập nhật kịp thời khi có thông báo deprecated.
  1.2.5. Phương án thực hiện

* Phân tích yêu cầu và thiết kế hệ thống

- Các sự kiện nghiệp vụ kích hoạt thông báo được xác định và ánh xạ vào hai bảng setting: `UserEmailNotificationSetting` và `UserTelegramSetting`.
- Luồng gửi email giao dịch (tạo tài khoản, reset mật khẩu) được tích hợp trực tiếp vào `auth.service.js`.
- Luồng gửi thông báo sự kiện đi qua `notifications.service.js`, tập trung xử lý logic kiểm tra setting và dispatch đến từng kênh.

* Thiết kế kiến trúc tích hợp:

- Brevo và Telegram mỗi dịch vụ được đóng gói trong một **Service Class** riêng biệt (`brevo.service.js`, `telegram.service.js`) trong thư mục `src/common/services/`.
- Giao tiếp ra ngoài được thực hiện qua **native `fetch` API** (Node.js 18+), không cần thêm thư viện HTTP client.
- Các lời gọi thông báo sự kiện được xử lý **fire-and-forget** (không await) để không ảnh hưởng đến response của API chính.
  \*Chọn công nghệ và công cụ tích hợp
  -Backend Runtime: Node.js 18+ – hỗ trợ native `fetch` API, không cần thư viện HTTP client bên ngoài.
  -Backend Framework: Express.js – xử lý routing, middleware và request/response.
- ORM: Prisma – quản lý schema và migration cơ sở dữ liệu MySQL/MariaDB.
- Brevo: Gọi trực tiếp REST API tại `https://api.brevo.com/v3/smtp/email` qua HTTP POST với header `api-key`.
  -Telegram: Gọi trực tiếp Telegram Bot API tại `https://api.telegram.org/bot{TOKEN}/sendMessage` qua HTTP POST.
- Bảo mật: HTTPS toàn bộ, credentials lưu trong `.env`, webhook Telegram xác thực qua `TELEGRAM_WEBHOOK_SECRET`.

- Tiến trình triển khai
  Bảng 1.5: Mốc thời gian triển khai các module tích hợp
  Mốc thời gian Công việc Mô tả
  Tuần 1-2 Phân tích yêu cầu và thiết kế kiến trúc Xác định các sự kiện cần thông báo, thiết kế schema bảng setting, thiết kế luồng gửi email và Telegram.
  Tuần 3 Tích hợp Brevo Email (giao dịch) Xây dựng brevo.service.js, tích hợp vào luồng tạo tài khoản và reset mật khẩu, kiểm thử thật.
  Tuần 4 Tích hợp Brevo Email (thông báo sự kiện) Xây dựng EMAIL_SETTING_MAP, tích hợp vào notifications.service.js, thêm migration và API cài đặt.
  Tuần 5 Tích hợp Telegram Bot Đăng ký bot qua BotFather, xây dựng telegram.service.js, luồng kết nối tài khoản qua deep link, webhook xử lý lệnh.
  Tuần 6 Kiểm thử tích hợp Kiểm thử end-to-end cả hai chức năng, bao gồm kiểm thử lỗi và edge case.
  Tuần 7 Hoàn thiện và triển khai Deploy lên môi trường production, viết tài liệu hướng dẫn sử dụng và vận hành.
  Tuần 8 Đánh giá và bảo trì Thu thập phản hồi, khắc phục sự cố, cập nhật tài liệu và đề xuất cải tiến.
- Kiểm thử và bảo trì

* Kiểm thử thủ công qua Postman: Kiểm thử trực tiếp các endpoint Brevo API và Telegram API với dữ liệu thật trước khi tích hợp vào code.
* Kiểm thử tích hợp: Kiểm thử luồng hoàn chỉnh từ trigger sự kiện (tạo tài khoản, phê duyệt nghỉ phép) đến khi thông báo được gửi thực tế đến người nhận.
* Kiểm thử lỗi: Kiểm thử các trường hợp API key sai, email người nhận không hợp lệ, server không phản hồi để đảm bảo xử lý gracefully.
* Bảo trì: Theo dõi log gửi thông báo, cập nhật khi API có thay đổi, kiểm tra rate limit định kỳ. 
  CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG
  2.1. Tổng quan giải pháp tích hợp
  Hệ thống ERP Innovision tích hợp hai dịch vụ thông báo bên thứ ba theo black-box: hệ thống chỉ tương tác với các dịch vụ này thông qua giao thức HTTPS và API chuẩn được công bố, không can thiệp vào cơ sở hạ tầng nội bộ của chúng.
  2.1.1 Kiến trúc tổng thể tích hợp

Hình 2.1: Kiến trúc tổng thể tích hợp hệ thống

- Đặc điểm tiếp cận black-box:

* ERP Innovision gửi request và nhận response theo chuẩn API đã công bố.
* Không biết và không cần biết cách Brevo xử lý, lưu trữ và phân phối email nội bộ.
* Không biết và không cần biết cách Telegram Server xử lý và phân phối tin nhắn đến thiết bị người dùng.
  2.1.2. Lợi ích của giải pháp tích hợp
* Email chuyên nghiệp qua Brevo: Template HTML chuẩn với inline CSS, tỷ lệ vào hộp thư chính cao, trả về `messageId` để theo dõi, tránh bị spam.
* Thông báo kịp thời qua Telegram: Người dùng nhận tin nhắn ngay trên điện thoại mà không cần mở ứng dụng ERP.
* Tăng độ tin cậy: Sử dụng hạ tầng đã được kiểm chứng của các nhà cung cấp lớn (Brevo, Telegram).
* Giảm chi phí vận hành: Không cần tự xây dựng và duy trì hệ thống gửi email hay push notification.
* Cài đặt linh hoạt theo cá nhân: Mỗi người dùng tự quyết định nhận loại thông báo nào qua kênh nào.
  2.1.3. Các yếu tố cần thiết để tích hợp
  Bảng 2.1 Yếu tố để tích hợp
  Dịch vụ Yếu tố cần thiết
  Brevo Email BREVO_API_KEY từ tài khoản Brevo, MAIL_FROM_ADDRESS và MAIL_FROM_NAME đã xác minh trên Brevo.
  Telegram Bot TELEGRAM_BOT_TOKEN từ BotFather, TELEGRAM_BOT_USERNAME, TELEGRAM_WEBHOOK_SECRET để bảo mật webhook.

  2.1.4. Các bước thực hiện tích hợp tổng quan

1. Đăng ký và cấu hình tài khoản/bot tại nhà cung cấp (Brevo dashboard, Telegram BotFather).
2. Lưu credentials vào biến môi trường (`.env`) của hệ thống.
3. Xây dựng Service Class tương ứng (`brevo.service.js`, `telegram.service.js`).
4. Tích hợp service vào các module nghiệp vụ cần thông báo.
5. Xây dựng schema và API quản lý cài đặt thông báo cá nhân.
6. Kiểm thử toàn bộ luồng và xử lý các trường hợp lỗi.
   2.2. Đặc tả các ca sử dụng
   2.2.1. Chức năng gửi email qua Brevo
   Gửi email qua Brevo là một trong những chức năng tích hợp quan trọng của ERP InnoVision với cơ chế **black-box service**, sử dụng REST API của Brevo để gửi email giao dịch (transactional email) như thiết lập tài khoản, đặt lại mật khẩu và thông báo sự kiện nghiệp vụ. Chức năng được thiết kế theo pattern fire-and-forget để không làm chậm luồng nghiệp vụ chính.
   2.2.1.1. Use Case 1: Gửi email thiết lập tài khoản và đặt lại mật khẩu

Hình 2.2 — Biểu đồ Use Case Gửi email qua Brevo
Đặc tả UC Gửi email thiết lập tài khoản qua Brevo:
Bảng đặc tả UC Gửi email thiết lập tài khoản qua Brevo
Thành phần Nội dung chi tiết
Tên Use Case Gửi email thiết lập tài khoản và đặt lại mật khẩu qua Brevo
Mô tả Quy trình tự động hóa việc gửi thông tin định danh và link bảo mật. Hệ thống ERP đóng vai trò là Client gọi đến Brevo REST API (Black-box) để thực hiện việc xác thực và phân phối email đến người nhận.
Tác nhân (Actor) ERP System (Tác nhân chính), Brevo Email Server (Hệ thống bên thứ 3), Người dùng cuối (Người nhận email).
Điều kiện 1. BREVO_API_KEY đã được cấu hình trong biến môi trường (.env). 2. Địa chỉ MAIL_FROM_ADDRESS đã được xác minh (Verified Domain/Sender) trên Dashboard của Brevo.
Tiền điều kiện 1. Admin vừa tạo tài khoản nhân viên mới hoặc người dùng vừa kích hoạt yêu cầu "Quên mật khẩu". 2. Biến FRONTEND_URL đã sẵn sàng để cấu trúc hóa đường dẫn hành động (Action Link).
Hậu điều kiện 1. Email được gửi thành công đến hộp thư người nhận với link có hiệu lực trong 24 giờ. 2. Brevo trả về messageId để hệ thống lưu vết. 3. Trong trường hợp lỗi API, hệ thống ghi log lỗi nhưng không làm gián đoạn các tiến trình nghiệp vụ khác.

Luồng sự kiện chính:
Bước Tác nhân Hành động
1 Quản trị viên Thực hiện thao tác tạo tài khoản nhân viên mới trên giao diện quản trị của hệ thống ERP.
2 Hệ thống ERP auth.service.js tạo token thiết lập (32 bytes ngẫu nhiên), thực hiện hash SHA-256 và lưu vào Database với thời hạn hết hạn là 24 giờ.
3 Hệ thống ERP Kích hoạt hàm sendAccountSetupEmail() trong brevo.service.js với các tham số: to, fullName, và setupUrl.
4 Hệ thống ERP Gọi hàm buildNotificationHtml() để khởi tạo nội dung HTML (sử dụng inline CSS để đảm bảo hiển thị trên các trình xem mail) và nhúng link thiết lập tài khoản.
5 Hệ thống ERP Thực hiện gửi yêu cầu HTTP POST đến https://api.brevo.com/v3/smtp/email. Header chứa api-key: BREVO_API_KEY; Body chứa thông tin sender, to, subject, và htmlContent.
6 Brevo Server Tiếp nhận Request, xác thực API Key, xử lý kết xuất nội dung và thực hiện phân phối email đến máy chủ thư của người nhận.
7 Brevo Server Trả về mã phản hồi HTTP 201 Created kèm theo JSON chứa messageId nếu quá trình tiếp nhận email thành công.
8 Hệ thống ERP Ghi nhận log thành công kèm messageId. Nếu có lỗi, hệ thống ném (throw) Error dựa trên mã lỗi trả về từ Brevo và ghi lại log tại tầng xử lý lỗi.
9 Người dùng cuối Kiểm tra hộp thư cá nhân, nhận email và nhấn vào link để tiến hành thiết lập mật khẩu lần đầu cho tài khoản.

Ngoại lệ:

- (API Key không hợp lệ) Brevo trả HTTP 401 → throw Error `"Gửi email thất bại (401): ..."`
- (Email người nhận không hợp lệ) Brevo trả HTTP 400 → ghi log và xử lý như lỗi thông thường
- (BREVO_API_KEY chưa cấu hình) Hàm `sendEmail()` log cảnh báo `"[Brevo] BREVO_API_KEY chưa được cấu hình. Bỏ qua gửi email."` và return sớm, không throw, đảm bảo ứng dụng không crash
- (Vượt giới hạn gói) Brevo trả HTTP 402 → cần nâng cấp gói hoặc giảm tần suất gửi

Hình 2.3: Biểu đồ hoạt động chức năng gửi email giao dịch qua Brevo

Hình 2.4: Biểu đồ trình tự chức năng gửi email giao dịch qua Brevo
2.2.1.2. Use Case 2: Gửi email thông báo sự kiện nghiệp vụ qua Brevo
Khác với Use Case 1 (gửi email do trigger trực tiếp từ admin), Use Case này được kích hoạt **gián tiếp** từ các sự kiện nghiệp vụ trong hệ thống (phê duyệt nghỉ phép, phân công task, cảnh báo số dư phép, v.v.) và phải kiểm tra cài đặt cá nhân của người dùng trước khi gửi.

Hình 2.5: Biểu đồ Use Case chức năng gửi email thông báo sự kiện qua Brevo

Đặc tả UC Gửi email thông báo sự kiện nghiệp vụ:
Bảng đặc tử usecase gửi email thông báo sự kiện qua Brevo
Thành phần Nội dung chi tiết
Tên Use Case Gửi email thông báo sự kiện theo cài đặt người dùng
Mô tả Hệ thống tự động lọc và gửi email thông báo dựa trên các sự kiện nghiệp vụ (phê duyệt, giao task, cảnh báo) sau khi đã đối soát với cấu hình nhận tin riêng tư của từng người dùng. Việc gửi email được thực hiện theo cơ chế fire-and-forget để đảm bảo hiệu năng.
Tác nhân (Actor) ERP System (Tự động trigger), Brevo Email Server (Hệ thống gửi tin), Người dùng cuối (Người nhận tin).
Điều kiện 1. BREVO_API_KEY đã được thiết lập chính xác. 2. Bảng cấu hình UserEmailNotificationSetting đã sẵn sàng trong cơ sở dữ liệu để truy vấn.
Tiền điều kiện 1. Một sự kiện nghiệp vụ hợp lệ vừa hoàn thành (ví dụ: Đơn nghỉ phép vừa được duyệt). 2. Người nhận thông báo đang ở trạng thái ACTIVE và có địa chỉ email hợp lệ.
Hậu điều kiện 1. Nếu người dùng bật thông báo: Email được đẩy vào hàng đợi gửi tin của Brevo thành công. 2. Nếu người dùng tắt thông báo: Hệ thống bỏ qua bước gửi mail, quy trình kết thúc bình thường. 3. Mọi sự cố về mạng hoặc API với Brevo không làm gián đoạn luồng nghiệp vụ chính của ERP.

Luồng sự kiện chính:
Bước Tác nhân / Thành phần Hành động
1 Hệ thống ERP Một sự kiện nghiệp vụ xảy ra (Ví dụ: Đơn nghỉ phép của nhân viên vừa được Manager phê duyệt).
2 Hệ thống ERP Module nghiệp vụ liên quan thực hiện gọi hàm notifications.service.notify kèm các tham số: userId, type, title, message, và actionUrl.
3 Hệ thống ERP Thông báo nội bộ: Hệ thống lưu bản ghi vào bảng Notification trong Database và phát sự kiện notification:new qua Socket.io để hiển thị thông báo tức thời trên Web App.
4 Hệ thống ERP Kích hoạt hàm nội bộ \_dispatchEmail() theo mô hình fire-and-forget (chạy nền) để không làm chậm thời gian phản hồi (response time) của luồng nghiệp vụ chính.
5 Hệ thống ERP Truy vấn bảng UserEmailNotificationSetting của người dùng. Nếu chưa có bản ghi cài đặt, hệ thống mặc định coi như tất cả các loại thông báo đều đang Bật (ON).
6 Hệ thống ERP Sử dụng hằng số EMAIL_SETTING_MAP để ánh xạ mã type của sự kiện (VD: LEAVE_APPROVED) sang trường dữ liệu tương ứng trong bảng cài đặt (VD: notifyOnLeaveApproved).
7 Hệ thống ERP Kiểm tra quyền: Nếu trường cài đặt là false, hệ thống dừng tiến trình gửi mail và ghi log thông tin: "User [ID] đã tắt thông báo loại [Type]".
8 Hệ thống ERP Nếu được phép gửi: Thực hiện gọi brevo.sendEmail() với nội dung HTML được render động từ hàm buildNotificationHtml({title, message, actionUrl}).
9 Brevo Server Tiếp nhận yêu cầu, xác thực API Key, kết xuất nội dung email và thực hiện phân phối đến máy chủ thư của người nhận.
10 Brevo Server Phản hồi mã HTTP 201 Created kèm theo mã định danh messageId để xác nhận đã tiếp nhận email thành công.
11 Người dùng cuối Nhận được email thông báo trong hộp thư cá nhân và có thể nhấn nút "Xem chi tiết" để truy cập trực tiếp vào trang nghiệp vụ tương ứng trên ERP.

Ngoại lệ:

- (User chưa có UserEmailNotificationSetting) Mặc định tất cả các loại thông báo đều bật — vẫn gửi email
- (User đã tắt loại thông báo) `_dispatchEmail()` return sớm, không gửi, không log error
- (Lỗi từ Brevo) Bắt error trong try-catch của `_dispatchEmail()`, log warning nhưng không throw — luồng nghiệp vụ chính (đã commit transaction trước đó) không bị ảnh hưởng
- (User không có email) `_dispatchEmail()` kiểm tra `user.email` null và bỏ qua

Hình 2.6: Biểu đồ trình tự chức năng gửi email thông báo sự kiện qua Brevo
2.2.2. Chức năng thông báo qua Telegram Bot
Thông báo qua Telegram là chức năng tích hợp đặc biệt cho phép người dùng nhận thông báo nghiệp vụ tức thời ngay trên ứng dụng Telegram cá nhân, với độ trễ thường < 2 giây — nhanh hơn email rất nhiều. Chức năng sử dụng cơ chế deep link để liên kết tài khoản Telegram với hệ thống ERP một cách an toàn.
Use Case: Gửi thông báo tức thời qua Telegram Bot

Hình 2.7: Biểu đồ Use Case chức năng thông báo Telegram

Đặc tả UC Gửi thông báo qua Telegram Bot:
Bảng đặc tả usecase gửi thông báo Telegram
Thành phần Nội dung chi tiết
Tên Use Case Gửi thông báo sự kiện theo cài đặt cá nhân qua Telegram Bot
Mô tả Hệ thống tự động đẩy thông báo nghiệp vụ (phê duyệt, nhắc lịch, giao việc) đến tài khoản Telegram cá nhân của người dùng đã liên kết. ERP đóng vai trò Client gửi yêu cầu đến Telegram Bot API, sau đó Telegram Server (Black-box) sẽ thực hiện việc chuyển phát tin nhắn.
Tác nhân (Actor) Hệ thống ERP (Tác nhân chính), Telegram Server (Hệ thống trung gian), Người dùng (Người nhận tin).
Điều kiện 1. TELEGRAM_BOT_TOKEN hợp lệ đã được cấu hình trong file .env. 2. Hệ thống đã cấu hình Webhook trỏ về endpoint /api/telegram/webhook để xử lý các phản hồi từ người dùng.
Tiền điều kiện 1. Người dùng đã thực hiện kết nối tài khoản (Link account) và hệ thống đã lưu trữ được telegramChatId trong bảng UserTelegramSetting. 2. Một sự kiện nghiệp vụ (Trigger) vừa xảy ra trong hệ thống.
Hậu điều kiện 1. Tin nhắn được gửi đến thiết bị của người dùng với độ trễ cực thấp (< 2 giây). 2. Nếu người dùng chưa liên kết hoặc đã tắt thông báo Telegram, hệ thống sẽ bỏ qua bước này một cách êm đẹp.

Luồng sự kiện chính (luồng kết nối tài khoản):
Bước Tác nhân / Thành phần Hành động
1 Người dùng Truy cập vào trang cấu hình cá nhân tại /settings/telegram trên ERP và nhấn nút "Kết nối Telegram".
2 Hệ thống ERP telegram.service.js tạo một Connect Token ngẫu nhiên (hiệu lực 15 phút), lưu vào DB gắn với UserID và sinh ra Deep Link: https://t.me/{BOT_USERNAME}?start={token}.
3 Người dùng Click vào Deep Link, trình duyệt tự động chuyển hướng mở ứng dụng Telegram và người dùng nhấn nút "START".
4 Telegram Server Gửi một Update object chứa tin nhắn /start {token} kèm theo chat_id của người dùng về URL Webhook đã cấu hình của ERP.
5 Hệ thống ERP Webhook Handler: Giải mã payload, xác minh token có khớp với bản ghi trong DB và còn trong thời gian 15 phút hay không.
6 Hệ thống ERP Mapping: Nếu hợp lệ, hệ thống lấy chat_id từ Telegram và cập nhật vào trường telegramChatId trong bảng UserTelegramSetting của người dùng đó.
7 Hệ thống ERP Gọi Telegram Bot API (sendMessage) để gửi tin nhắn phản hồi trực tiếp: "✅ Chúc mừng {fullName}, bạn đã kết nối thành công với InnoVision ERP!".
8 Hệ thống ERP Thu hồi (xóa) token vừa sử dụng để đảm bảo an toàn và cập nhật trạng thái "Đã kết nối" trên giao diện Web cho người dùng.

Luồng sự kiện chính (luồng gửi thông báo):
Bước Tác nhân / Thành phần Hành động
1 Hệ thống ERP Một sự kiện nghiệp vụ xảy ra (Ví dụ: Một task mới vừa được phân công cho nhân viên).
2 Hệ thống ERP Module nghiệp vụ thực hiện gọi hàm notifications.service.notify() tương tự như quy trình gửi Email.
3 Hệ thống ERP Kích hoạt hàm \_dispatchTelegram() theo mô hình fire-and-forget và thực hiện truy vấn bảng UserTelegramSetting để lấy telegramChatId của người nhận.
4 Hệ thống ERP Kiểm tra liên kết: Nếu telegramChatId là null (người dùng chưa thực hiện kết nối Bot), hệ thống dừng tiến trình gửi Telegram và kết thúc sớm.
5 Hệ thống ERP Sử dụng TELEGRAM_SETTING_MAP để ánh xạ loại sự kiện (type) sang trường cài đặt cụ thể. Nếu người dùng đã tắt loại thông báo này, hệ thống sẽ dừng lại và không gửi tin.
6 Hệ thống ERP Nếu đủ điều kiện gửi: Gọi hàm telegram.sendPersonalNotification(chatId, {title, message, actionUrl}).
7 Hệ thống ERP Thực hiện định dạng văn bản theo chuẩn HTML của Telegram: <b>{title}</b>\n\n{message}\n\n<a href="{actionUrl}">Xem chi tiết</a>.
8 Hệ thống ERP Gửi yêu cầu HTTP POST đến https://api.telegram.org/bot{TOKEN}/sendMessage với Body chứa: chat_id, text, parse_mode: "HTML" và disable_web_page_preview: true.
9 Telegram Server Tiếp nhận Request, xác thực Bot Token, xử lý dữ liệu nội bộ và định hướng phân phối tin nhắn đến thiết bị của người dùng.
10 Telegram Server Phản hồi kết quả xử lý dưới dạng JSON: Trả về {ok: true} kèm message_id nếu thành công, hoặc {ok: false} kèm mô tả lỗi nếu thất bại.
11 Người dùng Nhận thông báo đẩy (Push Notification) tức thì trên ứng dụng Telegram (điện thoại hoặc máy tính) và có thể nhấn vào liên kết để truy cập trực tiếp vào hệ thống ERP.

Ngoại lệ:

- (TELEGRAM_BOT_TOKEN chưa cấu hình) Hàm `sendMessage()` log cảnh báo `"[Telegram] TELEGRAM_BOT_TOKEN chưa cấu hình"` và return sớm, không throw
- (Chat ID không hợp lệ — user đã chặn bot hoặc xóa chat) Telegram trả `{ok: false, description: "Forbidden: bot was blocked by the user"}` → log warning và đánh dấu `UserTelegramSetting.telegramChatId = null` để không gửi tiếp
- (Người dùng chưa kết nối Telegram) `_dispatchTelegram()` kiểm tra `telegramChatId` null và bỏ qua, không gửi
- (Token deep link đã hết hạn) Webhook handler trả tin nhắn lỗi "❌ Link kết nối đã hết hạn. Vui lòng tạo link mới"
- (Rate limit từ Telegram — quá 30 message/giây) Bắt error 429, retry sau 1 giây; nếu vẫn lỗi → log warning
  Bước Tác nhân / Thành phần Hành động
  1 Hệ thống ERP Một sự kiện nghiệp vụ xảy ra (Ví dụ: Một task mới vừa được phân công cho nhân viên).
  2 Hệ thống ERP Module nghiệp vụ thực hiện gọi hàm notifications.service.notify() tương tự như quy trình gửi Email.
  3 Hệ thống ERP Kích hoạt hàm \_dispatchTelegram() theo mô hình fire-and-forget và thực hiện truy vấn bảng UserTelegramSetting để lấy telegramChatId của người nhận.
  4 Hệ thống ERP Kiểm tra liên kết: Nếu telegramChatId là null (người dùng chưa thực hiện kết nối Bot), hệ thống dừng tiến trình gửi Telegram và kết thúc sớm.
  5 Hệ thống ERP Sử dụng TELEGRAM_SETTING_MAP để ánh xạ loại sự kiện (type) sang trường cài đặt cụ thể. Nếu người dùng đã tắt loại thông báo này, hệ thống sẽ dừng lại và không gửi tin.
  6 Hệ thống ERP Nếu đủ điều kiện gửi: Gọi hàm telegram.sendPersonalNotification(chatId, {title, message, actionUrl}).
  7 Hệ thống ERP Thực hiện định dạng văn bản theo chuẩn HTML của Telegram: <b>{title}</b>\n\n{message}\n\n<a href="{actionUrl}">Xem chi tiết</a>.
  8 Hệ thống ERP Gửi yêu cầu HTTP POST đến https://api.telegram.org/bot{TOKEN}/sendMessage với Body chứa: chat_id, text, parse_mode: "HTML" và disable_web_page_preview: true.
  9 Telegram Server Tiếp nhận Request, xác thực Bot Token, xử lý dữ liệu nội bộ và định hướng phân phối tin nhắn đến thiết bị của người dùng.
  10 Telegram Server Phản hồi kết quả xử lý dưới dạng JSON: Trả về {ok: true} kèm message_id nếu thành công, hoặc {ok: false} kèm mô tả lỗi nếu thất bại.
  11 Người dùng Nhận thông báo đẩy (Push Notification) tức thì trên ứng dụng Telegram (điện thoại hoặc máy tính) và có thể nhấn vào liên kết để truy cập trực tiếp vào hệ thống ERP.

Hình 2.8: Biểu đồ trình tự chức năng thông báo Telegram

 
CHƯƠNG 3. XÂY DỰNG HỆ THỐNG
3.1. Công cụ và nền tảng phát triển
3.1.1. Môi trường lập trình
Visual Studio Code (VS Code) là trình biên tập mã nguồn chính được sử dụng trong dự án, với các extension hỗ trợ Node.js, ESLint và Prisma.
Postman được sử dụng để kiểm thử trực tiếp các endpoint Brevo API và Telegram Bot API trước khi tích hợp vào code, đảm bảo format request và xác minh credentials.
3.1.2. Ngôn ngữ và Framework

- Node.js 18+ / Express.js là nền tảng backend chính của ERP Innovision. Node.js 18 cung cấp native `fetch` API, cho phép gọi HTTP đến Brevo và Telegram mà không cần thêm thư viện. Express.js xử lý routing, middleware, webhook Telegram và API endpoint quản lý cài đặt thông báo.
- React (Vite + TypeScript)\** được sử dụng cho giao diện frontend, bao gồm trang cài đặt thông báo email và Telegram, và trang xem lịch sử thông báo.
  3.1.3. Hệ quản trị cơ sở dữ liệu và ORM
  *MySQL/MariaDB kết hợp với Prisma ORM được sử dụng để:

* Quản lý bảng `UserEmailNotificationSetting`: lưu cài đặt bật/tắt từng loại thông báo email theo từng người dùng.
* Quản lý bảng `UserTelegramSetting`: lưu `telegram_chat_id` và cài đặt bật/tắt từng loại thông báo Telegram theo từng người dùng.
* Quản lý bảng `AuthToken`: lưu token thiết lập tài khoản và reset mật khẩu (hash SHA-256) với thời hạn.

  3.1.4. Các dịch vụ bên thứ ba tích hợp
  Bảng 3.1: Thông tin kỹ thuật các dịch vụ tích hợp
  Dịch vụ Giao thức Endpoint chính Xác thực
  Brevo (Sendinblue) HTTPS REST https://api.brevo.com/v3/smtp/email Header api-key
  Telegram Bot API HTTPS REST https://api.telegram.org/bot{TOKEN}/sendMessage Token trong URL path

  3.2. Thiết kế giao diện
  3.2.1. Giao diện cài đặt thông báo Email (Brevo)

Hình 3.1: Giao diện cài đặt thông báo Email trong phần Cài đặt cá nhân
3.2.2. Giao diện kết nối Telegram

Hình 3.2: Giao diện kết nối tài khoản Telegram
3.2.3. Ví dụ email gửi qua Brevo

Hình 3.3: Giao diện email thiết lập tài khoản được gửi qua Brevo
3.2.4. Ví dụ tin nhắn Telegram

Hình 3.4: Tin nhắn thông báo sự kiện gửi từ Telegram Bot

 
KẾT LUẬN
Những kết quả đạt được
Qua quá trình nghiên cứu và triển khai, đề tài "Tích hợp hệ thống thông báo cho nền tảng ERP Innovision"*đã đạt được các mục tiêu đề ra:
*Về mặt kỹ thuật:

- Tích hợp thành công Brevo Email AP: Hệ thống gửi email giao dịch chuyên nghiệp (thiết lập tài khoản, reset mật khẩu) với template HTML chuẩn, tỷ lệ vào hộp thư chính cao hơn hẳn so với SMTP trực tiếp. Đồng thời gửi email thông báo sự kiện nghiệp vụ theo cài đặt cá nhân của từng người dùng.
- Tích hợp thành công Telegram Bot API: Người dùng có thể kết nối tài khoản Telegram cá nhân với ERP qua deep link, sau đó nhận thông báo tức thì về các sự kiện liên quan theo cài đặt.
- Xây dựng hệ thống cài đặt thông báo cá nhân hai kênh (`UserEmailNotificationSetting`, `UserTelegramSetting`) với 20+ loại sự kiện có thể bật/tắt độc lập.
  \*Về mặt kiến trúc:
- Áp dụng thành công mô hình black-box integration: Mỗi dịch vụ bên thứ ba được đóng gói trong Service Class riêng (`brevo.service.js`, `telegram.service.js`), giao tiếp thuần qua HTTPS/REST API chuẩn.
- Hệ thống có tính module hóa cao: Hàm `notify()` trong `notifications.service.js` là điểm tập trung xử lý, dùng `EMAIL_SETTING_MAP` và `TELEGRAM_SETTING_MAP` chung để dễ thêm kênh mới.
- Bảo mật được đảm bảo: Credentials (`BREVO_API_KEY`, `TELEGRAM_BOT_TOKEN`) lưu trong `.env`, không commit lên repository.
  \*Về mặt trải nghiệm người dùng:
- Email giao dịch đến hộp thư chính (không vào spam), template đẹp và chuyên nghiệp.
- Người dùng nhận thông báo kịp thời qua Telegram mà không cần mở ERP.
- Người dùng tự kiểm soát được loại thông báo muốn nhận qua từng kênh.
  Hạn chế và hướng phát triển
  \*Hạn chế:
- Webhook Telegram yêu cầu server có IP public và HTTPS, chưa hoàn thiện thử nghiệm trong môi trường development local.
- Chưa có cơ chế theo dõi trạng thái email sau khi gửi (delivered, opened, bounced) qua webhook Brevo.
- Khi Brevo hoặc Telegram gặp sự cố, không có kênh dự phòng tự động.
  \*Hướng phát triển:
- Tích hợp webhook Brevo: Nhận sự kiện `delivered`, `opened`, `bounced` từ Brevo để cập nhật trạng thái email trong database, phục vụ báo cáo.
- Dashboard thống kê thông báo: Giao diện admin thống kê tổng hợp tỷ lệ gửi email thành công, bounce rate, số người dùng kết nối Telegram.
- Mở rộng kênh thông báo: Tích hợp thêm Zalo OA hoặc SMS (VNPT SMS, Viettel SMS) theo cùng kiến trúc black-box đã xây dựng.
- Rate limiting ứng dụng: Thêm logic kiểm soát tần suất gửi ở tầng ứng dụng trước khi gọi API bên ngoài để tránh vượt ngưỡng của nhà cung cấp.
- Email notification batching: Gộp nhiều thông báo cùng loại vào một email tổng hợp để tránh spam hộp thư người dùng.

 
TÀI LIỆU THAM KHẢO
[1]. Brevo (2025), _Brevo API Documentation v3 – Transactional Emails_ [online]. Truy cập ngày [XX] tháng [XX] năm 2025, từ: https://developers.brevo.com/reference/sendtransacemail
[2]. Telegram (2025), _Telegram Bot API Documentation_ [online]. Truy cập ngày [XX] tháng [XX] năm 2025, từ: https://core.telegram.org/bots/api
[3]. Prisma (2025), _Prisma ORM Documentation_ [online]. Truy cập từ: https://www.prisma.io/docs
[4]. Node.js (2025), _Node.js v18 – Fetch API_ [online]. Truy cập từ: https://nodejs.org/en/blog/announcements/v18-release-announce
[5]. Express.js (2025), _Express.js Documentation_ [online]. Truy cập từ: https://expressjs.com
[6]. Hardt, D. (2012), _The OAuth 2.0 Authorization Framework_ (RFC 6749). IETF. Truy cập từ: https://datatracker.ietf.org/doc/html/rfc6749
[7]. Thạc Bình Cường (2002), _Phân tích và thiết kế hệ thống thông tin_. Nhà xuất bản Khoa học và Kỹ thuật, Hà Nội.
