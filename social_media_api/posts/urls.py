from rest_framework import routers
from django.urls import include, path
from social_media_api.posts.views import PostViewSet, CommentViewSet
from . import views
router = routers.DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path("",include(router.urls)),
    path("/posts/<int:pk>/like/",views.LikePostView.as_view() ,name="like"),
    path("/posts/<int:pk>/unlike/",views.UnlikePostView.as_view(),name="unlike"),
    # path('feed/', views.as_view(), name='user-feed'),
]