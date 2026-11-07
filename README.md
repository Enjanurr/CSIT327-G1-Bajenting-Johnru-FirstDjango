# CampusConnect — CSIT327 Lab Challenge

- **Student Name:** Johnru I. Bajenting
- **Section:** G1
- **Course:** CSIT327

---

## Overview

**CampusConnect** is a Django web portal with role-based user accounts, a dashboard, profile viewing and self-service profile editing (`UpdateView`), a sign-up success notification via Django's `messages` framework, and a responsive UI styled with **Bootstrap 5 (via CDN)**.

### Key Features

1. **Profile Page (`ProfileView` & `ProfileUpdateView`)**
   - Logged-in users can view (`/accounts/profile/`) and edit (`/accounts/profile/edit/`) their own profile using Django's class-based `UpdateView`.
   - Protected by `LoginRequiredMixin`. `get_object()` returns `self.request.user`, and the edit URL has no user id, so no user can open or edit another user's profile.
   - The `role` field is not in the edit form, so users cannot promote themselves to admin.

2. **Sign-Up Feedback (`SuccessMessageMixin` + Django Messages Framework)**
   - After a successful registration, the user is redirected to the login page and sees a dismissible Bootstrap alert (`alert alert-success`).
   - Profile updates show the same kind of alert.

3. **Bootstrap 5 Polish (`base.html` & Styled Forms)**
   - A shared `templates/base.html` loads Bootstrap 5 CSS and the JS bundle from the jsDelivr CDN (no Bootstrap files are downloaded into the project) and provides a responsive navigation bar and the messages alert block.
   - Every page extends `base.html`: `login.html`, `signup.html`, `profile.html`, `profile_edit.html`, `home.html`, `admin_panel.html`.
   - All forms (`StyledAuthenticationForm`, `CustomUserCreationForm`, `UserProfileUpdateForm`) use Bootstrap's `form-control` and `btn` classes.

4. **Role-Based Access**
   - Custom user model (`CustomUser`) with a `role` (Student, Instructor, Administrator) and `course`.
   - The dashboard requires login. The Admin Panel is restricted to users with the Administrator role (`UserPassesTestMixin`).

5. **Security**
   - CSRF protection (`{% csrf_token %}`) on every form, including logout.
   - Django's password validators on sign-up.
   - Duplicate email check on profile edit.

---

## Project Structure

```
CSIT327-Gx-Lastname-Firstname-FirstDjango/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── campusconnect/        # project settings and root urls
├── accounts/             # CustomUser, sign-up, profile views, forms
├── dashboard/            # dashboard home and admin panel
├── templates/
│   ├── base.html
│   ├── registration/     # login.html, signup.html
│   ├── accounts/         # profile.html, profile_edit.html
│   └── dashboard/        # home.html, admin_panel.html
└── static/css/style.css
```

---

## Steps to Run the Project

### 1. Clone the Repository
```bash
git clone <repository-url>
cd CSIT327-Gx-Lastname-Firstname-FirstDjango
```

### 2. Create and Activate a Virtual Environment
**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
The SQLite database is not committed, so this step creates it.
```bash
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```
Open your browser and visit: **http://127.0.0.1:8000/**

---

## Testing the App

1. Click **Sign Up**, register an account, and confirm the green success alert appears on the login page.
2. Log in and open **Profile**, then **Edit Profile**, change a field, save, and confirm the update alert.
3. Log out and try opening `/accounts/profile/` directly. You should be redirected to the login page.
4. To try the **Admin Panel**: log in at `/admin/` with your superuser, open your user, set **Role** to *Administrator* under *School Profile*, save, then visit the dashboard and click **Admin Panel**.

---

## Tech Stack

- Python, Django
- SQLite (development database)
- Bootstrap 5 and Bootstrap Icons (CDN)
