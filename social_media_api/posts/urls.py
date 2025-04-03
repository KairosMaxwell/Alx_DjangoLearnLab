from rest_framework import routers
from django.urls import include, path
from social_media_api.posts.views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path("",include(router.urls)),
path('feed/', views..as_view(), name='user-feed'),
]