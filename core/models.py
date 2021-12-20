from django.db import models


class Restaurants(models.Model):
    name = models.TextField(default='name')
    type_of_meal = models.TextField(default='type_of_meal')
    crusine = models.TextField(default='crusine')
    mean_prices = models.TextField(default='mean_prices')
    links = models.TextField(default='links')
    description = models.TextField(default='description')
    address = models.TextField(default='address')
    picture = models.TextField(default='picture')
    time = models.TextField(default='time')
    neighborhood = models.TextField(default='neighborhood')
    type_of_restaraunt = models.TextField(default='type_of_restaraunt')

    def __str__(self):
        return self.name
