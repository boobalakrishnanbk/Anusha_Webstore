from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date
import datetime
from .models import Worker_Catalog_Designations, Worker_Catalog_FarmingPlaces
from Accounts.models import Manager_Details
from django.contrib.auth.models import User
from Manager.models import Employee_Attendance, Employee_Salary_Transactions, Employee_Details
from django.db.models import Sum

# Create your views here.

@login_required
def dashboard(request):
    if request.user.is_superuser:

        # designation =
        designation = Employee_Details.objects.filter(active = True).values('designation').order_by('designation').distinct()
        for position in designation:
            # print(position['designation'])
            desig = position['designation']
            count1 = Employee_Details.objects.filter(designation = desig).count()
            position['total_count'] = count1
            count2 = Employee_Attendance.objects.filter(date = date.today() , designation = desig).count()
            position['count'] = count2
            position['absent'] = count1 - count2
            salary = Employee_Attendance.objects.filter(date = date.today(), designation = desig).aggregate(Sum('salary'))
            position['todaysalary'] = salary['salary__sum']

            salary = Employee_Attendance.objects.filter(date__month = date.today().month , designation = desig).aggregate(Sum('salary'))
            position['monthsalary'] = salary['salary__sum']

            # date = datetime.
            start_week = datetime.date.today() - datetime.timedelta(datetime.date.today().weekday())
            end_week = start_week + datetime.timedelta(7)
            salary = Employee_Attendance.objects.filter(date__range=[start_week, end_week] , designation = desig).aggregate(Sum('salary'))
            position['weeksalary'] = salary['salary__sum']

        return render(
            request,
            'Owner/dashboard.html',
            {
                'designation':designation,
                # 'counts':designation,
                'active':'dashboard',
                'date':date.today()
            }
        )
    else:
        return render(request, 'Fixed/Hack.html')

@login_required
def settings_salary(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            if request.POST.get('update'):
                name = request.POST.get('name')
                salary = list(Employee_Details.objects.filter(name = name.upper()).values())
                employee_Details = salary[0]
                Employee_Details.objects.filter(name = request.POST.get('name').upper()).update(salary = request.POST.get('salary'))
                return render(
                    request,
                    'Owner/settings_salary.html',
                    {
                        'active':'settings',
                        'employee':employee_Details,
                        'employees':0
                    }
                )
            else:
                name = request.POST.get('search')
                salary = list(Employee_Details.objects.filter(name = name.upper()).values())
                employee_Details = salary[0]
                employee = 1

        else:
            employee_Details = None
            employee = 0
        return render(
            request,
            'Owner/settings_salary.html',
            {
                'active':'settings',
                'employee':employee_Details,
                'employees':employee
            }
        )
    else:
        return render(request, 'Fixed/Hack.html')



@login_required
def employee_attendance(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST.get('search')
            employee = list(Employee_Attendance.objects.filter(name = name.upper()).values().order_by('-date','designation'))
            # print(employee)
            for id in employee:
                if id['salary'] != 0:
                    id['present'] = 'Worked'
                else:
                    id['present'] = 'Absent'
            # print(name)
        else:
            employee = 0
        return render(
            request,
            'Owner/employee_attendance.html',
            {
                'active':'employee',
                'employees':employee
            }
        )
    else:
        return render(request, 'Fixed/Hack.html')


@login_required
def employee_salary(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST.get('search')
            employee = list(Employee_Salary_Transactions.objects.filter(name = name.upper()).values().order_by('-date'))

        else:
            employee = 0
        return render(
            request,
            'Owner/employee_salary.html',
            {
                'active':'employee',
                'employees':employee
            }
        )
    else:
        return render(request, 'Fixed/Hack.html')



@login_required
def settings_options(request):
    if request.user.is_superuser:
        catalog = {}
        if request.method == 'POST':
            if request.POST.get('designation_button'):
                farmingplace = request.POST.get('farmingplace')
                designation = request.POST.get('designation')
                id = list(Worker_Catalog_FarmingPlaces.objects.filter(farmingplace = farmingplace).values('id'))
                if Worker_Catalog_Designations.objects.filter(designation = designation, farmingplace_id =  id[0]['id']).count() == 0:
                    Farmingplace = Worker_Catalog_FarmingPlaces.objects.get(farmingplace = farmingplace)
                    Designation = Worker_Catalog_Designations()
                    Designation.farmingplace = Farmingplace
                    Designation.designation = designation
                    Designation.save()
            else:

                farmingplace = request.POST.get('farmingplace')
                if Worker_Catalog_FarmingPlaces.objects.filter(farmingplace = farmingplace).count() == 0:
                    Farmingplace = Worker_Catalog_FarmingPlaces()
                    Farmingplace.farmingplace = farmingplace
                    Farmingplace.save()

        catalog['designation'] = list(Worker_Catalog_Designations.objects.values('designation','farmingplace').order_by('farmingplace'))
        for id in catalog['designation']:
            farmingplace = Worker_Catalog_FarmingPlaces.objects.filter(id = id['farmingplace']).values('farmingplace')
            id['farmingplace'] = farmingplace[0]['farmingplace']
        catalog['farmingplace'] = Worker_Catalog_FarmingPlaces.objects.values('farmingplace').distinct()
        return render(
            request,
            'Owner/settings_options.html',
            {
                'active':'settings',
                'catalog':catalog,
            }
        )
    else:
        return render(request, 'Fixed/Hack.html')

@login_required
def settings_manager(request):
    if request.user.is_superuser:
        managers = list(Manager_Details.objects.filter(active = True).values().all())
        for id in managers:
            instance = User.objects.filter(id = id['user_id']).values('username', 'email')
            id['username'] = instance[0]['username']
            id['email'] = instance[0]['email']

        # print(managers)
        farmingplaces = Worker_Catalog_FarmingPlaces.objects.values('farmingplace').distinct()
        return render(
            request,
            'Owner/settings_manager.html',
            {
                'active':'settings',
                'managers':managers,
                'farms':farmingplaces,
            }
        )
    else:
        return render(request, 'Fixed/Hack.html')
