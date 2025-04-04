from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

from social_media_api.accounts.models import User


# Create your models here.

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    target = GenericForeignKey('content_type', 'object_id')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actor')
    timestamp = models.DateTimeField(auto_now_add=True)
    verb = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.recipient} - {self.verb}"

