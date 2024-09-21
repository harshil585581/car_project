from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import JsonResponse
from adminDash.models import car_check

def explorecars(request):
    return render(request,"explore_cars/explorecar.html")

class car_view(TemplateView):
    template_name = "explore_cars/explorecar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = car_check.objects.all()
        context = {'userdata': user_data}
        return context