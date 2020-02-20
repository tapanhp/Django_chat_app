release: python manage.py migrate
web: gunicorn chat_app.wsgi:application
worker: daphne -p 8001 chat_app.asgi:application
