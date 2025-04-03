from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from social_media_api.accounts.models import CustomUserModel


class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,user_id):
        who_to_follow = CustomUserModel.objects.get(id=user_id)
        request.user.follow(who_to_follow)
        return Response(f"You are following {who_to_follow.username} ")




class UnFollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,user_id):
        who_to_unfollow = CustomUserModel.objects.get(id=user_id)
        request.user.unfollow(who_to_unfollow)
        return Response(f"message: You are unfollowed {who_to_unfollow.username} ")







