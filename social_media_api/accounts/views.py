from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,permissions
from rest_framework.response import Response
from social_media_api.accounts.models import CustomUser
from social_media_api.posts.models import Post
from social_media_api.posts.serializers import PostSerializer


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,user_id):
        who_to_follow = CustomUser.objects.all()
        request.user.follow(who_to_follow)
        return Response(f"You are following {who_to_follow} ")




class UnFollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,user_id):
        who_to_unfollow = CustomUser.objects.all()
        request.user.unfollow(who_to_unfollow)
        return Response(f"message: You are unfollowed {who_to_unfollow} ")











