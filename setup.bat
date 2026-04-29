@echo off
setlocal enabledelayedexpansion

echo.
echo   ╔════════════════════════════════════════════╗
echo   ║   CAD Viewer - Setup ^& Dependencies        ║
echo   ╚════════════════════════════════════════════╝
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo   ❌ Python not found!
    echo   Please install Python from https://www.python.org/downloads/
    echo   Make sure to tick "Add Python to PATH" during install.
    echo.
    pause
    exit /b 1
)

echo   ⬇ Installing dependencies...
echo   This may take a few minutes...
echo.

pip install --upgrade pip >nul 2>&1

python -m pip install cadquery==2.3.0

if errorlevel 1 (
    echo.
    echo   ⚠ Installation completed with some errors.
    echo   Try running setup.bat again, or:
    echo   pip install cadquery --upgrade
    echo.
) else (
    echo.
    echo   ✅ All dependencies installed!
    echo   STEP files are now fully supported.
    echo.
)

echo   You can now run: start.bat
echo.
pause
