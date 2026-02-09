# Detailed Setup Guide for Student Management System

## Understanding the CommandNotFoundException Error

### What is the error?
```
CategoryInfo : ObjectNotFound: (django-admin:String) [], CommandNotFoundException
FullyQualifiedErrorId : CommandNotFoundException
```

### Why does this happen?

This error appears when you try to run `django-admin startproject Home` without having Django installed. The error message indicates that:

1. **PowerShell cannot find the command**: The system doesn't recognize `django-admin` as a valid command
2. **Django is not installed**: The `django-admin` utility is part of Django and only becomes available after installation
3. **Not in PATH**: Even if Django is installed, it might not be in your system's PATH

### The Solution

You need to install Django first before you can use the `django-admin` command.

## Step-by-Step Installation Guide

### Step 1: Verify Python Installation

First, check if Python is installed:

**Windows (PowerShell or Command Prompt):**
```powershell
python --version
```

**Linux/Mac (Terminal):**
```bash
python3 --version
```

You should see output like: `Python 3.11.0` (version may vary)

**If Python is not installed:**
1. Download from [python.org](https://www.python.org/downloads/)
2. During installation, **CHECK** the box "Add Python to PATH"
3. Restart your terminal/PowerShell after installation

### Step 2: Verify pip Installation

```bash
pip --version
# or on Linux/Mac
pip3 --version
```

### Step 3: Create a Virtual Environment

A virtual environment keeps your project dependencies isolated.

**Windows (PowerShell):**
```powershell
# Navigate to your project directory
cd path\to\Student-Management-System-

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get an execution policy error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
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

**You'll know it's activated when you see `(venv)` at the start of your command prompt.**

### Step 4: Install Django

With the virtual environment activated:

```bash
# Install all requirements
pip install -r requirements.txt

# Or install Django only
pip install Django
```

**Wait for the installation to complete.** You should see output showing Django being downloaded and installed.

### Step 5: Verify Django Installation

```bash
django-admin --version
```

You should now see the Django version (e.g., `4.2.8`) instead of an error!

### Step 6: Create Your Django Project

Now you can successfully run:

```bash
django-admin startproject Home
```

This will create a directory structure:
```
Home/
├── Home/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── manage.py
```

### Step 7: Navigate and Run the Project

```bash
cd Home
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the Django welcome page!

## Common Issues and Solutions

### Issue 1: "Activate.ps1 cannot be loaded"

**Error:**
```
Activate.ps1 cannot be loaded because running scripts is disabled on this system
```

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue 2: "python is not recognized"

**Error:**
```
'python' is not recognized as an internal or external command
```

**Solutions:**
1. Reinstall Python and check "Add Python to PATH"
2. Manually add Python to PATH:
   - Search for "Environment Variables" in Windows
   - Add Python installation directory to PATH
   - Restart terminal

### Issue 3: "django-admin not found" even after installation

**Solutions:**
1. Make sure virtual environment is activated (you should see `(venv)`)
2. Try using: `python -m django --version`
3. Reinstall Django: `pip uninstall Django` then `pip install Django`

### Issue 4: "No module named 'django'"

**Solution:**
This means Django isn't installed in your current environment.
```bash
pip install Django
```

## Best Practices

1. **Always use a virtual environment** - Keeps dependencies isolated
2. **Activate environment before working** - Ensures correct packages are used
3. **Use requirements.txt** - Makes it easy to share and replicate environments
4. **Keep Django updated** - Run `pip install --upgrade Django` periodically
5. **Deactivate when done** - Run `deactivate` to exit the virtual environment

## Quick Reference Commands

### Virtual Environment
```bash
# Create
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (Windows CMD)
venv\Scripts\activate.bat

# Activate (Linux/Mac)
source venv/bin/activate

# Deactivate
deactivate
```

### Django
```bash
# Check version
django-admin --version

# Create project
django-admin startproject projectname

# Run development server
python manage.py runserver

# Create app
python manage.py startapp appname

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

## Next Steps

After setting up Django:

1. Explore the created project structure
2. Read Django's official tutorial: https://docs.djangoproject.com/en/stable/intro/tutorial01/
3. Start building your Student Management System features
4. Learn about Django models, views, and templates

## Getting Help

- Django Documentation: https://docs.djangoproject.com/
- Django Forum: https://forum.djangoproject.com/
- Stack Overflow: Tag your questions with `django`

## Summary

The `CommandNotFoundException` occurs simply because Django isn't installed. The solution is straightforward:
1. Install Python (if needed)
2. Create a virtual environment
3. Activate the virtual environment
4. Install Django via `pip install Django`
5. Now `django-admin` will work!
