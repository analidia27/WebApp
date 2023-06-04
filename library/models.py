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
        return f"{self.name} {self.surname}"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=50)
    numero_legajo = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
    

    
class Book(models.Model):
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    ISBN = models.CharField(max_length=13)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class BookLoan(models.Model):
    loan_date = models.DateField()
    return_date = models.DateField()
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

 