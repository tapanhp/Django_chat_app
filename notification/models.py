from django.db import models
from users.models import User
import datetime


class SentFriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender", null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver", null=True)
    receiver_accepted = models.BooleanField(default=False)
    send_request_at = models.DateTimeField(default=datetime.datetime.now)
    accepted_at = models.DateTimeField(default=None, null=True, blank=True)
    seen_requests = models.BooleanField(default=False)
    seen_notifications = models.BooleanField(default=False)


class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.CharField(max_length=50, null=True)
