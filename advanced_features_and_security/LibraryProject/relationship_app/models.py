from django.contrib.auth.backends import BaseBackend
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.






class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author= models.ForeignKey(Author, on_delete=models.CASCADE , name="Author")

    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE , name="Librarian")
    def __str__(self):
        return self.name




ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]
class UserProfile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE),
    role = models.CharField(choices=ROLE_CHOICES, max_length=100)

    def __str__(self):
        return f"{self.user} - {self.role}"

    @receiver(post_save, sender=User)
    def create_user_profile(self ,sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(self,sender, instance, **kwargs):
        instance.profile.save()




class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo =models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    def __str__(self):
        return self.username

class EmailBackend(BaseBackend):
    def authenticate(self,request, username =None, password=None):

        pass

#      Implement logic here
    def get_user(self, user_id):
        pass
        # Implement logic to retrieve user based on user TD

from django.contrib.auth.models import Permission

permission =Permission.objects.get(codename="add_book")

class Post(models.Model):
    pass

    class Meta:
        permissions = [
            ('can_add_post', 'Can add post'),
        ]





