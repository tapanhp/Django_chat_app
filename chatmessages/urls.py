from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('messages/', views.chatscreen, name="chatscreen"),
    path('load-more-chat/', views.load_more_chat, name="load-more-chat"),
    path('check-date/', views.check_date, name="check-date"),
    path('seen-message/', views.seen_message, name="seen_message"),
    path('seen-all-message/', views.seen_all_message, name="seen_all_message"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)