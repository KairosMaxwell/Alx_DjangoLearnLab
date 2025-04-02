from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
bio, profile_picture, and followers
"""

class CustomUserModel(AbstractUser):
    bio = models.ManyToManyField(User ,symmetrical=False)
    profile_picture = models.ImageField(upload_to="profile_pictures", null=True, blank=True)
    followers = models.ManyToManyField(User ,symmetrical=False)
