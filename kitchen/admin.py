from django.contrib import admin
from .models import Pizza, Sushis, Burger



@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Sushis)
class SushiAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


