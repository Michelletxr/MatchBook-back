from django import views
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class BookViewsSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]

class ListBookUserViewSet(generics.ListAPIView):
    "lista livros do usuário"
    def get_queryset(self):
        queryset = Book.objects.filter(user_id=self.kwargs['pk'])
        return queryset
    serializer_class = BookSerializer

