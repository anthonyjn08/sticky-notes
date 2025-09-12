# Sticky Notes App

A Django-based sticky notes application that allows users to create,
edit, delete, pin, and archive notes. Each user can only view their
own notes. Uses the default Django `User` model and standard Django
authentication with a custom `signup.html`. Styling includes Bootstrap,
FontAwesome, Google Fonts (`Handlee`), and some custom CSS.

---

## Features

- User registration, login, and logout
- Create, edit, and delete notes
- Pin and archive notes
- Notes are private per user
- Responsive design with Bootstrap
- Custom styling with CSS and Google Font Handlee

---

## Prerequisites

- Python 3.13 or higher
- Virtual environment tool (`venv` or `virtualenv`)
- Git (for cloning the repository)

---

## Installation

1. Clone the repository and navigate into it:

- git clone <repository-url>
- cd sticky_notes

2. Create a virtual environment:

- python -m venv .venv

Activate the virtual environment:

- Windows: `<name of virtual environment>\Scripts\activate` or `source <name of virtual environment>/Scripts/activate`
- macOS/Linux: `source <name of virtual environment>/bin/activate`

3. Install dependencies:

- pip install -r requirements.txt

4. Apply migrations:

- python manage.py makemigrations
- python manage.py migrate

5. (Optional) Collect static files:

- python manage.py collectstatic

> Note: `collectstatic` is only required in production or if serving static files via `STATIC_ROOT`.

---

## Running Locally

Start the development server:

- python manage.py runserver

Open your browser at `http://127.0.0.1:8000/`.

---

## Testing

Run tests using:

- python manage.py test

---

## Project Structure

- sticky_notes/
  - sticky_notes `Main app`
    - manage.py
  - notes/
    - migrations/
    - static/css `Custom CSS`
    - templates/notes/ `Notes views html template`
  - templates/
    - registration/ `login, logout, password templates`
    - signup.html
  - users
    - templates # Custom signup template
  - requirements.txt
  - README.md

---

## Notes

- Each user can only view their own notes
- Pin and archive functionality is included
- Custom CSS styles complement Bootstrap and FontAwesome
- Google Font Handlee is used for note styling
- Users can create, edit, and delete notes
- Users can pin and archive posts
