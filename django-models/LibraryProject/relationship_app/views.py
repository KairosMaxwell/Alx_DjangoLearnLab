from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Book,Author,Library

# Create your views here.

def list_all_books(author_name):
    books = Book.objects.all()
    context = {"books":books}
    template ="relationship_app/list_books.html/"
    for book in books:
        return f"\nTitle: {book.title}, Author: {book.author.name}\n"
    return HttpResponse(template, context)


class BookListView(ListView):
    model = Library
    template_path = "relationship_app/library_detail.html"
    context_object_name = "books"

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

