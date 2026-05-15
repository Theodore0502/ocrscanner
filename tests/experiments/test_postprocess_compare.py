# -*- coding: utf-8 -*-
"""
Test & So sánh 3 phương pháp post-processing OCR tiếng Việt:
1. Khong co post-processing (raw OCR output)
2. SymSpell + FIX_MAP (hiện tại)
3. ProtonX nano model (protonx-models/nano-protonx-legal-tc)

Chạy: python test_postprocess_compare.py
"""
import sys
import os
import time

# Fix Windows console UTF-8 encoding
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Thêm path để import từ project
_PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
_OCR_ROOT = os.path.join(_PROJECT_ROOT, "ocr_scanner")
sys.path.insert(0, _OCR_ROOT)

# ─── Sample OCR output thực tế (từ file dl_2025_0002.jpg) ──────────────────
RAW_OCR_OUTPUT = """BỘ CÔNG THƯƠNG
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
TRƯỜNG ĐẠI HỌC ĐIỆN LỰC
Độc lập - Tự do - Hạnh phúc
Só:2116/TB-ĐHDL
Hà Ni, ngày 9 tháng 8 năm 2025
THÔNG BÁO
Về việc nộp hồ sơ miễn, giảm học phí, hỗ trợ kinh phí học tập
hc k I năm hc 2025-2026 cho sinh viên khóa D20
Thực hiện Nghị định 81/2021/NĐ-CP ngày 27 tháng 8 năm 2021 v Quy
đnh cơ chế thu, quản lý học phí đi vi co s giáo dục thuộc hệ thống giáo dục
quốc dân và chính sách miễn, giảm học phí, hỗ trợ chi phí học tập; giá dch v trong
lĩnh vực giáo dục, đào tạo; Nghị định s 97/2023/NĐ-CP, ngày 31 tháng 12 năm
2023 ca Chính ph Sa đi, b sung mt s điu ca Nghị định s 81/2021/NĐ-
CP; Quyết định s 66/2013/QĐ-TTg chính sách hỗ trợ chi phí học tập đi vi sinh
viên là ngưi dân tộc thiểu số hc ti các cơ s giáo dục đi hc.
Đ triển khai vic xét miễn, giảm học phí, hỗ trợ chi phí học tập hc k I
năm hc 2025 - 2026 cho sinh viên khóa D20 Nhà trưng yêu cầu sinh viên np
đầy đủ h so theo hướng dẫn ti phụ lục 1 kèm theo thông báo này.
Hạn nộp: t ngày 12/9/2025 đn ht ngày 28/9/2025.
Nơi nhận h so: 126 ph Xm, phường Phú Lương, thành ph Hà Ni.
Trong quá trìnhỗ trợin khai thc hin nu gp vướng mắc sinh viên liên hệ cô:
Nguyn Th Mai Lý - Phòng Công tác Sinh viên đ đưc tư vấn và giải đáp.
Đề nghị các khoa quản lý sinh viên, Cố vấn học tập phổ biến đn sinh viên
do Khoa quản lý.
Nhn đưc thông báo này yêu cầu các đơn vị, cá nhân liên quan và sinh viên
nghiêm túc thc hin theo đúng thời gian quy định.
Nơi nhn:
TL. HIỆU TRƯỞNG
- Các khoa quản lý SV, CVHT;
TRƯỞNG PHÒNG CTSV
- CBL các lớp, SV các khóa;
- Hiệu trưởng (để b/c);
- Đăng webside, trang sinhvien.epu.edu.vn;
- Luu VT, CTSV, Lý NTM(02).
Phùng Thị Xuân Bình"""

# Ground truth (văn bản đúng để tính accuracy)
GROUND_TRUTH = """BỘ CÔNG THƯƠNG
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
TRƯỜNG ĐẠI HỌC ĐIỆN LỰC
Độc lập - Tự do - Hạnh phúc
Số: 2116/TB-ĐHDL
Hà Nội, ngày 9 tháng 8 năm 2025
THÔNG BÁO
Về việc nộp hồ sơ miễn, giảm học phí, hỗ trợ kinh phí học tập
học kỳ I năm học 2025-2026 cho sinh viên khóa D20
Thực hiện Nghị định 81/2021/NĐ-CP ngày 27 tháng 8 năm 2021 về Quy
định cơ chế thu, quản lý học phí đối với cơ sở giáo dục thuộc hệ thống giáo dục
quốc dân và chính sách miễn, giảm học phí, hỗ trợ chi phí học tập; giá dịch vụ trong
lĩnh vực giáo dục, đào tạo; Nghị định số 97/2023/NĐ-CP, ngày 31 tháng 12 năm
2023 của Chính phủ Sửa đổi, bổ sung một số điều của Nghị định số 81/2021/NĐ-
CP; Quyết định số 66/2013/QĐ-TTg chính sách hỗ trợ chi phí học tập đối với sinh
viên là người dân tộc thiểu số học tại các cơ sở giáo dục đại học.
Để triển khai việc xét miễn, giảm học phí, hỗ trợ chi phí học tập học kỳ I
năm học 2025 - 2026 cho sinh viên khóa D20 Nhà trường yêu cầu sinh viên nộp
đầy đủ hồ sơ theo hướng dẫn tại phụ lục 1 kèm theo thông báo này.
Hạn nộp: từ ngày 12/9/2025 đến hết ngày 28/9/2025.
Nơi nhận hồ sơ: 126 phố Xốm, phường Phú Lương, thành phố Hà Nội.
Trong quá trình triển khai thực hiện nếu gặp vướng mắc sinh viên liên hệ cô:
Nguyễn Thị Mai Lý - Phòng Công tác Sinh viên để được tư vấn và giải đáp.
Đề nghị các khoa quản lý sinh viên, Cố vấn học tập phổ biến đến sinh viên
do Khoa quản lý.
Nhận được thông báo này yêu cầu các đơn vị, cá nhân liên quan và sinh viên
nghiêm túc thực hiện theo đúng thời gian quy định.
Nơi nhận:
TL. HIỆU TRƯỞNG
- Các khoa quản lý SV, CVHT;
TRƯỞNG PHÒNG CTSV
- CBL các lớp, SV các khóa;
- Hiệu trưởng (để b/c);
- Đăng webside, trang sinhvien.epu.edu.vn;
- Lưu VT, CTSV, Lý NTM(02).
Phùng Thị Xuân Bình"""


# ─── Hàm tính Character Error Rate (CER) ───────────────────────────────────
def compute_cer(reference: str, hypothesis: str) -> float:
    """Tính Character Error Rate (thấp hơn = tốt hơn). 0.0 = hoàn hảo."""
    import difflib
    ref_chars = list(reference.replace('\n', ' '))
    hyp_chars = list(hypothesis.replace('\n', ' '))
    matcher = difflib.SequenceMatcher(None, ref_chars, hyp_chars)
    matches = sum(block.size for block in matcher.get_matching_blocks())
    total = max(len(ref_chars), len(hyp_chars))
    return 1.0 - (matches / total) if total > 0 else 0.0


def count_errors(reference: str, hypothesis: str) -> dict:
    """Đếm số từ sai."""
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    correct = sum(1 for r, h in zip(ref_words, hyp_words) if r == h)
    total = max(len(ref_words), len(hyp_words))
    return {
        "correct_words": correct,
        "total_words": total,
        "word_accuracy": correct / total if total else 0,
        "wrong_words": total - correct,
    }


def print_separator(title="", char="═", width=70):
    if title:
        side = (width - len(title) - 2) // 2
        print(f"\n{char * side} {title} {char * side}")
    else:
        print(char * width)


def print_result(name: str, text: str, ref: str, elapsed: float):
    stats = count_errors(ref, text)
    cer = compute_cer(ref, text)
    print(f"\n{'─'*70}")
    print(f"📊 {name}")
    print(f"   ⏱️  Thời gian : {elapsed:.3f}s")
    print(f"   📝 Từ đúng  : {stats['correct_words']}/{stats['total_words']} "
          f"({stats['word_accuracy']:.1%})")
    print(f"   ❌ Từ sai   : {stats['wrong_words']}")
    print(f"   📉 CER      : {cer:.3f} (thấp hơn = tốt hơn)")


# ─── Method 1: Raw OCR (no postprocessing) ──────────────────────────────────
def method1_raw():
    print_separator("METHOD 1: Raw OCR Output (không post-process)")
    t0 = time.time()
    result = RAW_OCR_OUTPUT
    elapsed = time.time() - t0
    print_result("Raw OCR", result, GROUND_TRUTH, elapsed)
    return result


# ─── Method 2: SymSpell + FIX_MAP (hiện tại) ────────────────────────────────
def method2_symspell():
    print_separator("METHOD 2: SymSpell + FIX_MAP (pipeline hiện tại)")
    t0 = time.time()
    try:
        from src.ocr.postprocess_pipeline import apply_postprocess
        result = apply_postprocess(RAW_OCR_OUTPUT, use_spellcheck=True)
        elapsed = time.time() - t0
        print_result("SymSpell + FIX_MAP", result, GROUND_TRUTH, elapsed)
        return result
    except Exception as e:
        print(f"   ❌ Lỗi: {e}")
        return RAW_OCR_OUTPUT


# ─── Method 3: ProtonX nano model ────────────────────────────────────────────
def method3_protonx(model_variant="nano"):
    model_map = {
        "nano": "protonx-models/nano-protonx-legal-tc",
        "distilled": "protonx-models/distilled-protonx-legal-tc",
        "full": "protonx-models/protonx-legal-tc",
    }
    model_path = model_map.get(model_variant, model_map["nano"])
    print_separator(f"METHOD 3: ProtonX {model_variant.upper()} ({model_path})")

    try:
        import torch
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

        print("   📥 Đang tải model...")
        t_load = time.time()
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)
        model.eval()
        load_time = time.time() - t_load
        device_name = "GPU 🚀" if torch.cuda.is_available() else "CPU 🐢"
        print(f"   ✅ Model loaded ({load_time:.1f}s) — chạy trên {device_name}")

        # Chạy correction theo từng dòng (giới hạn 160 tokens/lần)
        t0 = time.time()
        lines = RAW_OCR_OUTPUT.split('\n')
        corrected_lines = []

        MAX_TOKENS = 128
        for i, line in enumerate(lines):
            if not line.strip():
                corrected_lines.append(line)
                continue
            try:
                inputs = tokenizer(
                    line,
                    return_tensors="pt",
                    truncation=True,
                    max_length=MAX_TOKENS
                ).to(device)

                with torch.no_grad():
                    outputs = model.generate(
                        **inputs,
                        num_beams=4,          # Giảm beams để nhanh hơn khi test
                        num_return_sequences=1,
                        max_new_tokens=MAX_TOKENS,
                        early_stopping=True,
                    )
                corrected = tokenizer.decode(outputs[0], skip_special_tokens=True)
                corrected_lines.append(corrected)
                # Progress mỗi 5 dòng
                if (i + 1) % 5 == 0:
                    print(f"   ⏳ {i+1}/{len(lines)} dòng...", end='\r')
            except Exception as e:
                corrected_lines.append(line)  # fallback

        result = '\n'.join(corrected_lines)
        elapsed = time.time() - t0
        print(f"\n   ✅ Xử lý xong {len(lines)} dòng")
        print_result(f"ProtonX {model_variant.upper()}", result, GROUND_TRUTH, elapsed)
        return result

    except ImportError:
        print("   ❌ Chưa cài transformers!")
        print("   👉 Chạy: pip install transformers torch")
        return None
    except Exception as e:
        print(f"   ❌ Lỗi: {e}")
        return None


# ─── Method 4: FIX_MAP + ProtonX kết hợp ────────────────────────────────────
def method4_combined():
    print_separator("METHOD 4: FIX_MAP trước → ProtonX nano sau (KẾT HỢP)")
    t0 = time.time()
    try:
        from src.ocr.postprocess_pipeline import apply_postprocess
        # Bước 1: FIX_MAP nhanh
        after_fixmap = apply_postprocess(RAW_OCR_OUTPUT, use_spellcheck=False)

        # Bước 2: ProtonX
        import torch
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        model_path = "protonx-models/nano-protonx-legal-tc"
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)
        model.eval()

        lines = after_fixmap.split('\n')
        corrected_lines = []
        for line in lines:
            if not line.strip():
                corrected_lines.append(line)
                continue
            try:
                inputs = tokenizer(line, return_tensors="pt",
                                   truncation=True, max_length=128).to(device)
                with torch.no_grad():
                    outputs = model.generate(**inputs, num_beams=4,
                                             max_new_tokens=128, early_stopping=True)
                corrected_lines.append(tokenizer.decode(outputs[0], skip_special_tokens=True))
            except Exception:
                corrected_lines.append(line)

        result = '\n'.join(corrected_lines)
        elapsed = time.time() - t0
        print_result("FIX_MAP + ProtonX nano (kết hợp)", result, GROUND_TRUTH, elapsed)
        return result
    except Exception as e:
        print(f"   ❌ Lỗi: {e}")
        return None


# ─── Bảng so sánh chi tiết ───────────────────────────────────────────────────
def print_comparison_table(results: dict):
    print_separator("BẢNG SO SÁNH CHI TIẾT")
    print(f"\n{'Phương pháp':<30} {'Từ đúng':>10} {'Word Acc':>10} {'CER':>8} {'Thời gian':>12}")
    print("─" * 75)

    for name, (text, elapsed) in results.items():
        if text is None:
            print(f"{name:<30} {'N/A':>10} {'N/A':>10} {'N/A':>8} {'N/A':>12}")
            continue
        stats = count_errors(GROUND_TRUTH, text)
        cer = compute_cer(GROUND_TRUTH, text)
        print(f"{name:<30} {stats['correct_words']:>10} "
              f"{stats['word_accuracy']:>9.1%} {cer:>8.3f} {elapsed:>10.3f}s")


# ─── Hiển thị diff từng dòng ─────────────────────────────────────────────────
def show_diff_sample(method_name: str, corrected: str, n_lines: int = 8):
    """Hiển thị n dòng đầu có sự thay đổi."""
    print(f"\n📝 Mẫu output — {method_name} (8 dòng đầu có lỗi):")
    raw_lines = RAW_OCR_OUTPUT.split('\n')
    cor_lines = (corrected or "").split('\n')
    gt_lines  = GROUND_TRUTH.split('\n')

    shown = 0
    for i, (raw, gt) in enumerate(zip(raw_lines, gt_lines)):
        if raw != gt and shown < n_lines:
            cor = cor_lines[i] if i < len(cor_lines) else raw
            print(f"  RAW : {raw}")
            print(f"  FIX : {cor}")
            print(f"  GT  : {gt}")
            print()
            shown += 1


# ─── Main ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print_separator("OCR POST-PROCESSING BENCHMARK", "═")
    print("So sánh 3 phương pháp sửa lỗi OCR tiếng Việt pháp lý")
    print(f"Văn bản test: {len(RAW_OCR_OUTPUT.split())} từ, "
          f"{len(RAW_OCR_OUTPUT.split(chr(10)))} dòng")

    results = {}

    # Method 1: Raw
    t0 = time.time()
    r1 = method1_raw()
    results["1. Raw OCR"] = (r1, time.time() - t0)

    # Method 2: SymSpell
    t0 = time.time()
    r2 = method2_symspell()
    results["2. SymSpell + FIX_MAP"] = (r2, time.time() - t0)

    # Method 3: ProtonX nano
    t0 = time.time()
    r3 = method3_protonx("nano")
    results["3. ProtonX nano"] = (r3, time.time() - t0 if r3 else 0)

    # Method 4: Combined (chỉ chạy nếu ProtonX thành công)
    if r3 is not None:
        t0 = time.time()
        r4 = method4_combined()
        results["4. FIX_MAP + ProtonX nano"] = (r4, time.time() - t0 if r4 else 0)

    # Tổng kết
    print_comparison_table(results)

    # Diff mẫu
    show_diff_sample("SymSpell + FIX_MAP", r2)
    if r3:
        show_diff_sample("ProtonX nano", r3)

    print_separator("KHUYẾN NGHỊ")
    print("""
  📌 Chọn phương pháp tùy theo yêu cầu:

  ⚡ Nhanh nhất    → SymSpell + FIX_MAP (< 0.1s, không cần GPU)
  🎯 Chính xác nhất → FIX_MAP + ProtonX nano (kết hợp tốt nhất)
  💻 Máy yếu      → nano model chạy CPU (~ 1-5s/trang)
  🚀 Có GPU       → full model, beam=10 (~ 0.5s/trang)

  👉 Gợi ý: Thêm checkbox "ProtonX AI" vào app, dùng song song với SymSpell
""")
