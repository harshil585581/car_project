from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from django.views.generic import TemplateView
from django.http import JsonResponse
from adminDash.models import reg_check
from adminDash.models import car_check
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout


def dash(request):
    user_data = reg_check.objects.all()
    
    # Get the current user from the session
    username = request.session.get("user_data", "Guest")
    
    # Handle case where user might not be found
    user1 = get_object_or_404(reg_check, name=username)
    
    # Prepare context
    context = {
        'userdata': user_data,
        'currentuser': username,  # Use username directly
        'role': user1.role        #gets role of user
    }
    
    # Print the current user (for debugging purposes)
    print("***********:request ", username)
    
    # Render the template with the context
    return render(request, "adminDash/dash.html", context)



def users_table(request):
    return render(request,"adminDash/users_table.html")

def manage_cars(request):
    return render(request,"adminDash/manage_cars.html")

def add_car(request):
    return render(request,"adminDash/add_car.html")

def logout1(request):
    logout(request)
    return redirect("login_page")


class login_check(APIView):
    def post(self,request):
        username = request.POST['username']
        password = request.POST['pass']
        ent = reg_check.objects.filter(name = username, password = password).values()
        if(len(ent) > 0):
            request.session["user_data"]=ent[0]["name"]
            return JsonResponse({"status":"pass", "name": ent[0]["name"], "role": ent[0]["role"]})
        else:
            return JsonResponse({"status":"fail"})

        


class users_tb(APIView):
    def post(self, request):
        name = request.POST['name']
        cmob = request.POST['cmob']
        role = request.POST['role']
        age = request.POST['age']
        password = request.POST['password']
        usr = reg_check()
        usr.name = name
        usr.cmob = cmob
        usr.role = role
        usr.age = age
        usr.password = password
        usr.save()
        # print(username)
        # print(email)
        # print(password)
        # print(utype)
        return JsonResponse({"status": "pass"})


class users_view(TemplateView):
    template_name = "adminDash/users_table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = reg_check.objects.all()
        context = { 'userdata': user_data}
        return context
    
    
@csrf_exempt
def delete_user(request):
    if request.method == 'POST':
        try:
            cmob = request.POST.get('cmob')
            user = reg_check.objects.get(cmob=cmob)
            user.delete()
            return JsonResponse({'status': 'success'})
        except reg_check.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})



@csrf_exempt
def update_user(request):
    if request.method == 'POST':
        old_cmob = request.POST.get('old_cmob')
        new_cmob = request.POST.get('new_cmob')
        name = request.POST.get('name')
        age = request.POST.get('age')
        password = request.POST.get('password')

        try:
            user = reg_check.objects.get(cmob=old_cmob)
            user.name = name
            user.cmob = new_cmob
            user.age = age
            user.password = password
            user.save()        
            return JsonResponse({'status': 'success'})
        except reg_check.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User not found'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})




class car_tb(APIView):
    def post(self, request):
        carName = request.POST['carName']
        carDesc = request.POST['carDesc']
        carPrice = request.POST['carPrice']
        csr = car_check()
        csr.carName = carName
        csr.carDesc = carDesc
        csr.carPrice = carPrice
        csr.save()
        # print(username)
        # print(email)
        # print(password)
        # print(utype)
        return JsonResponse({"status": "pass"})



class managecar_view(TemplateView):
    template_name = "adminDash/manage_cars.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("***********:request ", self.request.session["user_data"])
        user_data = car_check.objects.all()
        context['userdata'] = user_data
        context["currentuser"] = self.request.session["user_data"]
        return context
    

class car_view(TemplateView):
    template_name = "explore_cars/explorecar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = car_check.objects.all()
        context = {'userdata': user_data}
        return context
    
@csrf_exempt
def delete_car(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            car = car_check.objects.get(id=id)
            car.delete()
            return JsonResponse({'status': 'success'})
        except reg_check.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def update_car(request):
    if request.method == "POST":
        car_id = request.POST.get('id')
        car_name = request.POST.get('carName')
        car_desc = request.POST.get('carDesc')
        car_price = request.POST.get('carPrice')

        try:
            car = car_check.objects.get(id=car_id)
            car.carName = car_name
            car.carDesc = car_desc
            car.carPrice = car_price
            car.save()
            return JsonResponse({"status": "success"})
        except car_check.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Car not found"})
    return JsonResponse({"status": "error", "message": "Invalid request"})
