from django.urls import path
from .views import add_contact, invite_contact, friend_request, add_friend, accept_request, decline_request, notification_seen


urlpatterns = [
    path('addcontact/', add_contact, name="addcontact"),
    path('friendrequest/', friend_request, name="friend_request"),
    path('invite_contact/', invite_contact, name="invite_contact"),
    path('addfriend/', add_friend, name="addfriend"),
    path('accept-request/', accept_request, name="accept-request"),
    path('decline-request/', decline_request, name="decline-request"),
    path('notification_seen/', notification_seen, name="notification"),
]
