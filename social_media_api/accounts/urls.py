from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.urls import include

from . import views


urlpattern =[

    # path("register/",views.RegisterView.as_view(template_name=""),name="register"),
    # path("login/",views.LoginView.as_view(template_name=""),name="login"),
    # path("profile/",views.ProfileView,name="profile"),
    path("follow/<int:user_id>",views.FollowUserView.as_view(),name='follow'),
    path('unfollow/<int:user_id>/', views.UnFollowUserView.as_view(), name='unfollow-user')
]