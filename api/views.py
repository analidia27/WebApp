from django.shortcuts import render
from library.models import Book

def list_books(request):
    books = Book.objects.all().values('id','title','author')
    context = {
        'books' : books
    }
    return render(request, 'list_book.html', context=context)
