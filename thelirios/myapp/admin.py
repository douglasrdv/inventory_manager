from django.contrib import admin
from .models import (Ingredient,
                    IngredientInventory,
                    IngredientToInventory,
                    IngredientOutOfInventory,
                    Recipe,
                    RecipeInventory,
                    RecipeToInventory,
                    RecipeOutOfInventory,
                    Product,
                    ProductInventory,
                    ProductToInventory,
                    ProductOutOfInventory
                    )


admin.site.register(Ingredient)
admin.site.register(IngredientInventory)
admin.site.register(IngredientToInventory)
admin.site.register(IngredientOutOfInventory)

admin.site.register(Recipe)
admin.site.register(RecipeInventory)
admin.site.register(RecipeToInventory)
admin.site.register(RecipeOutOfInventory)

admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(ProductToInventory)
admin.site.register(ProductOutOfInventory)