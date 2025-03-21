from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, name="author")
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)



