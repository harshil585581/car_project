from django.db import models

class reg_check(models.Model):
    name = models.CharField(max_length=250)
    cmob = models.IntegerField()
    age = models.IntegerField()
    password = models.CharField(max_length=250, default='')
    role = models.CharField(max_length=250, blank=True)