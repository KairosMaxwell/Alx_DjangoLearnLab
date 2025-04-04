"""
Set up views and methods to create notifications whenever relevant actions occur,
such as a user getting a new follower,
someone liking their post, or commenting on their post.
Provide an endpoint for users to fetch their notifications,
showcasing unread notifications prominently.

"""
from rest_framework import viewsets


class NotificationView(viewsets.ModelViewSet):
    pass
