from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

from . import views








urlpattern =[
    path("register/",views.RegisterView.as_view(template_name=""),name="register"),
    path("login/",views.LoginView.as_view(template_name=""),name="login"),
    path("profile/",views.ProfileView,name="profile"),
]