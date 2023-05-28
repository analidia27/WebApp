from django.urls import path
from . import views

urlpatterns = [
    path('empleados/nuevo', views.create_employee, name='create_employee'),
    path('empleados/listado', views.list_employees, name='list_employees'),
    path('empleados/editar/<int:id>', views.create_employee, name='update_employees'),
    path('empleados/estado/<int:id>', views.change_status_employee, name='change_status_employee'),
]