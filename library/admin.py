from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):

    # List Display: Muestra los atributos del objeto en forma de lista.
    list_display = (
        'title',
        'description', 
        'isbn',
        'author',
        'is_active',
        )

    # Muestra un filtro para todos los objetos.
    list_filter = ('is_active',)

    # Abre un campo "search" para poder buscar por los campos indicados.
    search_fields = (
        'title', 
        )



# Debo registrarlo junto con el modelo referido.
admin.site.register(Book, BookAdmin)