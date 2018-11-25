from django.db import models

from resort.models import Resort


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
