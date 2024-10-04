from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from django.views.generic import TemplateView
from django.http import JsonResponse
from adminDash.models import reg_check
from adminDash.models import car_check
from django.views.decorators.csrf import csrf_exempt


def vendorDash(request):
    user_data = reg_check.objects.all()

    username = request.session.get("user_data", "Guest")

    user1 = get_object_or_404(reg_check, name=username)

    context = {
        'userdata': user_data,        
        'currentuser': user1.name,    
        'mobile': user1.cmob,        
        'password': user1.password,  
        'role': user1.role            
    }

    print("***********:request ", username)
    print("Password: ", user1.password)

    return render(request, "vendordash/dash1.html", context)



def add_car(request):
    user_data = reg_check.objects.all()
    
    current_user = request.session.get("user_data", "Guest")
    
    context = {
        'userdata': user_data,
        'currentuser': current_user
    }
    
    print("***********:request ", current_user)
    return render(request,"vendordash/add_car1.html",context)


class managecar_view1(TemplateView):
    template_name = "vendordash/manage_cars1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("***********:request ", self.request.session["user_data"])
        user_data = car_check.objects.all()
        context['userdata'] = user_data
        context["currentuser"] = self.request.session["user_data"]
        return context
    

def logout2(request):
    logout(request)
    return redirect("home")