from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from .models import Library,Book,Author

# Create your views here.

def list_books(author_name):
    books = Book.objects.all()
    context = {"books":books}
    template ="relationship_app/list_books.html/"
    for book in books:
        return f"\nTitle: {book.title}, Author: {book.author.name}\n"
    return HttpResponse(template, context)


class LibraryDetailView(DetailView):
    library = Library
    template_path = "relationship_app/library_detail.html"
    context_object_name = "library"

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context


from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm


class LogoutView(login):
    template_path = "relationship_app/login.html"

class LoginView(logout):
    template_path = "relationship_app/logout.html"
    # return HttpResponse(template_path)

from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        # model = User
        fields = ("username", "email", "password1", "password2")

class RegisterView(CreateView):
    template_path = "relationship_app/register.html"
    success_url = reverse_lazy("login")
