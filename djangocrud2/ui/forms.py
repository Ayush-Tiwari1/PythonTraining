from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from  django.contrib.auth.models import User
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields = '__all__'
