from django.forms import inlineformset_factory
from django.shortcuts import render
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
from .forms import EmployeeForm, DepartmentForm


from .models import *

def update(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        fm=EmployeeForm(request.POST,instance=employee)
        if fm.is_valid():
            fm.save()
    else:
        fm = EmployeeForm(instance=employee)


    context={'form':fm}
    return render(request, 'form.html',context)

def delete(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        employee.delete()
        return HttpResponseRedirect('/')


def deletedep(request, pk):
    department = Department.objects.get(id=pk)
    if request.method == "POST":
        department.delete()
        return HttpResponseRedirect('/')



def addshow(request):
    if request.method == "POST":
        fm=EmployeeForm(request.POST)
        if fm.is_valid():
                fm.save()
                return redirect('/')
    else:
        fm=EmployeeForm()
        employee=Employee.objects.all()
        emp_dep=Department.objects.all()


    if request.method == "POST":
        dfm=DepartmentForm(request.POST)
        if dfm.is_valid():
                dfm.save()
                return redirect('/')
    else:
        dfm=DepartmentForm()
        department = Department.objects.all()
    context = {'form': fm,'dform':dfm,'employee':employee,'department':department,'emp_dep':emp_dep}
    return render(request,'addshow.html',context)


