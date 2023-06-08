import json
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from library.models import Book, Author, Partner, Employee


def list_books_json(request):
    #se obtiene los registros de libros, solamente id, titulo y autor
    books = Book.objects.all().values("id", "title", "author")
    #se pregunta si hay libros se crea una lista
    if books:
        list_books = list()
        #ciclo para recorrer los libros obtenidos
        for book in books:
            item = list(book.values())
            temp_book = {}
            temp_book["id"] = item[0]
            temp_book["titulo"] = item[1]
            #obtengo el nombre de autor pasando el id
            temp_book["autor"] = str(Author.objects.get(id=item[2]))
            list_books.append(temp_book)
    # si no hay libros se crea una lista vacia
    else:
        list_books = list()
        #se guarda la lista de libros
    data = {"libros": list_books}
    #se retorna en formato json con codificación utf-8
    return HttpResponse(
        json.dumps(data, ensure_ascii=False).encode("utf-8"),
        content_type="application/json",
    )


def book_json(request, id):
    #se obtiene el registro dado un id
    if request.method == "GET":
        try:
            book = Book.objects.get(id=id)
            #formato de libro
            data = {
                "Libro": {
                    "id": id,
                    "titulo": book.title,
                    "descripcion": book.description,
                    "autor": str(book.author),
                }
            }
            return JsonResponse(data)
        except:
            #si no lo encuentro, devuelvo un diccionario vacio
            msj = {"Libro": []}
            return JsonResponse(msj)


def list_partner_json(request):
    #se obtiene todos los registros de socios
    partners = Partner.objects.all().values(
        "id", "first_name", "last_name", "date_birth", "is_active"
    )
    #se pregunta si hay socios se crea una lista
    if partners:
        list_partners = list()
        #ciclo para recorrer los libros obtenidos
        for partner in partners:
            item = list(partner.values())
            temp_partner = {}
            temp_partner["id"] = item[0]
            temp_partner["first_name"] = item[1]
            temp_partner["last_name"] = item[2]
            temp_partner["date_birth"] = str(item[3])
            temp_partner["is_active"] = item[4]
            list_partners.append(temp_partner)
    # si no hay socios se crea una lista vacia
    else:
        list_partners = list()
        
    data = {"socios": list_partners}
    #se retorna en formato json con codificación utf-8
    return HttpResponse(
        json.dumps(data, ensure_ascii=False).encode("utf-8"),
        content_type="application/json",
    )


def list_employee_json(request):
    #se obtiene todos los registros de empleados
    employees = Employee.objects.all()
    #ciclo para recorrer los empleados obtenidos
    if employees:
        list_employees = list()
        #ciclo para recorrer los empleados obtenidos
        for employee in employees:
            aux = {
                "name": employee.name,
                "surname": employee.surname,
                "numero_legajo": employee.numero_legajo,
                "is_active": employee.is_active,
            }
            list_employees.append(aux)
    # si no hay empleados se crea una lista vacia
    else:
        list_employees = list()
    data = {"empleados": list_employees}
    #se retorna en formato json con codificación utf-8
    return HttpResponse(
        json.dumps(data, ensure_ascii=False).encode("utf-8"),
        content_type="application/json",
    )


def list_author_json(request):
    #se obtienen los registros de autores
    authors = Author.objects.all().values(
        "id", "name", "surname", "nationality", "is_active"
    )
    # si hay autores, se crea una lista
    if authors:
        list_authors = list()
        #ciclo para recorrer los autores obtenidos
        for author in authors:
            item = list(author.values())
            temp_author = {}
            temp_author["id"] = item[0]
            temp_author["nombre"] = item[1]
            temp_author["apellido"] = item[2]
            temp_author["nacionalidad"] = item[3]
            temp_author["activo"] = item[4]
            list_authors.append(temp_author)
    # si no hay autores se crea una lista vacia
    else:
        list_authors = list()
    data = {"autores": list_authors}
    #se retorna en formato json con codificación utf-8
    return HttpResponse(
        json.dumps(data, ensure_ascii=False).encode("utf-8"),
        content_type="application/json",
    )
