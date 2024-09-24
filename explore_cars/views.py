from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import JsonResponse
from adminDash.models import car_check
from explore_cars.models import Cart


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

        # Check if the car already exists in the cart
        cart_item, created = Cart.objects.get_or_create(car=car, user_id=user_id)

        if not created:
            # If the item exists, increment the quantity
            cart_item.quantity += 1
        
        # Update the total price of the item
        cart_item.update_total_price()

        return redirect('view_cart')  # Redirect to cart page after adding


def view_cart(request):
    user_id = request.user.id  # or get it from session, etc.
    cart_items = Cart.objects.filter(user_id=user_id).select_related('car')
    
    # Calculate the total price from the database
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