"""
EraX-VL-2B-V1.5 Engine — Vision-Language Model cho OCR tiếng Việt
Model: erax-ai/EraX-VL-2B-V1.5 (fine-tuned từ Qwen2-VL-2B-Instruct)

Ưu điểm so với PaddleOCR:
  - Hiểu ngữ nghĩa → không drop dấu thanh như Paddle
  - Chuyên văn bản hành chính tiếng Việt
  - Tự suy luận từ bị mờ dựa trên ngữ cảnh

Yêu cầu:
  - VRAM: ~3.5-4 GB (bfloat16) — phù hợp với RTX 3050 Ti 4GB
  - Tải model lần đầu: ~4.5 GB download
  - pip install qwen-vl-utils accelerate transformers>=4.45
"""

import os
import sys
import torch
from pathlib import Path
from typing import Optional

# Đặt HuggingFace cache vào ổ F (ổ C đã đầy)
# Có thể override bằng biến môi trường HF_HOME trước khi chạy
if not os.environ.get("HF_HOME"):
    _hf_cache = r"F:\HuggingFace_Cache"
    os.environ["HF_HOME"] = _hf_cache
    os.makedirs(_hf_cache, exist_ok=True)

MODEL_ID = "erax-ai/EraX-VL-2B-V1.5"
OCR_PROMPT = "Trích xuất toàn bộ nội dung văn bản từ hình ảnh được cung cấp. Giữ nguyên cấu trúc, xuống dòng và định dạng. Chỉ trả về văn bản, không giải thích thêm."

# Singletons
_model = None
_processor = None
_device = None


def _get_device():
    global _device
    if _device is None:
        if torch.cuda.is_available():
            free_vram = torch.cuda.mem_get_info()[0] / 1024**3
            _device = "cuda" if free_vram >= 2.0 else "cpu"
        else:
            _device = "cpu"
    return _device


def get_erax_model():
    """
    Load EraX-VL-2B model (singleton, lazy load).
    Lần đầu download ~4.5GB từ HuggingFace.
    """
    global _model, _processor

    if _model is not None:
        return _model, _processor

    from transformers import Qwen2VLForConditionalGeneration, AutoProcessor

    device = _get_device()
    print(f"Loading EraX-VL-2B-V1.5 on {device.upper()}...")

    # Chọn dtype dựa vào VRAM
    if device == "cuda":
        vram_gb = torch.cuda.get_device_properties(0).total_memory / 1024**3
        if vram_gb >= 6:
            dtype = torch.bfloat16
        else:
            # 4GB VRAM: dùng float16 + offload một phần lên CPU
            dtype = torch.float16
    else:
        dtype = torch.float32

    _model = Qwen2VLForConditionalGeneration.from_pretrained(
        MODEL_ID,
        dtype=dtype,
        attn_implementation="eager",   # flash_attention_2 cần build riêng
        device_map="auto",             # tự phân bổ layer lên GPU/CPU
    )
    _model.eval()

    # Giới hạn độ phân giải ảnh để vừa VRAM 4GB
    _processor = AutoProcessor.from_pretrained(
        MODEL_ID,
        min_pixels=256 * 28 * 28,     # ~200K pixels min
        max_pixels=1280 * 28 * 28,    # ~1M pixels — đủ rõ cho ảnh A4 scan
    )

    print("EraX-VL-2B ready!")
    return _model, _processor


def ocr_erax_image(image_path: str, prompt: str = OCR_PROMPT) -> str:
    """
    OCR một ảnh bằng EraX-VL-2B.

    Args:
        image_path: Đường dẫn đến file ảnh
        prompt: Câu lệnh cho model (mặc định: trích xuất toàn bộ văn bản)

    Returns:
        Văn bản được trích xuất
    """
    from qwen_vl_utils import process_vision_info
    from PIL import Image as PILImage

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Khong tim thay file: {image_path}")

    model, processor = get_erax_model()
    device = _get_device()

    # Load anh thanh PIL Image -- tranh loi URI parsing tren Windows
    pil_image = PILImage.open(image_path).convert("RGB")

    # Chuan bi messages voi PIL Image (khong dung URI)
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "image": pil_image,
                },
                {
                    "type": "text",
                    "text": prompt,
                },
            ],
        }
    ]

    # Tokenize
    text = processor.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )
    inputs = inputs.to(device)

    # Inference — dùng inference_mode (nhanh hơn no_grad ~5-10%)
    with torch.inference_mode():
        generated_ids = model.generate(
            **inputs,
            max_new_tokens=2048,        # A4 đầy chữ ~ 800-1500 tokens; 768 quá thấp gây loop '!!!'
            do_sample=False,            # greedy decode — nhanh hơn, ổn định hơn
            temperature=None,
            top_p=None,
            repetition_penalty=1.15,    # Tránh model lặp token ('!!!...' artifact)
        )

    # Decode output (bỏ phần prompt)
    generated_ids_trimmed = [
        out_ids[len(in_ids):]
        for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False,
    )

    # Giải phóng VRAM sau inference
    del inputs
    if device == "cuda":
        torch.cuda.empty_cache()

    return output_text[0].strip()


def ocr_erax_image_detailed(image_path: str) -> dict:
    """
    OCR và trả về dict tương thích với format của các engine khác.
    """
    text = ocr_erax_image(image_path)
    return {
        "text": text,
        "lines": [],
        "avg_confidence": 0.95   # VLM không cung cấp confidence box-level
    }


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        result = ocr_erax_image(sys.argv[1])
        print("=" * 60)
        print(result)
        print("=" * 60)
    else:
        print("Usage: python engine_erax.py <image_path>")
