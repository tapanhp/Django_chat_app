"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import channels.layers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_app.settings")
channel_layer = channels.layers.get_channel_layer()
