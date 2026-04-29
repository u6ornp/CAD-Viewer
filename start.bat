@echo off
title CAD Viewer
color 0A
echo.
echo   ╔════════════════════════════════════════════╗
echo   ║         CAD Viewer - Starting...           ║
echo   ╚════════════════════════════════════════════╝
echo.

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo   ❌ Python not found!
    echo.
    echo   Download from: https://www.python.org/downloads/
    echo   Tick "Add Python to PATH" during install.
    echo.
    pause
    exit /b 1
)

cd /d "%~dp0"
python server.py
pause
