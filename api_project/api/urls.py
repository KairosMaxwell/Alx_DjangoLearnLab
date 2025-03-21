from django.urls import path
from . import views
from django.urls import include

from rest_framework.routers import DefaultRouter

from .serializers import BookSerializer
from .views import BookViewSet

router = DefaultRouter()

router.register(r'books', BookViewSet,basename='book_all')



urlpatterns = [
    path("/books",views.BookList.as_view() , name="book_list"),
    path('', include(router.urls))


]