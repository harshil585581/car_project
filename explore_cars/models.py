from django.db import models

from adminDash.models import car_check

class Cart(models.Model):
    car = models.ForeignKey(car_check, on_delete=models.CASCADE)
    user_id = models.IntegerField(null=True) 
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Update total price method
    def update_total_price(self):
        self.total_price = self.car.carPrice * self.quantity
        self.save()