from django.db import models

class signup_check(models.Model):
    name = models.CharField(max_length=250)
    cmob = models.IntegerField()
    age = models.IntegerField()


class contact_us(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.CharField(max_length=2500)