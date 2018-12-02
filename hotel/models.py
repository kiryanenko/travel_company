from django.db import models

from resort.models import Resort
from user.models import User


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    resort = models.ForeignKey(Resort, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    description = models.TextField(max_length=600)


class Offer(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    FOOD_TYPE_CHOICES = (
        ('breakfast', 'Завтрак'),
        ('breakfast_and_lunch', 'Завтрак и обед'),
        ('breakfast_and_diner', 'Завтрак и ужин'),
        ('all_inclusive', 'Всё включено'),
    )
    food_type = models.CharField(max_length=20, choices=FOOD_TYPE_CHOICES, blank=True)

    people_count = models.SmallIntegerField(default=1)
    cost = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    removed_at = models.DateTimeField(null=True)


class Tour(models.Model):
    users = models.ManyToManyField(User)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    arrival_date = models.DateField()
    departure_date = models.DateField()

    STATUS_CHOICES = (
        ('payment_wait', 'Ожидание оплаты'),
        ('paid', 'Оплачено'),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, blank=True)

    cost = models.IntegerField()
    comment = models.TextField(max_length=200)
