from django.contrib import admin
from .models import Book, BookLoan, Author, Employee, Partner

#clase BookAdmin basada en el modelo Book
class BookAdmin(admin.ModelAdmin):
    # Lista de atributos visibles
    list_display = (
        "title",
        "description",
        "ISBN",
        "author",
        "active",
    )
    # Filtro para mostrar solo libros activos
    list_filter = ("active",)
    # Buscador por titulo del libro
    search_fields = ("title",)


#clase BookAdmin basada en el modelo BookLoan
class BookLoanAdmin(admin.ModelAdmin):
    # Lista de atributos visibles
    list_display = (
        "partner",
        "employee",
        "book",
        "loan_date",
        "return_date",
    )
    # Buscador por nombre o apellido del socio, 
    # nombre o apellido de empleado, o bien el titulo del libro 
    search_fields = (
        "partner__first_name",
        "partner__last_name",
        "employee__name",
        "employee__surname",
        "book__title",
    )

class AuthorAdmin(admin.ModelAdmin):
    # Lista de atributos visibles
    list_display = (
        "name",
        "surname",
        "nationality",
        "is_active",
    )
    #Filtro para mostrar autor activos o por nacionalidades
    list_filter = ("is_active", "nationality")
    #Buscador por nombre o apellido de autor
    search_fields = (
        "name", 
        "surname",
    )
class EmployeeAdmin(admin.ModelAdmin):
    # Lista de atributos visibles    
    list_display = (
        "name",
        "surname",
        "numero_legajo",
        "is_active",
    )
    #Filtro para mostrar solo empleados activos
    list_filter = ("is_active",)
    #Buscador por nombre o apellido de empleado
    search_fields = (
        "name",
        "surname",
    )

class PartnerAdmin(admin.ModelAdmin):
    # Lista de atributos visibles
    list_display = (
        "first_name",
        "last_name",
        "date_birth",
        "is_active",
    )
    #Filtro para mostrar solo socios activos
    list_filter = ("is_active",)
    #Buscador por nombre o apellido de socio
    search_fields = (
        "first_name",
        "last_name",
    )

#Se registran los modelos admin creados
admin.site.register(Book, BookAdmin)
admin.site.register(BookLoan, BookLoanAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Partner, PartnerAdmin)
