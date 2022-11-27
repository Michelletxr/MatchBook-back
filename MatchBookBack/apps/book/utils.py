

def generate_book_format(book):
    info = book['volumeInfo']
    book_format = {
        'title': info.get('title'),
        'authors': info.get('authors'),
        'publishedDate': info.get('publishedDate'),
        'description': info.get('description'),
        'imageLinks': info.get('imageLinks')
    }
    return book_format
