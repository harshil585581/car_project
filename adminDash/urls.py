from django.urls import path
from . import views

urlpatterns = [
    path("", views.dash, name="dash"),
    path("users_table", views.users_table, name="users_table"),
    path("manage_cars", views.manage_cars, name="manage_cars"),

    path("users_tb", views.users_tb.as_view(),name="users_tb"),
    path("users_view", views.users_view.as_view(),name="users_view"),
    path("delete_user", views.delete_user.as_view(),name="delete_user"),

]