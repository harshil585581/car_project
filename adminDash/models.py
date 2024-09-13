from django.db import models

class reg_check(models.Model):
    name = models.CharField(max_length=250)
    cmob = models.IntegerField()
    age = models.IntegerField()
    password = models.CharField(max_length=250, default='')
    role = models.CharField(max_length=250, blank=True)

class car_check(models.Model):
    carName = models.CharField(max_length=250)
    carDesc = models.CharField(max_length=2000)
    carPrice = models.CharField(max_length=250)