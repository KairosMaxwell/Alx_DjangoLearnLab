from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from .models import Library,Book,Author
from django.contrib.auth.decorators import user_passes_test
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



from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm


class LogoutView(login):
    template_path = "./templates/template/logout.html"

class LoginView(logout):
    template_path = "./templates/template/login.html"
    # return HttpResponse(template_path)

from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        # model = User
        fields = ("username", "email", "password1", "password2")

class register(CreateView):
    template_path = "./templates/template/register.html"
    success_url = reverse_lazy("login")

def role_required(role):
    def decorator(view_func):
        return user_passes_test(lambda u: u.userprofile.role == role)(view_func)
    return decorator

# Admin View
@role_required('Admin')
def admin_view(request):
    template_path="./templates/template/admin_view.html"
    return render(request, template_path)

# Librarian View
@role_required('Librarian')
def librarian_view(request):
    template_path = "./templates/template/login.html"
    return render(request, template_path)

# Member View
@role_required('Member')
def member_view(request):
    template_path = "./templates/template/member_view.html"
    return render(request, template_path)