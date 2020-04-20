from django.contrib import admin
from .models import Employee_Details, Employee_Attendance, Employee_Salary_Transactions
# Register your models here.
admin.site.register(Employee_Details)
admin.site.register(Employee_Attendance)
admin.site.register(Employee_Salary_Transactions)
