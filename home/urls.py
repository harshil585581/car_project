from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login_page", views.login, name="login_page"),
    path("register_page", views.register, name="register_page"),
]