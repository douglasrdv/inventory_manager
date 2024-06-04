from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    # Ingredients urls
    path('new-ingredient/', object_registration, {
        'model_name': 'Ingredient',
        'form_class': IngredientForm,
        'success_url_name': 'ingredients-list'
    }, name='new-ingredient'),

    path('ingredients-list/', list_all_objects, {'model_name': 'Ingredient'}, name='ingredients-list'),
    path('ingredient-delete/<int:id>/', ingredient_delete, name='ingredient-delete'),
    path('ingredient-update/<int:id>/', ingredient_update, name='ingredient-update'),
    path('inventory/ingredients-list/', ingredient_inventory_list, name='inventory-ingredients-list'),
    path('inventory/add-ingredients/', add_ingredients_to_inventory, name='add-ingredients'),
    path('inventory/ingredients-stock/', ingredient_stock, name='ingredients-stock'),

    # Recipes urls
    path('new-recipe/', object_registration, {
        'model_name': 'Recipe',  
        'form_class': RecipeForm,  
        'success_url_name': 'recipes-list',
        'detail_url_name': 'recipe-details'
    }, name='new-recipe'),

    path('recipes-list/', list_all_objects, {'model_name': 'Recipe'}, name='recipes-list'),
    path('recipe-delete/<int:id>', recipe_delete, name='recipe-delete'),
    path('recipe-update/<int:id>/', recipe_update, name='recipe-update'),
    path('recipe/<recipe_id>/', recipe_details, name='recipe-details'),
    path('inventory/recipes-list/', recipe_inventory_list, name='inventory-recipes-list'),
    path('inventory/add-recipes/', add_recipes_to_inventory, name='add-recipes'),
    path('inventory/recipes-stock/', recipe_stock, name='recipes-stock'),   

    # Products urls
    path('new-product/', object_registration, {
        'model_name': 'Product',
        'form_class': ProductForm,
        'success_url_name': 'products-list',
        'detail_url_name': 'product-details'
    }, name='new-product'),

    path('products-list/', list_all_objects, {'model_name': 'Product'}, name='products-list'),
    path('product-delete/<int:id>/', product_delete, name='product-delete'),
    path('product-update/<int:id>/', product_update, name='product-update'),
    path('product/<product_id>/', product_details, name='product-details'),
    path('inventory/products-list/', product_inventory_list, name='inventory-products-list'),
    path('inventory/add-products', add_products_to_inventory, name='add-products'),
    path('inventory/sold-products', remove_products, name='remove-products'),
    path('inventory/products-stock/', product_stock, name='products-stock'),  
]
