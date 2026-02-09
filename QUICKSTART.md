# Quick Start Guide

## 🚨 Got the "CommandNotFoundException" Error?

**Don't panic!** This is a common issue that's easy to fix.

### What happened?
You tried to run `django-admin startproject Home` but got an error because **Django is not installed yet**.

### Quick Fix (2 minutes)

#### Option 1: Automated Setup (Recommended)

**Windows Users:**
1. Open PowerShell in this folder
2. Run: `.\setup.bat`
3. Wait for it to finish
4. Done! ✅

**Mac/Linux Users:**
1. Open Terminal in this folder
2. Run: `./setup.sh`
3. Wait for it to finish
4. Done! ✅

#### Option 2: Manual Setup (5 minutes)

1. **Install Django:**
   ```bash
   pip install Django
   ```

2. **Verify it works:**
   ```bash
   django-admin --version
   ```

3. **Create your project:**
   ```bash
   django-admin startproject Home
   ```

That's it! Now `django-admin` will work.

### Next Steps

After setup:
```bash
cd Home
python manage.py runserver
```

Visit http://127.0.0.1:8000 in your browser to see your Django app! 🎉

### Need Help?

- **Still stuck?** Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Want details?** Read [SETUP_GUIDE.md](SETUP_GUIDE.md)
- **Understanding Django?** See [README.md](README.md)

---

**Remember:** `django-admin` is NOT a built-in command. You must install Django first!
