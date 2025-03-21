# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):

    def booklist(self):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        return Response(serializer_class(queryset, many=True).data)


from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from rest_framework import permissions


#     Defining a Viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    admin_user = [IsAdminUser]










