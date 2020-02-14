from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(name="phone", max_length=10, null=True)
    photo = models.ImageField(name="photo", upload_to='photos/', null=True, default='user_default.png')
    is_verified = models.BooleanField(default=False)
    unique_together = ("id", "phone",)

    def __str__(self):
        return self.username


class LoginLogoutDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logged_in_at = models.DateTimeField()
    logged_out_at = models.DateTimeField()

    def __str__(self):
        return self.user
