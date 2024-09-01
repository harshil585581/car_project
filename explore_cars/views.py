from django.shortcuts import render
from django.http import HttpResponse

def explorecars(request):
    return render(request,"explore_cars/explorecar.html")
