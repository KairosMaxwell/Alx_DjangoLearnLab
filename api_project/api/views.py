from django.shortcuts import render

# Create your views here.
from .models import Book
from rest_framework import generics
from rest_framework.response import Response
from .serializer import BookSerializer


class BookAPIView(generics.ListAPIView):

    def BookList(self):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        return Response(serializer_class(queryset, many=True).data)
