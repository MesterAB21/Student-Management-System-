#!/bin/bash
# Setup script for Student Management System (Linux/Mac)
# This script automates the Django setup process

set -e  # Exit on error

echo "========================================"
echo "Student Management System - Setup"
echo "========================================"
echo ""

# Detect Python command
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
    PIP_CMD=pip3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
    PIP_CMD=pip
else
    echo "ERROR: Python is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "[1/5] Python is installed"
$PYTHON_CMD --version
echo ""

# Create virtual environment
echo "[2/5] Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists, skipping creation"
else
    $PYTHON_CMD -m venv venv
    echo "Virtual environment created successfully"
fi
echo ""

# Activate virtual environment and install dependencies
echo "[3/5] Installing Django and dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo ""

# Verify Django installation
echo "[4/5] Verifying Django installation..."
django-admin --version
echo "Django installed successfully!"
echo ""

# Instructions for next steps
echo "[5/5] Setup Complete!"
echo "========================================"
echo ""
echo "Your environment is ready! Next steps:"
echo ""
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Create your Django project (if not exists):"
echo "   django-admin startproject Home"
echo ""
echo "3. Navigate to project and run server:"
echo "   cd Home"
echo "   python manage.py runserver"
echo ""
echo "For detailed instructions, see SETUP_GUIDE.md"
echo "========================================"
echo ""
