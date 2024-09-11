from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
from adminDash.models import reg_check
from django.views.decorators.csrf import csrf_exempt


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
        password = request.POST['password']
        usr = reg_check()
        usr.name = name
        usr.cmob = cmob
        usr.age = age
        usr.password = password
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

        try:
            user = reg_check.objects.get(cmob=old_cmob)
            # Update the user details
            user.cmob = new_cmob
            user.name = name
            user.age = age
            user.save()
            return JsonResponse({'status': 'success'})
        except reg_check.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
