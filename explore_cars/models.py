from django.db import models

from adminDash.models import car_check 
from home.models import signup_check   


class Cart(models.Model):
    car = models.ForeignKey(car_check, on_delete=models.CASCADE)
    user_id = models.IntegerField(null=True) 
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Update total price method
    def update_total_price(self):
        self.total_price = self.car.carPrice * self.quantity
        self.save()



class Enquiry(models.Model):
    car1 = models.ForeignKey(car_check, on_delete=models.CASCADE)
    enquiry_date = models.DateField(auto_now_add=True)
    user_name = models.CharField(max_length=100)
    user_phone_number = models.CharField(max_length=15)
    car_name = models.CharField(max_length=100)  # New field to store car name
    car_price = models.DecimalField(max_digits=10, decimal_places=2)  # New field to store car price

    def __str__(self):
        return f"{self.user_name} - {self.car_name} - {self.enquiry_date}"
