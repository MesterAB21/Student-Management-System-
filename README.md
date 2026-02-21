# Student Management System

A Django-based Student Management System for managing student records, courses, and academic information.

---

## 🚨 Getting CommandNotFoundException Error?

**Quick Answer:** Django is not installed! → See [Quick Start Guide](QUICKSTART.md) for the 2-minute fix.

---

## Problem: CommandNotFoundException for django-admin

If you encounter the error:
```
CategoryInfo : ObjectNotFound: (django-admin:String) [], CommandNotFoundException
FullyQualifiedErrorId : CommandNotFoundException
```

**What's the problem?**

This error occurs because:
1. **Django is not installed** on your system
2. **Python is not in your system PATH** 
3. **Virtual environment is not activated** (if you're using one)

The `django-admin` command is only available after Django is properly installed. It's not a built-in command in Windows PowerShell or any operating system.

## Quick Setup

### Prerequisites
- Python 3.8 or higher installed
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/MesterAB21/Student-Management-System-.git
   cd Student-Management-System-
   ```

2. **Create a virtual environment (recommended)**
   
   **Windows (PowerShell):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   python -m venv venv
   venv\Scripts\activate.bat
   ```
   
   **Linux/Mac:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Django and dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Django installation**
   ```bash
   django-admin --version
   ```

5. **Create/Run the Django project**
   ```bash
   # If starting fresh
   django-admin startproject Home
   
   # Navigate to project
   cd Home
   
   # Run migrations
   python manage.py migrate
   
   # Create superuser
   python manage.py createsuperuser
   
   # Run development server
   python manage.py runserver
   ```

## Alternative Setup Methods

### Using setup script (Windows)
```powershell
.\setup.bat
```

### Using setup script (Linux/Mac)
```bash
chmod +x setup.sh
./setup.sh
```

## Troubleshooting

### PowerShell Execution Policy Error
If you get an execution policy error when activating the virtual environment on Windows:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Django command not found after installation
Make sure your virtual environment is activated. You should see `(venv)` at the beginning of your command prompt.

### Python not recognized
Install Python from [python.org](https://www.python.org/downloads/) and make sure to check "Add Python to PATH" during installation.

## Project Structure
```
Student-Management-System/
├── README.md              # Main documentation (you are here)
├── QUICKSTART.md          # Fast 2-minute setup guide
├── SETUP_GUIDE.md         # Detailed installation instructions
├── TROUBLESHOOTING.md     # Solutions for common errors
├── requirements.txt       # Python dependencies
├── setup.bat              # Automated setup for Windows
├── setup.sh               # Automated setup for Linux/Mac
└── Home/                  # Django project (created after setup)
```

## 📚 Documentation Guide

| Document | Purpose | When to Use |
|----------|---------|-------------|
| [QUICKSTART.md](QUICKSTART.md) | Get started in 2 minutes | First time setup, need quick fix |
| [SETUP_GUIDE.md](SETUP_GUIDE.md) | Comprehensive installation guide | Want detailed instructions |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Fix CommandNotFoundException | Having django-admin errors |
| [README.md](README.md) | Project overview | Understanding the project |

**External Resources:**
- [Django 4.2 Official Documentation](https://docs.djangoproject.com/en/4.2/)
- [Django 4.2 Tutorial](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is open source and available under the MIT License.
