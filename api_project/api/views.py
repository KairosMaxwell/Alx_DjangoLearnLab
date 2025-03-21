# Create your views here.
from PyQt5.QtCore.QUrl import query
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):

    def BookList(self):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        return Response(serializer_class(queryset, many=True).data)

#     Defining a Viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer







