import json
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from library.models import Book,Author

def list_books_json(request):
    books = Book.objects.all().values('id', 'title','author')
    if(books):
        list_books = list()
        for book in books:  
            item = list(book.values())
            temp_book = {}
            temp_book['id'] = item[0]
            temp_book['titulo'] = item[1]
            temp_book['autor'] = str(Author.objects.get(id=item[2]))
            list_books.append(temp_book)

    else:
        list_books = list()
    data = {
        'libros': list_books
    }
    return HttpResponse(json.dumps(data, ensure_ascii=False).encode('utf-8'), content_type="application/json") 
