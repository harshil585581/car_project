from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login_page", views.login, name="login_page"),
    path("register_page", views.register, name="register_page"),
    path("cdocument", views.cdocument, name="cdocument"),
    path("cprofile", views.cprofile.as_view(), name="cprofile"), 
    path("contact_tb", views.contact_tb.as_view(), name="contact_tb"), 

    path('logout_view', views.logout_view, name='logout_view'),

    path('send_reset_link', views.send_reset_link.as_view(), name='send_reset_link'),

    path('subscribee', views.subscribee, name='subscribee'),  
    
]