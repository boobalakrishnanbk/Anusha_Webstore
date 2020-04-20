from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from Owner.views import settings_manager
from .models import Manager_Details
from datetime import date
# Create your views here.

def login_page(request):
    return User_Login(request)


def User_Login(request):
    message = None

    if request.user.is_active:
        return render(request, 'Fixed/default_homepage.html', {'active':'home' })

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)

            if user:
                if user.is_active:
                    login(request,user)
                    if user.is_superuser:
                        return render(request, 'Owner/dashboard.html', {'active':'dashboard' })
                    else:
                            return render(request,'Manager/homepage.html',{'active':'home', })
            else:
                message = '1'
    return render(request, 'Accounts/login_page.html', {'message':message})


@login_required
def User_Logout(request):
    logout(request)
    return User_Login(request)

@login_required
def Add_Manager(request):
    if request.user.is_superuser:
        manager = Manager_Details()
        username =  User.objects.filter(username = request.POST.get('username')).count()
        if username == 0:
            user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
            user.save()
            manager.user = user
            manager.farming_location = request.POST.get('farmlocation')
            manager.phone = request.POST.get('phone')
            manager.designation = request.POST.get('designation')
            manager.join_date = date.today()
            manager.locality = request.POST.get('locality')
            manager.active = True
            manager.save()
            return settings_manager(request)
        else:
            message = 'Oops'
    else:
        return render(request, 'Fixed/Hack.html')

@login_required
def Remove_Manager(request):
    if request.user.is_superuser:
        id = request.POST.get('user_id')
        Manager_Details.objects.filter(user_id = id).delete()
        User.objects.filter(id = id).delete()
        return settings_manager(request)
    else:
        return render(request, 'Fixed/Hack.html')
