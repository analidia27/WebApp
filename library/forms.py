from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'surname': 'Apellido',
            'numero_legajo': 'Número de legajo',
            'is_active': 'Activo'
        }

