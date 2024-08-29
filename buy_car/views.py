from django.shortcuts import render
from django.http import HttpResponse

def buy(request):
    return HttpResponse("buy car")