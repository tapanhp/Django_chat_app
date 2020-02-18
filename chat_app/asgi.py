"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import get_default_application
from chat_app.settings import SECRET_KEY

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_app.settings")
django.setup()
application = get_default_application()

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
        "symmetric_encryption_keys": [SECRET_KEY],
    },
}
ASGI_APPLICATION = 'chat_app.routing.application'
