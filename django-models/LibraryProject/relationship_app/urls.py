from django.urls import path
from .views import LibraryDetailView, list_books


url_patterns = [
    path("/relationship_app", list_books, name='list_all_books'),
    path("/relationship_app", LibraryDetailView, name='LibraryView')


]
