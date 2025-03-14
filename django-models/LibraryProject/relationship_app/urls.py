from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import LogoutView
from .views import LoginView
from . import views
from .views import admin_view, librarian_view, member_view



urlpatterns = [

    path("all_books/", list_books, name='list_all_books'),

    path("libraryView/", LibraryDetailView, name='LibraryView'),

    path('login/', LogoutView.as_view(template_name="")),

    path('register/', views.register, name='register'),

    path('logout/', LoginView.as_view(template_name=""), name='logout'),

    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

]
