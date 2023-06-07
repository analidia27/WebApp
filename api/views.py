import json
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from library.models import Book, Author, Partner, Employee

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



def book_json(request, id):

    if request.method == 'GET':
        try:

            book = Book.objects.get(id = id)

            data = {
                'Libro': {
                    'id' : id,
                    'titulo' : book.title,
                    'descripcion' : book.description,
                    'autor' : str(book.author)
                    }
            }

            return JsonResponse(data)
        
        except:
            msj = {
                'Libro' : []
                }

            return JsonResponse(msj)
        
def list_partner_json(request):
    partners = Partner.objects.all().values('id', 'first_name','last_name','date_birth','is_active')
    if(partners):
        list_partners = list()
        for partner in partners:  
            item = list(partner.values())
            temp_partner = {}
            temp_partner['id'] = item[0]
            temp_partner['first_name'] = item[1]
            temp_partner['last_name'] = item[2]
            temp_partner['date_birth'] = str(item[3])
            temp_partner['is_active'] = item[4]
            list_partners.append(temp_partner)

    else:
        list_partners = list()
    data = {
        'socios': list_partners
    }
    return HttpResponse(json.dumps(data, ensure_ascii=False).encode('utf-8'), content_type="application/json")

def list_employee_json(request):
    employees = Employee.objects.all()
    if employees:
        list_employees = list()
        for employee in employees:
            list_employees.append(employee.__dict__())

    else:
        list_employees = list()
    data = {
        'empleados': list_employees
    }
    return HttpResponse(json.dumps(data, ensure_ascii=False).encode('utf-8'), content_type="application/json")