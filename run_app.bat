@echo off
cd /d "%~dp0"
set PYTHONUTF8=1
if not defined HF_HOME set HF_HOME=%~dp0.hf_cache
python desktop_app/main.py
pause
