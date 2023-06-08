from django.urls import path
from . import views

urlpatterns = [
    path('api/libros', views.list_books_json, name='api_libros'),
    path('api/libros/<int:id>', views.book_json, name='api_libro'),
    path('api/socios', views.list_partner_json, name='api_socios'),
    path('api/empleados', views.list_employee_json, name='api_empleados'),
    path('api/autores', views.list_author_json, name='api_autores'),

]