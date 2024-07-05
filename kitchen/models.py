from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    size = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField()


class Sushis(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    quantity = models.IntegerField()  # Количество
    consist = models.TextField()  # Состав
    price = models.FloatField()
    image = models.ImageField()

    class Meta:
        verbose_name = 'Суша'
        verbose_name_plural = 'Суши'

class Burger(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_meat = models.BooleanField()
    consist = models.TextField () # Состав
    price = models.FloatField()
    image = models.ImageField()
