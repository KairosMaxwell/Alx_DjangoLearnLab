from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

User =get_user_model()



class CustomUserModel(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures", null=True, blank=True)
    following = models.ManyToManyField("self" ,symmetrical=False, related_name="following")


    def follow(self,user):
        self.following.add(user)

    def unfollow(self,user):
        self.following.remove(user)

