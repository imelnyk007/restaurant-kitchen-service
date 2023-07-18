from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True)


class Dish(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField(blank=True)
    price = models.FloatField()
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="cooks")

    def __str__(self):
        return self.name
