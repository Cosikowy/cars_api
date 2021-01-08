from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)

class Rate(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rate = models.IntegerField(max_value=5, min_value=1)
