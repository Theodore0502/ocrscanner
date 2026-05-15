KẾ HOẠCH SỬA BÁO CÁO
Giai đoạn 1: Sửa lỗi bắt buộc để báo cáo khớp dự án

1. Sửa toàn bộ “Split/Merge PDF” thành “Split PDF”

Vì code thực tế chỉ có chức năng tách PDF, chưa có chức năng gộp PDF, nên báo cáo không được viết là “Split/Merge PDF”.

Cần sửa ở các chỗ:

chia tách/gộp tài liệu PDF (Split/Merge)

thành:

chia tách tài liệu PDF (Split PDF)

Các tiêu đề nên đổi:

Luồng chức năng: Chia cắt và Gộp tài liệu (Split/Merge PDF)

thành:

Luồng chức năng: Chia cắt tài liệu PDF (Split PDF)

Chú thích hình nên đổi:

Hình 3.x. Biểu đồ minh họa luồng chức năng: Chia cắt tài liệu PDF

Không nên code thêm Merge PDF lúc này vì dễ phát sinh lỗi mới. Sửa báo cáo là cách an toàn nhất.

2. Sửa tên module SymSpell

Trong báo cáo nếu có câu:

symspell_checker.py

thì sửa thành:

fast_spell_checker.py

Câu nên viết lại:

Thuật toán SymSpell được triển khai trong module fast_spell_checker.py tại đường dẫn ocr_scanner/src/ocr/fast_spell_checker.py. Module này hỗ trợ hậu xử lý văn bản OCR, giúp đề xuất và sửa các lỗi sai chính tả phổ biến sau quá trình nhận dạng. 3. Sửa vị trí file cấu hình config.json

Nếu báo cáo viết:

Tệp config.json được đặt tại thư mục gốc của dự án.

thì sửa thành:

Tệp config.json được đặt trong thư mục cấu hình config/ của dự án, cụ thể tại đường dẫn ocr_scanner/config/config.json. Tệp này lưu các tham số cấu hình phục vụ quá trình tích hợp OCR Engine, mô hình AI hậu xử lý và các tùy chọn vận hành của hệ thống. 4. Bổ sung ảnh giao diện còn thiếu

Code có 2 chức năng tốt nhưng báo cáo chưa “khoe” rõ:

PDF to Word
Đánh số thứ tự file

Nếu còn thời gian, thêm vào cuối phần giao diện chương 3:

3.7.4. Giao diện chuyển đổi PDF sang Word
3.7.5. Giao diện đánh số thứ tự tệp tin

Nội dung mô tả ngắn:

3.7.4. Giao diện chuyển đổi PDF sang Word

Chức năng chuyển đổi PDF sang Word cho phép người dùng lựa chọn tệp PDF đầu vào và thực hiện chuyển đổi sang định dạng Word nhằm hỗ trợ chỉnh sửa nội dung sau khi số hóa. Tính năng này giúp mở rộng khả năng xử lý tài liệu của hệ thống, đặc biệt trong các tình huống người dùng cần tiếp tục biên tập văn bản sau khi trích xuất.

Hình 3.x. Giao diện chức năng chuyển đổi PDF sang Word
3.7.5. Giao diện đánh số thứ tự tệp tin

Chức năng đánh số thứ tự tệp tin hỗ trợ người dùng tự động đánh số cho nhiều tệp theo quy tắc định sẵn. Tính năng này giúp chuẩn hóa tên tài liệu, hỗ trợ quản lý hồ sơ theo lô và giảm thao tác thủ công khi xử lý số lượng lớn tệp tin.

Hình 3.x. Giao diện chức năng đánh số thứ tự tệp tin
Giai đoạn 2: Sửa cấu trúc bên trong 3 chương

Bạn không đổi tên chương lớn, chỉ sửa mục nhỏ.

Chương 1. Giới thiệu dự án

Chương này nên giữ vai trò: giới thiệu đề tài, hiện trạng, mục tiêu, phạm vi, yêu cầu hệ thống.

Cấu trúc đề xuất:

CHƯƠNG 1. GIỚI THIỆU DỰ ÁN

1.1. Giới thiệu về đơn vị thực tập
1.1.1. Giới thiệu tổng quan đơn vị
1.1.2. Lĩnh vực hoạt động
1.1.3. Vai trò của công nghệ thông tin trong doanh nghiệp

1.2. Tổng quan bài toán
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
1.5.5. Biểu thức chính quy Regex

Ở 1.4.1, bảng yêu cầu chức năng nên sửa thành:

ID Chức năng Mô tả
FR-01 OCR ảnh Nhận diện văn bản từ ảnh
FR-02 OCR PDF Trích xuất văn bản từ file PDF
FR-03 Batch OCR Xử lý OCR hàng loạt
FR-04 Batch Rename Đổi tên file tự động
FR-05 Split PDF Tách file PDF thành nhiều phần
FR-06 PDF to Word Chuyển đổi PDF sang Word
FR-07 Numbering File Đánh số thứ tự tệp tin
FR-08 AI Correction Sửa lỗi tiếng Việt bằng AI
FR-09 Export File Xuất kết quả ra TXT/JSON

Lưu ý: không đưa Merge PDF vào bảng.

Giai đoạn 3: Bổ sung phần Scrum vào Chương 2

Bạn nói đang thiếu Scrum, vậy nên thêm Scrum vào đầu Chương 2. Quản lý dự án. Hiện báo cáo có mô hình Incremental kết hợp Agile, nhưng nếu yêu cầu môn học cần Scrum thì nên chuyển phần này sang Scrum.

Cấu trúc Chương 2 nên sửa thành
CHƯƠNG 2. QUẢN LÝ DỰ ÁN

2.1. Mô hình phát triển phần mềm Scrum
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
2.4.4. Chi phí dự phòng
2.4.5. Tổng mức đầu tư dự kiến

2.5. Ước lượng rủi ro
2.5.1. Nhận diện và đánh giá rủi ro
2.5.2. Kế hoạch phòng ngừa và xử lý

2.6. Quản lý chất lượng phần mềm
2.6.1. Mục tiêu chất lượng
2.6.2. Quy trình đảm bảo chất lượng
2.6.3. Quy trình kiểm soát thay đổi
Nội dung thêm cho mục 2.1.1 — Giới thiệu Scrum

Bạn có thể chèn đoạn này:

2.1.1. Giới thiệu mô hình Scrum

Dự án OCR Scanner được quản lý theo mô hình Scrum, một khung làm việc thuộc nhóm Agile, phù hợp với các dự án phần mềm có yêu cầu thay đổi linh hoạt và cần kiểm thử thường xuyên. Scrum chia quá trình phát triển thành các vòng lặp ngắn gọi là Sprint. Mỗi Sprint tập trung hoàn thành một nhóm chức năng cụ thể, sau đó tiến hành kiểm thử, đánh giá kết quả và điều chỉnh kế hoạch cho Sprint tiếp theo.

Đối với hệ thống nhận dạng và xử lý văn bản tiếng Việt, việc áp dụng Scrum giúp giảm rủi ro trong quá trình tích hợp các công nghệ AI như DocTR, PaddleOCR và ProtonX Nano. Các module như OCR ảnh, OCR PDF, Batch Rename, Split PDF, PDF to Word, đánh số tệp tin và hậu xử lý tiếng Việt bằng AI có thể được chia nhỏ để phát triển, kiểm thử và tích hợp theo từng Sprint.
Nội dung thêm cho mục 2.1.2 — Lý do chọn Scrum
2.1.2. Lý do lựa chọn Scrum cho dự án OCR Scanner

Scrum được lựa chọn cho dự án vì hệ thống OCR Scanner có nhiều module độc lập, dễ chia thành các nhóm chức năng để phát triển theo từng Sprint. Ngoài ra, dự án có sự tham gia của nhiều thư viện AI và OCR bên thứ ba, do đó việc phát triển theo hướng lặp giúp phát hiện lỗi tương thích sớm, giảm rủi ro khi tích hợp và tạo điều kiện kiểm thử liên tục.

Các lý do chính gồm:

- Dễ quản lý tiến độ thông qua từng Sprint.
- Phù hợp với dự án có nhiều module độc lập.
- Giúp kiểm thử sớm các OCR Engine và AI Correction.
- Dễ điều chỉnh phạm vi khi phát hiện chức năng chưa khớp với code thực tế.
- Phù hợp với dự án cá nhân trong phạm vi môn học.
  Bảng vai trò Scrum nên thêm
  Vai trò Scrum Người đảm nhiệm Trách nhiệm
  Product Owner Đại diện yêu cầu nghiệp vụ / đơn vị thực tập Xác định nhu cầu số hóa tài liệu, ưu tiên chức năng và đánh giá sản phẩm sau mỗi Sprint
  Scrum Master Sinh viên thực hiện Lập kế hoạch Sprint, theo dõi tiến độ, ghi nhận rủi ro và điều phối quá trình thực hiện
  Development Team Sinh viên thực hiện Phân tích yêu cầu, thiết kế, lập trình, tích hợp OCR/AI, kiểm thử và hoàn thiện báo cáo
  Product Backlog nên thêm
  Mã User Story / Chức năng Độ ưu tiên Ghi chú
  PB01 Là người dùng, tôi muốn OCR ảnh để trích xuất văn bản từ tài liệu scan Cao Chức năng lõi
  PB02 Là người dùng, tôi muốn OCR file PDF để xử lý tài liệu nhiều trang Cao Chức năng lõi
  PB03 Là người dùng, tôi muốn xử lý OCR hàng loạt để tiết kiệm thời gian Cao Batch OCR
  PB04 Là người dùng, tôi muốn sửa lỗi tiếng Việt bằng AI để tăng độ chính xác văn bản Cao ProtonX/SymSpell
  PB05 Là người dùng, tôi muốn xem đối chiếu kết quả OCR với tài liệu gốc Cao Dual-panel
  PB06 Là người dùng, tôi muốn đổi tên tệp hàng loạt để chuẩn hóa hồ sơ Trung bình Batch Rename
  PB07 Là người dùng, tôi muốn tách file PDF để xử lý từng phần tài liệu Trung bình Split PDF
  PB08 Là người dùng, tôi muốn chuyển PDF sang Word để chỉnh sửa nội dung Trung bình PDF to Word
  PB09 Là người dùng, tôi muốn đánh số thứ tự file để quản lý tài liệu theo lô Trung bình Numbering
  PB10 Là quản trị viên, tôi muốn cấu hình OCR Engine và tham số hệ thống Trung bình config.json
  PB11 Là người dùng, tôi muốn xuất kết quả ra TXT/JSON để lưu trữ và sử dụng lại Trung bình Export
  PB12 Là người dùng, tôi muốn hệ thống không bị treo khi xử lý file lớn Cao Yêu cầu chất lượng
  Kế hoạch Sprint nên thêm

Vì báo cáo hiện nói dự án 8 tuần, nên chia thành 4 Sprint, mỗi Sprint 2 tuần là hợp lý.

Sprint Thời gian Mục tiêu Sprint Kết quả cần đạt
Sprint 1 Tuần 1–2 Khảo sát, xác định yêu cầu, thiết kế kiến trúc và lập Product Backlog Tài liệu yêu cầu, phạm vi dự án, kiến trúc tổng quan, Product Backlog
Sprint 2 Tuần 3–4 Xây dựng giao diện Desktop, module File Tools cơ bản Core GUI, Batch Rename, Split PDF, PDF to Word, Numbering
Sprint 3 Tuần 5–6 Tích hợp OCR Engine và AI hậu xử lý tiếng Việt DocTR, PaddleOCR, fast_spell_checker.py, ProtonX Nano, cấu hình config.json
Sprint 4 Tuần 7–8 Kiểm thử, tối ưu hiệu năng, đóng gói và hoàn thiện báo cáo Bộ test, kết quả thực nghiệm, bản đóng gói ứng dụng, báo cáo hoàn chỉnh
Sprint Review và Retrospective nên thêm
Sprint Kết quả đạt được Vấn đề phát sinh Điều chỉnh
Sprint 1 Hoàn thành khảo sát, mục tiêu, phạm vi và kiến trúc sơ bộ Phạm vi ban đầu có nhắc Merge PDF nhưng code chưa có Loại bỏ Merge PDF khỏi phạm vi chính thức
Sprint 2 Hoàn thành giao diện và các công cụ file cơ bản Cần bổ sung ảnh giao diện PDF to Word và Numbering vào báo cáo Bổ sung mô tả/ảnh giao diện ở Chương 3
Sprint 3 Tích hợp OCR Engine và hậu xử lý tiếng Việt Tên module SymSpell trong báo cáo chưa đúng với code Sửa thành fast_spell_checker.py
Sprint 4 Hoàn thành kiểm thử, tối ưu và báo cáo Một số mục lục, hình ảnh, đường dẫn config chưa thống nhất Cập nhật mục lục, sửa đường dẫn config.json và đánh lại số hình/bảng
Giai đoạn 4: Bổ sung dự toán chi phí xây dựng dự án

Báo cáo hiện đã có ước lượng chi phí nhưng nên viết lại rõ hơn theo hướng dự toán chi phí xây dựng hệ thống OCR Scanner, vì bạn nói phần này còn thiếu.

Mục 2.4 nên viết như sau
2.4. Dự toán chi phí xây dựng dự án

Dự toán chi phí được xây dựng nhằm xác định nguồn lực cần thiết để triển khai hệ thống OCR Scanner trong phạm vi 8 tuần. Chi phí bao gồm chi phí nhân công, chi phí thiết bị/hạ tầng, chi phí công cụ phần mềm và chi phí dự phòng rủi ro.
Bảng 2.4. Chi phí nhân công
Hạng mục Số lượng Đơn giá Thời gian Thành tiền
Phân tích yêu cầu và thiết kế hệ thống 1 150.000 VNĐ/giờ 40 giờ 6.000.000 VNĐ
Lập trình giao diện Desktop 1 150.000 VNĐ/giờ 45 giờ 6.750.000 VNĐ
Tích hợp OCR Engine 1 150.000 VNĐ/giờ 50 giờ 7.500.000 VNĐ
Tích hợp AI hậu xử lý tiếng Việt 1 150.000 VNĐ/giờ 40 giờ 6.000.000 VNĐ
Xây dựng File Tools 1 150.000 VNĐ/giờ 30 giờ 4.500.000 VNĐ
Kiểm thử và tối ưu hiệu năng 1 150.000 VNĐ/giờ 30 giờ 4.500.000 VNĐ
Viết tài liệu và hoàn thiện báo cáo 1 150.000 VNĐ/giờ 25 giờ 3.750.000 VNĐ
Tổng chi phí nhân công 260 giờ 39.000.000 VNĐ

Nếu bạn muốn mức sinh viên hơn, có thể giảm đơn giá xuống 50.000 VNĐ/giờ hoặc 25.000 VNĐ/giờ. Nhưng nếu báo cáo theo dự án thực tế, 150.000 VNĐ/giờ nghe hợp lý hơn.

Bảng 2.5. Chi phí hạ tầng và thiết bị
Hạng mục Số lượng Chi phí dự kiến Ghi chú
Máy tính/Workstation có GPU 1 2.000.000 VNĐ Chi phí khấu hao trong thời gian dự án
Dung lượng lưu trữ tài liệu thử nghiệm 1 300.000 VNĐ Lưu file ảnh/PDF test
Chi phí điện năng vận hành thử nghiệm 1 300.000 VNĐ Chạy OCR/AI cục bộ
Thiết bị scan/tạo dữ liệu đầu vào 1 500.000 VNĐ Khấu hao/thuê/mượn thiết bị
Tổng chi phí hạ tầng 3.100.000 VNĐ
Bảng 2.6. Chi phí phần mềm và công cụ
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
Bảng 2.7. Tổng mức đầu tư dự kiến
Nhóm chi phí Thành tiền
Chi phí nhân công 39.000.000 VNĐ
Chi phí hạ tầng và thiết bị 3.100.000 VNĐ
Chi phí phần mềm và công cụ 0 VNĐ
Chi phí dự phòng 10% 4.210.000 VNĐ
Tổng dự toán 46.310.000 VNĐ

Đoạn kết cho phần chi phí:

Tổng chi phí dự kiến để xây dựng hệ thống OCR Scanner là 46.310.000 VNĐ. Trong đó, chi phí nhân công chiếm tỷ trọng lớn nhất do dự án yêu cầu phân tích, lập trình, tích hợp và kiểm thử nhiều module AI/OCR. Các thư viện phần mềm sử dụng chủ yếu là mã nguồn mở nên giúp giảm đáng kể chi phí bản quyền. Chi phí dự phòng 10% được bổ sung nhằm xử lý các rủi ro phát sinh như lỗi tương thích thư viện, yêu cầu tối ưu GPU hoặc kéo dài thời gian kiểm thử.
Giai đoạn 5: Sửa Chương 3 cho đúng “Triển khai chương trình”

Chương 3 nên chứa toàn bộ phần kỹ thuật, thiết kế, cài đặt, giao diện, kết quả.

Cấu trúc nên là:

CHƯƠNG 3. TRIỂN KHAI CHƯƠNG TRÌNH

3.1. Tổng quan kiến trúc hệ thống
3.1.1. Kiến trúc phân lớp
3.1.2. Tầng giao diện
3.1.3. Tầng điều phối cốt lõi
3.1.4. Tầng tích hợp AI/OCR bên thứ ba

3.2. Tích hợp hệ thống bên thứ ba
3.2.1. Tích hợp DocTR
3.2.2. Tích hợp PaddleOCR
3.2.3. Tích hợp ProtonX Nano
3.2.4. Tích hợp fast_spell_checker.py
3.2.5. Cấu hình config.json

3.3. Thiết kế hệ thống
3.3.1. Biểu đồ Use Case tổng quát
3.3.2. Biểu đồ hoạt động chức năng OCR
3.3.3. Biểu đồ hoạt động chức năng Batch Rename
3.3.4. Biểu đồ hoạt động chức năng Split PDF
3.3.5. Biểu đồ trình tự
3.3.6. Biểu đồ lớp
3.3.7. Biểu đồ triển khai

3.4. Công nghệ sử dụng

3.5. Cài đặt hệ thống

3.6. Kết quả thực nghiệm

3.7. Giao diện chương trình
3.7.1. Giao diện đối chiếu kết quả OCR Dual-panel
3.7.2. Giao diện đổi tên tệp tin hàng loạt
3.7.3. Giao diện chia tách tài liệu PDF
3.7.4. Giao diện chuyển đổi PDF sang Word
3.7.5. Giao diện đánh số thứ tự tệp tin
Giai đoạn 6: Sửa lỗi hình thức cuối cùng

Trước khi nộp, sửa các lỗi sau:

Sửa GVHD trong lời cảm ơn cho khớp với bìa. Bìa đang ghi TS. Phạm Đức Hồng, lời cảm ơn không được ghi thầy khác.
Xóa toàn bộ lỗi Error! Bookmark not defined.
Cập nhật lại mục lục.
Đánh lại số hình.
Đánh lại số bảng.
Sửa “Levenstein” thành Levenshtein.
Sửa “Tiền độ” thành Tiến độ.
Sửa “Phiên bản đầy đủ” trong danh mục viết tắt thành Tên đầy đủ.
Bổ sung giải thích CPU/GPU/RAM trong danh mục viết tắt.
Kiểm tra tài liệu tham khảo có đủ [1], [2], [5].
Thứ tự làm thực tế để không bị rối

Bạn nên làm theo thứ tự này:

Bước 1: Sửa tên chương/mục nhỏ trong Heading cho đúng 3 chương đã chốt.
Bước 2: Chuyển toàn bộ phần Scrum, WBS, PERT, Gantt, chi phí, rủi ro, chất lượng vào Chương 2.
Bước 3: Viết thêm phần Scrum: vai trò Scrum, Product Backlog, Sprint Backlog, Sprint Review.
Bước 4: Viết lại phần dự toán chi phí xây dựng hệ thống OCR Scanner.
Bước 5: Chuyển phần kiến trúc, tích hợp, thiết kế, giao diện sang Chương 3.
Bước 6: Sửa các lỗi khớp code: Split PDF, fast_spell_checker.py, config/config.json.
Bước 7: Thêm ảnh PDF to Word và Numbering nếu có.
Bước 8: Đánh lại số hình/bảng.
Bước 9: Update lại mục lục, danh mục hình, danh mục bảng.
Bước 10: Rà lần cuối lỗi chính tả, GVHD, tài liệu tham khảo.

Kết luận: không cần đổi đề tài, không cần đổi chương lớn, không cần code thêm Merge PDF. Việc cần làm chính là tái sắp xếp nội dung, bổ sung Scrum, viết rõ dự toán chi phí, và sửa các điểm lệch giữa báo cáo với code thực tế.
