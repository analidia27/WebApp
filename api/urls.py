from django.urls import path
from . import views

urlpatterns = [
    path('api/libros', views.list_books_json, name='api_libros'),
]