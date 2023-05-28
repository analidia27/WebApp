from django import forms
from .models import Employee, Author


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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')

        if instance:
            # Si existe una instancia, ocultar el campo is_active durante la actualización
            self.fields['is_active'].widget = forms.HiddenInput()

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
                'name': 'Nombre',
                'surname': 'Apellido',
                'nationality': 'Nacionalidad',
                'is_active': 'Activo'
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')

        if instance:
            # Si existe una instancia, ocultar el campo is_active durante la actualización
            self.fields['is_active'].widget = forms.HiddenInput()