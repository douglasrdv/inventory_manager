from django.contrib import admin
from .models import Ingredient, Recipe, Product


admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Product)
