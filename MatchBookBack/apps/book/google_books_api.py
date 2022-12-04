import requests
import json

from django.conf import settings
from .utils import generate_book_format


def format_data(data):
    books = []
    for x in data:
        books.append(generate_book_format(x))
    return books


def get_books_from_name(name):
    req = requests.get(f"{settings.BOOK_API_URL}/volumes?q={name}"
                       f"&projection=lite"
                       f"&key={settings.API_SECRET_KEY}")
    return req
