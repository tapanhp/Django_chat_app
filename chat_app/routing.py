# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chatmessages.routing
from chatmessages.consumers import ChatConsumer

# middlewarestack which set url for socket connection

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chatmessages.routing.websocket_urlpatterns
        )
    ),
})

ASGI_APPLICATION = "chat_app.routing.application"
