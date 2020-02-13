from django.contrib import admin
from .models import SentFriendRequest, Notifications


admin.site.register(SentFriendRequest)
admin.site.register(Notifications)
