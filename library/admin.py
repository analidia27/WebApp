from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    
    # Lista display, muestra los atributos
    list_display = ('title', 'description', 'ISBN', 'author', 'active',)
    
    # Filtrar los objetos
    list_filter = ('active',)

    # Buscar por campos especificados
    search_fields = ('title',)

admin.site.register(Book, BookAdmin)

