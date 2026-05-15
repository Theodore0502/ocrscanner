import pytest\r
from core.ocr_worker import FileResult, BatchProgress, is_supported_image, is_supported_pdf\r
\r
def test_file_result_initialization():\r
    result = FileResult(file_path="test.jpg", status="pending")\r
    assert result.file_path == "test.jpg"\r
    assert result.status == "pending"\r
    assert result.raw_text == ""\r
    assert result.error == ""\r
\r
def test_batch_progress_initialization():\r
    progress = BatchProgress(total_files=10)\r
    assert progress.total_files == 10\r
    assert progress.processed_files == 0\r
    assert progress.successful_files == 0\r
    assert progress.failed_files == 0\r
    assert progress.is_finished is False\r
\r
def test_is_supported_image():\r
    assert is_supported_image("document.jpg") is True\r
    assert is_supported_image("scan.png") is True\r
    assert is_supported_image("report.pdf") is False\r
    assert is_supported_image("data.txt") is False\r
\r
def test_is_supported_pdf():\r
    assert is_supported_pdf("document.pdf") is True\r
    assert is_supported_pdf("document.PDF") is True\r
    assert is_supported_pdf("image.jpg") is False\r
