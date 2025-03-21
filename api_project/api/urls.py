from django.urls import path
from . import views
from django.urls import include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .serializers import BookSerializer
from .views import BookViewSet

router = DefaultRouter()

router.register(r'books', BookViewSet,basename='book_all')



urlpatterns = [
    path("books",views.BookList.as_view() , name="book_list"),
    path('', include(router.urls)),
    path("api-token-auth",obtain_auth_token,name="api_token_auth"),


]