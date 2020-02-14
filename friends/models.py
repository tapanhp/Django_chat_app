from django.db import models
from users.models import User


class Friends(models.Model):
    user1 = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user2")
    room_name = models.CharField(max_length=50)
    friends = models.BooleanField(default=True)


class BlockFriends(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user")
    blocked_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="Blocked_user")
    blocked_at = models.DateTimeField(auto_now_add=True)
