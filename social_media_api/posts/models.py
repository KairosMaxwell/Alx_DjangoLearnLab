from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    Post = models.ForeignKey(Post , on_delete=models.CASCADE)
    content = models
    User = models.ForeignKey(User , on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)



class LikeModel(models.Model):

    post = models.ForeignKey(Post , on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name='user')

    class Meta:
        unique_together =('post','user')  # Prevent users from liking multiple times



