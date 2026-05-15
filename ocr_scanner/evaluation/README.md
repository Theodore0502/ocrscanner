# OCR Evaluation Tools

This folder contains scripts for evaluating OCR accuracy and visualizing results.

## Scripts

### `calculate_accuracy.py`

Calculates accuracy metrics for OCR results by comparing with ground truth files.

**Metrics:**

- **CER (Character Error Rate):** Percentage of character-level errors
- **WER (Word Error Rate):** Percentage of word-level errors
- **Character Accuracy:** `(1 - CER) × 100%`
- **Word Accuracy:** `(1 - WER) × 100%`

**Usage:**

```powershell
python ocr_scanner/evaluation/calculate_accuracy.py
```

**Output:**

- Console summary with metrics for each document
- `results/accuracy_report.json` - Detailed JSON report

### `visualize_results.py`

Creates visualizations from the accuracy report.

**Generates:**

- `results/accuracy_chart.png` - Bar charts comparing accuracy metrics
- `results/performance_metrics.png` - Summary dashboard with statistics

**Usage:**

```powershell
python ocr_scanner/evaluation/visualize_results.py
```

**Requirements:**

- `matplotlib` - Install with `pip install matplotlib`
- Must run `calculate_accuracy.py` first

## Workflow

1. **Process OCR documents** (already done via `batch_ocr_gpu.py`)
2. **Calculate accuracy:**
   ```powershell
   python ocr_scanner/evaluation/calculate_accuracy.py
   ```
3. **Generate visualizations:**
   ```powershell
   python ocr_scanner/evaluation/visualize_results.py
   ```
4. **Review results** in `results/` folder

## Documents Evaluated

Documents with ground truth available:

- `dl_2025_0002` - Image-based OCR
- `dl_2025_0003` - ProtonX corrected
- `dl_2025_0005` - To be processed

## Results Location

All results are saved in `ocr_scanner/evaluation/results/`:

- `accuracy_report.json` - Raw metrics data
- `accuracy_chart.png` - Accuracy comparison visualizations
- `performance_metrics.png` - Performance dashboard
