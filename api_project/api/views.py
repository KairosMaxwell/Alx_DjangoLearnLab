# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter
from .models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):

    def BookList(self):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        return Response(serializer_class(queryset, many=True).data)

#     Defining a viewset
class BookViewSet(ModelViewSet):
    pass

router = DefaultRouter()
router.register(r'books',BookViewSet, basename='book_all')


