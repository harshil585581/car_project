from django.urls import path
from . import views

urlpatterns = [
    path("", views.explorecars, name="explorecars"),
    path("car_view", views.car_view.as_view(),name="car_view"),
]