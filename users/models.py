from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_pic = models.ImageField(upload_to="public/profile_pic/", null=True, blank=True)
