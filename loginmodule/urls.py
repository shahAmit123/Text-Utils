
from django.contrib import admin
from django.urls import path
from . import views
#from . import textpycharm

urlpatterns = [
    path('signup/',views.signuphandle,name='signuphandle'),   
    path('login/',views.loginhandle,name='loginhandle'),
    path('logout/',views.logouthandle,name='logouthandle')
]
