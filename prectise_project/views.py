from django.http import HttpResponse


def home(request):
    return HttpResponse("This is home")


def about(request):
    return HttpResponse("This is about")
