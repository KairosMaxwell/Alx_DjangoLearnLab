from social_media_api.accounts.models import CustomUserModel
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
"""
accounts/serializers.py doesn't contain: 
["from rest_framework.authtoken.models import Token", 
"serializers.CharField()",
 "Token.objects.create", "get_user_model().objects.create_user"]

"""

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields =["id","username","password","email","profile_picture"]

    def createUser(self):
        user =User.objects.create(**self.validated_data)
        Token.objects.create(user=user)
        return user



