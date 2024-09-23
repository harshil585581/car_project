from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_view, name='car_view'),
    path('add-to-cart/<int:car_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path("ex", views.ex, name="ex"),
]