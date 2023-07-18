from django.contrib import admin
from django.contrib.auth.models import Group

from kitchen.models import DishType, Cook, Dish

admin.site.unregister(Group)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "dish_type", "price"]


admin.site.register(DishType)
admin.site.register(Cook)
