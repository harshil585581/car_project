from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import JsonResponse
from adminDash.models import car_check
from explore_cars.models import Cart

def car_view(request):
    userdata = car_check.objects.all()
    return render(request, 'explore_cars/explorecar.html', {'userdata': userdata})
    

def add_to_cart(request, car_id):
    if request.method == "POST":
        user_id = request.user.id  # or get it from session, etc.
        car = get_object_or_404(car_check, id=car_id)

        # Check if the car already exists in the cart
        cart_item, created = Cart.objects.get_or_create(car=car, user_id=user_id)

        if not created:
            # If the item exists, increment the quantity
            cart_item.quantity += 1
            cart_item.save()

        return redirect('cart')  # Redirect to cart page after adding

def view_cart(request):
    user_id = request.user.id  # or get it from session, etc.
    cart_items = Cart.objects.filter(user_id=user_id).select_related('car')
    
    # Calculate the total price
    total_price = sum(item.car.carPrice * item.quantity for item in cart_items)
    
    # Ensure total_price is a float
    total_price = float(total_price)

    return render(request, 'explore_cars/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def ex(request):
    # return HttpResponse("Hello, world. You're at the loans index.")
    return render(request,"explore_cars/cart.html")