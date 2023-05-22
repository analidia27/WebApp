from django.contrib import admin
from .models import Book
from .models import Author

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # Lista display, muestra los atributos
    list_display = (
        "title",
        "description",
        "ISBN",
        "author",
        "active",
    )

    # Filtrar los objetos
    list_filter = ("active",)

    # Buscar por campos especificados
    search_fields = ("title",)


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
        "nationality",
        "is_active",
    )
    list_filter = ("is_active","nationality")
    search_fields = ("name", "surname")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
