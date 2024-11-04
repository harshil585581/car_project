from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_view.as_view(), name='car_view'),
    path('car/<int:car_id>/', views.car_details, name='car_details'),
    path('add-to-cart/<int:car_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart', views.view_cart, name='view_cart'),
    path("ex", views.ex, name="ex"),
    path('explore_cars/enquire/<int:car_id>/', views.enquire, name='enquire'),
    path('remove_item', views.remove_item, name='remove_item'), 
]