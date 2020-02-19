release: python manage.py migrate
web: daphne chat_app.asgi:application --port $PORT --bind 0.0.0.0
worker: python manage.py runworker -v2
