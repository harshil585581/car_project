from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import JsonResponse
from adminDash.models import car_check,reg_check  
from explore_cars.models import Cart, Enquiry


class car_view(TemplateView):
    template_name = "explore_cars/explorecar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = car_check.objects.all()
        context = {'userdata': user_data}
        return context
# or
# def car_view(request):
#     userdata = car_check.objects.all()
#     return render(request, 'explore_cars/explorecar.html', {'userdata': userdata})
    

def add_to_cart(request, car_id):
    if request.method == "POST":
        user_id = request.user.id  # or get it from session, etc.
        car = get_object_or_404(car_check, id=car_id)

        cart_item, created = Cart.objects.get_or_create(car=car, user_id=user_id)
        if created:
            cart_item.quantity = 1
        cart_item.update_total_price()

        return redirect('view_cart') 



def view_cart(request):
    user_id = request.user.id 
    cart_items = Cart.objects.filter(user_id=user_id).select_related('car')
    
    total_price = sum(item.total_price for item in cart_items)

    item_prices = [{
        'car': item.car,  # This includes car details
        'quantity': item.quantity,
        'total_price': item.total_price
    } for item in cart_items]

    return render(request, 'explore_cars/cart.html', {
        'item_prices': item_prices,
        'total_price': total_price
    })



def ex(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"explore_cars/cart.html")



def enquire(request, car_id):
    if request.method == "POST":
        # Fetch the car from the database based on car_id
        car = get_object_or_404(car_check, id=car_id)
        
        # Get user data from the session (assuming 'user_data' is stored in the session)
        username = request.session.get('user_data')
        current_user = get_object_or_404(reg_check, name=username)

        Enquiry.objects.create(
            car1=car,
            user_name=current_user.name,
            user_phone_number=current_user.cmob,
            car_name=car.carName,  # Save car name
            car_price=car.carPrice  # Save car price
        )
        return redirect('view_cart')