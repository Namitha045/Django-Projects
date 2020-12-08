from django.db import models

class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    superdepartment = models.ForeignKey('self', blank = True, null= True, on_delete = models.CASCADE)

class Office(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    manager = models.ForeignKey('self', blank = True, null =True, on_delete = models.CASCADE)
    department = models.ForeignKey(Department, blank = True, null = True, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, blank = True, null = True, on_delete=models.CASCADE)
