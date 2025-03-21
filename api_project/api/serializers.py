from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    book_model = Book
    fields ="__all__"