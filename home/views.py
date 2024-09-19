from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
from adminDash.models import reg_check
from django.contrib.auth import logout
from django.views.generic import TemplateView


def home(request):
    user_data = reg_check.objects.all()
    
    # Get the current user from the session
    current_user = request.session.get("user_data", "Guest")
    
    # Prepare context
    context = {
        'userdata': user_data,
        'currentuser': current_user
    }
    
    # Print the current user (for debugging purposes)
    print("***********:request ", current_user)
    
    # Render the template with the context
    return render(request,"home/home.html", context)

def login(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"home/login.html")

def register(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"home/register.html")

def cprofile(request):
    user_data = reg_check.objects.all()
    
    # Get the current user from the session
    current_user = request.session.get("user_data", "Guest")
    
    # Prepare context
    context = {
        'userdata': user_data,
        'currentuser': current_user
    }
    
    # Print the current user (for debugging purposes)
    print("***********:request ", current_user)
    
    # Render the template with the context
    return render(request,"home/cprofile.html", context)



class cprofile(TemplateView):
    template_name = "home/cprofile.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.session.get("user_data")
        user = reg_check.objects.get(name=username)
        print(user.password)
        context['currentuser'] = user.name
        context['mobile'] = user.cmob
        context['password'] = user.password
        return context



def logout_view(request):
    logout(request)
    return redirect("home")