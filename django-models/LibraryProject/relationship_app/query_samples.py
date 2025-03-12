from .models import Author,Library,Librarian,Book

# Query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        book = Book.objects.filter(author=author)
        return book

    except Author.DoesNotExist:
        return f"Author '{author_name}' does not exist."

# List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        book = library.books.all()
        return book
    except Library.DoesNotExist:
        return f"Library '{library_name}' does not exist."

# Retrieve the librarian for a library
def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        return f"Library '{library_name}' does not exist."
    except Librarian.DoesNotExist:
        return

books = Book.objects.filter(author=Author)
