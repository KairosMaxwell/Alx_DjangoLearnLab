from django.shortcuts import render
from rest_framework import serializers
from .models import CustomUserModel
from django.views.generic.base import TemplateView
# Create your views here.
# loginView, ProfileView, registerView


class LoginView(TemplateView):
    renderer_classes = TemplateView


class RegisterView(TemplateView):
    pass

class ProfileView(TemplateView):
    pass




class CustomUserSerializer(serializers.ModelSerializer):
    model = CustomUserModel
    fields ="__all__"

    class Meta:
        query_data = CustomUserModel.objects.all()




