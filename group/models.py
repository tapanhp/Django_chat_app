from django.db import models
from users.models import User


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="admin")
    room_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class GroupMembers(models.Model):
    member_user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
