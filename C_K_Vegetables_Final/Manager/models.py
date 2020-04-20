from django.db import models

# Create your models here.
class Employee_Details(models.Model):
    name = models.CharField(max_length = 50)
    phone = models.BigIntegerField()
    designation = models.CharField(max_length = 50)
    locality = models.CharField(max_length = 50)
    date_joined = models.DateField()
    advance = models.IntegerField()
    worked_days = models.IntegerField()
    salary = models.IntegerField()
    active = models.BooleanField()

    def __str__(self):
        return self.name


class Employee_Attendance(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length = 50)
    date =  models.DateField()
    salary = models.IntegerField()
    manager = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 50)
    locality = models.CharField(max_length = 50)

    def __str__(self):
        return self.name+' '+str(self.date)

class Employee_Salary_Transactions(models.Model):
    employee_id = models.IntegerField()
    name = models.CharField(max_length = 50)
    date =  models.DateField()
    salary = models.IntegerField()
    advance = models.IntegerField()
    manager = models.CharField(max_length = 50)

    def __str__(self):
        return self.name+' '+str(self.date)
