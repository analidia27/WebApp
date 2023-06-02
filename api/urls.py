from django.urls import path
from . import views

urlpatterns = [
    path('api/libros', views.list_books, name='api_libros'),
]