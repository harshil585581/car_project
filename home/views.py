from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"home/home.html")

def login(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"home/login.html")

def register(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"home/register.html")