from django.contrib import admin
from .models import Book

# Register your models here.
class Books(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name', 'id')

admin.site.register(Book, Books)