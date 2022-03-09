from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def employee(request):
    return render(request, 'employee/index.html')


def home(request):
    return render(request, 'employee/home/index.html')


def contact(request):
    return render(request, 'employee/contact/index.html')


def about(request):
    return render(request, 'employee/about/index.html')
