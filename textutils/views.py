# i have cerated this file " Amit Shah "
from django.http import HttpResponse
from django.shortcuts import render
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
#     #return HttpResponse('''<h1> This is My First Page</h1><br> <a href="https://www.google.com"> Search Anything Any time "</a> ''')
# def about(request):
#     return HttpResponse("about Amit bro")
# def removepunc(request):
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse('''<h1> Remove Punctuations </h1> <br> <a href="/"> Go Back </a>''')
# def capitalize(request):
#     return HttpResponse('''<h1>your text will be capitalize soon! </h1> <br> <a href="http://127.0.0.1:8000/">Go Back</a>''')
# def roundoff(request):
#     return HttpResponse('''<h1>your integer will be rounded off soon!</h1> <br> <a href="http://127.0.0.1:8000/">Go Back</a>''')
# def count(request):
#     return HttpResponse('''<h1>your string length will be given soon! </h1> <br> <a href="http://127.0.0.1:8000/">Go Back</a>''')
