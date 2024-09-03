from django.db import models

class signup_check(models.Model):
    name = models.CharField(max_length=250)
    cmob = models.IntegerField()
    age = models.IntegerField()