from django.contrib import admin
from .models import Ingredient, Recipe, Product, IngredientInventory


admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Product)
admin.site.register(IngredientInventory)
