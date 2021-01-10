from django.db import models
from django.db.models.signals import post_save
from django.db.models import Avg, Count


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
        car_obj = Rate.objects.filter(
            car_id=car_id).aggregate(avg=Avg('rate'),count = Count('*'))
        
        average = car_obj['avg']
        rate_count = car_obj['count']
        Car.objects.filter(pk=car_id).update(
            avg_rate=round(average, 4), rate_count=rate_count)


post_save.connect(update_rate, sender=Rate)
