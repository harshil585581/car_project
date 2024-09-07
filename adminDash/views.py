from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
from adminDash.models import reg_check

def dash(request):
    return render(request,"adminDash/dash.html")

def users_table(request):
    return render(request,"adminDash/users_table.html")

def manage_cars(request):
    return render(request,"adminDash/manage_cars.html")



class login_check(APIView):
    def post(self,request):
        username = request.POST['username']
        password = request.POST['pass']
        if username == 'harshil':
            return JsonResponse({"status":"pass"})
        else:
            return JsonResponse({"status":"fail"})



class users_tb(APIView):
    def post(self, request):
        name = request.POST['name']
        cmob = request.POST['cmob']
        age = request.POST['age']
        usr = reg_check()
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

class users_view(TemplateView):
    template_name = "adminDash/users_table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = reg_check.objects.all()
        context = { 'userdata': user_data}
        return context
    
class delete_user(APIView):
    def post(self, request):
        cmob = request.POST['cmob']
        reg_check.objects.filter(cmob=cmob).delete()
        return JsonResponse({"status": "pass"})

