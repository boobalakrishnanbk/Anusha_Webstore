from django.shortcuts import render
from .models import Employee_Details, Employee_Attendance, Employee_Salary_Transactions
from Owner.models import Worker_Catalog_Designations,Worker_Catalog_FarmingPlaces
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from django.db.models import Q,Sum

# Create your views here.

@login_required
def employee_Salary(request):
    if request.method == 'POST':
        if request.POST.get('paysalary'):
            if request.POST.get('pay') == '0':
                advance = int(request.POST.get('advance')) - int(request.POST.get('salary'))
            else:
                advance = 0
            Employee_Details.objects.filter(id = request.POST.get('id')).update(worked_days = 0,advance = advance)
            name = Employee_Details.objects.filter(id = request.POST.get('id')).values('name')
            instance = Employee_Salary_Transactions()
            instance.employee_id = request.POST.get('id')
            instance.name = name[0]['name']
            instance.date = date.today()
            instance.salary = request.POST.get('pay')
            instance.manager = request.user
            instance.advance = advance
            instance.save()
        if request.POST.get('paydebt'):
            advance = Employee_Details.objects.filter(id = request.POST.get('id')).values('advance')
            amount = advance[0]['advance'] + int(request.POST.get('amount'))
            Employee_Details.objects.filter(id = request.POST.get('id')).update(advance = amount)
            name = Employee_Details.objects.filter(id = request.POST.get('id')).values('name')
            instance = Employee_Salary_Transactions()
            instance.employee_id = request.POST.get('id')
            instance.name = name[0]['name']
            instance.date = date.today()
            instance.salary = 0
            instance.manager = request.user
            instance.advance = int(request.POST.get('amount'))
            instance.save()
    employee = Employee_Details.objects.filter(~Q(worked_days = 0), active = True).values().order_by('name')
    for id in employee:
        temp_1 = Employee_Attendance.objects.filter(user_id = id['id']).order_by('-date')[:id['worked_days']].aggregate(Sum('salary'))
        id['temp'] = temp_1['salary__sum']
        if id['advance'] > id['temp']:
            id['payamount'] = 0
        else:
            print('hi')
            temp_2 = id['advance'] - id['temp']
            if temp_2 < 0:
                id['payamount'] = -1 * temp_2
            else:
                id['payamount'] = temp_2
    return render(
        request,
        'Manager/employee_salary.html',
        {
            'active':'salary',
            'employees':employee,
            'designation':Employee_Details.objects.filter(active = True).values('designation').order_by('designation').distinct(),
            'locality':Employee_Details.objects.filter(active = True).values('locality').order_by('locality').distinct(),

        }
    )



@login_required
def home(request):
    # print('hi')
    return render(
        request,
        'Manager/homepage.html',
        {
            'active':'home',
        }
    )

@login_required
def employee_Attendance(request):
    if request.method == 'POST':
        if request.POST.get('yesterday'):
            yesterday = date.today() - timedelta(days = 1)
            employees = Employee_Details.objects.filter(active = True).values('id', 'name', 'designation','worked_days', 'locality', 'salary').order_by('name')

            for employee in employees:
                if not request.POST.get('shift'+str(employee['id'])) == None:
                    if int(request.POST.get('shift'+str(employee['id']))) == 1:
                        salary = employee['salary']
                    elif int(request.POST.get('shift'+str(employee['id']))) == 2:
                        salary = int(employee['salary']) + int(employee['salary'] / 2)
                    else:
                        salary = 0
                    instance = Employee_Attendance()
                    instance.user_id = employee['id']
                    instance.name = employee['name'].upper()
                    instance.date = date.today() - timedelta(days = 1)
                    instance.salary = salary
                    instance.manager = request.user
                    instance.designation = employee['designation']
                    instance.locality = employee['locality']
                    instance.save()
                    Employee_Details.objects.filter(id = employee['id']).update(worked_days = employee['worked_days']+1 )

            employees = Employee_Details.objects.filter(active = True).values().order_by('designation')
            return render(
                request,
                'Manager/employee_attendance.html',
                {
                    'active':'attendance',
                    'employees':employees,
                    'designation':Employee_Details.objects.filter(active = True).values('designation').order_by('designation').distinct(),
                    'locality':Employee_Details.objects.filter(active = True).values('locality').order_by('locality').distinct(),
                    'date':yesterday,
                    'yesterday':1,
                    # 'count':
                }
            )
        else:
            employees = Employee_Details.objects.filter(active = True).values('id', 'name', 'designation','worked_days', 'locality', 'salary').order_by('name')

            for employee in employees:
                if not request.POST.get('shift'+str(employee['id'])) == None:
                    if int(request.POST.get('shift'+str(employee['id']))) == 1:
                        salary = employee['salary']
                    elif int(request.POST.get('shift'+str(employee['id']))) == 2:
                        salary = int(employee['salary']) + int(employee['salary'] / 2)
                    else:
                        salary = 0
                    instance = Employee_Attendance()
                    instance.user_id = employee['id']
                    instance.name = employee['name'].upper()
                    instance.date = date.today()
                    instance.salary = salary
                    instance.manager = request.user
                    instance.designation = employee['designation']
                    instance.locality = employee['locality']
                    instance.save()
                    Employee_Details.objects.filter(id = employee['id']).update(worked_days = employee['worked_days']+1 )

    today = date.today()
    employees = Employee_Attendance.objects.filter(date = today).values('user_id')
    employee_id = []
    for id in employees:
        employee_id.append(id['user_id'])

    print(employees)
    employees = Employee_Details.objects.filter(~Q(id__in = employee_id),active = True).values().order_by('designation')
    # print(Employee_Attendance.objects.filter(date = (date.today() - timedelta(days = 1))).count())
    return render(
        request,
        'Manager/employee_attendance.html',
        {
            'active':'attendance',
            'employees':employees,
            'designation':Employee_Details.objects.filter(active = True).values('designation').order_by('designation').distinct(),
            'locality':Employee_Details.objects.filter(active = True).values('locality').order_by('locality').distinct(),
            'date':date.today(),
            'yesterday':Employee_Attendance.objects.filter(date = (date.today() - timedelta(days = 1))).count(),
            # 'count':
        }
    )


@login_required
def employee_Details(request):
    return render(
        request,
        'Manager/employee_details.html',
        {
            'active':'employeedetails',
            'employees':Employee_Details.objects.filter(active = True).values().order_by('designation'),
            'designation':Employee_Details.objects.filter(active = True).values('designation').order_by('designation').distinct(),
        }
    )


@login_required
def employee_Add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        designation = request.POST.get('designation')
        locality = request.POST.get('locality')
        salary = request.POST.get('salary')

        instance = Employee_Details()
        instance.name = name.upper()
        instance.phone = phone
        instance.designation = designation
        instance.locality = locality
        instance.date_joined = date.today()
        instance.advance = 0
        instance.worked_days = 0
        instance.salary = salary
        instance.active = True
        instance.save()

        return render(
            request,
            'Manager/employee_details.html',
            {
                'active':'employeedetails',
                'employees':Employee_Details.objects.filter(active = True).values().order_by('designation'),
                'designation':Employee_Details.objects.filter(active = True).values('designation').order_by('designation').distinct(),
            }
        )

    designation = list(Worker_Catalog_Designations.objects.values().order_by('farmingplace_id'))
    for position in designation:
        farmingplace = list(Worker_Catalog_FarmingPlaces.objects.filter(id = position['farmingplace_id']).values('farmingplace'))
        position['location'] = str(farmingplace[0]['farmingplace']+ ' - ( '+ position['designation']+' )')
    return render(
        request,
        'Manager/employee_add.html',
        {
            'active':'employeedetails',
            'designation':designation
        }
    )

@login_required
def employee_Remove(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        Employee_Details.objects.filter(id = id).delete()
        return employee_Details(request)
