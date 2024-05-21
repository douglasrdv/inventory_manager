from django.contrib import admin
from .models import Ingredient, Recipe, Product, IngredientInventory, IngredientToInventory, RecipeInventory, RecipeToInventory, ProductInventory, ProductToInventory


admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Product)
admin.site.register(IngredientInventory)
admin.site.register(IngredientToInventory)
admin.site.register(RecipeInventory)
admin.site.register(RecipeToInventory)
admin.site.register(ProductInventory)
admin.site.register(ProductToInventory)