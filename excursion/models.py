from django.db import models

from resort.models import Resort
from user.models import User


class Excursion(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=800)
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE)
    cost = models.IntegerField()


class ExcursionTour(models.Model)
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, on_delete=models.CASCADE)
    time = models.DateTimeField()
