@echo off
chcp 65001 >nul
title 考研英语二背诵 - 手机端局域网服务
cd /d "%~dp0"
python serve_mobile.py
pause
