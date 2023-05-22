from django.contrib import admin
from .models import Book
from .models import Author
from .models import Employee
from .models import Partner
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

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
        "numero_legajo",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("name", "surname",)


class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "date_birth",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("first_name", "last_name",)
    

    
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Partner, PartnerAdmin)
