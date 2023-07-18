from django.contrib import admin
from django.contrib.auth.models import Group

from kitchen.models import DishType, Cook, Dish

admin.site.unregister(Group)

admin.site.register(DishType)
admin.site.register(Cook)
admin.site.register(Dish)
