from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import login



url_patterns = [
    path("/relationship_app", list_books, name='list_all_books'),
    path("/relationship_app", LibraryDetailView, name='LibraryView'),
    path("/login",login,name='login'),
    path("/logout",login,name='logout'),
    path("/register",login,name='register')

]
