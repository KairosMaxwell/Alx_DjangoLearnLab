from social_media_api.accounts.models import CustomUserModel
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    model = CustomUserModel
    fields ="__all__"

    class Meta:
        query_data = CustomUserModel.objects.all()



