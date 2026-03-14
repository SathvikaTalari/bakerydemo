# How to Contribute LOCAL_SETUP.md to the Wagtail Bakery Demo Project

This guide walks you through the process of contributing your improved setup documentation to the official Wagtail Bakery Demo project via a GitHub Pull Request.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setting Up for Contribution](#setting-up-for-contribution)
3. [Making Your Changes](#making-your-changes)
4. [Committing Changes](#committing-changes)
5. [Creating a Pull Request](#creating-a-pull-request)
6. [Handling Feedback](#handling-feedback)
7. [Tips for Success](#tips-for-success)

---

## Prerequisites

Before you start, you'll need:

- **Git** installed and configured with your name and email
- **GitHub account** (free at https://github.com/signup)
- The Wagtail Bakery Demo repository cloned locally
- **Familiarity with basic Git commands**

### Configure Git (if you haven't already)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Verify it worked:
```bash
git config --global user.name
git config --global user.email
```

---

## Setting Up for Contribution

### Step 1: Fork the Official Repository

1. Go to https://github.com/wagtail/bakerydemo
2. Click the **Fork** button in the top-right corner
3. This creates a copy of the project under your GitHub account (e.g., `your-username/bakerydemo`)

### Step 2: Clone Your Fork Locally

In your terminal, clone **your forked repository** (not the official one):

```bash
git clone https://github.com/YOUR-USERNAME/bakerydemo.git
cd bakerydemo
```

Replace `YOUR-USERNAME` with your actual GitHub username.

### Step 3: Add Upstream Remote

Add the official repository as a remote called "upstream" so you can stay updated:

```bash
git remote add upstream https://github.com/wagtail/bakerydemo.git
```

Verify you have both remotes:
```bash
git remote -v
```

You should see:
```
origin    https://github.com/YOUR-USERNAME/bakerydemo.git (fetch)
origin    https://github.com/YOUR-USERNAME/bakerydemo.git (push)
upstream  https://github.com/wagtail/bakerydemo.git (fetch)
upstream  https://github.com/wagtail/bakerydemo.git (push)
```

### Step 4: Create a Feature Branch

Create a new branch for your documentation work. **Never commit directly to `main`!**

```bash
# First, make sure you're on main and up-to-date
git checkout main
git pull upstream main

# Create and switch to a new branch
git checkout -b docs/local-setup-guide
```

Good branch naming conventions:
- `docs/` - for documentation
- `feature/` - for new features
- `fix/` - for bug fixes
- `refactor/` - for refactoring

Examples: `docs/local-setup-guide`, `docs/vs-code-setup`, `docs/windows-setup`

---

## Making Your Changes

### Add or Update LOCAL_SETUP.md

Now you can add or update the LOCAL_SETUP.md file:

```bash
# If you already have a LOCAL_SETUP.md, you can verify it's there
ls LOCAL_SETUP.md

# Or add your content (it should already be there from your fork)
# Edit the file with your text editor or VS Code
```

### Make Sure Documentation Follows Project Style

1. **Check existing documentation** style in the project
2. **Use markdown formatting** correctly (headings, code blocks, etc.)
3. **Keep line lengths** reasonable (around 80-100 characters)
4. **Use clear, concise language** for beginners
5. **Include examples** for each step
6. **Add table of contents** for long documents
7. **Link to official resources** (Wagtail docs, Django docs, etc.)

### Verify Your Changes

Before committing, ensure your markdown renders correctly:

```bash
# View your file in terminal with syntax highlighting
# (requires `bat` or use `cat` as fallback)
cat LOCAL_SETUP.md

# Or open it in VS Code and use the Markdown Preview
# (Ctrl+Shift+V)
```

---

## Committing Changes

### Step 1: Stage Your Changes

```bash
# Check what files you've changed
git status

# Stage your changes
git add LOCAL_SETUP.md

# Verify what's staged
git diff --staged
```

### Step 2: Write a Clear Commit Message

```bash
git commit -m "Add comprehensive LOCAL_SETUP.md guide for beginners

- Add VS Code setup instructions for all platforms
- Include troubleshooting section with common issues
- Add project structure documentation
- Include quick reference sections for different platforms
- Add support for Windows PowerShell, cmd, macOS, and Linux
- Include recommended VS Code extensions"
```

**Good commit message tips:**
- **First line:** Short, descriptive summary (50 characters max)
- **Blank line:** Separate the summary from the body
- **Body:** Explain *what* and *why*, not *how* (2-3 lines)
- **Be specific:** Mention features, platforms, or sections you added

### Step 3: Push to Your Fork

```bash
git push origin docs/local-setup-guide
```

If this is the first push of this branch, you might need to use:
```bash
git push --set-upstream origin docs/local-setup-guide
```

---

## Creating a Pull Request

### Step 1: Open Pull Request on GitHub

1. Go to https://github.com/YOUR-USERNAME/bakerydemo
2. You should see a notification: **"docs/local-setup-guide had recent pushes"**
3. Click the green **"Compare & pull request"** button
4. Or go to the **"Pull requests"** tab and click **"New pull request"**

### Step 2: Fill Out the PR Template

When creating a PR, you'll see a form. Fill it out carefully:

**PR Title:**
```
Add comprehensive LOCAL_SETUP.md guide for beginners
```

**PR Description:**
```
## What does this PR do?

This PR adds a comprehensive LOCAL_SETUP.md file that provides detailed, beginner-friendly setup instructions for the Wagtail Bakery Demo project.

## Why is this needed?

- Official docs are concise but may confuse beginners
- No centralized guide for VS Code setup
- Lacks platform-specific guidance (Windows PowerShell, cmd, macOS, Linux)
- No troubleshooting section for common issues
- No VS Code extension recommendations

## What's included?

- [x] Step-by-step installation instructions
- [x] VS Code setup and configuration
- [x] Platform-specific commands (Windows, macOS, Linux)
- [x] Common commands reference
- [x] Comprehensive troubleshooting section
- [x] Project structure explanation
- [x] Quick reference for power users

## Testing

This guide was tested on:
- [x] Windows 11 with PowerShell
- [x] Windows 11 with Command Prompt
- [x] macOS 13+ with Zsh
- [ ] Ubuntu 22.04 (if you tested on Linux)

## Screenshots/Examples

The document includes:
- Terminal output examples
- File creation examples
- URL references for browser access

## Checklist

- [x] My changes follow the project's style guide
- [x] I've added/updated documentation as needed
- [x] I've tested the instructions work as documented
- [x] I've added links to relevant external resources
```

### Step 3: Review Before Submitting

Before clicking "Create pull request":

1. **Verify the base branch** is `main` (not another branch)
2. **Check the diff** at the bottom to ensure only your changes are included
3. **Proofread** your PR title and description
4. **Add meaningful labels** if the repository uses them (e.g., `documentation`)

### Step 4: Submit the PR

Click the green **"Create pull request"** button.

---

## Handling Feedback

### Step 1: Respond to Review Comments

Maintainers may suggest improvements. Here's how to handle it:

1. **Read comments carefully** - maintainers often explain why changes are needed
2. **Ask clarifying questions** if you don't understand
3. **Engage respectfully** - open source is collaborative
4. **Don't take criticism personally** - it's about improving the project

### Step 2: Make Requested Changes

If you need to update your PR:

```bash
# Make your changes to the file
# Edit LOCAL_SETUP.md with your text editor

# Stage and commit the changes
git add LOCAL_SETUP.md
git commit -m "Address review feedback: clarify Windows setup steps"

# Push the updated commits
git push origin docs/local-setup-guide
```

The PR automatically updates with new commits—no need to create a new one!

### Step 3: Request Re-review

After pushing updates:

1. Go back to your PR on GitHub
2. Look for a **"Request review"** or **"Reviewers"** section
3. Click it and select the reviewer again
4. Add a comment: "Ready for re-review, thanks!"

### Step 4: Celebrate When Merged!

Once approved, a maintainer will merge your PR. Congratulations! 🎉

Your contribution is now part of the official Wagtail Bakery Demo project.

---

## Tips for Success

### 1. Keep PRs Focused

- **One feature/improvement per PR** if possible
- Smaller PRs are easier to review and merge
- If your changes are large, consider splitting into multiple PRs

### 2. Communicate Clearly

- Explain *why* your changes matter
- Link to related issues or discussions
- Reference relevant documentation or standards

### 3. Be Responsive

- Check for feedback regularly
- Reply to comments within a day if possible
- Be patient—maintainers volunteer their time

### 4. Learn From Feedback

- View rejected feedback as learning opportunities
- Ask questions if you don't understand suggestions
- Thank reviewers for their time

### 5. Test Thoroughly

Before submitting:
- Test all commands in the guide
- Verify links work
- Check formatting in markdown preview
- Test on different platforms if possible

### 6. Check the Contributing Guidelines

Every project has its own rules:

```bash
# Check if there's a CONTRIBUTING.md file
cat CONTRIBUTING.md

# Or visit: https://github.com/wagtail/bakerydemo/blob/main/CONTRIBUTING.md
```

Read it before submitting your PR!

### 7. Keep Your Branch Updated

If the main branch changes before your PR is merged:

```bash
# Fetch latest changes from upstream
git fetch upstream

# Rebase your branch on top of upstream/main
git rebase upstream/main

# If there are conflicts, resolve them and push
git push origin docs/local-setup-guide --force-with-lease
```

### 8. Common PR Rejection Reasons (and how to avoid them)

| Reason | Solution |
|--------|----------|
| Doesn't follow project style | Read CONTRIBUTING.md and follow existing patterns |
| Too large/unfocused | Split into smaller, focused PRs |
| Missing tests/documentation | Add relevant tests or docs for code changes |
| Conflicts with other PRs | Rebase and resolve conflicts |
| Outdated information | Test thoroughly and update with latest best practices |
| Poor commit messages | Write clear, descriptive commit messages |
| Doesn't address an issue | Reference related issues or create one first |

---

## Full Example Workflow

Here's a complete example of the entire process:

```bash
# 1. Fork on GitHub (via web browser)

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/bakerydemo.git
cd bakerydemo

# 3. Add upstream
git remote add upstream https://github.com/wagtail/bakerydemo.git

# 4. Create feature branch
git checkout main
git pull upstream main
git checkout -b docs/local-setup-guide

# 5. Add your file
# Copy or create LOCAL_SETUP.md

# 6. Stage changes
git add LOCAL_SETUP.md
git status

# 7. Commit with clear message
git commit -m "Add comprehensive LOCAL_SETUP.md for beginners

- Add VS Code setup for all platforms
- Include troubleshooting guide
- Add quick reference sections"

# 8. Push to your fork
git push origin docs/local-setup-guide

# 9. Create PR via GitHub web interface
# Visit https://github.com/YOUR-USERNAME/bakerydemo
# Click "Compare & pull request"

# 10. Fill out PR form and submit

# 11. If feedback received, make changes
git add LOCAL_SETUP.md
git commit -m "Address review feedback: clarify step X"
git push origin docs/local-setup-guide

# 12. Once merged, clean up
git checkout main
git pull upstream main
git branch -d docs/local-setup-guide
git push origin --delete docs/local-setup-guide
```

---

## Helpful Resources

- **GitHub Docs:** https://docs.github.com/en/pull-requests
- **Git Basics:** https://git-scm.com/docs
- **Markdown Guide:** https://www.markdownguide.org/
- **Wagtail Contributing:** https://docs.wagtail.org/en/stable/contributing/index.html
- **Open Source Guide:** https://opensource.guide/
- **Pro Tip:** Use GitHub Desktop if command line feels intimidating: https://desktop.github.com/

---

## Getting Help

If you get stuck:

1. **Search GitHub Issues** - your question might be answered
2. **Check Wagtail Community** - https://wagtail.io/community/
3. **Ask in PR Comments** - maintainers are usually helpful
4. **Consult GitHub Docs** - very comprehensive

---

**Good luck with your contribution!** 🚀

Every successful open-source project is built by people like you who contribute documentation, code, and ideas. Thank you for helping make Wagtail better!
