from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    # path("", name="")
    path("login/",LoginView.as_view(template_name="./login.html"),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("register/" ,"",name="register"),
    path("profile/" ,"",name="profile"),

]



