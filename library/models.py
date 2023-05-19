from django.db import models

# Create your models here.

class Partner():
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_birth = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)                      # El isbn es de 13 cifras
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=50)
    numero_legajo = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    