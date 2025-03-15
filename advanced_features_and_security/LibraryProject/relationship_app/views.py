from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from .models import Library,Book,Author
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

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
    template_path = "templates/relationship_app/logout.html"

class LoginView(logout):
    template_path = "templates/relationship_app/login.html"
    # return HttpResponse(template_path)

from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        # model = User
        fields = ("username", "email", "password1", "password2")

class register(CreateView):
    template_path = "templates/relationship_app/register.html"
    success_url = reverse_lazy("login")

def role_required(role):
    def decorator(view_func):
        return user_passes_test(lambda u: u.userprofile.role == role)(view_func)
    return decorator

# Admin View
@role_required('Admin')
def Admin(request):
    template_path= "templates/relationship_app/admin_view.html"
    return render(request, template_path)

# Librarian View
@role_required('Librarian')
def Librarian(request):
    template_path = "templates/relationship_app/login.html"
    return render(request, template_path)

# Member View
@role_required('Member')
def Member(request):
    template_path = "templates/relationship_app/member_view.html"
    return render(request, template_path)



@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to a book listing page
    else:
        form = BookForm()
    return render(request, './add_book.html', {'form': form})

# View to edit an existing book
class BookForm:
    pass


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to a book listing page
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to a book listing page
    return render(request, 'delete_book.html', {'book': book})



def my_view(request):
    if request.user.has_perm('relationship_app.add_book'):
        pass
    else:
        pass