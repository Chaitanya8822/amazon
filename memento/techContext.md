# Tech Context

## Technologies Used

| Layer       | Technology                          |
|-------------|-------------------------------------|
| Language    | Python 3.10+                        |
| Framework   | Django 4.2 LTS                      |
| Frontend    | HTML5, CSS3, Bootstrap 5.3          |
| Database    | SQLite (dev) / PostgreSQL (prod)    |
| Auth        | Django built-in + custom UserProfile|
| Static      | Django staticfiles + WhiteNoise     |
| Images      | Pillow (for ImageField)             |
| IDE         | VS Code                             |
| VCS         | Git & GitHub                        |

## Key Dependencies (requirements.txt)
```
Django==4.2.13
Pillow==10.3.0
whitenoise==6.7.0
crispy-forms==2.1
django-crispy-bootstrap5==2024.2
```

## Development Setup
```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Django Settings Highlights
- `SECRET_KEY` loaded from env var in production
- `DEBUG = True` in development
- `MEDIA_ROOT` / `MEDIA_URL` set for product images
- `LOGIN_URL = '/accounts/login/'`
- `LOGIN_REDIRECT_URL = '/'`
- `CRISPY_TEMPLATE_PACK = 'bootstrap5'`
- Custom context processor: `cart.context_processors.cart`

## Project Module Name
`amazon_project` (settings module, avoids collision with workspace dir name `amazon`)