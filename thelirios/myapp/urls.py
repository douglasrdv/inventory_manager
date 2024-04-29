from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # Ingredients urls
    path("new-ingredient", views.ingredient_registration, name="new-ingredient"),
    path("ingredients-list", views.list_all_ingredients, name="ingredients-list"),
    path("ingredient-delete/<int:id>", views.ingredient_delete, name="ingredient-delete"),
    path("ingredient-update/<int:id>", views.ingredient_update, name="ingredient-update"),
    # Recipes urls
    path("new-recipe", views.recipe_registration, name="new-recipe"),
    path("recipes-list", views.list_all_recipes, name="recipes-list"),
    path("recipe-delete/<int:id>", views.recipe_delete, name="recipe-delete"),
    path("recipe-update/<int:id>", views.recipe_update, name="recipe-update"),
    # Products urls
    path("new-product", views.product_registration, name="new-product"),
    path("products-list", views.list_all_products, name="products-list"),
]
