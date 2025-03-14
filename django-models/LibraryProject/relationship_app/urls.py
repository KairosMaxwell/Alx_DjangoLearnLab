from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import LogoutView
from .views import LoginView
from . import views
from .views import Admin, Librarian, Member



urlpatterns = [

    path("all_books/", list_books, name='list_all_books'),

    path("libraryView/", LibraryDetailView, name='LibraryView'),

    path('login/', LogoutView.as_view(template_name="")),

    path('register/', views.register, name='register'),

    path('logout/', LoginView.as_view(template_name=""), name='logout'),

    path('admin/', Admin, name='admin_view'),
    path('librarian/', Librarian, name='librarian_view'),
    path('member/', Member, name='member_view'),

]
