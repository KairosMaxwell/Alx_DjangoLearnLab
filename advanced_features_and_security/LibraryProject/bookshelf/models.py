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


# class CustomManger(BaseUserManager):
#     create_user =
#     create_superuser =
#
#     class Meta:
#         permissions = [
#             ("create_user", "create_superuser")
#         ]


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


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Specify the fields to display in the admin interface
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')
    # Define fields for filtering in the admin sidebar
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    # Allow searching for users by specific fields
    search_fields = ('email', 'first_name', 'last_name')
    # Read-only fields for display purposes
    readonly_fields = ('last_login', 'date_joined')
    # Specify fieldsets for creating and editing users
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Information', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Fields for creating new users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    # Specify ordering of displayed records
    # ordering = ('email',)
