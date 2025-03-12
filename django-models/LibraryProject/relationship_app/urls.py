from django.urls import path
from .views import LibraryView ,list_all_books


url_patterns = [
    path("/relationship_app", list_all_books, name='list_all_books'),
    path("/relationship_app", LibraryView, name='LibraryView')


]
