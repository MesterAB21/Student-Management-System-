@echo off
REM Setup script for Student Management System (Windows)
REM This script automates the Django setup process

echo ========================================
echo Student Management System - Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [1/5] Python is installed
python --version
echo.

REM Create virtual environment
echo [2/5] Creating virtual environment...
if exist venv (
    echo Virtual environment already exists, skipping creation
) else (
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully
)
echo.

REM Activate virtual environment and install dependencies
echo [3/5] Installing Django and dependencies...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

REM Verify Django installation
echo [4/5] Verifying Django installation...
django-admin --version
if errorlevel 1 (
    echo ERROR: Django was not installed correctly
    pause
    exit /b 1
)
echo Django installed successfully!
echo.

REM Instructions for next steps
echo [5/5] Setup Complete!
echo ========================================
echo.
echo Your environment is ready! Next steps:
echo.
echo 1. Activate the virtual environment:
echo    venv\Scripts\activate.bat
echo.
echo 2. Create your Django project (if not exists):
echo    django-admin startproject Home
echo.
echo 3. Navigate to project and run server:
echo    cd Home
echo    python manage.py runserver
echo.
echo For detailed instructions, see SETUP_GUIDE.md
echo ========================================
echo.
pause
