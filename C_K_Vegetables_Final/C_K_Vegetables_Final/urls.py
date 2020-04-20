from django.contrib import admin
from django.urls import path,include
from Accounts import urls
from Owner import urls
from Manager import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Accounts.urls')),
    path('',include('Owner.urls')),
    path('',include('Manager.urls')),

]
