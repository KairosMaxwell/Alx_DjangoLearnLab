from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import LogoutView
from .views import LoginView
from . import views



url_patterns = [

    path("/relationship_app", list_books, name='list_all_books'),

    path("/relationship_app", LibraryDetailView, name='LibraryView'),

    path('login/', LogoutView.as_view(template_name=""), name='login'),

    path('register/', views.register, name='register'),

    path('logout/', LoginView.as_view(template_name=""), name='logout'),


]
