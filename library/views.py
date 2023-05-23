from django.shortcuts import render, redirect
#from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponseRedirect

# Create your views here.

def create_employee(request):

    form = EmployeeForm()

    if request.method == "POST":

        form = EmployeeForm(request.POST)

        if form.is_valid():

            form.save()

            #return redirect('/empleados/lista')

        else:
        
            return HttpResponseRedirect('create_employee/')

    context = {'form': form}
    
    return render(request, 'create_employee.html', context)