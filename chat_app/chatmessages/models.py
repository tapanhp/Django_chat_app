from django.db import models
from group.models import Group
from users.models import User
from datetime import datetime


class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="msg_sender", null=True, blank=True)
    receiver = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="receiver_user")
    receiver_group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE, related_name="receiver_group")
    message = models.TextField()
    message_seen = models.BooleanField(default=False)
    sent_at = models.DateTimeField(default=datetime.now)


class ChatList(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_sender", null=True)
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_user", null=True)
    receiver_group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="received_group", null=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

