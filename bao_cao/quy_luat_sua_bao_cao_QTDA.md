# QUY LUẬT SỬA BÁO CÁO QUẢN TRỊ DỰ ÁN PHẦN MỀM

> **File:** `bao_cao_QTDA_PhanMem.md`  
> **Môn:** Thực tập Quản trị Dự án Phần mềm  
> **Giảng viên:** TS. Phạm Quang Huy  
> **Đề tài:** Hệ Thống Nhận dạng Và Xử Lý Văn Bản Tiếng Việt (OCR Scanner)

---

## ⚠️ RÀNG BUỘC CỨNG — KHÔNG ĐƯỢC THAY ĐỔI

Các tên chương sau đã nộp cho thầy, **KHÔNG ĐƯỢC SỬA tên chương lớn**:

```
Chương 1. Giới thiệu dự án
Chương 2. Quản lý dự án 
Chương 3. Triển khai chương trình
Kết luận và hướng nghiên cứu trong tương lai.
```

Tuy nhiên **được phép sửa/thêm/bớt** các tiêu đề mục nhỏ (1.1, 1.1.1, 2.3.2, ...) bên trong.

---

## 📋 CẤU TRÚC 3 CHƯƠNG CHUẨN PHẢI FOLLOW

### CHƯƠNG 1: GIỚI THIỆU DỰ ÁN
> Theo đề cương đã nộp: "Trình bày vấn đề thực tiễn trong hoạt động số hóa tài liệu cần giải quyết + Giới thiệu tổng quan giải pháp và mục tiêu của dự án OCR Scanner"

**Các mục nhỏ được đề xuất:**
```
1.1. Giới thiệu đơn vị thực tập
1.2. Tổng quan bài toán (vấn đề thực tiễn số hóa tài liệu)
1.3. Mục tiêu dự án
1.4. Phạm vi dự án
  1.4.1. Phạm vi chức năng
  1.4.2. Đối tượng sử dụng
1.5. Phân tích yêu cầu hệ thống
  1.5.1. Yêu cầu chức năng
  1.5.2. Yêu cầu phi chức năng
```

**Quy tắc Chương 1:**
- ✅ Giữ lại: Giới thiệu đơn vị, bài toán, mục tiêu, phạm vi, yêu cầu hệ thống
- ✅ Tái sử dụng từ báo cáo HTTT TichHop: Phần 1.1-1.5 (sửa lại ngữ cảnh cho phù hợp)
- ❌ Bỏ đi: Cơ sở lý thuyết OCR (Levenshtein, SymSpell, Transformer — đây là nội dung quá kỹ thuật, không phải nội dung "Quản trị dự án")
- ❌ Bỏ đi: Công nghệ nền tảng sử dụng (sẽ chuyển sang Chương 2 - Giải pháp kỹ thuật)
- 📏 Dung lượng mục tiêu: 2-5 trang (theo đề cương syllabus)

---

### CHƯƠNG 2: QUẢN LÝ DỰ ÁN  
> Theo đề cương đã nộp: "Trình bày kiến thức và lý thuyết quản trị dự án áp dụng (Mô hình phát triển, Kế hoạch dự án, Ước lượng rủi ro và chi phí) + Mô tả chi tiết giải pháp kỹ thuật và công nghệ sử dụng để xây dựng hệ thống (Kiến trúc hệ thống, AI/OCR, cấu trúc dữ liệu)"

**Chương này là TRỌNG TÂM của môn — phải chiếm 50-60% báo cáo.**

**Các mục nhỏ được đề xuất:**
```
--- PHẦN A: LÝ THUYẾT VÀ KẾ HOẠCH QUẢN TRỊ DỰ ÁN ---

2.1. Mô hình phát triển phần mềm
  2.1.1. Giới thiệu mô hình áp dụng (Waterfall/Incremental)
  2.1.2. Lý do lựa chọn mô hình

2.2. Kế hoạch thực hiện dự án
  2.2.1. Các mốc thời gian chính (Milestones)
  2.2.2. Ước lượng thời gian (PERT: MO, ML, MP → EST)
  2.2.3. Cấu trúc phân rã công việc (WBS)
  2.2.4. Biểu đồ Gantt                          ← BẮT BUỘC, CHƯA CÓ!

2.3. Ước lượng chi phí
  2.3.1. Chi phí nhân công
  2.3.2. Chi phí hạ tầng (Workstation GPU, phần mềm)
  2.3.3. Tổng mức đầu tư

2.4. Ước lượng rủi ro
  2.4.1. Nhận diện rủi ro
  2.4.2. Đánh giá rủi ro (Ma trận rủi ro)
  2.4.3. Phương án phòng ngừa và xử lý

--- PHẦN B: GIẢI PHÁP KỸ THUẬT ---

2.5. Công nghệ sử dụng
  (Bảng stack: Python, CustomTkinter, PyTorch, PaddlePaddle,...)

2.6. Tổng quan kiến trúc hệ thống
  (Sơ đồ kiến trúc tổng thể: GUI → OCR Engines → NLP → Output)

2.7. Phân tích thiết kế hệ thống (1-2 chức năng chính)
  2.7.1. Biểu đồ Use Case tổng quát
  2.7.2. Phân tích chức năng OCR Nhận dạng văn bản
    - Đặc tả Use Case
    - Biểu đồ hoạt động
    - Biểu đồ trình tự
  2.7.3. Phân tích chức năng Xử lý hàng loạt (Batch Processing)
    - Đặc tả Use Case
    - Biểu đồ hoạt động
    - Biểu đồ trình tự
```

**Quy tắc Chương 2:**
- ✅ **BẮT BUỘC phải có:** WBS, PERT, Gantt, Chi phí, Rủi ro (theo đề cương syllabus)
- ✅ Tái sử dụng: Kiến trúc hệ thống, Use Case, biểu đồ hoạt động, trình tự (từ HTTT TichHop)
- ✅ Tham khảo cấu trúc: AnNinh (mục 2.1-2.5) cho phần quản trị; Ninh cho WBS/PERT
- ❌ CHỈ giữ 1-2 chức năng chính cho phần thiết kế (đề cương yêu cầu "1 đến 2 chức năng chính")
- ❌ Không cần Class Diagram, Deployment Diagram nếu thiếu trang (chỉ bắt buộc Use Case + Activity + Sequence)
- 📏 Dung lượng mục tiêu: 18-25 trang (theo đề cương syllabus)

---

### CHƯƠNG 3: TRIỂN KHAI CHƯƠNG TRÌNH
> Theo đề cương đã nộp: "Kiểm thử hệ thống + Cài đặt, demo kết quả phần mềm"

**Các mục nhỏ được đề xuất:**
```
3.1. Kiểm thử hệ thống                          ← BẮT BUỘC, CHƯA CÓ!
  3.1.1. Kế hoạch kiểm thử (mục tiêu, phạm vi, chiến lược)
  3.1.2. Kiểm thử chức năng OCR
    - Kiểm thử giao diện (UI Test)
    - Kiểm thử chức năng (Function Test)
    - Kiểm thử hiệu năng (Performance Test)
  3.1.3. Kiểm thử chức năng Batch Processing
    - Kiểm thử giao diện
    - Kiểm thử chức năng
    - Kiểm thử hiệu năng
  3.1.4. Phân tích sai lệch và hướng khắc phục

3.2. Cài đặt hệ thống
  (Yêu cầu phần cứng/phần mềm, hướng dẫn cài đặt)

3.3. Kết quả demo
  (Screenshot giao diện + kết quả chạy thực tế)
```

**Quy tắc Chương 3:**
- ✅ **Kiểm thử phải đặt LÊN ĐẦU** chương (theo đúng thứ tự đề cương đã nộp)
- ✅ Format test case: Bảng có cột ID, Thành phần, Kịch bản, Kết quả mong đợi, Trạng thái (Pass/Fail)
- ✅ Tham khảo cấu trúc: AnNinh Ch4 (3 loại test: UI + Function + Performance cho mỗi chức năng)
- ✅ Tham khảo: Quân (test API bằng Postman — có thể áp dụng cho OCR API endpoint)
- ✅ Phải có ít nhất 1-2 test case FAILED (thể hiện tính trung thực, giống AnNinh và Quân)
- ✅ Tái sử dụng: Giao diện + kết quả thực nghiệm từ HTTT TichHop
- 📏 Kiểm thử nên chiếm khoảng 4-6 trang

---

### KẾT LUẬN VÀ HƯỚNG NGHIÊN CỨU TRONG TƯƠNG LAI
> Theo đề cương đã nộp: "Những kết quả đạt được + Những hạn chế và hướng phát triển"

```
- Những kết quả đạt được
- Những hạn chế và hướng phát triển
```
- ✅ Tái sử dụng từ HTTT TichHop, bổ sung góc nhìn "quản trị dự án"
- 📏 Khoảng 1-2 trang

---

## 📌 PHẦN ĐẦU BÁO CÁO — CẦN SỬA

| Mục | Trạng thái hiện tại | Cần sửa thành |
|---|---|---|
| Tiêu đề trang bìa | "THỰC TẬP HỆ THỐNG THÔNG TIN TÍCH HỢP" | **"THỰC TẬP QUẢN TRỊ DỰ ÁN PHẦN MỀM"** |
| Tiêu đề phiếu đánh giá | "HỆ THỐNG THÔNG TIN TÍCH HỢP" | **"QUẢN TRỊ DỰ ÁN PHẦN MỀM"** |
| Mục lục | Theo cấu trúc HTTT TichHop | **Theo cấu trúc 3 chương mới** |
| Đề cương tóm tắt (mục 5) | Theo HTTT TichHop | **Theo cấu trúc đã nộp cho thầy** |
| Giảng viên | TS. Phạm Quang Huy | Giữ nguyên (đúng rồi) |

---

## 🔄 BẢNG ÁNH XẠ NỘI DUNG CŨ → MỚI

| Nội dung từ HTTT TichHop (hiện tại) | Đưa vào đâu trong QTDA | Hành động |
|---|---|---|
| 1.1. Giới thiệu đơn vị thực tập | → Ch1: 1.1 | Giữ nguyên |
| 1.2. Giới thiệu tổng quan đề tài | → Ch1: 1.2 | Sửa ngữ cảnh → "vấn đề thực tiễn số hóa" |
| 1.3. Khảo sát hiện trạng | → Ch1: 1.2 (gộp) | Thu gọn |
| 1.4. Xác lập dự án | → Ch1: 1.3-1.4 | Giữ nguyên |
| 1.5. Phân tích yêu cầu | → Ch1: 1.5 | Giữ nguyên |
| 1.6. Cơ sở lý thuyết (Levenshtein, SymSpell...) | ❌ **BỎ** | Quá kỹ thuật cho môn QTDA |
| 1.7. Công nghệ nền tảng | → Ch2: 2.5 | Chuyển sang Ch2 |
| 2.1. Tổng quan kiến trúc | → Ch2: 2.6 | Giữ, đặt sau phần quản trị |
| 2.2. Tích hợp hệ thống bên thứ ba | ❌ **BỎ hoặc thu gọn** | Không liên quan QTDA |
| 2.3. Thiết kế hệ thống (UML) | → Ch2: 2.7 | Chỉ giữ 1-2 chức năng |
| 2.4. Cài đặt tích hợp | → Ch3: 3.2 | Thu gọn |
| 3.1. Công nghệ sử dụng | → Ch2: 2.5 (gộp) | Chuyển lên Ch2 |
| 3.2. Giao diện hệ thống | → Ch3: 3.3 | Giữ nguyên |
| 3.3. Kết quả thực nghiệm | → Ch3: 3.3 | Giữ nguyên |
| _Chưa có_ | → Ch2: 2.1 (Mô hình phát triển) | **TẠO MỚI** |
| _Chưa có_ | → Ch2: 2.2 (WBS + PERT + Gantt) | **TẠO MỚI** |
| _Chưa có_ | → Ch2: 2.3 (Ước lượng chi phí) | **TẠO MỚI** |
| _Chưa có_ | → Ch2: 2.4 (Ước lượng rủi ro) | **TẠO MỚI** |
| _Chưa có_ | → Ch3: 3.1 (Kiểm thử hệ thống) | **TẠO MỚI** |

---

## 📊 NỘI DUNG TẠO MỚI — CHI TIẾT

### 1. Biểu đồ Gantt (Mục 2.2.4)
- **Dạng:** Bảng text (dạng timeline × task) hoặc Mermaid Gantt chart
- **Thời gian:** 8 tuần (theo đề cương syllabus)
- **Các giai đoạn:**
  1. Tuần 1: Khảo sát, xác lập dự án
  2. Tuần 2: Phân tích yêu cầu, thiết kế
  3. Tuần 3-4: Xây dựng tài liệu quản trị (WBS, rủi ro, chi phí, phân tích thiết kế)
  4. Tuần 5-6: Cài đặt thực nghiệm, checklist testcase
  5. Tuần 7-8: Demo, hiệu chỉnh, hoàn thiện báo cáo

### 2. WBS — Bảng phân rã công việc (Mục 2.2.3)
- **Tham khảo:** Ninh (43 mã công việc) và AnNinh (phân rã rất chi tiết)
- **Format:**

| STT | Giai đoạn | Tên công việc | Mã CV | CV đi trước |
|---|---|---|---|---|
| 1 | 1.0 Khảo sát | 1.1 Khảo sát hiện trạng | KS.1.1 | — |

### 3. PERT — Ước lượng thời gian (Mục 2.2.2)
- **Công thức:** EST = (MO + 4×ML + MP) / 6
- **Format:**

| Mã CV | Công việc | MO | ML | MP | EST | Ngày công |
|---|---|---|---|---|---|---|

### 4. Ước lượng chi phí (Mục 2.3)
- **Nhân công:** 1 người × 8 tuần, tính theo lương thị trường
- **Hạ tầng:** Workstation GPU (RTX 3060), phần mềm (miễn phí/open-source)
- **Tham khảo:** AnNinh (Bảng 2.9-2.12) — format rất chuẩn

### 5. Ước lượng rủi ro (Mục 2.4)
- **Tham khảo:** AnNinh (R1-R6) — rất tốt cho dự án 1 người
- **Rủi ro đặc thù dự án OCR:**
  - R1: Mô hình AI không tương thích GPU/CPU → giải pháp: Fallback CPU mode
  - R2: Tỷ lệ nhận dạng tiếng Việt thấp → giải pháp: Ensemble + SymSpell
  - R3: Thư viện PaddlePaddle/PyTorch xung đột phiên bản
  - R4: File PDF quá nặng gây crash hệ thống
  - R5: Trễ tiến độ do debug model AI

### 6. Kiểm thử hệ thống (Mục 3.1)
- **Tham khảo:** AnNinh Ch4 (cấu trúc 3 lớp test rất chuẩn)
- **Chức năng cần test:**
  1. **OCR Nhận dạng:** UI test + Function test + Performance test
  2. **Batch Processing:** UI test + Function test + Performance test
- **Format test case:**

| ID | Thành phần kiểm tra | Kịch bản | Kết quả mong đợi | Trạng thái |
|---|---|---|---|---|
| FT-01 | OCR file ảnh JPG | Quét ảnh chụp rõ nét | Trích xuất ≥90% ký tự | Pass |
| FT-02 | OCR file PDF scan mờ | Quét PDF chất lượng thấp | Cảnh báo chất lượng | Failed |

- **Lưu ý:** Phải có ít nhất 1-2 test case **Failed** (trung thực)

---

## 📐 QUY TẮC TRANG

| Phần | Số trang tối thiểu | Ghi chú |
|---|---|---|
| Chương 1 | 2-5 trang | Ngắn gọn, đi thẳng vào vấn đề |
| Chương 2 | 18-25 trang | **TRỌNG TÂM** — WBS/Gantt/Chi phí/Rủi ro chiếm ~10 trang |
| Chương 3 | 5-8 trang | Kiểm thử ~4-6 trang, Demo ~2 trang |
| Kết luận | 1-2 trang | |
| **Tổng** | **15-30 trang** | Hoặc 10-20 trang không kể hình |

---

## 🔗 NGUỒN THAM KHẢO TỪ BÁO CÁO BẠN BÈ

| Nội dung | Tham khảo chính | Lý do |
|---|---|---|
| WBS + PERT | **Ninh** (Bảng 2.1-2.2) | 43 mã công việc, rất chi tiết |
| Biểu đồ Gantt | **AnNinh** (Hình 2.3-2.8) | Có biểu đồ Gantt chia theo giai đoạn |
| Ước lượng chi phí | **AnNinh** (Bảng 2.9-2.12) | Phân tách nhân công + hạ tầng + dự phòng |
| Ước lượng rủi ro | **AnNinh** (2.3) + **Ninh** (2.4) | Ma trận rủi ro + phương án xử lý |
| Quản lý chất lượng | **AnNinh** (2.5) | Quality Baseline + Kế hoạch kiểm thử đa tầng |
| Kiểm thử hệ thống | **AnNinh** (Ch4) | 3 loại test cho mỗi chức năng, rất mẫu mực |
| Phân tích sai lệch | **AnNinh** (4.5) | Trung thực, phân tích lỗi có chiều sâu |
| Mô hình Scrum | **AnNinh** (2.1) | Giới thiệu + bảng lý do + quy trình Sprint |

---

## ⚡ THỨ TỰ THỰC HIỆN (ĐỀ XUẤT)

1. ☐ Sửa trang bìa + đề cương tóm tắt + phiếu đánh giá → đổi tên môn
2. ☐ Viết lại Chương 1 (thu gọn từ HTTT TichHop)
3. ☐ Viết mới Chương 2 - Phần A: Mô hình phát triển + WBS + PERT + Gantt + Chi phí + Rủi ro
4. ☐ Viết lại Chương 2 - Phần B: Giải pháp kỹ thuật (thu gọn từ HTTT TichHop, chỉ giữ 1-2 chức năng)
5. ☐ Viết mới Chương 3 - Kiểm thử hệ thống (test case)
6. ☐ Viết lại Chương 3 - Cài đặt + Demo (giữ từ HTTT TichHop)
7. ☐ Sửa Kết luận
8. ☐ Cập nhật Mục lục + Danh mục hình + Danh mục bảng
