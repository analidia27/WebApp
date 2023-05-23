from django.urls import path
from . import views

urlpatterns = [
    path('empleados/nuevo', views.create_employee, name='create_employee'),
    path('empleados/listado', views.list_employees, name='list_employees'),
]