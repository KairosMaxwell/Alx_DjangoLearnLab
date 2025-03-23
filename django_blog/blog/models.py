from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, name="author")
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    pass



"""
In your blog app, create a Comment model with the following fields:
post: a ForeignKey linking to the Post model, establishing a many-to-one relationship.
author: a ForeignKey to Django’s User model, indicating the user who wrote the comment.
content: a TextField for the comment’s text.
created_at: a DateTimeField that records the time the comment was made.
updated_at: a DateTimeField that records the last time the comment was updated.

"""

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)