from django.urls import path
from . import views

urlpatterns = [
    path("", views.vendorDash, name="vendorDash"),
    path("add_car", views.add_car, name="add_car"),
    path("managecar_view1", views.managecar_view1.as_view(),name="managecar_view1"),
    path("logout2", views.logout2, name="logout2"),
]