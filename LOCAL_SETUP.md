# Local Setup Guide for Wagtail Bakery Demo

This guide provides comprehensive, beginner-friendly instructions for setting up and running the Wagtail Bakery Demo locally on Windows, macOS, and Linux using VS Code.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation Steps](#installation-steps)
3. [VS Code Setup](#vs-code-setup)
4. [Running the Project](#running-the-project)
5. [Common Commands](#common-commands)
6. [Troubleshooting](#troubleshooting)
7. [Project Structure](#project-structure)
8. [Next Steps](#next-steps)

---

## Prerequisites

Before starting, ensure you have the following installed on your system:

### Required Software

1. **Python 3.10+** (preferably 3.12+)
   - Download from: https://www.python.org/downloads/
   - During installation, **make sure to check "Add Python to PATH"**
   
2. **Git**
   - Download from: https://git-scm.com/downloads
   - This is needed to clone the repository
   
3. **VS Code (Optional but Recommended)**
   - Download from: https://code.visualstudio.com/
   - Provides a user-friendly interface for development

### Verify Installation

Open your terminal/PowerShell and run these commands to verify everything is installed:

```bash
python --version
pip --version
git --version
```

You should see version numbers for each. If any command is not recognized, reinstall that software and ensure it's added to your PATH.

---

## Installation Steps

### Step 1: Clone the Repository

First, decide where you want to store the project. We'll use a development directory as an example.

**On Windows:**
```bash
# Open PowerShell or Command Prompt
# Create a dev directory (optional)
mkdir C:\dev
cd C:\dev

# Clone the repository
git clone https://github.com/wagtail/bakerydemo.git
cd bakerydemo
```

**On macOS/Linux:**
```bash
# Open Terminal
# Create a dev directory (optional)
mkdir -p ~/dev
cd ~/dev

# Clone the repository
git clone https://github.com/wagtail/bakerydemo.git
cd bakerydemo
```

### Step 2: Create Virtual Environment

A virtual environment isolates project dependencies from your system Python. This is essential for clean development.

**On Windows (PowerShell):**
```powershell
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate.bat
```

> **Note for PowerShell Users:** If you get an execution policy error, run this once:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

✅ **Success indicator:** You should see `(venv)` at the beginning of your terminal prompt after activation.

### Step 3: Upgrade pip

Ensure you have the latest version of pip:

```bash
pip install --upgrade pip
```

### Step 4: Install Project Dependencies

Install all required packages from the requirements file:

```bash
pip install -r requirements/development.txt
```

This will install:
- **Django 6.0+** - Web framework
- **Wagtail 7.2+** - CMS framework
- **All supporting packages** (python-dotenv, django-debug-toolbar, Pillow for image handling, etc.)

> **Note:** This step may take a few minutes as it downloads and installs multiple packages.

### Step 5: Create Configuration Files

The project requires two configuration files for local setup:

**Create `.env` file:**
```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

**Create `bakerydemo/settings/local.py` file:**
```bash
# Windows
copy bakerydemo/settings/local.py.example bakerydemo/settings/local.py

# macOS/Linux
cp bakerydemo/settings/local.py.example bakerydemo/settings/local.py
```

These files contain local settings that should not be committed to version control.

### Step 6: Initialize the Database

Run migrations to set up the database schema:

```bash
python manage.py migrate
```

This creates the SQLite database (`db.sqlite3`) and initializes all tables.

### Step 7: Load Sample Data (Recommended)

Populate the database with sample bakery content:

```bash
python manage.py load_initial_data
```

This loads example pages, recipes, locations, staff profiles, and other content so you can immediately see the site in action.

### Step 8: Create a Superuser Account

Create an admin account to access the Wagtail admin interface:

```bash
python manage.py createsuperuser
```

You'll be prompted for:
- **Username** - Your admin username (e.g., `admin`)
- **Email** - Your email address
- **Password** - Enter a secure password (8+ characters)
- **Password (again)** - Confirm the password

Example:
```
Username: admin
Email: admin@example.com
Password: ••••••••
Password (again): ••••••••
Superuser created successfully.
```

### Step 9: Start the Development Server

Run the Django development server:

```bash
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Step 10: Access the Application

Open your web browser and visit:

- **Frontend (Website):** http://localhost:8000/
- **Admin Panel:** http://localhost:8000/admin/
  - Log in with the superuser credentials you created in Step 8

🎉 **Success!** The Wagtail Bakery Demo is now running locally on your machine.

---

## VS Code Setup

### Install Python Extension

1. Open VS Code
2. Click on the **Extensions** icon in the left sidebar (Ctrl+Shift+X)
3. Search for **"Python"**
4. Click **Install** on the official Python extension by Microsoft
5. Also install **Pylance** for better code intelligence (optional but recommended)

### Configure Python Interpreter

1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
2. Type **"Python: Select Interpreter"** and press Enter
3. Choose the interpreter from your `venv` folder (it will show something like `./venv/bin/python`)
4. This tells VS Code to use your virtual environment

### Create Debug Configuration

To easily run and debug the project from VS Code:

1. Create a new folder `.vscode` in your project root (if it doesn't exist)
2. Inside `.vscode`, create a file named `launch.json` with this content:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": ["runserver"],
            "django": true,
            "jinja": true,
            "justMyCode": true,
            "console": "integratedTerminal",
            "env": {"PYTHONUNBUFFERED": "1"}
        }
    ]
}
```

Now you can:
- Press **F5** to start the server with debugging
- Set breakpoints by clicking on line numbers
- Use the Debug Console to inspect variables

### Recommended VS Code Extensions

Install these extensions for a better development experience:

| Extension | Publisher | Purpose |
|-----------|-----------|---------|
| Python | Microsoft | Core Python support |
| Pylance | Microsoft | Enhanced code intelligence |
| Django | Baptiste Darthenay | Django syntax highlighting |
| Prettier | Prettier | Code formatting |
| REST Client | Huachao Mao | Test API endpoints |
| Thunder Client | Thunder Client | API testing (alternative to REST Client) |
| Markdown Preview | Built-in | Preview markdown files |

### VS Code Terminal Usage

1. Open the integrated terminal: `Ctrl+` `` (backtick) or `Ctrl+Shift+~`
2. The terminal will automatically activate your virtual environment if configured correctly
3. You can run management commands directly from this terminal

---

## Running the Project

### Daily Workflow

Each time you work on the project:

1. **Navigate to project directory:**
   ```bash
   cd path/to/bakerydemo
   ```

2. **Activate virtual environment:**
   - Windows PowerShell: `venv\Scripts\Activate.ps1`
   - Windows Command Prompt: `venv\Scripts\activate.bat`
   - macOS/Linux: `source venv/bin/activate`

3. **Start development server:**
   ```bash
   python manage.py runserver
   ```

4. **Open browser to:** http://localhost:8000

5. **When finished, deactivate virtual environment:**
   ```bash
   deactivate
   ```

### Running on a Different Port

If port 8000 is already in use:

```bash
python manage.py runserver 8001
```

Then access the site at http://localhost:8001

---

## Common Commands

### Django Management Commands

```bash
# Show all available commands
python manage.py help

# Create database migrations for model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Run the development server (default: port 8000)
python manage.py runserver

# Create a new superuser account
python manage.py createsuperuser

# Reset admin password
python manage.py reset_admin_password

# Load initial fixture data
python manage.py load_initial_data

# Create random demo data
python manage.py create_random_data

# Reset everything to initial state
python manage.py reset_demo

# Run tests
python manage.py test

# Create an interactive Python shell with Django context
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic
```

### Virtual Environment Commands

```bash
# Activate virtual environment (run these in project directory)
# Windows PowerShell:
venv\Scripts\Activate.ps1
# Windows Command Prompt:
venv\Scripts\activate.bat
# macOS/Linux:
source venv/bin/activate

# Deactivate virtual environment (from anywhere)
deactivate

# Show installed packages
pip list

# Check for outdated packages
pip list --outdated

# Upgrade a specific package
pip install --upgrade package_name
```

---

## Troubleshooting

### Python-Related Issues

#### Python not found / Command 'python' not recognized

**On Windows:**
- Reinstall Python and **check "Add Python to PATH"** during installation
- Try using `python3` instead of `python`
- Verify installation: `python --version`

**On macOS/Linux:**
- Use `python3` instead of `python`
- If `python3` is not available: `brew install python3` (requires Homebrew)

#### Wrong Python version

```bash
# Check which Python the virtual environment is using
which python        # macOS/Linux
where python        # Windows

# Create venv with specific Python version
python3.12 -m venv venv
```

### Virtual Environment Issues

#### Virtual environment not activating

**Windows PowerShell:** Ensure execution policy allows scripts:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating again:
```powershell
venv\Scripts\Activate.ps1
```

**macOS/Linux:** Make sure you're in the project directory:
```bash
cd path/to/bakerydemo
source venv/bin/activate
```

#### Can't find pip

Reinstall pip:
```bash
python -m pip install --upgrade pip
```

### Installation Issues

#### Dependencies fail to install

```bash
# Upgrade pip first
pip install --upgrade pip

# Try installing requirements again with verbose output
pip install -r requirements/development.txt -v

# If specific package fails, install individually
pip install Django==5.0
```

#### Missing Microsoft Visual C++ (Windows)

Some packages require C++ compiler. Download from:
https://visualstudio.microsoft.com/visual-cpp-build-tools/

### Database Issues

#### Database locked error

```bash
# Stop the server (Ctrl+C) and try again
# If problem persists, delete and recreate:
rm db.sqlite3
python manage.py migrate
python manage.py load_initial_data
```

#### Migration errors

```bash
# Show migration status
python manage.py showmigrations

# Reapply all migrations
python manage.py migrate --plan
python manage.py migrate

# If stuck, reset migrations (WARNING: deletes data)
rm db.sqlite3
python manage.py migrate
```

#### "No such table" error

```bash
# Run migrations to create tables
python manage.py migrate
```

### Server Issues

#### Port 8000 already in use

```bash
# Use a different port
python manage.py runserver 8001

# Or find and kill the process using port 8000
# Windows:
netstat -ano | findstr :8000

# macOS/Linux:
lsof -i :8000
kill -9 <PID>
```

#### Can't access http://localhost:8000

- Check if server is running (should see "Starting development server" message)
- Try http://127.0.0.1:8000 instead
- Check firewall settings
- Try a different port: `python manage.py runserver 8001`

### Admin Panel Issues

#### Can't log in to admin

**Forgot password?**
```bash
python manage.py reset_admin_password
```

**Create a new superuser:**
```bash
python manage.py createsuperuser
```

#### Admin styles/CSS not showing

```bash
python manage.py collectstatic --noinput
```

### Performance Issues

#### Slow startup time

This is normal for the first run. Subsequent runs are faster.

If very slow:
- Check system resources (RAM, CPU)
- Ensure SSD is not full
- Close other applications

#### Slow page loading

- Run in production mode settings (not recommended for local development)
- Disable debug toolbar: Comment out `django_extensions` in `INSTALLED_APPS`
- Check database size: `ls -lh db.sqlite3`

---

## Project Structure

```
bakerydemo/
│
├── bakerydemo/                    # Main Django project directory
│   ├── settings/
│   │   ├── base.py               # Base settings for all environments
│   │   ├── dev.py                # Development settings
│   │   ├── production.py          # Production settings
│   │   ├── test.py               # Test settings
│   │   ├── local.py.example      # Example local settings (DO NOT edit)
│   │   └── __init__.py
│   ├── static/                    # Static files (CSS, JS, images)
│   ├── media/                     # User-uploaded files
│   ├── templates/                 # Main templates
│   ├── urls.py                   # Main URL configuration
│   ├── wsgi.py                   # WSGI application (for production)
│   ├── asgi.py                   # ASGI application (for async)
│   └── __init__.py
│
├── bakerydemo/                    # Django apps directory
│   ├── base/                      # Base app (homepage, layout)
│   │   ├── models.py             # Models for base functionality
│   │   ├── views.py              # View functions
│   │   ├── templates/            # HTML templates
│   │   ├── migrations/           # Database migrations
│   │   ├── management/commands/  # Management commands
│   │   ├── tests/                # Tests for this app
│   │   └── wagtail_hooks.py      # Wagtail customizations
│   │
│   ├── blog/                      # Blog app
│   │   ├── models.py
│   │   ├── templates/
│   │   └── migrations/
│   │
│   ├── breads/                    # Products/Breads app
│   │   ├── models.py
│   │   ├── templates/
│   │   └── migrations/
│   │
│   ├── locations/                 # Store locations app
│   │   ├── models.py
│   │   ├── templates/
│   │   └── migrations/
│   │
│   ├── people/                    # Staff profiles app
│   │   ├── models.py
│   │   ├── templates/
│   │   └── migrations/
│   │
│   ├── recipes/                   # Recipes app
│   │   ├── models.py
│   │   ├── templates/
│   │   └── migrations/
│   │
│   └── search/                    # Search functionality
│       ├── views.py
│       └── templates/
│
├── manage.py                      # Django management script
├── requirements/                  # Python dependencies
│   ├── base.txt                  # Core dependencies
│   ├── development.txt           # Development tools
│   └── production.txt            # Production packages
├── .env.example                   # Example environment variables (DO NOT edit)
├── .gitignore                     # Files to exclude from git
├── README.md                      # Official project documentation
├── LOCAL_SETUP.md                 # This file
└── Makefile                       # Useful make commands
```

### Key Files Explained

| File | Purpose |
|------|---------|
| `manage.py` | Command-line tool for Django management |
| `db.sqlite3` | SQLite database (created after first migration) |
| `.env` | Local environment variables (gitignored, never commit) |
| `bakerydemo/settings/base.py` | Main Django configuration |
| `bakerydemo/urls.py` | URL routing configuration |
| `requirements/development.txt` | Python packages needed for development |

---

## Next Steps

After successfully setting up the project:

### 1. Explore the Admin Interface

- Visit http://localhost:8000/admin/
- Browse existing pages and content
- Try creating a new page or blog post
- Explore the page editor interface

### 2. Understand Wagtail Structure

- Read [Wagtail Documentation](https://docs.wagtail.org/)
- Learn about StreamFields for flexible content
- Understand page hierarchies and inheritance

### 3. Customize the Project

- Modify templates in `bakerydemo/base/templates/`
- Add new page types in the app models
- Create new Django apps for new features
- Customize styling with CSS

### 4. Write Code

- Create new models in `models.py`
- Create views in `views.py`
- Add templates to `templates/` directories
- Run tests: `python manage.py test`

### 5. Learn Django and Wagtail

- [Django Documentation](https://docs.djangoproject.com/)
- [Wagtail Official Tutorial](https://docs.wagtail.org/en/stable/getting_started/tutorial.html)
- [Wagtail API Documentation](https://docs.wagtail.org/en/stable/advanced_topics/api/index.html)

### 6. Version Control

Remember to:
- Never commit `.env` or `bakerydemo/settings/local.py`
- Commit only code changes and migrations
- Write meaningful commit messages
- Push to your fork before creating pull requests

---

## Getting Help

### If You Get Stuck

1. **Check the [Troubleshooting](#troubleshooting) section** in this guide
2. **Search the [Wagtail Documentation](https://docs.wagtail.org/)**
3. **Ask on [Wagtail Community Forums](https://wagtail.io/community/)**
4. **Check [Stack Overflow](https://stackoverflow.com/questions/tagged/wagtail)** for similar issues
5. **Report bugs on [GitHub Issues](https://github.com/wagtail/bakerydemo/issues)**

### Contributing to This Guide

If you find:
- Unclear instructions
- Errors in the guide
- Better ways to explain concepts
- Missing troubleshooting sections

Please open a pull request or file an issue on GitHub to help improve this guide for future developers!

---

## Quick Reference

### Windows PowerShell Quick Setup
```powershell
git clone https://github.com/wagtail/bakerydemo.git
cd bakerydemo
python -m venv venv
venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements/development.txt
copy .env.example .env
copy bakerydemo/settings/local.py.example bakerydemo/settings/local.py
python manage.py migrate
python manage.py load_initial_data
python manage.py createsuperuser
python manage.py runserver
# Then visit http://localhost:8000/admin/ in your browser
```

### macOS/Linux Quick Setup
```bash
git clone https://github.com/wagtail/bakerydemo.git
cd bakerydemo
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements/development.txt
cp .env.example .env
cp bakerydemo/settings/local.py.example bakerydemo/settings/local.py
python manage.py migrate
python manage.py load_initial_data
python manage.py createsuperuser
python manage.py runserver
# Then visit http://localhost:8000/admin/ in your browser
```

---

**Last Updated:** March 2026

This guide complements the [official Wagtail documentation](https://docs.wagtail.org/). For detailed information about Wagtail features and concepts, please refer to the official docs.
