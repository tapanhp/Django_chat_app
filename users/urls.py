from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from chatmessages.views import chat_app
from . import views
from .views import EmailValidationOnForgotPassword
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registration/', views.registration, name="registration"),
    path('registartion/otpverify', views.otp_verification, name="otpverify"),
    path('login/', views.login, name="login"),
    path('home/', chat_app, name="home"),
    path('profile/', views.profile, name="profile"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('user_profile/<str:username>', views.user_profile, name="user_profile"),
    path('home/logout/', views.logout, name="logout"),
    url('^', include('django.contrib.auth.urls')),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword), name='password_reset'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
