# 📋 Listify

A clean, elegant list management web application built with **Django**. Listify lets users organise their notes and tasks into folders and lists — with support for bullet point, numbered, and checkbox list types — all wrapped in a light fuchsia, gold, and grey theme.

---

## ✨ Features

- **Authentication** — Session-based sign up, log in, and log out with confirmation prompt
- **Folders** — Create and manage folders to group your lists
- **Lists** — Three list types: Bullet Point, Numbered, and Checkbox
- **List Items** — Add, edit, delete, and check off items without leaving the page
- **PDF Export** — Export any list as a formatted PDF file
- **Profile Page** — View your account details and activity stats
- **No extra pages** — All create/edit actions use in-page modals; no unnecessary navigation

---

## 🖥️ Pages

| Page | URL | Description |
|---|---|---|
| Login | `/login/` | Sign in with username and password |
| Sign Up | `/signup/` | Create a new account |
| Home | `/home/` | Dashboard with folder preview and stats |
| Folders | `/folders/` | View and create folders |
| Lists | `/folders/<id>/lists/` | View lists inside a folder; edit folder details |
| List Detail | `/lists/<id>/` | Manage list items; export to PDF |
| Profile | `/profile/` | View account details (read-only) |

---

## 🗄️ Data Models

```
User
├── username       (PK, auto-generated, e.g. "john1")
├── email
├── password
├── created_at
└── updated_on

Folder  →  belongs to User
├── folderid      (PK, auto-generated, e.g. "john1-f1")
├── folder_name
├── folder_description
├── created_at
└── updated_at

List  →  belongs to Folder
├── listid        (PK, auto-generated, e.g. "john1-f1-1")
├── list_title
├── list_description
├── list_type     (Bulletpoint | Numbered | Checkbox)
├── created_at
└── updated_at

ListMembers  →  belongs to List
├── content
├── status        (Nocheck | Checked)
├── created_at
└── updated_at
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Laura003-t/my-list.git
cd my-list
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install django reportlab
```

**4. Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Run the development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 📁 Project Structure

```
my-list/
├── listCreator/
│   ├── templates/
│   │   ├── base.html          # Shared layout, nav, styles, toast & logout modal
│   │   ├── login.html         # Login page
│   │   ├── register.html      # Sign up page
│   │   ├── home.html          # Dashboard / home page
│   │   ├── myfolders.html       # Folders listing page
│   │   ├── lists.html         # Lists inside a folder
│   │   ├── listdetails.html   # List item management page
│   │   └── profile.html       # User profile page
│   ├── models.py              # User, Folder, List, ListMembers
│   ├── views.py               # All view logic
│   └── urls.py                # URL routing
├── manage.py
└── README.md
```

---

## ⚙️ URL Reference

```
GET/POST  /login/                              Login
GET/POST  /sign-up/                             Sign up
GET       /logout/                             Log out
GET       /home/                               Dashboard
GET       /folders/                            All folders
POST      /folders/create/                     Create folder
POST      /folders/<folderid>/update/          Update folder details
GET       /folders/<folderid>/lists/           Lists in a folder
POST      /folders/<folderid>/lists/create/    Create a list
GET       /lists/<listid>/                     List detail
POST      /lists/<listid>/add-item/            Add list item
GET       /lists/<listid>/export-pdf/          Export list as PDF
POST      /lists/item/<pk>/toggle-item/             Toggle checkbox (AJAX)
POST      /lists/item/<pk>/edit/               Edit item content (AJAX)
POST      /lists/item/<pk>/delete/             Delete item (AJAX)
GET       /profile/                            User profile
```

---

## 🎨 Design

| Token | Value |
|---|---|
| Primary | Fuchsia `#c0256b` |
| Accent | Golden cream `#c9a84c` |
| Neutral | Grey scale (`#1c1c1e` → `#fafafa`) |
| Display font | Playfair Display |
| Body font | DM Sans |
| Theme | Light |

All styles live in `base.html` using CSS custom properties, making it straightforward to theme or extend.

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `django` | Web framework |
| `reportlab` | PDF generation for list export |

---

