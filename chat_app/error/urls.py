from django.urls import path
from .views import not_found, server_error


urlpatterns = [
    path('notfound/', not_found, name="Notfound"),
    path('servererror/', server_error, name="servererror")
]
