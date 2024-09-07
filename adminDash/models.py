from django.db import models

class reg_check(models.Model):
    name = models.CharField(max_length=250)
    cmob = models.IntegerField()
    age = models.IntegerField()