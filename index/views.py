from cgitb import text
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'index/index.html')


# def home(request):
#     text={
#         'name':'Nguyen Van A',
#         'age':'20',
#         'phone':'0989898989',
#         'email':'admin@admin.com',
#         'friend':['Nguyen Van B','Nguyen Van C','Nguyen Van D']
#     }
#     return render(request, 'employee/home/index.html', text)