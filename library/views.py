from django.shortcuts import render, redirect
from .models import Employee, Author
from .forms import EmployeeForm, AuthorForm
from django.http import HttpResponseRedirect

# Create your views here.

def create_employee(request,id=None):
    """"""
    if(id != None):
        requested_employed = Employee.objects.get(id=id)
        form = EmployeeForm(instance=requested_employed) 
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
        requested_author = Author.objects.get(id=id)
        form = AuthorForm(instance=requested_author) 
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