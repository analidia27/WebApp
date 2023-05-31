from django import forms
from .models import Book, Employee, Author,Partner


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','surname','numero_legajo']
        labels = {
            'name': 'Nombre',
            'surname': 'Apellido',
            'numero_legajo': 'Número de legajo'
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','surname','nationality']
        labels = {
                'name': 'Nombre',
                'surname': 'Apellido',
                'nationality': 'Nacionalidad'
            }




class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['first_name','last_name','date_birth']
        labels = {
                'first_name': 'Nombre',
                'last_name': 'Apellido',
                'date_birth': 'Fecha de Nacimiento'
            }
        widgets = {
            'date_birth': forms.DateInput(attrs={'type': 'date'})
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','description','ISBN','author']
        labels = {
                'title': 'Titulo',
                'description': 'Descripción',
                'ISBN': 'ISBN',
                'author':'Autor'
            }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['author'].queryset = Author.objects.filter(is_active=True)