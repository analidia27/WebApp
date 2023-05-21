from django.db import models

# Create your models here.

class Partner(models.Model):
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
    

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=50)
    numero_legajo = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.surname
    

    
    