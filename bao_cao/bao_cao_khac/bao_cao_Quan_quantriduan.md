 

ĐỀ CƯƠNG THỰC TẬP MÔN
THỰC TẬP QUẢN TRỊ DỰ ÁN PHẦN MỀM

1. Tên đề tài: Xây Dựng website bán rượu
2. Sinh viên thực hiện:
   Họ và tên: Bùi Anh Quân. MSSV: 22810310251.
   Số điện thoại: 0965254277. Email: quanbui4704@gmail.com.
   Vị trí thực tập: Thực tập sinh lập trình.
3. Giảng viên hướng dẫn:
   Họ và tên: Phạm Đức Hồng. Học vị: Tiến sĩ.
   Số điện thoại: 0987403915. Email: hongpd@epu.edu.vn.
   Đơn vị công tác: Khoa Công Nghệ Thông Tin trường Đại học Điện lực.
4. Mô tả tóm tắt đề tài
   Báo cáo trình bày đề tài "Quản Trị Dự Án Phát Triển Phần Mềm: Xây Dựng Website Bán Rượu" — một nền tảng kinh doanh đặc sản rượu trực tuyến toàn diện, được phát triển nhằm hiện đại hóa quy trình bán hàng và quản lý kho vốn đang thực hiện thủ công (Excel, sổ sách) tại các cơ sở sản xuất rượu truyền thống. Hệ thống tích hợp các module nghiệp vụ cốt lõi gồm: quản lý sản phẩm, danh mục (rượu hạ thổ, rượu ngâm, phụ kiện), bộ sưu tập, giỏ hàng, quản lý người dùng và liên hệ. Kiến trúc dự án sử dụng Backend (NestJS/TypeScript) và Frontend (Next.js/TypeScript), cơ sở dữ liệu MongoDB đảm bảo tính linh hoạt và mở rộng. Hệ thống còn tích hợp thông báo qua Email (SMTP), lưu trữ hình ảnh trên Google Cloud Storage, cùng cơ chế xác thực bảo mật JWT.
5. Nội dung báo cáo thực tập
   Chương 1. Khảo sát hiện trạng và xác lập dự án
   • Đánh giá hiện trạng: Phân tích quy trình kinh doanh rượu truyền thống, chỉ ra những hạn chế về việc tiếp cận khách hàng hạn hẹp, thông tin sản phẩm phân tán và việc tiếp nhận đơn hàng thủ công dễ sai sót; từ đó khẳng định sự cần thiết của một hệ thống thương mại điện tử hỗ trợ giới thiệu sản phẩm, giỏ hàng và checkout mô phỏng.
   • Xác định mục tiêu: Thiết lập các mục tiêu cụ thể như tối ưu hóa quy trình đặt hàng, nâng cao trải nghiệm người dùng qua giao diện hiện đại và cung cấp công cụ quản trị kho hàng hiệu quả cho chủ cơ sở.
   • Yêu cầu và Công nghệ: Xác định các yêu cầu chức năng (quản lý sản phẩm, giỏ hàng, thanh toán) và yêu cầu phi chức năng (bảo mật, tốc độ tải trang). Lựa chọn hệ sinh thái TypeScript với NestJS và Next.js làm nền tảng công nghệ cốt lõi để đảm bảo hiệu suất và khả năng bảo trì lâu dài.
   Chương 2. Phân tích và thiết kế hệ thống
   • Phân quyền người dùng: Định nghĩa trách nhiệm của các nhóm người dùng: Admin (quản lý toàn diện sản phẩm, đơn hàng, người dùng), Customer (tìm kiếm, đặt hàng, quản lý cá nhân) thông qua hệ thống biểu đồ Use Case tổng quát và chi tiết.
   • Đặc tả quy trình: Chi tiết hóa logic vận hành của các quy trình trọng tâm như: quy trình xem sản phẩm, thêm sản phẩm vào giỏ hàng, thao tác checkout mô phỏng COD/QR trên giao diện, quản lý sản phẩm và quy trình xác thực người dùng bằng JWT. Phần lưu đơn hàng, quản lý trạng thái giao hàng và xác nhận thanh toán được xác định là phạm vi phát triển tiếp theo.
   • Thiết kế dữ liệu: Xây dựng cấu trúc cơ sở dữ liệu NoSQL (MongoDB) với các bộ sưu tập (Collections) được thiết kế tối ưu cho việc truy xuất nhanh, đảm bảo tính nhất quán dữ liệu giữa các module: Products, Orders, Users.
   Chương 3. Xây dựng hệ thống
   • Triển khai kỹ thuật: Giải trình cách thức sử dụng NestJS để xây dựng các RESTful API mạnh mẽ, ứng dụng Next.js cho Frontend để tối ưu SEO và trải nghiệm người dùng, cùng việc tích hợp các dịch vụ bên thứ ba như Google Cloud Storage để lưu trữ hình ảnh sản phẩm.
   • Kết quả triển khai: Trình bày giao diện thực tế của các chức năng quan trọng như: Trang chủ với slider sản phẩm nổi bật, Dashboard quản trị trực quan, trang chi tiết sản phẩm và quy trình Checkout mượt mà.
   • Đánh giá và Hướng phát triển: Đưa ra những đánh giá khách quan về thành quả đạt được (hệ thống chạy ổn định, giao diện đẹp), nhìn nhận các hạn chế (chưa tích hợp thanh toán trực tuyến qua cổng VNPay/Momo) và đề xuất lộ trình nâng cấp AI để dự báo nhu cầu tiêu thụ trong tương lai.
   Giảng viên hướng dẫn
   (Ký, Ghi rõ họ tên) Sinh viên thực hiện
   (Ký, Ghi rõ họ tên)

 
ĐÁNH GIÁ ĐỒ ÁN THỰC TẬP THỰC TẬP QUẢN TRỊ DỰ ÁN PHẦN MỀM
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
1.1. Khảo sát hiện trạng. 2
1.2. Xác định bài toán cần giải quyết. 2
1.3. Phân tích và đặc tả nghiệp vụ hệ thống. 3
1.3.1. Cơ cấu tổ chức người dùng. 3
1.3.2. Quy trình nghiệp vụ tổng quát. 4
CHƯƠNG 2: TRIỂN KHAI THỰC HIỆN - PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG 5
2.1. Tổng quan dự án. 5
2.1.1. Giới thiệu hệ thống website bán rượu “Rượu Phương”. 5
2.1.2. Mô tả hoạt động của hệ thống. 6
2.1.3. Ưu – nhược của hệ thống kinh doanh hiện tại. 6
2.1.4. Mục đích thiết kế website Rượu Phương. 6
2.2. Khảo sát và xác lập dự án. 7
2.2.1 Yêu cầu của dự án. 7
2.2.1.1. Mục tiêu của dự án. 7
2.2.1.2. Yêu cầu chức năng. 7
2.2.1.3. Yêu cầu phi chức năng. 9
2.2.2 Công nghệ sử dụng. 10
2.2.3 Hiệu quả dự kiến. 11
2.3. Xây dựng kế hoạch dự án. 11
2.3.1. Quyết định khởi động dự án. 11
2.3.2. Các mốc kiểm soát dự án. 12
2.3.3. Lập lịch trình theo dõi dự án. 12
2.4. Ước lượng rủi ro. 14
2.4.1. Rủi ro về kế hoạch. 14
2.4.2. Rủi ro về nhân lực và nội bộ. 15
2.4.3. Rủi ro về thực hiện. 15
2.5. Ước lượng chi phí. 16
2.5.1. Bảng ước lượng chi phí. 16
2.5.2. Bảng ước lượng thời gian. 17
2.6. Phân tích và thiết kế hệ thống theo hướng đối tượng 17
2.6.1. Xác định các Actor và Use Case tổng quát. 18
2.6.2. Phân tích chi tiết – Chức năng 1: quản lý danh mục. 20
2.6.2.1. Biểu đồ Use Case chức năng quản lý danh mục 20
2.6.2.2. Biểu đồ hoạt động chức năng quản lý danh mục. 21
2.6.2.3. Biểu đồ trình tự chức năng quản lý danh mục. 22
2.6.3. Phân tích chi tiết - Chức năng 2: quản lý sản phẩm. 22
2.6.3.1. Biểu đồ Use Case chức năng quản lý sản phẩm. 22
2.6.3.2. Biểu đồ hoạt động chức năng quản lý sản phẩm. 23
2.6.3.3. Biểu đồ trình tự chức năng quản lý sản phẩm 24
CHƯƠNG 3: CÀI ĐẶT VÀ KIỂM THỬ 25
3.1. Kiểm thử hệ thống. 25
3.1.1. Phương pháp kiểm thử. 26
3.1.2. Giới thiệu phương pháp kiểm thử Postman. 26
3.1.3. Kiểm thử API bằng Postman. 27
3.1.4. Kết quả kiểm thử. 29
3.2. Cài đặt. 30
3.2.1. Yêu cầu. 32
3.2.2. Hướng dẫn triển khai. 32
3.3. Giao diện hệ thống. 33
3.3.1. Giao diện trang chủ. 33
3.3.2. Giao diện đăng nhập. 34
3.3.3. Giao diện đăng ký. 34
3.3.4. Giao diện danh sách sản phẩm. 35
3.3.5. Giao diện chi tiết sản phẩm. 35
3.3.6. Giao diện giỏ hàng. 36
3.3.7. Giao diện danh sách yêu thích. 36
3.3.8. Giao diện liên hệ. 37
3.3.9. Giao diện quản lý sản phẩm. 37
3.3.10. Giao diện quản lý danh mục. 38
3.3.11. Giao diện quản lý người dùng. 38
3.4. Đánh giá về kết quả dự án. 38
3.4.1. Đánh giá về kết quả đạt được. 38
3.4.2. Một số vấn đề và bài học rút kinh nghiệm. 39
3.4.3. Bài học rút ra. 40
KẾT LUẬN 41
TÀI LIỆU THAM KHẢO 42

 
DANH MỤC TỪ VIẾT TẮT

Từ viết tắt Tên đầy đủ/ Giải thích
API Application Programming Interface – Giao diện lập trình ứng dụng
CDN Content Delivery Network – Mạng phân phối nội dung
COD Cash on Delivery – Thanh toán khi nhận hàng
CORS Cross-Origin Resource Sharing – Cơ chế chia sẻ tài nguyên giữa các nguồn khác nhau
CSDL Cơ sở dữ liệu
DTO Data Transfer Object – Đối tượng truyền dữ liệu
GCS Google Cloud Storage – Dịch vụ lưu trữ đám mây của Google
HTTP HyperText Transfer Protocol – Giao thức truyền tải siêu văn bản
JSON JavaScript Object Notation – Định dạng trao đổi dữ liệu
JWT JSON Web Token – Chuẩn mã thông báo dùng trong xác thực
NoSQL Not Only SQL – Cơ sở dữ liệu phi quan hệ
OTP One-Time Password – Mật khẩu dùng một lần
QR Quick Response – Mã phản hồi nhanh
REST Representational State Transfer – Kiểu kiến trúc API
SEO Search Engine Optimization – Tối ưu hóa công cụ tìm kiếm
SMTP Simple Mail Transfer Protocol – Giao thức gửi thư điện tử
SSL/TLS Secure Sockets Layer / Transport Layer Security – Giao thức bảo mật truyền tải
URL Uniform Resource Locator – Địa chỉ tài nguyên trên Internet
VND Việt Nam Đồng

 
DANH MỤC HÌNH ẢNH
Hình 2.1. Biểu đồ Use Case tổng quát 19
Hình 2.2. Biểu đồ Use Case chức năng quản lý danh mục 20
Hình 2.3. Đặc tả Use Case chức năng quản lý danh mục 20
Hình 2.4. Biểu đồ hoạt động chức năng quản lý danh mục 21
Hình 2.5. Biểu đồ trình tự chức năng quản lý danh mục 22
Hình 2.6. Biểu đồ Use Case chức năng quản lý sản phẩm 22
Hình 2.7. Đặc tả Use Case chức năng quản lý sản phẩm 23
Hình 2.8. Biểu đồ hoạt động chức năng quản lý sản phẩm 23
Hình 2.9. Biểu đồ trình tự chức năng quản lý sản phẩm 24
Hình 3.1. Giao diện trang chủ 33
Hình 3.2. Giao diện đăng nhập 34
Hình 3.3. Giao diện đăng ký 34
Hình 3.4. Giao diện danh sách sản phẩm 35
Hình 3.5. Giao diện chi tiết sản phẩm 35
Hình 3.6. Giao diện giỏ hàng 36
Hình 3.7. Giao diện danh sách yêu thích 36
Hình 3.8. Giao diện liên hệ 37
Hình 3.9. Giao diện quản lý sản phẩm 37
Hình 3.10. Giao diện quản lý danh mục 38
Hình 3.11. Giao diện quản lý người dùng 38

 
DANH MỤC BẢNG BIỂU
Bảng 1.1. Cơ cấu tổ chức người dùng 3
Bảng 2.1. Tổng quan về hệ thống 5
Bảng 2.2. Yêu cầu chức năng của hệ thống 8
Bảng 2.3. Yêu cầu phi chức năng của hệ thống 9
Bảng 2.4. Công nghệ sử dụng trong dự án 10
Bảng 2.5. Tổng quan khởi động dự án 11
Bảng 2.6. Các mốc kiểm soát dự án 12
Bảng 2.7. Lịch theo dõi dự án 13
Bảng 2.8. Ước lượng rủi do 14
Bảng 2.9. Rủi ro về kế hoạch 14
Bảng 2.10. Rủi ro về nhân lực và nội bộ 15
Bảng 2.11. Rủi ro về thực hiện 15
Bảng 2.12. Ước lượng chi phí 16
Bảng 2.13. Ước lượng thời gian 17
Bảng 2.14. Actor và Use Case tổng quát của hệ thống 18
Bảng 3.1. Tổng hợp API kiểm thử bằng Postman 27
Bảng 3.2. Kết quả kiểm thử 29

 
LỜI CẢM ƠN
Trong quá trình thực hiện báo cáo thực tập và xây dựng dự án website bán rượu này, em xin gửi lời cảm ơn chân thành nhất đến quý thầy cô khoa Công nghệ thông tin – Trường Đại học Điện lực, những người đã tận tình truyền dạy kiến thức nền tảng và tạo điều kiện thuận lợi cho em trong suốt những năm tháng học tập tại trường.
Đặc biệt, em xin bày tỏ lòng biết ơn sâu sắc nhất tới thầy TS. Phạm Đức Hồng. Với sự hướng dẫn tận tâm, những chỉ bảo quý báu về tư duy quản trị dự án cũng như định hướng kỹ thuật, thầy đã giúp em vượt qua những khó khăn trong quá trình nghiên cứu, triển khai hệ thống NestJS và Next.js để hoàn thành tốt báo cáo này. Những kiến thức và kinh nghiệm thực tế thầy truyền đạt không chỉ giúp ích cho đồ án mà còn là hành trang quý giá cho sự nghiệp phát triển phần mềm của em sau này.
Em cũng xin gửi lời cảm ơn đến tập thể lớp D17CNPM4 cùng các anh, chị và bạn bè đã luôn đồng hành, cùng thảo luận và sẻ chia những kinh nghiệm lập trình quý báu trong suốt khóa học.
Mặc dù đã nỗ lực hoàn thành bài báo cáo với tinh thần nghiêm túc và cầu thị nhất, song do kiến thức và kinh nghiệm thực tế còn hạn chế nên không tránh khỏi những thiếu sót. Em rất mong nhận được những ý kiến đóng góp, phê duyệt quý báu từ quý thầy cô để sản phẩm Website "Rượu Phương" ngày càng hoàn thiện hơn.
Em xin chân thành cảm ơn!
Hà Nội, ngày 16 tháng 02 năm 2026
Sinh viên thực hiện

Bùi Anh Quân

LỜI NÓI ĐẦU
Trong bối cảnh công nghệ thông tin phát triển mạnh mẽ và làn sóng chuyển đổi số ngày càng lan rộng, việc ứng dụng các hệ thống phần mềm vào hoạt động kinh doanh không còn là xu hướng mà đã trở thành yêu cầu tất yếu để tồn tại và phát triển. Đặc biệt đối với các ngành nghề kinh doanh truyền thống tại Việt Nam như rượu, nhu cầu thay thế các phương thức bán hàng trực tiếp và quản lý thủ công rời rạc bằng một nền tảng thương mại điện tử tích hợp, tự động hóa và có tính thẩm mỹ cao đang ngày càng trở nên cấp thiết hơn bao giờ hết.
Được sự phân công của nhà trường và sự tiếp nhận của đơn vị thực tập, em đã có cơ hội tiếp cận thực tế với môi trường phát triển phần mềm chuyên nghiệp, từ đó vận dụng các kiến thức đã học vào việc xây dựng một sản phẩm cụ thể, có giá trị ứng dụng thực tiễn cao. Qua quá trình đó, em đã chọn và thực hiện đề tài: "Quản Trị Dự Án Phát Triển Phần Mềm: Xây Dựng Website Bán Rượu".
Báo cáo này trình bày toàn bộ quá trình khảo sát, phân tích, thiết kế và triển khai hệ thống Website "Rượu Phương" — một ứng dụng web thương mại điện tử hiện đại, tích hợp các nghiệp vụ cốt lõi bao gồm: quản lý danh mục sản phẩm đặc thù (theo năm ủ và loại rượu), quản lý giỏ hàng, quy trình đặt hàng trực tuyến, hệ thống đánh giá sản phẩm và quản lý tương tác khách hàng.
Bên cạnh đó, hệ thống còn được tối ưu hóa bằng các công nghệ tiên tiến như kiến trúc Decoupled (Next.js & NestJS) giúp tăng tốc độ tải trang, hạ tầng Google Cloud Storage để quản lý hình ảnh sản phẩm chuyên nghiệp, cùng cơ chế bảo mật JWT và xác thực qua Email, nhằm mang lại một giải pháp kinh doanh toàn diện, hiệu quả và phù hợp với thực tế thị trường đồ uống cao cấp tại Việt Nam.

CHƯƠNG 1: KHẢO SÁT HIỆN TRẠNG VÀ XÁC LẬP DỰ ÁN
1.1. Khảo sát hiện trạng.
Đề tài: “QUẢN TRỊ DỰ ÁN PHÁT TRIỂN PHẦN MỀM: XÂY DỰNG WEBSITE BÁN RƯỢU RƯỢU PHƯƠNG”.
Qua khảo sát mô hình kinh doanh tại các cửa hàng rượu truyền thống, có thể thấy phần lớn hoạt động quản lý vẫn phụ thuộc vào phương pháp thủ công hoặc bán thủ công. Thông tin sản phẩm thường được ghi chép bằng sổ tay, bảng tính Excel hoặc lưu rời rạc trên nhiều thiết bị. Khi số lượng sản phẩm tăng lên, đặc biệt với các dòng rượu có nhiều thuộc tính như nồng độ, dung tích, năm sản xuất, xuất xứ, giá bán, số lượng trong kho và hình ảnh sản phẩm, việc tra cứu và cập nhật dữ liệu trở nên mất thời gian.
Hoạt động bán hàng trực tiếp phụ thuộc nhiều vào vị trí cửa hàng và lượng khách quen. Khách hàng mới khó tiếp cận thông tin sản phẩm nếu không đến trực tiếp cửa hàng hoặc liên hệ qua điện thoại, mạng xã hội. Điều này làm giảm khả năng mở rộng thị trường và khiến doanh nghiệp khó xây dựng hình ảnh chuyên nghiệp trên môi trường số.
Một vấn đề khác là quy trình tiếp nhận đơn hàng và chăm sóc khách hàng chưa được chuẩn hóa. Khi khách đặt hàng qua nhiều kênh như Facebook, Zalo hoặc gọi điện, nhân viên phải tổng hợp thủ công, dễ bỏ sót thông tin, sai địa chỉ giao hàng hoặc nhầm sản phẩm. Ngoài ra, dữ liệu phản hồi và liên hệ của khách hàng chưa được lưu trữ tập trung, khiến doanh nghiệp khó phân tích mức độ quan tâm của khách hàng và cải thiện chất lượng dịch vụ.
1.2. Xác định bài toán cần giải quyết.
Bài toán đặt ra là xây dựng một hệ thống website kinh doanh rượu cho hai nhóm người dùng chính: khách hàng và quản trị viên. Khách hàng cần có khả năng truy cập website, xem danh sách sản phẩm, lọc sản phẩm theo danh mục, giá bán hoặc đặc điểm sản phẩm, xem chi tiết sản phẩm, thêm vào giỏ hàng, nhập thông tin giao hàng và thao tác checkout mô phỏng với COD hoặc mã QR. Quản trị viên cần có công cụ để quản lý danh mục, bộ sưu tập, sản phẩm, hình ảnh, người dùng và thông tin liên hệ từ khách hàng. Phần tạo đơn hàng thật, lưu trạng thái đơn và xác nhận thanh toán được xác định là phạm vi phát triển tiếp theo.
Ngoài các yêu cầu nghiệp vụ, hệ thống cần đảm bảo các yêu cầu kỹ thuật quan trọng như bảo mật tài khoản, kiểm soát phân quyền, tối ưu tốc độ tải trang, hỗ trợ hiển thị trên nhiều thiết bị và dễ mở rộng trong tương lai. Do sản phẩm rượu là mặt hàng nhạy cảm, website cũng cần định hướng bổ sung thông tin cảnh báo, xác nhận độ tuổi và tuân thủ quy định pháp luật trong các phiên bản tiếp theo.
1.3. Phân tích và đặc tả nghiệp vụ hệ thống.
1.3.1. Cơ cấu tổ chức người dùng.
Bảng 1.1. Cơ cấu tổ chức người dùng
Tác nhân Vai trò Nhiệm vụ chính
Khách vãng lai Người chưa đăng nhập Xem trang chủ, danh sách sản phẩm, chi tiết sản phẩm, tìm kiếm, gửi liên hệ
Khách hàng Người dùng đã đăng nhập Đăng nhập, quản lý thông tin tài khoản, thêm sản phẩm vào giỏ hàng, thao tác checkout trên giao diện
Quản trị viên Người quản lý hệ thống Quản lý danh mục, bộ sưu tập, sản phẩm, người dùng, liên hệ và cấu hình nội dung
Hệ thống Các tiến trình xử lý nền Xác thực token, validate dữ liệu, gửi email, upload ảnh lên Google Cloud Storage, lưu dữ liệu MongoDB

1.3.2. Quy trình nghiệp vụ tổng quát.
• Quy trình xem và lựa chọn sản phẩm: Khách hàng truy cập website, xem trang chủ, chọn danh mục hoặc tìm kiếm sản phẩm, xem chi tiết sản phẩm và thêm sản phẩm vào giỏ hàng.
• Quy trình checkout hiện tại: Khách hàng mở trang thanh toán, nhập thông tin giao hàng, chọn tỉnh/thành - quận/huyện - phường/xã qua API địa chính Esgoo, chọn COD hoặc QR. Hiện tại giao diện đã xử lý hiển thị thành công/QR; phần gọi API Backend tạo đơn hàng đang được đánh dấu TODO trong mã nguồn.
• Quy trình quản trị sản phẩm: Admin đăng nhập khu vực quản trị, thêm mới hoặc cập nhật sản phẩm, upload hình ảnh lên Google Cloud Storage, lưu URL ảnh cùng dữ liệu sản phẩm trong MongoDB và hiển thị sản phẩm trên website.
• Quy trình quản lý liên hệ: Khách vãng lai gửi biểu mẫu liên hệ; Backend lưu nội dung vào collection contacts; Admin có màn hình xem danh sách/chi tiết liên hệ. Backend có API xử lý trạng thái liên hệ, tuy nhiên phần gọi trạng thái từ Frontend cần đồng bộ đúng phương thức endpoint trước khi xem là hoàn thiện hoàn toàn.

 
CHƯƠNG 2: TRIỂN KHAI THỰC HIỆN - PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG
2.1. Tổng quan dự án.
2.1.1. Giới thiệu hệ thống website bán rượu “Rượu Phương”.
Rượu Phương là hệ thống website thương mại điện tử phục vụ hoạt động kinh doanh rượu. Dự án được tổ chức theo hướng tách Frontend và Backend. Frontend Next.js chịu trách nhiệm hiển thị giao diện khách hàng, giao diện quản trị và quản lý trạng thái giỏ hàng [2]. Backend NestJS cung cấp REST API, xử lý xác thực, phân quyền, quản lý dữ liệu nghiệp vụ và kết nối MongoDB [1], [3].
Bảng 2.1. Tổng quan về hệ thống
Thuộc tính Giá trị
Tên dự án Website thương mại điện tử bán rượu Rượu Phương
Mã dự án DA-RP-01
Loại sản phẩm Web Application / E-commerce
Kiến trúc Decoupled: Next.js Frontend + NestJS REST API
Ngôn ngữ chính TypeScript
Cơ sở dữ liệu MongoDB / MongoDB Atlas
Lưu trữ ảnh Google Cloud Storage
Mô hình phát triển Iterative-Incremental
Thời gian thực hiện 8 tuần
Thuộc tính Giá trị
Vai trò thực hiện Fullstack Developer

2.1.2. Mô tả hoạt động của hệ thống.
Hệ thống hoạt động theo mô hình khách hàng - máy chủ. Người dùng truy cập website qua trình duyệt. Frontend Next.js hiển thị giao diện, xử lý tương tác, lưu trạng thái giỏ hàng bằng Redux Persist và gọi API tới Backend [2]. Backend NestJS tiếp nhận request, validate dữ liệu bằng DTO/class-validator, xác thực quyền truy cập bằng Passport.js/JWT, xử lý nghiệp vụ và thao tác với MongoDB thông qua Mongoose [1], [3], [4], [6].
Các tệp hình ảnh sản phẩm được xử lý qua module Storage và lưu trữ trên Google Cloud Storage [5]. Dữ liệu sản phẩm, danh mục, bộ sưu tập, cấu hình chung, người dùng, liên hệ và đánh giá được lưu theo schema MongoDB. Giỏ hàng, yêu thích sản phẩm và checkout hiện chủ yếu được xử lý ở Frontend; dự án chưa có Order Module để lưu đơn hàng, trạng thái giao hàng hoặc xác nhận thanh toán ở Backend.
2.1.3. Ưu – nhược của hệ thống kinh doanh hiện tại.
Các phương thức bán hàng hiện tại như bán trực tiếp, quản lý bằng Excel hoặc nhận đơn qua mạng xã hội có ưu điểm là chi phí ban đầu thấp, dễ triển khai và phù hợp với nhóm khách quen. Nhân viên có thể tư vấn trực tiếp, khách hàng được xem sản phẩm thực tế và quyết định mua nhanh chóng.
Tuy nhiên, các phương thức này bộc lộ nhiều hạn chế khi quy mô sản phẩm và số lượng khách hàng tăng. Dữ liệu sản phẩm không tập trung, khó cập nhật nhanh, dễ sai lệch tồn kho. Kênh bán hàng phụ thuộc vào vị trí cửa hàng, chưa tận dụng tốt khả năng tiếp cận khách hàng qua Internet. Quy trình tiếp nhận đơn hàng thủ công gây khó khăn khi phải xử lý nhiều đơn cùng lúc.
2.1.4. Mục đích thiết kế website Rượu Phương.
• Tập trung hóa dữ liệu sản phẩm, danh mục, bộ sưu tập, người dùng và liên hệ vào một hệ thống duy nhất.
• Hỗ trợ khách hàng tiếp cận sản phẩm nhanh hơn thông qua tìm kiếm, bộ lọc, phân loại và giao diện responsive.
• Tự động hóa các thao tác quản trị thường gặp như tạo sản phẩm, cập nhật sản phẩm, upload ảnh, quản lý danh mục và xử lý liên hệ.
• Tạo nền tảng để mở rộng các chức năng đơn hàng, thanh toán trực tuyến, quản lý kho nâng cao, khuyến mãi và hoàn thiện đánh giá sản phẩm trong tương lai.
2.2. Khảo sát và xác lập dự án.
2.2.1 Yêu cầu của dự án.
2.2.1.1. Mục tiêu của dự án.
• Xây dựng giao diện khách hàng hiện đại, dễ sử dụng, phù hợp với đặc thù sản phẩm rượu.
• Cho phép khách hàng tìm kiếm, lọc, xem chi tiết sản phẩm, thêm vào giỏ hàng và thao tác checkout ở mức giao diện.
• Xây dựng khu vực quản trị giúp Admin quản lý dữ liệu sản phẩm, danh mục, bộ sưu tập, người dùng và liên hệ.
• Tích hợp xác thực người dùng bằng email/mật khẩu, JWT và bcrypt để bảo vệ mật khẩu.
• Lưu trữ hình ảnh sản phẩm trên Google Cloud Storage nhằm giảm tải cho máy chủ ứng dụng.
• Thiết kế cơ sở dữ liệu MongoDB linh hoạt, phù hợp với dữ liệu sản phẩm có nhiều thuộc tính thay đổi.
• Ghi nhận rõ các phần chưa hoàn thiện để đưa vào kế hoạch phát triển tiếp theo.
2.2.1.2. Yêu cầu chức năng.

 
Bảng 2.2. Yêu cầu chức năng của hệ thống
Tên yêu cầu Trạng thái theo mã nguồn Mô tả
Đăng ký tài khoản Đã có giao diện/API Khách hàng tạo tài khoản, kích hoạt tài khoản và đăng nhập
Đăng nhập Đã có Đăng nhập email/mật khẩu; Backend sử dụng Passport/JWT
Xem danh sách sản phẩm Đã có Hiển thị sản phẩm, phân trang/tìm kiếm theo API
Tìm kiếm/lọc sản phẩm Đã có một phần Tìm kiếm, lọc theo danh mục và tham số sản phẩm
Chi tiết sản phẩm Đã có Hiển thị thông tin sản phẩm, ảnh, giá, mô tả
Giỏ hàng Đã có Frontend Quản lý giỏ hàng bằng Redux Persist
Checkout COD/QR Đã có giao diện, chưa lưu Backend Trang checkout có địa chỉ Esgoo, COD/QR/VietQR hiển thị; chưa có Order Module ở Backend
Quản lý sản phẩm Đã có Admin thêm/sửa/xóa sản phẩm, upload ảnh
Quản lý danh mục Đã có Admin quản lý categories
Quản lý bộ sưu tập Đã có Admin quản lý collections hiển thị trang chủ
Quản lý người dùng Đã có Admin quản lý users
Tên yêu cầu Trạng thái theo mã nguồn Mô tả
Quản lý liên hệ Đã có, cần đồng bộ resolve Khách gửi liên hệ; Admin xem danh sách/chi tiết; endpoint xử lý trạng thái cần đồng bộ PATCH ở Frontend
Quản lý đơn hàng Chưa hoàn thiện Chưa có module orders trong Backend, cần phát triển thêm
Đánh giá sản phẩm Có khung Backend, chưa hoàn thiện Có schema/controller và API đọc theo sản phẩm; create/update/delete trong service chưa xử lý thật, Frontend chưa tích hợp đầy đủ
Thống kê doanh thu Định hướng Chưa có dữ liệu đơn hàng thực nên thống kê doanh thu mới ở mức định hướng

2.2.1.3. Yêu cầu phi chức năng.
Bảng 2.3. Yêu cầu phi chức năng của hệ thống
Yêu cầu Mô tả
Hiệu năng Trang danh sách và chi tiết sản phẩm cần tải nhanh trong điều kiện mạng ổn định; API phản hồi nhanh với các truy vấn phổ biến.
Bảo mật Sử dụng JWT, bcrypt, Passport.js, guard phân quyền Admin/Customer và cấu hình CORS theo domain cho phép.
Khả năng mở rộng Kiến trúc module hóa, tách frontend/backend, dễ bổ sung module Orders, Reviews, Promotion, Payment.
Yêu cầu Mô tả
Tương thích Giao diện responsive trên desktop, tablet và mobile; hỗ trợ các trình duyệt phổ biến.
Dễ bảo trì Mã nguồn TypeScript, tổ chức theo module, DTO validation và tách controller/service/schema rõ ràng.
Tính chính xác Dữ liệu sản phẩm, danh mục, bộ sưu tập, người dùng và liên hệ phải cập nhật nhất quán.

2.2.2 Công nghệ sử dụng.
Bảng 2.4. Công nghệ sử dụng trong dự án
Lớp Công nghệ Mục đích
Backend NestJS 10, TypeScript Xây dựng REST API, tổ chức code theo module, service, controller
Backend Mongoose 8 Kết nối và thao tác dữ liệu MongoDB
Backend Passport.js, JWT, bcrypt Xác thực, phân quyền và bảo vệ mật khẩu
Backend @google-cloud/storage Upload và quản lý hình ảnh sản phẩm trên Google Cloud Storage
Backend @nestjs-modules/mailer, Nodemailer, Handlebars Gửi email đăng ký, quên mật khẩu, liên hệ
Frontend Next.js 15, React 18, TypeScript Xây dựng giao diện, routing, tối ưu tốc độ tải trang
Frontend TailwindCSS, HeroUI, Framer Motion Thiết kế giao diện responsive, hiện đại
Frontend Redux Toolkit, Redux Persist Quản lý trạng thái giỏ hàng và lưu trạng thái qua phiên
Lớp Công nghệ Mục đích
Frontend Formik, Yup Xử lý form và validate dữ liệu
Database MongoDB Lưu trữ dữ liệu NoSQL linh hoạt
Tooling Git/GitHub, Postman Quản lý mã nguồn và kiểm thử API

2.2.3 Hiệu quả dự kiến.
• Giảm thời gian tra cứu, cập nhật và quản lý dữ liệu sản phẩm so với phương pháp thủ công.
• Mở rộng kênh bán hàng trực tuyến, giúp khách hàng tiếp cận sản phẩm mọi lúc, mọi nơi.
• Tăng tính chuyên nghiệp của cửa hàng thông qua website có giao diện rõ ràng, chuẩn hóa danh mục và thông tin sản phẩm.
• Tạo dữ liệu tập trung cho sản phẩm, danh mục, bộ sưu tập, người dùng và liên hệ.
• Làm nền tảng để bổ sung Order Module, xác nhận thanh toán, quản lý trạng thái đơn, hoàn thiện Reviews Module và thống kê doanh thu trong các phiên bản sau.
2.3. Xây dựng kế hoạch dự án.
2.3.1. Quyết định khởi động dự án.
Bảng 2.5. Tổng quan khởi động dự án
Thuộc tính Giá trị
Tên dự án Xây dựng website thương mại điện tử Rượu Phương
Mã dự án DA-RP-01
Mục tiêu Số hóa dữ liệu sản phẩm, xây dựng website bán hàng và khu vực quản trị
Thời gian 8 tuần
Thuộc tính Giá trị
Mô hình Iterative-Incremental
Nhân sự 01 Fullstack Developer
Sản phẩm bàn giao Mã nguồn Frontend, Backend, CSDL mẫu, tài liệu báo cáo, kết quả kiểm thử

2.3.2. Các mốc kiểm soát dự án.
Bảng 2.6. Các mốc kiểm soát dự án
Mốc Nội dung Kết quả cần đạt
M1 Hoàn thành khảo sát và đặc tả yêu cầu Danh sách yêu cầu, phạm vi dự án
M2 Hoàn thành thiết kế dữ liệu và kiến trúc Schema MongoDB, kiến trúc frontend/backend
M3 Hoàn thành Backend core Auth, Users, Products, Categories, Collections, Contacts, Storage API; Reviews ở mức khung ban đầu
M4 Hoàn thành Frontend khách hàng Trang chủ, danh sách, chi tiết, giỏ hàng, checkout, liên hệ
M5 Hoàn thành Admin Dashboard Quản lý sản phẩm, danh mục, bộ sưu tập, người dùng, liên hệ
M6 Kiểm thử và hoàn thiện Bộ test Postman, sửa lỗi, xác định phần chưa hoàn thiện

2.3.3. Lập lịch trình theo dõi dự án.
Bảng 2.7. Lịch theo dõi dự án
Giai đoạn Công việc trọng tâm Thời gian
Khảo sát Thu thập yêu cầu, xác định phạm vi, viết mô tả nghiệp vụ Tuần 1
Thiết kế Thiết kế giao diện, kiến trúc hệ thống, schema dữ liệu Tuần 2
Backend Xây dựng API xác thực, người dùng, sản phẩm, danh mục, bộ sưu tập, liên hệ, upload ảnh; tạo khung reviews Tuần 3-4
Frontend Xây dựng giao diện khách hàng, giỏ hàng, checkout, liên hệ Tuần 5-6
Admin Xây dựng dashboard và các màn hình quản trị Tuần 7
Kiểm thử Kiểm thử API, sửa lỗi, cập nhật báo cáo theo thực tế mã nguồn Tuần 8

 
2.4. Ước lượng rủi ro.
Bảng 2.8. Ước lượng rủi ro
Rủi ro Xác xuất Ảnh hưởng Biện pháp giảm nhẹ
Phạm vi chức năng quá rộng Trung bình Cao Ưu tiên tính năng cốt lõi: sản phẩm, danh mục, giỏ hàng, liên hệ, quản trị
Chức năng đơn hàng chưa hoàn thiện Cao Cao Tách thành giai đoạn sau: thiết kế module Orders, API tạo đơn, trạng thái đơn
Ước lượng thời gian chưa chính xác Trung bình Trung bình Chia nhỏ task theo tuần, có buffer cho kiểm thử và sửa lỗi

2.4.1. Rủi ro về kế hoạch.
Bảng 2.9. Rủi ro về kế hoạch
Rủi ro Xác suất Ảnh hưởng Biện pháp giảm nhẹ
Sinh viên thiếu kinh nghiệm với công nghệ mới Trung bình Trung bình Dành thời gian nghiên cứu tài liệu, xây dựng mẫu thử trước khi tích hợp
Quá tải do thực hiện fullstack một mình Trung bình Cao Ưu tiên hoàn thiện luồng chính trước, hạn chế chức năng phụ
Thiếu thời gian viết báo cáo song song với code Trung bình Trung bình Ghi nhật ký công việc hằng tuần, cập nhật báo cáo theo từng giai đoạn

 
2.4.2. Rủi ro về nhân lực và nội bộ.
Bảng 2.10. Rủi ro về nhân lực và nội bộ
Rủi ro Xác suất Ảnh hưởng Biện pháp giảm nhẹ
Sinh viên thiếu kinh nghiệm với công nghệ mới Trung bình Trung bình Dành thời gian nghiên cứu tài liệu, xây dựng mẫu thử trước khi tích hợp
Quá tải do thực hiện fullstack một mình Trung bình Cao Ưu tiên hoàn thiện luồng chính trước, hạn chế chức năng phụ
Thiếu thời gian viết báo cáo song song với code Trung bình Trung bình Ghi nhật ký công việc hằng tuần, cập nhật báo cáo theo từng giai đoạn

2.4.3. Rủi ro về thực hiện.
Bảng 2.11. Rủi ro về thực hiện
Rủi ro Xác suất Ảnh hưởng Biện pháp giảm nhẹ
Lỗi upload ảnh lên Google Cloud Storage Trung bình Trung bình Kiểm tra credentials, tách Storage Module, log lỗi đầy đủ
Lỗi xác thực JWT hoặc phân quyền Trung bình Cao Viết guard riêng cho Admin, kiểm thử API cần quyền
Dữ liệu sản phẩm không đồng nhất Thấp Trung bình Dùng DTO validation và quy định rõ trường bắt buộc
Rủi ro Xác suất Ảnh hưởng Biện pháp giảm nhẹ
Checkout chưa lưu đơn thật Cao Cao Bổ sung Order schema, Order service, API tạo đơn và validate trạng thái đơn trong giai đoạn sau
Giao diện chưa tương thích mobile Trung bình Trung bình Kiểm thử responsive theo breakpoint, ưu tiên mobile-first

2.5. Ước lượng chi phí.
2.5.1. Bảng ước lượng chi phí.
Bảng 2.12. Ước lượng chi phí
Hạng mục Cách ước lượng Chi phí dự kiến
Phân tích yêu cầu và thiết kế 40 giờ x 25.000 VND 1.000.000 VND
Lập trình Backend 70 giờ x 25.000 VND 1.750.000 VND
Lập trình Frontend 70 giờ x 25.000 VND 1.750.000 VND
Kiểm thử và sửa lỗi 30 giờ x 25.000 VND 750.000 VND
Tài liệu và báo cáo 20 giờ x 25.000 VND 500.000 VND
Dịch vụ cloud free tier MongoDB Atlas, GCS, Vercel/Render 0 - 200.000 VND
Tổng dự kiến ~5.950.000 VND

2.5.2. Bảng ước lượng thời gian.
Bảng 2.13. Ước lượng thời gian
Công việc Thời lượng dự kiến Ghi chú
Khảo sát hiện trạng và xác định yêu cầu 5 ngày Thu thập yêu cầu và viết phạm vi
Thiết kế database và API 7 ngày Thiết kế schema, endpoint, guard
Xây dựng Backend 14 ngày Auth, users, products, categories, collections, contacts, storage; reviews mới ở mức khung
Xây dựng Frontend khách hàng 12 ngày Trang chủ, danh sách, chi tiết, giỏ hàng, checkout, liên hệ
Xây dựng Admin Dashboard 8 ngày Quản lý sản phẩm, danh mục, bộ sưu tập, người dùng, liên hệ
Kiểm thử và sửa lỗi 7 ngày Postman, responsive, kiểm tra bảo mật
Hoàn thiện báo cáo 3 ngày Tổng hợp kết quả và tài liệu

2.6. Phân tích và thiết kế hệ thống theo hướng đối tượng

 
2.6.1. Xác định các Actor và Use Case tổng quát.
Bảng 2.14. Actor và Use Case tổng quát của hệ thống
Actor Vai trò Use Case chính
Khách vãng lai Người dùng chưa đăng nhập Xem sản phẩm, tìm kiếm, xem chi tiết, gửi liên hệ, đăng ký
Khách hàng Người dùng đã đăng nhập Đăng nhập, quản lý tài khoản, giỏ hàng, checkout, yêu thích sản phẩm
Quản trị viên Người quản trị hệ thống Quản lý danh mục, bộ sưu tập, sản phẩm, người dùng, liên hệ
Hệ thống Các tiến trình tự động Xác thực token, gửi email, lưu ảnh lên GCS, validate dữ liệu

Use Case tổng quát gồm các nhóm chức năng: xác thực, xem sản phẩm, yêu thích sản phẩm, giỏ hàng - checkout giao diện, liên hệ và quản trị hệ thống. Các chức năng quản trị chỉ được thực hiện bởi Admin sau khi đăng nhập và xác thực token hợp lệ.

Hình 2.1. Biểu đồ Use Case tổng quát

Biểu đồ Use Case tổng quát mô tả mối quan hệ giữa các tác nhân với những nhóm chức năng chính của hệ thống. Khách vãng lai có thể xem và tìm kiếm sản phẩm, gửi liên hệ hoặc đăng ký tài khoản. Khách hàng sau khi đăng nhập có thể quản lý tài khoản, thêm sản phẩm vào giỏ hàng và thao tác checkout ở giao diện. Quản trị viên có quyền truy cập khu vực quản trị để quản lý dữ liệu sản phẩm, danh mục, bộ sưu tập, người dùng và liên hệ. Các chức năng quản trị đều yêu cầu xác thực JWT và phân quyền hợp lệ.
2.6.2. Phân tích chi tiết – Chức năng 1: quản lý danh mục.
2.6.2.1. Biểu đồ Use Case chức năng quản lý danh mục

Hình 2.2. Biểu đồ Use Case chức năng quản lý danh mục

Đặc tả Use Case chức năng quản lý danh mục:

Hình 2.3. Đặc tả Use Case chức năng quản lý danh mục

 
2.6.2.2. Biểu đồ hoạt động chức năng quản lý danh mục.

Hình 2.4. Biểu đồ hoạt động chức năng quản lý danh mục

Mô tả chi tiết các bước chức năng quản lý danh mục
Bước 1: Truy cập giao diện quản lý danh mục.
Bước 2: Nhấn chọn thao tác Thêm hoặc Sửa.
Bước 3: Cập nhật thông tin (Tên danh mục, Thứ tự ưu tiên, Cờ hiển thị trang chủ).
Bước 4: Hệ thống tự động tính toán URL SEO dựa trên tên mới.
Bước 5: Xác nhận lưu thông tin.
Bước 6: Hệ thống cập nhật lại cây danh mục trên toàn bộ website.
2.6.2.3. Biểu đồ trình tự chức năng quản lý danh mục.

Hình 2.5. Biểu đồ trình tự chức năng quản lý danh mục
2.6.3. Phân tích chi tiết - Chức năng 2: quản lý sản phẩm.
2.6.3.1. Biểu đồ Use Case chức năng quản lý sản phẩm.

Hình 2.6. Biểu đồ Use Case chức năng quản lý sản phẩm

Đặc tả Use Case chức năng quản lý sản phẩm:

Hình 2.7. Đặc tả Use Case chức năng quản lý sản phẩm
2.6.3.2. Biểu đồ hoạt động chức năng quản lý sản phẩm.

Hình 2.8. Biểu đồ hoạt động chức năng quản lý sản phẩm

Mô tả chi tiết các bước chức năng quản lý sản phẩm:
Bước 1: Admin đăng nhập vào trang quản trị, chọn quản lý Sản phẩm.
Bước 2: Nhấn nút "Add New" để mở Modal/Trang thêm mới.
Bước 3: Điền thông tin (Tên rượu, Giá, Sale off, Danh mục, Mô tả...).
Bước 4: Chọn ảnh sản phẩm từ máy tính.
Bước 5: Nhấn "Save". Hệ thống xử lý logic backend (GCS Upload -> MongoDB Save).
Bước 6: Hệ thống thông báo "Thao tác thành công" và làm mới danh sách.
2.6.3.3. Biểu đồ trình tự chức năng quản lý sản phẩm

Hình 2.9. Biểu đồ trình tự chức năng quản lý sản phẩm

 
CHƯƠNG 3: CÀI ĐẶT VÀ KIỂM THỬ
3.1. Kiểm thử hệ thống.
Hệ thống được phát triển và vận hành dựa trên một hệ sinh thái công nghệ hiện đại, được lựa chọn kỹ lưỡng nhằm đáp ứng yêu cầu về hiệu năng, bảo mật và khả năng mở rộng:
• Ngôn ngữ và Môi trường: Backend sử dụng Node.js với framework NestJS 10, viết bằng TypeScript [1], đảm bảo khả năng xử lý nghiệp vụ ổn định và dễ mở rộng nhờ kiến trúc module hóa. Frontend được xây dựng bằng Next.js 15 (TypeScript, React 18) [2], [8], mang lại giao diện hiện đại, thân thiện và hỗ trợ server-side rendering để tối ưu hiệu năng. Quá trình thực nghiệm được triển khai trên hệ điều hành Windows 11.
• Cơ sở dữ liệu: Hệ thống sử dụng MongoDB 5.0 — cơ sở dữ liệu NoSQL hướng tài liệu [3], được triển khai trong Docker container. MongoDB lưu trữ toàn bộ dữ liệu nghiệp vụ bao gồm thông tin người dùng, sản phẩm, danh mục, bộ sưu tập, đánh giá, liên hệ và cấu hình hệ thống. MongoDB được lựa chọn nhờ cấu trúc document linh hoạt, phù hợp với dữ liệu sản phẩm có nhiều thuộc tính đa dạng.
• Hệ thống lưu trữ hình ảnh: Google Cloud Storage (GCS) đóng vai trò là dịch vụ lưu trữ đám mây cho toàn bộ hình ảnh sản phẩm, ảnh đại diện người dùng và ảnh bộ sưu tập [5]. GCS cho phép upload hình ảnh nhanh chóng, cung cấp URL công khai với CDN toàn cầu, đồng thời đảm bảo khả năng mở rộng khi số lượng hình ảnh tăng lên.
• Dịch vụ email: Gmail SMTP được tích hợp để gửi email tự động phục vụ xác thực tài khoản (mã OTP), đặt lại mật khẩu và phản hồi liên hệ khách hang [7]. Kết nối qua giao thức SMTP với SSL/TLS trên port 465, nội dung email sử dụng Handlebars template.
• Dịch vụ chống spam: Google reCAPTCHA v2 được tích hợp để bảo vệ chức năng quên mật khẩu khỏi các hành vi tấn công tự động và spam.
• Bảo mật: Hệ thống áp dụng cơ chế xác thực JWT (JSON Web Token) kết hợp Passport.js, giúp đảm bảo an toàn cho thông tin người dung [6]. Mật khẩu được mã hóa bằng bcrypt. JWT cho phép phân quyền theo vai trò (Admin, Customer), đồng thời ngăn chặn các hành vi truy cập trái phép. CORS được cấu hình chặt chẽ chỉ cho phép frontend truy cập từ domain được chỉ định.
3.1.1. Phương pháp kiểm thử.
Quá trình kiểm thử tập trung vào tính đúng đắn của nghiệp vụ, tính ổn định của API và khả năng sử dụng của giao diện. Dự án áp dụng kiểm thử thủ công kết hợp kiểm thử API bằng Postman. Các nhóm kiểm thử gồm kiểm thử chức năng, kiểm thử phân quyền, kiểm thử dữ liệu đầu vào, kiểm thử responsive và kiểm thử luồng nghiệp vụ end-to-end ở mức Frontend.
• Kiểm thử chức năng: kiểm tra đăng ký, đăng nhập, xem sản phẩm, yêu thích sản phẩm, giỏ hàng, checkout giao diện, quản lý sản phẩm.
• Kiểm thử API: gửi request bằng Postman, kiểm tra status code, response body và dữ liệu trong MongoDB.
• Kiểm thử phân quyền: đảm bảo API quản trị chỉ cho phép Admin truy cập.
• Kiểm thử giao diện: kiểm tra hiển thị trên desktop, tablet và mobile.
• Kiểm thử giới hạn: ghi nhận rõ các phần chưa hoàn thiện như Orders, xác nhận thanh toán, thống kê doanh thu và Reviews service để tránh mô tả vượt quá mã nguồn thực tế.
3.1.2. Giới thiệu phương pháp kiểm thử Postman.
Postman là công cụ hỗ trợ kiểm thử REST API, cho phép tạo request với nhiều phương thức HTTP như GET, POST, PUT, PATCH, DELETE; cấu hình header Authorization; truyền dữ liệu JSON; lưu collection và kiểm tra phản hồi từ server. Trong dự án Rượu Phương, Postman được sử dụng để kiểm thử các nhóm API xác thực, người dùng, sản phẩm, danh mục, bộ sưu tập, liên hệ và upload ảnh.

 
3.1.3. Kiểm thử API bằng Postman.
Bảng 3.1. Tổng hợp API kiểm thử bằng Postman
Nhóm API Endpoint mẫu Phương thức Mục đích kiểm thử
Auth /auth/login POST Kiểm tra đăng nhập, nhận JWT và thông tin người dùng
Auth /auth/signup, /auth/active, /auth/forgot-password POST Kiểm tra đăng ký, kích hoạt tài khoản, quên/đặt lại mật khẩu
Users /users/find, /users/:id GET/POST/PUT/DELETE Admin quản lý người dùng
Products /products, /products/find, /products/detail/:id GET Lấy danh sách, tìm kiếm và xem chi tiết sản phẩm
Products /products, /products/:id POST/PUT/DELETE Admin tạo, cập nhật và xóa sản phẩm
Nhóm API Endpoint mẫu Phương thức Mục đích kiểm thử
Categories /categories/search, /categories/find, /categories/:id GET/POST/PUT/DELETE Quản lý danh mục
Collections /collections, /collections/find, /collections/:id GET/POST/PUT/DELETE Quản lý bộ sưu tập/banner
Contact /contact, /contact/:id, /contact/:id/resolve GET/POST/PATCH/DELETE Gửi liên hệ, xem liên hệ và xử lý trạng thái liên hệ
Storage /storage/upload, /storage/delete POST/DELETE Upload/xóa ảnh sản phẩm trên Google Cloud Storage
Reviews

    /reviews/product/:productId	GET	Đọc đánh giá theo sản phẩm; các thao tác tạo/sửa/xóa chưa hoàn thiện service

3.1.4. Kết quả kiểm thử.
Bảng 3.2. Kết quả kiểm thử
STT Chức năng Kết quả mong đợi Trạng thái
1 Đăng nhập bằng email/mật khẩu Trả về access token và thông tin user Đạt
2 Đăng ký, kích hoạt, quên mật khẩu API xử lý luồng tài khoản và gửi email theo cấu hình Đạt theo phạm vi kiểm thử thủ công
3 Xem danh sách/chi tiết sản phẩm Hiển thị sản phẩm đúng theo dữ liệu MongoDB Đạt
4 Lọc/tìm kiếm sản phẩm Danh sách thay đổi theo tham số name, category, minPrice, maxPrice Đạt một phần
5 Thêm sản phẩm vào giỏ hàng/yêu thích Sản phẩm được lưu trong state Frontend bằng Redux Persist Đạt
6 Checkout COD/QR Hiển thị form giao hàng, chọn COD/QR và modal thành công/QR Đạt giao diện, chưa lưu Backend
7 Admin thêm/cập nhật sản phẩm Dữ liệu sản phẩm được lưu/cập nhật và hiển thị lại trên website Đạt
8 Upload ảnh lên GCS Trả về URL ảnh để lưu cùng sản phẩm Đạt
9 API quản trị khi không có token Trả về lỗi Unauthorized/không cho truy cập Đạt
STT Chức năng Kết quả mong đợi Trạng thái
10 Gửi liên hệ Liên hệ được lưu vào collection contacts Đạt
11 Xử lý trạng thái liên hệ Frontend gọi đúng method PATCH tới endpoint resolve Cần đồng bộ lại do service Frontend đang dùng PUT
12 Tạo đơn hàng Backend Đơn hàng được lưu với trạng thái chờ xác nhận Chưa hoàn thiện
13 Tạo/sửa/xóa đánh giá Review được lưu/cập nhật/xóa thật trong MongoDB Chưa hoàn thiện service

3.2. Cài đặt.
Quá trình cài đặt hệ thống được tiến hành theo từng bước, đảm bảo sự phối hợp nhịp nhàng giữa các thành phần frontend, backend, cơ sở dữ liệu và các dịch vụ bên thứ ba.
Trước hết, cơ sở dữ liệu MongoDB được khởi tạo thông qua Docker Compose. File docker-compose.yml định nghĩa service MongoDB với image mongo:5.0.15, thiết lập tài khoản root và tên database ban đầu. Dữ liệu được lưu trữ persistent trong Docker volume mongodb_data_container, đảm bảo không bị mất khi container khởi động lại. MongoDB chạy trên port 27017, backend kết nối thông qua connection string được cấu hình trong file .env. Hệ thống có sẵn dữ liệu mẫu cho 7 collection: users, products, categories, collections, reviews, contacts và commons, phục vụ cho việc kiểm thử và demo.
Tiếp theo, backend được triển khai bằng NestJS với các module chức năng độc lập. Module: AuthModule xử lý đăng nhập, đăng ký, kích hoạt tài khoản, quên mật khẩu và đăng nhập Google. Module: UsersModule quản lý người dùng. Module: ProductsModule quản lý sản phẩm rượu. Module: CategoriesModule quản lý danh mục. Module: CollectionsModule quản lý bộ sưu tập. Module: ContactModule xử lý liên hệ khách hàng. Module: StorageModule quản lý upload và xóa hình ảnh trên Google Cloud Storage. Module: ReviewsModule quản lý đánh giá sản phẩm. Module: CommonModule cung cấp dữ liệu cấu hình chung. Thư viện Mongoose được sử dụng để định nghĩa schema và tương tác với MongoDB. Backend chạy trên port 8081 với prefix API /api/v1. Hệ thống cũng tích hợp Swagger/OpenAPI tại đường dẫn /api/docs, tự động tạo tài liệu API giúp việc kiểm thử và phát triển thuận tiện hơn.
Ở phía frontend, hệ thống được xây dựng bằng Next.js 15 với TypeScript và React 18. Các trang giao diện được chia thành hai nhóm chính: trang khách hàng (trang chủ, danh sách sản phẩm, chi tiết sản phẩm, giỏ hàng, thanh toán, yêu thích, liên hệ) và trang quản trị (quản lý sản phẩm, danh mục, bộ sưu tập, người dùng, liên hệ). Giao diện được thiết kế theo nguyên tắc trực quan, dễ sử dụng, sử dụng thư viện HeroUI kết hợp TailwindCSS để tạo giao diện responsive, và Framer Motion để tạo các hiệu ứng tương tác mượt mà. Quản lý trạng thái ứng dụng sử dụng Redux Toolkit kết hợp Redux Persist để duy trì dữ liệu qua các phiên làm việc. Frontend giao tiếp với backend thông qua Axios HTTP client với hệ thống interceptor tự động gắn JWT token vào mỗi request và xử lý lỗi xác thực (401).
Về tích hợp các dịch vụ bên thứ ba, Google Cloud Storage được cấu hình thông qua file service account JSON (googleservice-account.json), kết nối đến bucket wine_data_img. Backend sử dụng thư viện @google-cloud/storage để thực hiện upload file dạng stream và xóa file theo URL. Hệ thống có cron job chạy lúc 1 giờ sáng mỗi ngày để tự động dọn dẹp hình ảnh thừa trên GCS. Gmail SMTP được cấu hình trong MailerModule với host smtp.gmail.com, port 465, kết nối SSL. Ba template email Handlebars (register.hbs, forgot_password.hbs, contact.hbs) được đặt trong thư mục src/mail/templates/. Google reCAPTCHA được cấu hình với secret key ở phía backend và site key ở phía frontend, xác minh token thông qua API siteverify của Google.
Cuối cùng, hệ thống bảo mật được triển khai đầy đủ. JWT được cấu hình với secret key và thời hạn token 3600 giây (1 giờ). Passport.js sử dụng hai strategy: LocalStrategy cho đăng nhập email/password và JwtStrategy cho xác thực token. JwtAdminAuthGuard được đăng ký làm global guard, mặc định yêu cầu quyền Admin cho mọi route. Các route công khai được đánh dấu bằng decorator @Public() để bỏ qua xác thực. Mật khẩu người dùng được mã hóa bằng thuật toán bcrypt trước khi lưu vào MongoDB. Middleware ở phía frontend kiểm tra token trong cookie để điều hướng người dùng — nếu chưa đăng nhập mà truy cập trang admin sẽ bị redirect về trang đăng nhập, nếu đã đăng nhập mà truy cập trang login sẽ được redirect về trang chủ.
3.2.1. Yêu cầu.
Để cài đặt và chạy hệ thống website Rượu Phương, máy tính phát triển cần đáp ứng một số yêu cầu cơ bản về phần cứng, phần mềm và dịch vụ hỗ trợ. Về phần cứng, máy nên sử dụng CPU Intel Core i5 hoặc tương đương, RAM tối thiểu 8GB và ổ SSD còn trống khoảng 10GB để đảm bảo quá trình cài đặt thư viện, chạy Backend và Frontend diễn ra ổn định.
Về phần mềm, dự án cần cài đặt Node.js phiên bản LTS, npm, Git, trình duyệt Chrome hoặc Edge để kiểm tra giao diện, Postman để kiểm thử API và một trình soạn thảo mã nguồn như Visual Studio Code hoặc Cursor. Ngoài ra, hệ thống cần sử dụng MongoDB Atlas hoặc MongoDB local để lưu trữ dữ liệu, Google Cloud Storage để lưu ảnh sản phẩm.
3.2.2. Hướng dẫn triển khai.
Quá trình triển khai hệ thống được chia thành hai phần chính là Backend và Frontend. Trước tiên, người phát triển tải mã nguồn dự án về máy bằng lệnh git clone <repository>. Sau đó, mở thư mục Backend của dự án bằng lệnh cd ruouque-backend và cài đặt các thư viện cần thiết bằng npm install.
Sau khi cài đặt thư viện Backend, cần tạo file .env để khai báo các biến môi trường như đường dẫn MongoDB, khóa JWT, cấu hình Google Cloud Storage và cấu hình gửi mail. Khi cấu hình hoàn tất, Backend được khởi động ở chế độ phát triển bằng lệnh npm run start:dev. Nếu quá trình khởi động thành công, hệ thống Backend sẽ sẵn sàng tiếp nhận request từ Frontend và Postman.
Tiếp theo, người phát triển chuyển sang thư mục Frontend bằng lệnh cd ruouphuong và chạy npm install để cài đặt các thư viện giao diện. Sau đó tạo file .env hoặc .env.local để khai báo NEXT_PUBLIC_API_URL trỏ tới địa chỉ Backend. Cuối cùng, chạy lệnh npm run dev để khởi động Frontend và truy cập website thông qua trình duyệt.
Quy trình triển khai tổng quát có thể tóm tắt như sau:
• Tải mã nguồn dự án về máy.
• Cài đặt thư viện cho Backend.
• Cấu hình file .env cho Backend.
• Khởi động Backend bằng npm run start:dev.
• Cài đặt thư viện cho Frontend.
• Cấu hình file môi trường cho Frontend.
• Khởi động Frontend bằng npm run dev và kiểm tra hệ thống trên trình duyệt.
3.3. Giao diện hệ thống.
3.3.1. Giao diện trang chủ.

Hình 3.1. Giao diện trang chủ
3.3.2. Giao diện đăng nhập.

Hình 3.2. Giao diện đăng nhập
3.3.3. Giao diện đăng ký.

Hình 3.3. Giao diện đăng ký
3.3.4. Giao diện danh sách sản phẩm.

Hình 3.4. Giao diện danh sách sản phẩm
3.3.5. Giao diện chi tiết sản phẩm.

Hình 3.5. Giao diện chi tiết sản phẩm
3.3.6. Giao diện giỏ hàng.

Hình 3.6. Giao diện giỏ hàng
3.3.7. Giao diện danh sách yêu thích.

Hình 3.7. Giao diện danh sách yêu thích
3.3.8. Giao diện liên hệ.

Hình 3.8. Giao diện liên hệ
3.3.9. Giao diện quản lý sản phẩm.

Hình 3.9. Giao diện quản lý sản phẩm
3.3.10. Giao diện quản lý danh mục.

Hình 3.10. Giao diện quản lý danh mục
3.3.11. Giao diện quản lý người dùng.

Hình 3.11. Giao diện quản lý người dùng
3.4. Đánh giá về kết quả dự án.
3.4.1. Đánh giá về kết quả đạt được.
Dự án website thương mại điện tử Rượu Phương đã hoàn thành nhiều mục tiêu chính trong phạm vi thực tập. Hệ thống đáp ứng được các nghiệp vụ cốt lõi như hiển thị sản phẩm, tìm kiếm/lọc sản phẩm, yêu thích sản phẩm, quản lý giỏ hàng, checkout ở phía giao diện, quản lý danh mục, bộ sưu tập, sản phẩm, người dùng, liên hệ và upload ảnh.
• Về mặt chức năng: hoàn thiện các module chính phục vụ khách hàng và Admin, đặc biệt là Product, Category, Collection, Contact, User và Storage; Reviews Module đã có cấu trúc ban đầu nhưng chưa được xem là hoàn thiện nghiệp vụ.
• Về mặt kỹ thuật: áp dụng kiến trúc Decoupled, sử dụng TypeScript ở cả Frontend và Backend, lưu trữ dữ liệu bằng MongoDB và ảnh bằng Google Cloud Storage.
• Về mặt giao diện: xây dựng giao diện responsive, dễ sử dụng, phù hợp với đặc thù thương mại điện tử.
• Về mặt quản trị dự án: vận dụng được các nội dung lập kế hoạch, ước lượng chi phí, quản lý rủi ro, phân tích thiết kế, kiểm thử và đánh giá kết quả.
3.4.2. Một số vấn đề và bài học rút kinh nghiệm.
Trong quá trình rà soát mã nguồn, có thể nhận thấy một số phần đang ở trạng thái chưa hoàn thiện hoặc mới hoàn thiện ở phía giao diện. Cụ thể, trang checkout đã có form nhập địa chỉ, chọn COD/QR và thông báo thành công, nhưng trong mã nguồn vẫn còn ghi chú TODO gọi API Backend tạo đơn hàng. Backend hiện tại chưa có Order Module. Reviews Module đã có controller/schema và API đọc review theo sản phẩm, nhưng các hàm tạo, cập nhật, xóa trong service còn trả về chuỗi mẫu, nên chưa thể mô tả là chức năng đánh giá hoàn chỉnh.
• Cần xác định phạm vi rõ ngay từ đầu để tránh phát sinh quá nhiều chức năng ngoài kế hoạch.
• Cần thiết kế API và schema dữ liệu trước khi lập trình giao diện để giảm việc sửa đổi lặp lại.
• Cần kiểm thử phân quyền ngay từ sớm vì các API quản trị có liên quan trực tiếp đến an toàn dữ liệu.
• Cần đối chiếu báo cáo với mã nguồn thực tế để tránh ghi các chức năng chưa hoàn thành là đã hoàn thành.
3.4.3. Bài học rút ra.
Qua dự án, em rút ra rằng quản trị dự án phần mềm không chỉ là viết mã nguồn mà còn bao gồm toàn bộ quá trình xác định vấn đề, phân tích yêu cầu, lựa chọn công nghệ, chia nhỏ công việc, kiểm soát tiến độ, quản lý rủi ro và đánh giá kết quả. Một dự án có phạm vi vừa phải nhưng được tổ chức tốt sẽ dễ hoàn thành hơn một dự án có nhiều chức năng nhưng thiếu kế hoạch cụ thể.
Việc áp dụng mô hình Iterative-Incremental giúp dự án tiến triển theo từng vòng lặp nhỏ. Sau mỗi vòng lặp, hệ thống có thêm một nhóm chức năng hoàn chỉnh để kiểm thử và điều chỉnh. Cách làm này phù hợp với sinh viên thực hiện dự án fullstack vì có thể kiểm soát chất lượng từng phần và phát hiện lỗi sớm.

 
KẾT LUẬN
Dự án “Website bán rượu Rượu Phương” được xây dựng nhằm giải quyết bài toán số hóa hoạt động kinh doanh của cửa hàng rượu truyền thống. Hệ thống hỗ trợ khách hàng tiếp cận thông tin sản phẩm nhanh chóng, xem danh mục, xem chi tiết, thao tác yêu thích sản phẩm, giỏ hàng và checkout ở phía giao diện. Đồng thời, hệ thống giúp Admin quản lý tập trung dữ liệu sản phẩm, danh mục, bộ sưu tập, người dùng, hình ảnh và phản hồi khách hàng.
Về mặt kỹ thuật, dự án sử dụng kiến trúc Decoupled với Next.js ở Frontend, NestJS ở Backend, MongoDB cho cơ sở dữ liệu và Google Cloud Storage cho lưu trữ hình ảnh. Kiến trúc này phù hợp với yêu cầu mở rộng, bảo trì và triển khai cloud. Về mặt quản trị dự án, quá trình thực hiện đã vận dụng các nội dung quan trọng của môn học như xác định phạm vi, lập kế hoạch, ước lượng chi phí, quản lý rủi ro, phân tích thiết kế, kiểm thử và đánh giá kết quả.
Mặc dù dự án vẫn còn một số hạn chế như chưa có Order Module ở Backend, chưa lưu đơn hàng thật, chưa có quản lý trạng thái đơn hàng đầy đủ, Reviews Module chưa hoàn thiện nghiệp vụ tạo/cập nhật/xóa và chưa tích hợp cổng thanh toán trực tuyến chính thức, nhưng hệ thống đã tạo nền tảng tốt cho các phiên bản phát triển tiếp theo. Trong tương lai, dự án có thể mở rộng thêm Order Module, hoàn thiện Review Module, tích hợp VNPay/MoMo, đơn vị vận chuyển, mã giảm giá, phân tích doanh thu và gợi ý sản phẩm dựa trên hành vi người dùng.

 
TÀI LIỆU THAM KHẢO
[1]. NestJS Documentation, "NestJS - A progressive Node.js framework," 2024, from: https://docs.nestjs.com/.
[2]. Vercel Inc., "Next.js: The React Framework for the Web," 2024, from: https://nextjs.org/docs.
[3]. MongoDB Inc., "MongoDB Manual," 2024, from: https://www.mongodb.com/docs/manual/.
[4]. Mongoose, "Mongoose Documentation," 2024, from: https://mongoosejs.com/docs/.
[5]. Google Cloud, "Cloud Storage Documentation," 2024, from: https://cloud.google.com/storage/docs.
[6]. Auth0, "JSON Web Tokens (JWT) Introduction," 2024, from: https://jwt.io/introduction.
[7]. Nodemailer, "Nodemailer Documentation," 2024, from: https://nodemailer.com/about/.
[8]. React Core Team, "React Documentation," 2024, from: https://react.dev.
[9]. Tailwind Labs, "Tailwind CSS Documentation," 2024, from: https://tailwindcss.com/docs.
[10]. Framer B.V., "Framer Motion Documentation," 2024, from: https://www.framer.com/motion/.
[11]. Axios, "Axios Documentation," 2024, from: https://axios-http.com/docs/intro.
[12]. Docker Inc., "Docker Compose Overview," 2024, from: https://docs.docker.com/compose/.
[13]. Postman, "Postman Learning Center," 2024, from: https://learning.postman.com/docs/.
