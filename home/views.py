from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse

def home(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"home/home.html")

def login(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"home/login.html")

def register(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"home/register.html")

class login_check(APIView):
    def post(self,request):
        username = request.POST['username']
        password = request.POST['pass']
        if username == 'test':
            return JsonResponse({"status":"pass"})
        else:
            return JsonResponse({"status":"fail"})