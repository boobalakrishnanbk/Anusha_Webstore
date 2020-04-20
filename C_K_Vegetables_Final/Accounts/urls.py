from django.urls import path
from . import views

#

app_name = 'Accounts'

urlpatterns = [
    path('', views.login_page, name = 'login_page'),
    path('logout/', views.User_Logout, name = 'User_Logout'),
    path('settings/addmanager/', views.Add_Manager, name = 'Add_Manager'),
    path('settings/removemanager/', views.Remove_Manager, name = 'Remove_Manager')

]
