from django.urls import path
from . import views
#
app_name = 'Manager'

urlpatterns = [
    path('Manager/employee/details/', views.employee_Details, name = 'employee_Details'),
    path('Manager/employee/addemployee/', views.employee_Add, name = 'employee_Add'),
    path('Manager/employee/removeemployee/', views.employee_Remove, name = 'employee_Remove'),
    path('Manager/home/', views.home, name = 'home'),
    path('Manager/employee/attendance', views.employee_Attendance, name = 'employee_Attendance'),
    path('Manager/employee/salary', views.employee_Salary, name = 'employee_Salary'),

]
