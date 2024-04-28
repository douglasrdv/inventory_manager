from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new-ingredient", views.ingredient_registration, name="new-ingredient"),
    path("ingredients-list", views.list_all_ingredients, name="ingredients-list"),
    path("ingredient-delete/<int:id>", views.ingredient_delete, name="ingredient-delete"),
    path("ingredient-update/<int:id>", views.ingredient_update, name="ingredient-update"),
    path("new-recipe", views.recipe_registration, name="new-recipe"),
    path("recipes-list", views.list_all_recipes, name="recipes-list"),
    path("new-product", views.product_registration, name="new-product"),
    path("products-list", views.list_all_products, name="products-list"),
]
