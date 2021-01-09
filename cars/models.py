from django.db import models
from django.db.models.signals import post_save
from django.db.models import Avg


class Car(models.Model):
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    avg_rate = models.FloatField(default=0, null=True)
    rate_count = models.IntegerField(default=0, null=True)

    class Meta:
        unique_together = ('make', 'model')
        ordering = ('-rate_count',)


class Rate(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    model = models.CharField(max_length=64)
    make = models.CharField(max_length=64)
    rate = models.IntegerField(null=True)


def update_rate(sender, instance, created, **kwargs):
    if created:
        car_id = instance.car.id
        average = Rate.objects.filter(
            car_id=car_id).aggregate(Avg('rate'))['rate__avg']
        rate_count = Rate.objects.filter(car_id=car_id).count()
        Car.objects.filter(pk=car_id).update(
            avg_rate=round(average, 4), rate_count=rate_count)


post_save.connect(update_rate, sender=Rate)
