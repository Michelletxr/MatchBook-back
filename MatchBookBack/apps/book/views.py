from django import views
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
import json
import requests

from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .google_books_api import get_books_from_name,format_data,get_books_from_user

class BookViewsSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ListBookUserViewSet(generics.ListAPIView):
    "list books from user"

    def get_queryset(self):
        queryset = Book.objects.filter(user_id=self.kwargs['pk'])
        return queryset

    serializer_class = BookSerializer


class BookApiViewSet(viewsets.ModelViewSet):
    serializer_class = None
    queryset = None

    @action(detail=False, methods=["get"], url_path="books-api/<str:name>/")
    def info(self, request, name=None, pk=None):
        req = get_books_from_name(name)
        data = []

        if req.status_code == 200:
            objets = json.loads(req.content)
            if objets['totalItems']:
                data = format_data(objets['items'])

        return Response(data, status=req.status_code)


class BookApiUserViewSet(viewsets.ModelViewSet):
    serializer_class = None
    queryset = None

    @action(detail=False, methods=["get"], url_path="books-api/user/<str:id>/")
    def info(self, request, id=None, pk=None):
        req = get_books_from_user(id)
        data = []

        if req.status_code == 200:
            objets = json.loads(req.content)
            if objets['totalItems']:
                data = format_data(objets['items'])

        return Response(data, status=req.status_code)
