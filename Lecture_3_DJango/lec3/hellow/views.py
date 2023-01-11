from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def honey(request):
    return HttpResponse("Hello Honey")

def greet(request, name):
    return render(request,"hello/greet.html",{"name":name.capitalize()})

# return an entire html template

def home(request):
    return render(request, "hello/index.html")