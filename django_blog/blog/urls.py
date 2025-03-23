from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django_blog.blog.views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView
from .views import CommentCreateView,CommentDeleteView,CommentUpdateView
# from views import *
urlpatterns = [
    # path("", name="")
    path("login/",LoginView.as_view(template_name="./login.html"),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("register/" ,"",name="register"),
    path("profile/" ,"",name="profile"),

    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view()),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:post_id>/comments/new/', views.add_comment, name='add-comment'),
    path("",CommentCreateView.as_view(), name='comment-list'),
    path("",CommentUpdateView.as_view(), name='comment-update'),
    path("",CommentDeleteView.as_view(), name='comment-delete'),

    """
    "CommentCreateView", "CommentUpdateView", "CommentDeleteView"
    """

]



