from django.shortcuts import render
from .models import Book
# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('bookshelf.can_view', raise_exception=True)
def view_instance(request, pk):
    # Logic for viewing an instance
    return render(request, 'view_instance.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_instance(request, pk):
    # Logic for editing an instance
    return render(request, 'edit_instance.html')


def book_list(request):
    """View to display a list of all books."""
    books = Book.objects.all()  # Query all book instances from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})