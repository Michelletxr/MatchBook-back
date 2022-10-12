from dataclasses import fields
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'lauch_date', 'sinopse']
        read_only_fields = ("created_at", "updated_at")