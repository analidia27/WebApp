from django.contrib import admin
from .models import Book,BookLoan

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


class BookLoanAdmin(admin.ModelAdmin):
    # Lista display, muestra los atributos
    list_display = (
        "partner",
        "employee",
        "book",
        "loan_date",
        "return_date",
    )

    # Buscar por campos especificados
    search_fields = ("partner","book","employee")


admin.site.register(Book, BookAdmin)
admin.site.register(BookLoan, BookLoanAdmin)
