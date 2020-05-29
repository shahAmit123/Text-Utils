# i have cerated this file " Amit Shah "
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext =request.POST.get('text','default')
    djremovepunc =request.POST.get('removepunc','off')
    djcapitalization = request.POST.get('capitalization', 'off')
    djextraspaceremover=request.POST.get('extraspaceremover','off')
    djnewline=request.POST.get('newlineremover','off')
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed=djtext
    if djnewline == 'off' and djremovepunc == 'off' and djcapitalization=='off' and djextraspaceremover == 'off':
        return render(request,'error.html')
    if djnewline == 'on':
        analyzed1=""
        flag = 0
        for i in analyzed:
            if (i == '\n' or i=='\r') and flag == 1:
                pass
            elif i is '\n' or i is '\r':
                analyzed1 = analyzed1 + i
                flag = 1
            else:
                analyzed1 = analyzed1 + i
                flag = 0
        analyzed=analyzed1
    if djremovepunc=='on':
        analyzed1=""
        for i in analyzed :
            if i not in punctuations :
                analyzed1= analyzed1+i
        analyzed=analyzed1
    if djcapitalization == 'on':
        analyzed1=""
        for i in analyzed:
            analyzed1= analyzed1 + i.capitalize()
        analyzed=analyzed1
    if djextraspaceremover == 'on':
        analyzed1=""
        flag=0
        for i in analyzed:
            if i == ' ' and flag==1:
                pass
            elif i is ' ':
                analyzed1 = analyzed1 + i
                flag=1
            else:
                analyzed1 = analyzed1 + i
                flag=0
        analyzed=analyzed1
    params={'purpose':'Capitalization','analyzed_text':analyzed}
    return render(request,'textutils.html',params)

