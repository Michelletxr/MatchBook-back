from rest_framework import filters
from .models import Book


class BookFilters(filters.FilterSet):
        class Meta:
            model = Book
            fields = {
                "id": ["in", "exact"], 
                "name": ["exact", "icontains", "contains"], 
                "author": ["exact", "icontains", "contains"]
            }