import re

def fix_report(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to re-insert the deleted architecture section into Chapter 3.
    # Where to insert it?
    # In Chapter 3, we currently have:
    # 3.1. Kiểm thử hệ thống
    # 3.2. Cài đặt hệ thống
    # 3.3. Giao diện hệ thống
    # 3.4. Kết quả thực nghiệm
    # We should restructure Chapter 3 into:
    # 3.1. Tổng quan kiến trúc hệ thống
    # 3.2. Tích hợp hệ thống bên thứ ba
    # 3.3. Thiết kế hệ thống
    # 3.4. Cài đặt hệ thống
    # 3.5. Kiểm thử hệ thống
    # 3.6. Giao diện chương trình
    # 3.7. Kết quả thực nghiệm

    deleted_content = """3.1. Tổng quan kiến trúc hệ thống
Hệ thống được thiết kế dựa trên sự kết hợp giữa mô hình Kiến trúc phân lớp (Layered Architecture) và Mẫu thiết kế Plugin (Plugin Pattern). Việc lựa chọn kiến trúc này bắt nguồn từ bản chất của hệ thống: Đây là một hệ thống mang tính chất Điều phối (Orchestration).
Hệ thống chia làm ba tầng chính:
• Tầng Giao diện (Presentation Layer): Được xây dựng bằng thư viện CustomTkinter. Tầng này chịu trách nhiệm tương tác trực tiếp với người dùng, nhận các tệp tin hình ảnh, tiếp nhận các sự kiện click chuột và hiển thị hình ảnh cùng văn bản đối chiếu. Tầng này hoàn toàn không chứa bất kỳ logic xử lý AI nào.
• Tầng Điều phối cốt lõi (Core Orchestrator Layer): Đây là "bộ não" của hệ thống phần mềm. Tầng này tiếp nhận lệnh từ giao diện, thực hiện các bước tiền xử lý hình ảnh (sử dụng thư viện OpenCV để cắt, xoay, cân bằng sáng). Sau đó, dựa vào file cấu hình (config.json), tầng này sẽ quyết định sẽ đóng gói dữ liệu và gửi yêu cầu (Request) đến Engine AI nào. Khi nhận được kết quả trả về, nó tiến hành ghép nối các đoạn văn bản (text alignment) và áp dụng các thuật toán nội bộ.
• Tầng Dịch vụ Tích hợp Bên thứ ba (Black-box Layer): Đây là nơi chứa các mô hình Học sâu (Deep Learning) nặng nề và phức tạp. Các mô hình này được bọc lại bằng một lớp Giao diện lập trình (Wrapper Interface). Tầng Core Orchestrator chỉ cần gọi một hàm chuẩn duy nhất như `extract_text()`, và Interface này sẽ lo liệu việc giao tiếp phức tạp với các thư viện PyTorch hay Paddle bên dưới.
Đặc điểm của kiến trúc này là sự tách biệt hoàn toàn giữa ứng dụng và mô hình. Cơ sở dữ liệu và các luồng xử lý AI chạy trong không gian bộ nhớ riêng. Việc thiết kế này giúp hệ thống quản lý tài nguyên bộ nhớ hiệu quả, đặc biệt là RAM đồ họa (VRAM), đồng thời giảm thiểu tối đa rủi ro phần mềm ngừng hoạt động do lỗi từ bên thứ ba.

3.2. Tích hợp hệ thống bên thứ ba
Trong phạm vi của dự án, khái niệm "Tích hợp Hộp đen" (Black-box Integration) được áp dụng một cách triệt để. Hệ thống nội bộ không cần hiểu cấu trúc mạng Neural bên trong DocTR hay PaddleOCR có bao nhiêu lớp, không cần tham gia vào quá trình lan truyền ngược (Backpropagation) hay huấn luyện mô hình. Hệ thống chỉ quan tâm đến Dữ liệu Đầu vào (Input) và Dữ liệu Đầu ra (Output).

3.2.1 Tích hợp các Engine OCR (DocTR và PaddleOCR).
Việc tích hợp được thực hiện thông qua việc gọi các thư viện API được cung cấp bởi nhà phát triển.
• Đối với DocTR [1]: Hệ thống Core Orchestrator sau khi chuyển đổi hình ảnh thành một ma trận đa chiều (Numpy Array) sẽ truyền ma trận này vào hàm `Predictor` của DocTR. Khối lượng xử lý khổng lồ sẽ diễn ra bên trong không gian của bộ thư viện này. Kết quả mà hệ thống nhận lại là một cấu trúc dữ liệu dạng cây (JSON/Dictionary) bao gồm các trang (Pages), các khối (Blocks), các dòng (Lines) và cuối cùng là các từ (Words) kèm theo tọa độ (X, Y) của chúng trên ảnh.
• Đối với PaddleOCR [2]: Quá trình tích hợp cũng tương tự. Lớp Wrapper của PaddleOCR sẽ nhận vào đường dẫn hoặc ma trận ảnh và kích hoạt hàm `paddleocr.ocr()`. Phản hồi trả về là một danh sách chứa nội dung văn bản thô (Raw text) cùng với độ tin cậy (Confidence score) của mỗi từ. Core Orchestrator sẽ lấy danh sách này, lọc bỏ các từ có độ tin cậy quá thấp để chuẩn bị cho bước tiếp theo.

3.2.2 Tích hợp mô hình ngôn ngữ lớn ProtonX Nano [5].
Sau khi có được văn bản thô từ tầng nhận diện hình ảnh, văn bản này thường xuyên gặp các lỗi mất dấu hoặc nhầm lẫn ký tự. Hệ thống tiếp tục quy trình tích hợp hộp đen bằng cách gửi đoạn văn bản này đến mô hình ProtonX Nano Legal Text Correction.
ProtonX Nano được tích hợp thông qua thư viện `Transformers` của HuggingFace. Cơ chế được sử dụng ở đây là Sequence-to-Sequence (Dịch chuỗi sang chuỗi). Toàn bộ đoạn văn bản chứa lỗi sẽ được truyền qua giao thức API nội bộ tới mô hình.
Nhờ vào cấu trúc Transformer đã được huấn luyện trên khối lượng dữ liệu hành chính và pháp luật khổng lồ của tiếng Việt, ProtonX Nano sẽ đóng vai trò như một bộ "dịch thuật", phân tích ngữ cảnh của toàn bộ câu và phản hồi lại cho hệ thống phiên bản văn bản đã được khôi phục dấu và sửa lỗi chính tả chính xác. Quy trình tích hợp tinh vi này giúp hệ thống đạt được sự hoàn thiện về mặt ngữ nghĩa mà một mô hình quang học đơn thuần không bao giờ có thể làm được.

3.3. Thiết kế hệ thống
Dưới đây là các biểu đồ thiết kế hệ thống theo tiêu chuẩn ngôn ngữ mô hình hóa thống nhất (UML), nhằm minh họa trực quan sự tương tác giữa các thành phần và các luồng xử lý dữ liệu phức tạp bên trong phần mềm.

3.3.1. Biểu đồ Usecase tổng quát
Biểu đồ Usecase dưới đây mô tả các ca sử dụng chính của hệ thống từ góc nhìn của người dùng cuối và quản trị viên, đồng thời thể hiện rõ vai trò của Hệ thống Blackbox AI như một tác nhân bên ngoài (Actor) liên tục hỗ trợ hệ thống chính.

Hình 3.1. Biểu đồ Usecase tổng quát

Các Tác nhân (Actors) và Mối quan hệ:
• User (Người dùng cuối): Là nhân viên văn phòng, chuyên viên hành chính sử dụng phần mềm để thực hiện các nghiệp vụ số hóa và xử lý tài liệu hàng ngày. User có quyền truy cập vào các nhóm chức năng thao tác tệp tin và nhận diện OCR cơ bản.
• Quản trị viên: Là người có kiến thức về kỹ thuật hoặc được phân quyền quản lý phần mềm. Quản trị viên có mũi tên quan hệ Kế thừa (Generalization) trỏ về phía User. Điều này có nghĩa là Quản trị viên kế thừa toàn bộ các quyền hạn, chức năng của User, đồng thời có thêm quyền truy cập vào các chức năng cấu hình hệ thống chuyên sâu.

Các Nhóm chức năng (Use Cases) phân rã theo System Boundary: Hệ thống được chia thành 3 nhóm chức năng (Packages) chính để dễ quản lý:
• Nhóm quản trị hệ thống: Cấu hình hệ thống chuyên sâu: Chức năng độc quyền của Quản trị viên, cho phép can thiệp vào các file cài đặt (config.json), thay đổi thông số phần cứng (VRAM) hoặc cấu hình các mô hình trí tuệ nhân tạo bên dưới lõi phần mềm.
• Nhóm chức năng tiện ích: Cung cấp bộ công cụ mạnh mẽ hỗ trợ User xử lý tệp tin trước và sau khi OCR. Bao gồm:
  o Đổi tệp tin hàng loạt (Chuẩn hóa tên file).
  o Tách tài liệu PDF (Phục vụ xử lý hồ sơ dung lượng lớn).
  o Chuyển định dạng PDF sang Word.
  o Đánh số thứ tự tệp tin tự động.
• Nhóm chức năng số hóa (Core OCR): Đây là phân hệ quan trọng nhất của ứng dụng, nơi User thực hiện nghiệp vụ trích xuất văn bản. Bao gồm:
  o Nạp tài liệu ảnh/PDF.
  o Xem đối chiếu kết quả (Dual-panel): So sánh văn bản đầu ra với ảnh gốc.
  o Lưu và xuất kết quả văn bản.
  o Thực thi nhận diện tài liệu (Single).
  o Lựa chọn cấu hình nhận diện.
  o Thực thi quét tự động hàng loạt.

Các Mối quan hệ ràng buộc (Include) giữa các Use Case: Biểu đồ chỉ ra luồng ràng buộc logic trong nghiệp vụ chuyển đổi số:
• Nạp tài liệu ảnh/PDF/TIFF: Để hệ thống có thể chạy AI trích xuất chữ, điều kiện tiên quyết và bắt buộc là User phải nạp tài liệu vào phần mềm thành công.
• Lựa chọn cấu hình nhận diện: Việc thiết lập cấu hình nhận diện (chọn Engine nào, có dùng Hậu xử lý hay không) được đính kèm và tích hợp trực tiếp vào quá trình thực thi OCR.
• Thực thi quét tự động hàng loạt: Bản chất của tính năng quét hàng loạt (Batch Processing) là vòng lặp gọi lại luồng xử lý của việc quét một tài liệu đơn lẻ nhiều lần liên tiếp.

3.3.2. Các biểu đồ hoạt động (Activity Diagrams)
Hệ thống bao gồm nhiều luồng chức năng hỗ trợ toàn diện cho quy trình chuyển đổi số văn bản. Thay vì chỉ nhận diện đơn thuần, phần mềm được trang bị đầy đủ các công cụ để xử lý vòng đời của một tài liệu. Dưới đây là các biểu đồ hoạt động chi tiết:

3.3.2.1. Luồng chức năng cốt lõi: Nhận diện và xử lý OCR
Biểu đồ mô tả chi tiết luồng điều khiển và quá trình ra quyết định của hệ thống bắt đầu từ thời điểm người dùng nạp dữ liệu cho đến khi màn hình hiển thị kết quả. Sự phân nhánh thể hiện tính linh hoạt trong việc chọn Engine tùy cấu hình.

Hình 3.2. Biểu đồ minh họa luồng chức năng cốt lõi: Nhận diện và xử lý OCR

3.3.2.2. Luồng chức năng: Tiện ích Đổi tên tệp tin hàng loạt (Batch Rename)
Trong chuyển đổi số, việc chuẩn hóa tên file là bước cực kỳ quan trọng. Chức năng này giúp nhân sự hành chính chuẩn hóa tên hàng ngàn tài liệu lộn xộn trước khi lưu trữ hoặc quét OCR.

3.3.2.3. Luồng chức năng: Chia cắt tài liệu PDF (Split PDF)
Công cụ đắc lực để xử lý các tệp công văn nhiều trang. Nhân viên có thể bóc tách lấy 1 trang cần thiết để OCR thay vì quét cả tệp nặng nề.

Hình 3.3. Biểu đồ minh họa luồng chức năng: Chia cắt tài liệu PDF

3.3.2.4. Luồng chức năng: Xử lý quét văn bản hàng loạt (Batch Processing OCR)
Đây là chức năng thể hiện sức mạnh tự động hóa của phần mềm. Thay vì thao tác từng ảnh, luồng này cho phép số hóa toàn bộ thư mục một cách tự động, hoàn toàn không cần sự can thiệp của con người.

Hình 3.4. Biểu đồ minh họa luồng chức năng: Xử lý quét văn bản hàng loạt

3.3.3. Biểu đồ trình tự (Sequence Diagram)
Biểu đồ trình tự là một công cụ phân tích quan trọng giúp hiểu rõ sự trao đổi thông điệp (Message passing) theo thời gian giữa các thành phần độc lập trong kiến trúc. Biểu đồ dưới đây minh họa rõ rệt sự phân tách trách nhiệm giữa ba thực thể: Tầng Giao diện (UI), Tầng Điều phối (Core) và Tầng Tích hợp (Black-box). Tầng Giao diện tuyệt đối không liên lạc trực tiếp với các mô hình AI mà mọi mệnh lệnh đều phải thông qua Bộ điều phối.

Hình 3.5. Biểu đồ trình tự hệ thống OCR Scanner

3.3.4. Biểu đồ Lớp (Class Diagram)
Biểu đồ lớp dưới đây thể hiện việc áp dụng Mẫu thiết kế phần mềm (Design Pattern) chuyên nghiệp vào thực tiễn. Thay vì mã hóa cứng (Hard-code) việc gọi trực tiếp đến từng thư viện AI, hệ thống định nghĩa một Lớp trừu tượng `BaseOCREngine`.
Tất cả các mô hình học sâu muốn tích hợp vào hệ thống đều phải tạo ra một Lớp triển khai (Implement) thừa kế từ Lớp trừu tượng này và ghi đè phương thức `extract_text()`. Lớp trung tâm `OCRController` chỉ tương tác với Lớp trừu tượng, nhờ đó đạt được nguyên tắc Mở/Đóng (Open/Closed Principle) trong kỹ nghệ phần mềm: Hệ thống mở rộng dễ dàng (thêm mô hình mới) mà không cần phải chỉnh sửa mã nguồn cốt lõi hiện tại.

Hình 3.6. Biểu đồ lớp hệ thống OCR Scanner

3.3.5. Biểu đồ triển khai (Deployment Diagram)
Biểu đồ triển khai dưới đây mô tả cách các thành phần phần mềm được bố trí và vận hành trên hạ tầng vật lý thực tế. Do đặc thù là ứng dụng Desktop xử lý cục bộ (Local Processing), toàn bộ hệ thống được triển khai trên một máy tính duy nhất của người dùng, không yêu cầu máy chủ hay kết nối mạng.

Hình 3.7. Biểu đồ triển khai hệ thống OCR Scanner

Điểm đặc biệt của mô hình triển khai này là tính tự chủ hoàn toàn: Không có bất kỳ thành phần nào yêu cầu kết nối tới máy chủ bên ngoài (Cloud Server) hay dịch vụ API trả phí. Mọi quá trình nhận diện hình ảnh, suy luận ngôn ngữ và kiểm tra chính tả đều diễn ra trong không gian bộ nhớ cục bộ của máy tính người dùng.
Kiến trúc này đảm bảo tuyệt đối tính bảo mật cho các tài liệu hành chính nhạy cảm, đồng thời cho phép phần mềm hoạt động hoàn toàn ở chế độ ngoại tuyến (Offline).

3.3.6. Cấu trúc dữ liệu hệ thống (Data Schema)
Do đặc thù là một ứng dụng Desktop xử lý theo phiên (Session-based), hệ thống không sử dụng các hệ quản trị cơ sở dữ liệu quan hệ (RDBMS) truyền thống như MySQL hay SQL Server. Thay vào đó, chiến lược lưu trữ dữ liệu được thiết kế tối giản theo triết lý "File-based Storage", phù hợp với quy mô và yêu cầu của phần mềm:

Bảng 3.1. Bảng cấu trúc dữ liệu vật lý
| Tên file / Đối tượng | Định dạng | Dung lượng | Mục đích sử dụng | Thời điểm truy xuất |
|---|---|---|---|---|
| config.json | JSON | ~1 KB | Lưu cấu hình mặc định của hệ thống: Engine OCR, trạng thái AI, thư mục lưu trữ, tham số xử lý | Đọc khi khởi động, ghi khi thay đổi cấu hình |
| raw_dict.jsonl | JSONL | ~4.9 MB | Từ điển Tiếng Việt gồm hơn 100.000 từ phục vụ thuật toán sửa lỗi SymSpell | Nạp toàn bộ vào RAM khi khởi động hệ thống |
| FileResult | In-memory Object | Dynamic | Lưu kết quả OCR của từng file: đường dẫn, engine sử dụng, trạng thái, văn bản gốc, văn bản hậu xử lý, thời gian xử lý, độ tin cậy, số dòng, số ký tự | Khởi tạo trong mỗi phiên quét và giải phóng khi kết thúc |
| *.txt | Plain Text | Dynamic | Lưu văn bản đầu ra sau khi OCR và hậu xử lý hoàn tất | Ghi xuống ổ cứng sau khi xử lý thành công |

Schema chi tiết file `config.json`:

Hình 3.8. Schema chi tiết file `config.json`

Cấu trúc một mục từ điển trong raw_dict.jsonl (mỗi dòng là một JSON object):

Hình 3.9. Cấu trúc một mục từ điển trong raw_dict.jsonl

Việc lựa chọn chiến lược File-based thay vì RDBMS mang lại hai lợi ích thiết thực: Thứ nhất, giảm thiểu hoàn toàn độ phức tạp cài đặt cho người dùng cuối (không cần cài đặt MySQL Server). Thứ hai, tốc độ truy xuất cấu hình nhanh chóng (đọc file JSON nhỏ nhanh hơn nhiều so với khởi tạo kết nối tới database server).

"""
    
    # 1. We replace 3.1 and 3.2 headers in the original file with 3.4 and 3.5.
    content = content.replace("3.1. Kiểm thử hệ thống", "3.5. Kiểm thử hệ thống")
    content = content.replace("3.1.1. Kế hoạch", "3.5.1. Kế hoạch")
    content = content.replace("3.1.1.1", "3.5.1.1")
    content = content.replace("3.1.1.2", "3.5.1.2")
    content = content.replace("3.1.1.3", "3.5.1.3")
    content = content.replace("3.1.2.", "3.5.2.")
    content = content.replace("3.1.2.1", "3.5.2.1")
    content = content.replace("3.1.2.2", "3.5.2.2")
    content = content.replace("3.1.2.3", "3.5.2.3")
    content = content.replace("3.1.3.", "3.5.3.")
    content = content.replace("3.1.3.1", "3.5.3.1")
    content = content.replace("3.1.3.2", "3.5.3.2")
    content = content.replace("3.1.3.3", "3.5.3.3")
    content = content.replace("3.1.4.", "3.5.4.")
    content = content.replace("3.1.4.1", "3.5.4.1")
    
    content = content.replace("3.4.1.2.", "3.5.4.2.")
    content = content.replace("3.4.1.3.", "3.5.4.3.")
    
    content = content.replace("3.2. Cài đặt hệ thống", "3.4. Cài đặt hệ thống")
    content = content.replace("3.2.1.", "3.4.1.")
    content = content.replace("3.2.2.", "3.4.2.")
    content = content.replace("3.2.3.", "3.4.3.")
    content = content.replace("3.2.4.", "3.4.4.")
    content = content.replace("3.2.5.", "3.4.5.")
    
    content = content.replace("3.3. Giao diện hệ thống", "3.6. Giao diện hệ thống")
    content = content.replace("3.3.1.", "3.6.1.")
    content = content.replace("3.3.2.", "3.6.2.")
    content = content.replace("3.3.3.", "3.6.3.")
    
    content = content.replace("3.4. Kết quả thực nghiệm", "3.7. Kết quả thực nghiệm")

    # Change "thư mục gốc của dự án"
    content = content.replace("tại thư mục gốc của dự án", "trong thư mục cấu hình config/ của dự án, cụ thể tại đường dẫn ocr_scanner/config/config.json")
    
    # Change Levenstein
    content = content.replace("Levenstein", "Levenshtein")

    # 2. Insert the missing content right after THỰC NGHIỆM VÀ ĐÁNH GIÁ
    parts = content.split("THỰC NGHIỆM VÀ ĐÁNH GIÁ")
    if len(parts) > 1:
        content = parts[0] + "THỰC NGHIỆM VÀ ĐÁNH GIÁ\n\n" + deleted_content + "\n\n" + parts[1]

    # Add 3.6.4 and 3.6.5
    missing_ui = """
3.6.4. Giao diện chuyển đổi PDF sang Word

Chức năng chuyển đổi PDF sang Word cho phép người dùng lựa chọn tệp PDF đầu vào và thực hiện chuyển đổi sang định dạng Word nhằm hỗ trợ chỉnh sửa nội dung sau khi số hóa. Tính năng này giúp mở rộng khả năng xử lý tài liệu của hệ thống, đặc biệt trong các tình huống người dùng cần tiếp tục biên tập văn bản sau khi trích xuất.

Hình 3.13. Giao diện chức năng chuyển đổi PDF sang Word

3.6.5. Giao diện đánh số thứ tự tệp tin

Chức năng đánh số thứ tự tệp tin hỗ trợ người dùng tự động đánh số cho nhiều tệp theo quy tắc định sẵn. Tính năng này giúp chuẩn hóa tên tài liệu, hỗ trợ quản lý hồ sơ theo lô và giảm thao tác thủ công khi xử lý số lượng lớn tệp tin.

Hình 3.14. Giao diện chức năng đánh số thứ tự tệp tin
"""
    content = content.replace("3.7. Kết quả thực nghiệm", missing_ui + "\n3.7. Kết quả thực nghiệm")
    
    # Let's fix table and figure numbers
    # We'll just do a clean pass and build the TOC programmatically
    # Or just replace the old TOC with a simple one.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_report(r"f:\-----OCR_Scanner\bao_cao\bao_cao_chuan\bao_cao_QTDA_PhanMem.md")
