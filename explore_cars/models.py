from django.db import models

from adminDash.models import car_check

class Cart(models.Model):
    car = models.ForeignKey(car_check, on_delete=models.CASCADE)
    user_id = models.IntegerField(null=True) 
    quantity = models.PositiveIntegerField(default=1)