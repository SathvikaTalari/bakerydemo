# Local Setup Guide for Bakery Demo (Wagtail CMS)

This guide will help you set up and run the Wagtail-based Bakery Demo project locally using VS Code.

## Prerequisites

Before starting, ensure you have the following installed:

- **Python 3.12.1** or higher - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **VS Code** - [Download VS Code](https://code.visualstudio.com/)
- **pip** (comes with Python) or **pip3**

### Verify Installation

Open your terminal and run:

```bash
python --version      # or python3 --version
pip --version         # or pip3 --version
git --version
```

## Step 1: Clone the Repository

If you haven't already, clone the repository:

```bash
git clone https://github.com/SathvikaTalari/bakerydemo.git
cd bakerydemo
```

## Step 2: Create a Virtual Environment

Creating a virtual environment isolates project dependencies:

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate

# On Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```

**You should see `(venv)` at the start of your terminal prompt.**

## Step 3: Upgrade pip

```bash
pip install --upgrade pip
```

## Step 4: Install Dependencies

Install the development dependencies:

```bash
pip install -r requirements/development.txt
```

This will install:
- Django 6.0+
- Wagtail 7.2+
- All required packages (python-dotenv, django-debug-toolbar, etc.)

## Step 5: Create Environment File

Create a `.env` file in the project root:

```bash
# Copy the example file
cp .env.example .env
```

Or create `.env` manually with these basic settings:

```
DEBUG=True
SECRET_KEY=your-secret-key-here-change-in-production
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

## Step 6: Run Database Migrations

Initialize the database with existing migrations:

```bash
python manage.py migrate
```

## Step 7: Load Initial Data (Optional)

To populate the database with sample bakery content:

```bash
python manage.py load_initial_data
```

Or create random demo data:

```bash
python manage.py create_random_data
```

## Step 8: Create a Superuser

Create an admin account to access the Wagtail admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter:
- Username
- Email
- Password (enter twice to confirm)

## Step 9: Start the Development Server

Run the Django development server:

```bash
python manage.py runserver
```

You should see output like:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Step 10: Access the Application

Open your browser and visit:

- **Website**: http://localhost:8000/
- **Wagtail Admin**: http://localhost:8000/admin/
  - Log in with the superuser credentials you created in Step 8

## VS Code Setup (Recommended)

### 1. Install Python Extension

In VS Code:
1. Go to Extensions (Ctrl+Shift+X)
2. Search for "Python"
3. Install the official Python extension by Microsoft

### 2. Select Python Interpreter

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Type "Python: Select Interpreter"
3. Choose the one from your `venv` directory (it will show the virtual environment path)

### 3. Create VS Code Launch Configuration

Create `.vscode/launch.json` in your project root:

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
            "console": "integratedTerminal"
        }
    ]
}
```

Then, you can run the server from VS Code using F5 or the Run menu.

### 4. Install Recommended Extensions

Search for and install these extensions in VS Code:
- **Python** (Microsoft)
- **Pylance** (Microsoft) - Better code intelligence
- **Django** (Baptiste Darthenay) - Django syntax highlighting
- **Prettier** - Code formatting
- **Thunder Client** or **REST Client** - For API testing

## Common Commands

### Helpful Django Management Commands

```bash
# Reset everything and start fresh
python manage.py reset_demo

# Reset admin password
python manage.py reset_admin_password

# Run tests
python manage.py test

# Create migrations for changes
python manage.py makemigrations

# See all available commands
python manage.py help
```

### Deactivate Virtual Environment

When you're done working:

```bash
deactivate
```

## Troubleshooting

### Python version mismatch
If you have multiple Python versions:
```bash
python3.12 -m venv venv
```

### Permission denied on Linux/Mac
```bash
chmod +x manage.py
```

### Port 8000 already in use
```bash
# Use a different port
python manage.py runserver 8001
```

### Database errors
```bash
# Delete the database and start fresh
rm db.sqlite3
python manage.py migrate
python manage.py load_initial_data
```

### Missing dependencies
```bash
# Reinstall all requirements
pip install -r requirements/development.txt --force-reinstall
```

## Project Structure

```
bakerydemo/
├── bakerydemo/              # Main project settings
│   ├── settings/
│   │   ├── base.py         # Base settings
│   │   ├── dev.py          # Development settings
│   │   ├── production.py    # Production settings
│   │   └── test.py         # Test settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI application
├── bakerydemo/
│   ├── base/               # Base app (homepage, layout)
│   ├── blog/               # Blog app
│   ├── breads/             # Breads/products app
│   ├── locations/          # Store locations
│   ├── people/             # Staff profiles
│   ├── recipes/            # Recipes
│   └── search/             # Search functionality
├── manage.py               # Django management script
├── requirements/           # Python dependencies
│   ├── base.txt           # Core dependencies
│   ├── development.txt    # Dev tools
│   └── production.txt     # Production packages
└── README.md              # Project documentation
```

## Next Steps

1. Explore the Wagtail admin at http://localhost:8000/admin/
2. Create new pages and content
3. Customize templates in the app directories
4. Modify models to add new features

For more information, visit:
- [Wagtail Documentation](https://docs.wagtail.org/)
- [Django Documentation](https://docs.djangoproject.com/)

---

Need help? Check the project's README.md or visit the Wagtail community forum.
