from django import forms
from .models import Employee, Author,Partner


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

