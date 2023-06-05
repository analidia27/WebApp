from django import forms
from .models import Book, Employee, Author,Partner, BookLoan
from datetime import timedelta

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
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            initial = kwargs.get('initial', {})
            initial['date_birth'] = instance.date_birth.strftime('%Y-%m-%d')
            kwargs['initial'] = initial
        super().__init__(*args, **kwargs)


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



class BookLoanForm(forms.ModelForm):
    class Meta:
        model = BookLoan
        
        fields = ['book','partner','employee','loan_date','return_date']
        labels = {
                'book':'Libro',
                'partner': 'Socio',
                'employee':'Empleado',
                'loan_date': 'Fecha de Prestamo',
                'return_date': 'Fecha de Retorno'
            }

        widgets = {
                'loan_date': forms.DateInput(attrs={'type': 'date',}),
                'return_date': forms.DateInput(attrs={'type': 'date','readonly':'readonly'})
            }
        
    book = forms.ModelChoiceField(queryset=Book.objects.filter(active=True))
    partner = forms.ModelChoiceField(queryset=Partner.objects.filter(is_active=True))
    employee = forms.ModelChoiceField(queryset=Employee.objects.filter(is_active=True))
            
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            initial = kwargs.get('initial', {})
            initial['loan_date'] = instance.loan_date.strftime('%Y-%m-%d')
            kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

