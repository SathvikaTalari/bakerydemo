# Password Reset Link Fix - Visual Guide

## Problem & Solution Visualization

### THE PROBLEM

```
Settings Configuration:
┌─────────────────────────────────────────────────────────┐
│ WAGTAILUSERS_PASSWORD_RESET_ENABLED = False             │
└─────────────────────────────────────────────────────────┘
                            ↓
              "Password reset is disabled"
                            ↓
          But the login link STILL appears!
                            ↓
┌─────────────────────────────────────────────────────────┐
│  Sign in to Wagtail                                     │
│  ┌─────────────────────────────────────────────────┐   │
│  │ Username: [_____________________]               │   │
│  │ Password: [_____________________]               │   │
│  │ [Sign in]                                       │   │
│  │ Forgotten password?  ← STILL APPEARS (BUG)     │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## THE SOLUTION

```
Architecture Diagram:

    USER VISITS /admin/
            ↓
    ┌───────────────────────────────┐
    │ Django Admin Login View       │
    │ (Wagtail's login handler)    │
    └───────────────────────────────┘
            ↓
    ┌───────────────────────────────────────────────────┐
    │ Settings Check:                                  │
    │ WAGTAILADMIN_USER_LOGIN_FORM = ?               │
    │                                                  │
    │ ✓ Found: CustomAuthenticationForm              │
    └───────────────────────────────────────────────────┘
            ↓
    ┌─────────────────────────────────────────────────┐
    │ CustomAuthenticationForm.__init__()             │
    │                                                  │
    │ 1. Call parent __init__()                      │
    │ 2. Read setting:                               │
    │    WAGTAILUSERS_PASSWORD_RESET_ENABLED?        │
    │ 3. Store in form:                              │
    │    self.password_reset_enabled = True/False    │
    └─────────────────────────────────────────────────┘
            ↓
    ┌─────────────────────────────────────────────────┐
    │ Render Template:                                │
    │ wagtailadmin/login.html                        │
    └─────────────────────────────────────────────────┘
            ↓
    ┌─────────────────────────────────────────────────┐
    │ Template Logic:                                 │
    │                                                  │
    │ {% if form.password_reset_enabled %}           │
    │     Show "Forgotten password?" link            │
    │ {% endif %}                                    │
    │                                                  │
    │ ✓ Form has the setting value                  │
    │ ✓ Can make decision in template               │
    └─────────────────────────────────────────────────┘
            ↓
    ┌─────────────────────────────────────────────────┐
    │ Browser sees:                                   │
    │                                                  │
    │ Sign in to Wagtail                             │
    │ Username: [_____________________]              │
    │ Password: [_____________________]              │
    │ [Sign in]                                      │
    │ ← NO "Forgotten password?" link ✓             │
    └─────────────────────────────────────────────────┘
```

---

## File Relationships

```
┌─────────────────────────────────────────────────────────────────┐
│                    DJANGO WAGTAIL ADMIN                         │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                              ↓
        ┌─────────────────────┴──────────────────────┐
        ↓                                             ↓
┌────────────────────┐                   ┌──────────────────────┐
│ settings/base.py   │                   │ WAGTAIL CORE         │
├────────────────────┤                   ├──────────────────────┤
│ Line 224:          │                   │ Default LoginForm    │
│ WAGTAILADMIN_USER_ │                   │ (not respecting our  │
│ LOGIN_FORM =       │──────points to────│  setting)           │
│ "bakerydemo.base.  │                   └──────────────────────┘
│  forms.            │
│ CustomAuth..."     │
└────────────────────┘
        ↓
        ↓
┌─────────────────────────────────────────────────────────────────┐
│               bakerydemo/base/forms.py (NEW)                    │
├─────────────────────────────────────────────────────────────────┤
│ class CustomAuthenticationForm(WagtailAuthenticationForm):      │
│     def __init__(self, ...):                                    │
│         super().__init__(...)                                   │
│         self.password_reset_enabled = getattr(settings, ...)   │
│                           ↓                                      │
│                    Reads setting from                           │
│                    settings/base.py                            │
│                           ↓                                      │
│         Stores in form object, accessible in templates         │
└─────────────────────────────────────────────────────────────────┘
        ↓
        ↓ Used by Django to render
        ↓
┌─────────────────────────────────────────────────────────────────┐
│          bakerydemo/templates/wagtailadmin/login.html (NEW)     │
├─────────────────────────────────────────────────────────────────┤
│ {% if form.password_reset_enabled %}                           │
│     <a href="{% url 'wagtailadmin_password_reset' %}">         │
│         Forgotten password?                                    │
│     </a>                                                        │
│ {% endif %}                                                    │
│                           ↓                                      │
│         Reads form.password_reset_enabled                      │
│         Only renders link if True                             │
└─────────────────────────────────────────────────────────────────┘
        ↓
        ↓ Browser renders
        ↓
  LOGIN PAGE (with or without link based on setting)
```

---

## Code Flow Sequence

```
Timeline of Execution:

1. User navigates to /admin/
   └─ REQUEST: GET /admin/

2. Django routes to Wagtail's admin login view
   └─ Wagtail admin view detects unauthenticated user

3. Checks WAGTAILADMIN_USER_LOGIN_FORM setting
   └─ READS: "bakerydemo.base.forms.CustomAuthenticationForm"

4. Instantiates the form class
   └─ CALLS: CustomAuthenticationForm()

5. Form's __init__ method runs
   ├─ Calls super().__init__(...) [parent Wagtail form]
   │  └─ Parent initializes form fields (username, password)
   │
   └─ Reads WAGTAILUSERS_PASSWORD_RESET_ENABLED from settings
      └─ Gets value: False
      └─ Sets self.password_reset_enabled = False

6. Form instance passed to template context
   └─ Template has access to: form.password_reset_enabled

7. Django renders wagtailadmin/login.html
   ├─ Renders form fields (username, password, button)
   │
   └─ Checks: {% if form.password_reset_enabled %}
      ├─ Condition is False
      └─ SKIPS rendering "Forgotten password?" link

8. HTML sent to browser
   └─ User sees login form WITHOUT password reset link

9. Browser displays the page
   └─ "Forgotten password?" link is absent ✓
```

---

## Before & After Comparison

### BEFORE (With Bug)

```
File Structure:
bakerydemo/
├── settings/
│   ├── base.py              ← No custom form setting
│   └── ...
├── base/
│   ├── forms.py            ✗ DOESN'T EXIST
│   └── ...
└── templates/
    └── ...                  ✗ No custom login.html
```

```
Settings Check:
WAGTAILADMIN_USER_LOGIN_FORM = "wagtail.users.forms.AuthenticationForm"
                                 (Default Wagtail form)
                                        ↓
                              Form doesn't check
                              WAGTAILUSERS_PASSWORD_RESET_ENABLED
                                        ↓
                              Login template always shows
                              "Forgotten password?" link
```

---

### AFTER (Fixed)

```
File Structure:
bakerydemo/
├── settings/
│   ├── base.py              ✓ Updated with custom form setting
│   └── ...
├── base/
│   ├── forms.py            ✓ NEW - Custom form
│   └── ...
└── templates/
    └── wagtailadmin/
        └── login.html       ✓ NEW - Custom template
```

```
Settings Check:
WAGTAILADMIN_USER_LOGIN_FORM = "bakerydemo.base.forms.CustomAuthenticationForm"
                                        ↓
                              CustomAuthenticationForm.__init__:
                              1. Reads WAGTAILUSERS_PASSWORD_RESET_ENABLED
                              2. Stores in self.password_reset_enabled
                                        ↓
                              Template accesses form.password_reset_enabled
                                        ↓
                              {% if form.password_reset_enabled %}
                              - True: Show link
                              - False: Don't show link
```

---

## Decision Tree in Template

```
                    PAGE RENDERING
                          ↓
                  ┌───────────────┐
                  │ Render Form   │
                  │ Fields        │
                  │ (username,    │
                  │  password,    │
                  │  button)      │
                  └───────────────┘
                          ↓
            ┌─────────────────────────┐
            │ Check form setting      │
            │ form.password_reset_    │
            │ enabled = ?             │
            └─────────────────────────┘
                   ↙           ↖
              True           False
                ↙               ↖
        ┌──────────────┐    ┌──────────────┐
        │ RENDER:      │    │ SKIP:        │
        │ "Forgotten   │    │ "Forgotten   │
        │  password?"  │    │  password?"  │
        │ link         │    │ link         │
        └──────────────┘    └──────────────┘
                ↙               ↖
            USER SEES       USER SEES
            Link            No Link
            ✗              ✓
```

---

## Impact Diagram

```
Original System:
┌─────────────────────────────────────────┐
│ WAGTAILUSERS_PASSWORD_RESET_ENABLED=F   │
└─────────────────────────────────────────┘
    ↓ Affects these components:
    ├─ User creation forms        ✓ Respects setting
    ├─ User profile pages         ✓ Respects setting
    └─ Login page link            ✗ IGNORES setting ← BUG
       
New System with Fix:
┌─────────────────────────────────────────┐
│ WAGTAILUSERS_PASSWORD_RESET_ENABLED=F   │
└─────────────────────────────────────────┘
    ↓ Affects these components:
    ├─ User creation forms        ✓ Respects setting
    ├─ User profile pages         ✓ Respects setting
    └─ Login page link            ✓ NOW RESPECTS ← FIXED
```

---

## Summary Table

| Aspect | Before | After |
|--------|--------|-------|
| **Forgotten password? Link** | Always shows | Respects setting |
| **Custom Form** | Not used | Used |
| **Login Template** | Default Wagtail | Custom bakerydemo |
| **Files Changed** | 0 | 3 |
| **Lines Added** | 0 | 53 |
| **Breaking Changes** | N/A | 0 |
| **User Experience** | Confusing | Consistent |
| **Settings Respected** | Partial | Complete ✓ |

---

## How to Verify the Fix is Working

```bash
# 1. Check files exist
ls bakerydemo/base/forms.py                          # Should exist ✓
ls bakerydemo/templates/wagtailadmin/login.html     # Should exist ✓

# 2. Check settings updated
grep "WAGTAILADMIN_USER_LOGIN_FORM" bakerydemo/settings/base.py  # Should find it ✓

# 3. Run the server
python manage.py runserver

# 4. Visit login page
# Open: http://localhost:8000/admin/

# 5. Visual check
# If WAGTAILUSERS_PASSWORD_RESET_ENABLED = False
# → "Forgotten password?" link should NOT appear ✓

# If WAGTAILUSERS_PASSWORD_RESET_ENABLED = True
# → "Forgotten password?" link SHOULD appear ✓
```

---

## Deployment Checklist

- [ ] Files created: `bakerydemo/base/forms.py`
- [ ] Files created: `bakerydemo/templates/wagtailadmin/login.html`
- [ ] Settings updated: `bakerydemo/settings/base.py`
- [ ] Settings configured: `WAGTAILADMIN_USER_LOGIN_FORM` set
- [ ] Settings check: `WAGTAILUSERS_PASSWORD_RESET_ENABLED` value
- [ ] Test in browser: Link hidden when setting is False
- [ ] Test in browser: Link visible when setting is True
- [ ] No migrations needed
- [ ] No cache clear needed
- [ ] Ready to commit and push

---

**Visual Guide Complete** ✓

For technical details, see: `ISSUE_FIX_PASSWORD_RESET.md`  
For implementation details, see: `CHANGES_SUMMARY.md`
