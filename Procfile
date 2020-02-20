release: python manage.py migrate
web: gunicorn chat_app.wsgi:application
web: daphne -p 8001 chat_app.asgi:application
