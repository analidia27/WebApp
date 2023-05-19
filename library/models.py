from django.db import models

# Create your models here.

class Partner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_birth = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    ISBN = models.IntegerField(max_length=13)
    active = models.BooleanField(default=True)
