from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('empleados/nuevo', views.create_employee, name='create_employee'),
    path('empleados/listado', views.list_employees, name='list_employees'),
    path('empleados/editar/<int:id>', views.create_employee, name='update_employees'),
    path('empleados/estado/<int:id>', views.change_status_employee, name='change_status_employee'),
    path('autores/nuevo', views.create_update_author, name='create_author'),
    path('autores/editar/<int:id>', views.create_update_author, name='update_author'),
    path('autores/listado', views.list_authors, name='list_authors'),
    path('autores/estado/<int:id>', views.change_status_author, name='change_status_author'),
    path('socios/nuevo', views.create_update_partner, name='create_partner'),
    path('socios/listado', views.list_partners, name='list_partners'),
    path('socios/editar/<int:id>', views.create_update_partner, name='update_partner'),
    path('socios/estado/<int:id>', views.change_status_partner, name='change_status_partner'),
    path('libros/nuevo', views.create_update_book, name='create_book'),
    path('libros/listado', views.list_books, name='list_books'),
    path('libros/editar/<int:id>', views.create_update_book, name='update_book'),
    path('libros/estado/<int:id>', views.change_status_book, name='change_status_book'),
    
]