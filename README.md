# Django Spotify Clone

This is a Django-based music streaming application inspired by Spotify. It allows users to browse, search, and play music.

## Features
- User authentication (signup/login/logout)
- Upload and manage songs
- Create and manage playlists
- Search functionality for songs and artists
- Audio streaming

## Installation

### Prerequisites
- Python 3.x
- Django 4.x
- PostgreSQL (or SQLite for development)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/django-spotify-clone.git
   cd django-spotify-clone
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`


## Technologies Used
- Django
- Django Rest Framework (DRF) (if API support is needed)
- PostgreSQL/SQLite
- HTML, CSS, JavaScript (Frontend)

## Contribution
Feel free to contribute by opening an issue or submitting a pull request.
