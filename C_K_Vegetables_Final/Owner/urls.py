from django.urls import path
from . import views

#

app_name = 'Owner'

urlpatterns = [
    path('Owner/dashboard/', views.dashboard, name = 'dashboard'),
    path('Owner/settings/options/', views.settings_options, name = 'settings_options'),
    path('Owner/settings/manager/', views.settings_manager, name = 'settings_manager'),
    path('Owner/settings/salary/', views.settings_salary, name = 'settings_salary'),
    path('Owner/employee/attendance/', views.employee_attendance, name = 'employee_attendance'),
    path('Owner/employee/salary/', views.employee_salary, name = 'employee_salary'),


]
