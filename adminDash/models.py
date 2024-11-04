from django.db import models

class reg_check(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True,default="")
    cmob = models.IntegerField()
    age = models.IntegerField()
    password = models.CharField(max_length=250, default='')
    role = models.CharField(max_length=250, blank=True)


class car_check(models.Model):
    carName = models.CharField(max_length=250)
    carDesc = models.TextField()  # Use TextField for long descriptions
    carPrice = models.DecimalField(max_digits=10, decimal_places=2)
    carColor = models.CharField(max_length=250, null=True) 
    seatingCapacity = models.IntegerField(default=0)
    milage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    fuelType = models.CharField(max_length=50, null=True)  
    features = models.CharField(max_length=2000, null=True)  # Set null=True for optional fields
    carImage = models.ImageField(upload_to='cars/', null=True, blank=True) 

    def __str__(self):
        return self.carName  # String representation of the model

