from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
from adminDash.models import reg_check
from home.models import contact_us
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings



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

def cdocument(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"home/cdocument.html")



class contact_tb(APIView):
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        mob = request.POST['mob']
        msg = request.POST['msg']
        csr = contact_us()
        csr.name = name
        csr.email = email
        csr.subject = mob
        csr.message = msg
        csr.save()
        # print(username)
        # print(email)
        # print(password)
        # print(utype)
        return JsonResponse({"status": "pass"})


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

from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password

# View to send a reset password link
class send_reset_link(APIView):
    def post(self, request):
        email = request.data.get('email')  
        try:
            # Look up the customer by email
            customer = reg_check.objects.get(email=email)
            reset_link = f"http://127.0.0.1:8000/home/reset_password_confirm/{customer.id}/"

            # Send reset email
            send_mail(
                'Password Reset Request',
                f'Click the link to reset your password: {reset_link}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return JsonResponse({"status": "pass", "message": "Reset link sent"})
        
        except reg_check.DoesNotExist:
            return JsonResponse({"status": "fail", "message": "Email not found"})



from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import json

def subscribee(request):
    if request.method == 'POST':
        try:
            # Parse the JSON request body
            data = json.loads(request.body)

            # Get the email from the request data
            email = data.get('email')
            
            # Check if email is provided
            if not email:
                return JsonResponse({'message': 'Invalid email address.'}, status=400)

            # Send the subscription confirmation email
            send_mail(
                'Subscription Confirmation',
                'Thank you for subscribing to our newsletter.',
                settings.DEFAULT_FROM_EMAIL,  # This should be configured in settings.py
                [email],
                fail_silently=False,
            )
            
            # Return success response
            return JsonResponse({'message': f"Thank you for subscribing, {email}. Check your inbox for confirmation."})

        except json.JSONDecodeError:
            # Handle invalid JSON in the request
            return JsonResponse({'message': 'Invalid request body.'}, status=400)
        
        except Exception as e:
            # Catch any other errors (e.g., email sending failure)
            return JsonResponse({'message': f"An error occurred: {str(e)}"}, status=500)

    # If the request method is not POST, return 405 (Method Not Allowed)
    return HttpResponse(status=405)
