from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
from home.models import signup_check

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
        


class create_signup(APIView):
    def post(self, request):
        name = request.POST['name']
        cmob = request.POST['cmob']
        age = request.POST['age']
        usr = signup_check()
        usr.name = name
        usr.cmob = cmob
        usr.age = age
        usr.save()
        # print(username)
        # print(email)
        # print(password)
        # print(utype)
        return JsonResponse({"status": "pass"})

from django.views.generic import TemplateView

class signup_view(TemplateView):
    template_name = "view_signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = signup_check.objects.all()
        context = { 'userdata': user_data}
        return context