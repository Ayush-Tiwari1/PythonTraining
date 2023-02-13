from django.db import models

# Create your models here.


class Department(models.Model):
    dep_name = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.dep_name



class Employee(models.Model):
    name = models.CharField(max_length=25, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=25, null=True)
    dapartment=models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)
    age=models.IntegerField(null=True)

    def __str__(self):
        return self.name



