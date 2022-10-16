from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'user', 'author', 'lauch_date', 'sinopse']
        read_only_fields = ("created_at", "updated_at")

class BooksByUser(serializers.ManyRelatedField):
    "livros do usuário serializer"
    user = serializers.ReadOnlyField(source='user.name')
    class Meta:
        model = Book
        fields = ["user"]