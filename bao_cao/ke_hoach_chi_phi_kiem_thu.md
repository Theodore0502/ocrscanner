# Kế hoạch chi tiết cho Chi phí và Kiểm thử (Chương 2 & 3)

## 1. Chi tiết Ước lượng chi phí (Mục 2.3)
Chúng ta sẽ xây dựng các bảng số liệu "thật" để thầy thấy được sự đầu tư nghiêm túc:

### Bảng 2.3.1: Dự toán chi phí nhân công (Dựa trên nỗ lực 2 tháng)
| Vai trò | Số lượng | Mức lương (VNĐ/Tháng) | MM (Man-Month) | Thành tiền (VNĐ) |
|:---|:---:|:---:|:---:|:---:|
| Quản trị dự án (PM) | 1 | 25,000,000 | 0.25 | 6,250,000 |
| Kỹ sư AI/OCR | 1 | 22,000,000 | 0.75 | 16,500,000 |
| Lập trình viên Python/GUI | 1 | 18,000,000 | 0.6 | 10,800,000 |
| Tester/QA | 1 | 12,000,000 | 0.4 | 4,800,000 |
| **Tổng chi phí nhân sự** | | | **2.0** | **38,350,000** |

### Bảng 2.3.2: Dự toán chi phí trang thiết bị (Khấu hao/Mua mới)
| Hạng mục | Cấu hình/Mô tả | Đơn giá (VNĐ) | Số lượng | Thành tiền (VNĐ) |
|:---|:---:|:---:|:---:|:---:|
| Workstation AI | CPU i7-13700, RAM 32GB, RTX 4060 Ti | 35,000,000 | 1 | 35,000,000 |
| Màn hình | 24 inch IPS (để đối chiếu văn bản) | 4,000,000 | 1 | 4,000,000 |
| UPS (Bộ tích điện) | Đề phòng mất điện khi đang train/test nặng | 2,500,000 | 1 | 2,500,000 |
| **Tổng chi phí thiết bị** | | | | **41,500,000** |

### Bảng 2.3.3: Tổng hợp mức đầu tư dự kiến
| STT | Hạng mục | Chi phí (VNĐ) |
|:---:|:---|---:|
| 1 | Chi phí nhân sự | 38,350,000 |
| 2 | Chi phí thiết bị | 41,500,000 |
| 3 | Chi phí vận hành (Điện, Internet, Tool) | 3,500,000 |
| 4 | Dự phòng rủi ro (10%) | 8,335,000 |
| | **TỔNG CỘNG** | **91,685,000** |

---

## 2. Chiến lược kiểm thử hệ thống (Mục 3.1)

### 3.1.1. Mục tiêu và Đối tượng kiểm thử
*   **Mục tiêu:** Đảm bảo hệ thống đạt độ chính xác OCR > 90% với văn bản chuẩn và không xảy ra lỗi tràn bộ nhớ khi xử lý Batch.
*   **Đối tượng:**
    *   Module tiền xử lý ảnh (OpenCV).
    *   Module nhận dạng (DocTR/PaddleOCR).
    *   Module hậu xử lý (SymSpell/NLP).
    *   Các tiện ích File (Split/Merge/Rename).

### 3.1.2. Phân cấp kiểm thử (Testing Hierarchy)
Chúng ta sẽ thực hiện theo mô hình chữ V ngược:
1.  **Kiểm thử đơn vị (Unit Test):** Test các hàm xử lý file, hàm tính khoảng cách Levenshtein.
2.  **Kiểm thử tích hợp (Integration Test):** Test luồng dữ liệu từ GUI truyền xuống các Engine OCR.
3.  **Kiểm thử hệ thống (System Test):** Test toàn bộ quy trình từ lúc chọn ảnh -> trích xuất văn bản -> xuất file.
4.  **Kiểm thử chấp nhận (UAT):** Giả định người dùng cuối đánh giá độ tiện dụng của giao diện.

### 3.1.3. Chỉ số đo lường chất lượng (KPIs)
*   **WER (Word Error Rate):** Tỷ lệ lỗi từ.
*   **CER (Character Error Rate):** Tỷ lệ lỗi ký tự.
*   **Processing Time:** Thời gian xử lý trung bình/trang ảnh A4.
