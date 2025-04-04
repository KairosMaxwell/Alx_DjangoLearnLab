from django.shortcuts import render
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
# Create your views here.
from .models import Post,Comment
from serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework import permissions,viewsets,filters
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user




class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by("-created_at")
    permission_class = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)


from rest_framework import generics

class PostFeed(generics.GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # Get the users this user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

from .models import LikeModel
from social_media_api.notifications.models import Notification

class LikePostView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes =[permissions.IsAuthenticatedOrReadOnly ]

    def liking(self,request,post_id):
        post = Post.objects.get(id=post_id)
        liked, created = LikeModel.objects.get_or_create(user = request.user , post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            Response(f"You are now liked {post}")

            return Response({'message': 'Post liked'})
        return Response({'message': 'You already liked this post'})

class UnlikePostView(viewsets.ModelViewSet):
    permission_classes =[permissions.IsAuthenticatedOrReadOnly]

    def unliking(self,request,post_id):
        post = generics.get_object_or_404(Post, pk=post_id)
        try:
            liked_post = LikeModel.objects.get(user=request.user, post=post)
            liked_post.delete()
            # if liked_post.delete():
            #     Notification.objects.create(
            #         recipient=post.author,
            #         actor=request.user,
            #         verb="Unliked your post",
            #         target=post
            #     )
            Response(f"You are now unliked {post}")
        except LikeModel.DoesNotExist:
            Response(f"You are not liked this {post}")






