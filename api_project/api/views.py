from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView

# Existing list view (optional, can keep or remove)
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for all CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, updating, and deleting books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, updating, and deleting books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class Bookview(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer