"""Insert ocr_paddle_image_detailed_fast into engine_paddle.py"""
with open('ocr_scanner/src/ocr/engine_paddle.py', 'rb') as f:
    content = f.read().decode('utf-8')

fast_fn = (
    "\n"
    "def ocr_paddle_image_detailed_fast(image_path: str, apply_postprocessing: bool = True) -> dict:\n"
    "    \"\"\"OCR nhanh cho PDF batch - dung fast singleton (khong unwarping) -> nhanh ~3-5x.\"\"\"\n"
    "    ocr = get_paddle_ocr_fast()\n"
    "    result = ocr.ocr(image_path)\n"
    "    text, lines_info = extract_text_from_result(result)\n"
    "    avg_confidence = (\n"
    "        sum(l['confidence'] for l in lines_info) / len(lines_info)\n"
    "        if lines_info else 0.0\n"
    "    )\n"
    "    if apply_postprocessing and text:\n"
    "        text = post_process_vietnamese(text)\n"
    "        for line in lines_info:\n"
    "            line['text_cleaned'] = post_process_vietnamese(line['text'])\n"
    "    return {'text': text, 'lines': lines_info, 'avg_confidence': avg_confidence}\n"
    "\n"
    "\n"
)

marker = "def ocr_paddle_image_with_protonx"
if marker in content:
    content = content.replace(marker, fast_fn + marker, 1)
    with open('ocr_scanner/src/ocr/engine_paddle.py', 'wb') as f:
        f.write(content.encode('utf-8'))
    print("OK: fast function inserted successfully")
else:
    print("ERROR: marker 'def ocr_paddle_image_with_protonx' not found")
