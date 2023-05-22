from django.contrib import admin
from .models import Book, Employee

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    
    # Lista display, muestra los atributos
    list_display = ('title', 'description', 'ISBN', 'author', 'active',)
    
    # Filtrar los objetos
    list_filter = ('active',)

    # Buscar por campos especificados
    search_fields = ('title',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'numero_legajo', 'is_active')
    search_fields = ('name','surname')
    list_filter = ('is_active')


    
admin.site.register(Book, BookAdmin)
admin.site.register(Employee,EmployeeAdmin)
