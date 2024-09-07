from django.shortcuts import render
from django.http import HttpResponse

def admindash(request):
    return render(request,"adminDash/dash.html")
