from django.urls import path
from . import views
from django.urls import include
from .views import router

urlpatterns = [
    path("/books",views.BookList.as_view() , name="book_list"),
    path('', include(router.urls))


]