from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def signuphandle(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pwd = request.POST['pwd']
        uname = request.POST['uname']

        myuser = User.objects.create_user(uname , email, pwd)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
    return redirect('index')

def loginhandle(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']

        myuser = authenticate(username = uname , password = pwd)

        if myuser is not None: 
            login(request,myuser)
            messages.success(request,"Successfully logged in")
            return redirect('index')
        
        else:
            messages.error(request,"Invalid Credential, Please try again")
            return redirect('index')

def logouthandle(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('index')