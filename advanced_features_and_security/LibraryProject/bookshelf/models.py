from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title




# class CustomUser(AbstractUser):
#     date_of_birth = models.DateField(null=True, blank=True)
#     profile_photo = models.ImageField(null=True, blank=True)
#
#     def __str__(self):
#         return self.username




class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None  # Remove the username field
    USERNAME_FIELD = "email"  # Use email as the unique identifier
    REQUIRED_FIELDS = []  # No additional fields required

    objects = CustomUserManager()

class CustomModel(models.Model):
    # Example fields in your model
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        permissions = [
            ("can_view", "Can view instances of MyModel"),
            ("can_create", "Can create instances of MyModel"),
            ("can_edit", "Can edit instances of MyModel"),
            ("can_delete", "Can delete instances of MyModel"),
        ]

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import UpdateView


class EditInstanceView(PermissionRequiredMixin, UpdateView):
    model = CustomModel
    fields = ['name', 'description']
    template_name = 'edit_instance.html'
    permission_required = 'app_name.can_edit'
