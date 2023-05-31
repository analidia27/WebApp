from django.shortcuts import render, redirect
from .models import Employee, Author,Partner, Book, BookLoan
from .forms import EmployeeForm, AuthorForm, PartnerForm, BookForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_employee(request,id=None):
    """Si se envia el id del empleado se obtiene el objeto y se crea el formulario con datos, 
        sino se crea el formulario vacio"""
    if(id != None):
        try:
            requested_employed = Employee.objects.get(id=id)
            form = EmployeeForm(instance=requested_employed)         
        except Exception:
            return render(request, 'error.html')
    else:
        form = EmployeeForm()
    if request.method == "POST":

        if(id):
            form = EmployeeForm(request.POST,instance=requested_employed) 
        else:
            form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_employees')


        else:
            return HttpResponseRedirect('create_employee/')

    context = {'form': form,'is_update':id != None}
    
    return render(request, 'create_employee.html', context)


def list_employees(request):

    employees = Employee.objects.all()

    context = {
        'employees' : employees
    }
    
    return render(request, 'list_employees.html', context=context)

def change_status_employee(request,id):
    employee = Employee.objects.get(id=id)
    if employee.is_active:
        employee.is_active = False
    else:
        employee.is_active = True
    employee.save()
    return redirect('list_employees') 


def create_update_author(request, id=None):
    if(id):
        """ Si se envia el id del autor se obtiene el objeto y se crea el formulario con datos, 
        sino se crea el formulario vacio"""
        try:
            requested_author = Author.objects.get(id=id)
            form = AuthorForm(instance=requested_author)
        except Exception:
            return render(request, 'error.html') 
    else:
        form = AuthorForm()
        
    if request.method == "POST":
        if(id):
            form = AuthorForm(request.POST,instance=requested_author) 
        else:
            form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/autores/listado')

        else:
            return HttpResponseRedirect('create_author/')
        
    context = {'form': form,'is_update': id != None}
    
    return render(request, 'create_author.html', context)


def list_authors(request):

    authors = Author.objects.all()

    context = {
        'authors' : authors
    }
    
    return render(request, 'list_authors.html', context=context)

def change_status_author(request,id):
    author = Author.objects.get(id=id)
    if author.is_active:
        author.is_active = False
    else:
        author.is_active = True
    author.save()
    return redirect('list_authors') 

def create_update_partner(request, id=None):
    if(id):
        """ Si se envia el id del socio se obtiene el objeto y se crea el formulario con datos, 
        sino se crea el formulario vacio"""
        try: 
            requested_partner = Partner.objects.get(id=id)
            form = PartnerForm(instance=requested_partner) 
        except Exception:
            return render(request, 'error.html')
    else:
        form = PartnerForm()
        
    if request.method == "POST":
        if(id):
            form = PartnerForm(request.POST,instance=requested_partner) 
        else:
            form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/socios/listado')

        else:
            return HttpResponseRedirect('create_partner/')
        
    context = {'form': form,'is_update': id != None}
    
    return render(request, 'create_partner.html', context)

def list_partners(request):

    partners = Partner.objects.all()

    context = {
        'partners' : partners
    }
    
    return render(request, 'list_partners.html', context=context)

def change_status_partner(request,id):
    partner = Partner.objects.get(id=id)
    if partner.is_active:
        partner.is_active = False
    else:
        partner.is_active = True
    partner.save()
    return redirect('list_partners') 


def create_update_book(request, id=None):
    if(id):
        """ Si se envia el id del libro se obtiene el objeto y se crea el formulario con datos, 
        sino se crea el formulario vacio"""
        try:
            requested_book = Book.objects.get(id=id)
            form = BookForm(instance=requested_book) 
        except Exception:
            return render(request, 'error.html')
    else:
        form = BookForm()
        
    if request.method == "POST":
        if(id):
            form = BookForm(request.POST,instance=requested_book) 
        else:
            form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/libros/listado')

        else:
            return HttpResponseRedirect('create_book/')
        
    context = {'form': form,'is_update': id != None}
    
    return render(request, 'create_book.html', context)

def list_books(request):

    books = Book.objects.all()

    context = {
        'books' : books
    }
    
    return render(request, 'list_books.html', context=context)

def change_status_book(request,id):
    book = Book.objects.get(id=id)
    if book.active:
        book.active = False
    else:
        book.active = True
    book.save()
    return redirect('list_books') 


def list_book_loans(request):

    book_loans = BookLoan.objects.all()

    context = {
        'book_loans' : book_loans
    }
    
    return render(request, 'list_book_loans.html', context=context)