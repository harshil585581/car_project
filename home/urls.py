from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login_page", views.login, name="login_page"),
    path("register_page", views.register, name="register_page"),
    path("login_check",views.login_check.as_view(),name="login_check"),

    path("create_signup", views.create_signup.as_view(),name="create_signup"),
    path("signup_view", views.signup_view.as_view(),name="signup_view"),
    path("delete_register", views.delete_register.as_view(),name="delete_register")
]