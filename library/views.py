from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
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
