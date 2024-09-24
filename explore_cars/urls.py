from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_view.as_view(), name='car_view'),
    path('add-to-cart/<int:car_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart', views.view_cart, name='view_cart'),
    path("ex", views.ex, name="ex"),
]