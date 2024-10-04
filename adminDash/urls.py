from django.urls import path
from . import views


urlpatterns = [
    path('', views.adminDash, name="adminDash"),
    path("users_table", views.users_table, name="users_table"),

    path("login_check",views.login_check.as_view(),name="login_check"),
    path("logout1",views.logout1,name="logout1"),

    path("users_tb", views.users_tb.as_view(),name="users_tb"),
    path("users_view", views.users_view.as_view(),name="users_view"),
    path("delete_user", views.delete_user,name="delete_user"),
    path("update_user", views.update_user,name="update_user"),

    path("car_tb", views.car_tb.as_view(),name="car_tb"),
    path("managecar_view", views.managecar_view.as_view(),name="managecar_view"),
    
    path("delete_car", views.delete_car,name="delete_car"),
    path("update_car", views.update_car,name="update_car"),

    path('enquire_view/', views.enquire_view.as_view(), name='enquire_view'),

    path('ContactUsView', views.ContactUsView.as_view(), name='ContactUsView'),
    path('delete_contact/', views.delete_contact, name='delete_contact'),
]