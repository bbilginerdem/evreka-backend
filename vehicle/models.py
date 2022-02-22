from django.utils import timezone
from django.db import models


class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    plate = models.CharField(max_length=30)

    def __str__(self):
        return str(self.plate)


class NavigationRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str(self.vehicle)
