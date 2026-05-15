import pytest\r
import json\r
import os\r
from pathlib import Path\r
\r
def test_config_json_exists_and_valid():\r
    # Verify config.json exists and is valid JSON\r
    project_root = Path(__file__).resolve().parent.parent.parent\r
    config_path = project_root / "ocr_scanner" / "config.json"\r
    \r
    assert config_path.exists(), f"config.json not found at {config_path}"\r
    \r
    with open(config_path, "r", encoding="utf-8") as f:\r
        config_data = json.load(f)\r
        \r
    assert "ocr" in config_data\r
    assert "post_processing" in config_data\r
    assert "default_engine" in config_data["ocr"]\r
