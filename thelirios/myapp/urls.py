from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new-ingredient", views.productRegistration, name="new-ingredient"),
    path("register", views.productRegistration, name="register"),
    path("ingredients-list", views.list_all_ingredients, name="list"),
    path("recipes-list", views.list_all_recipes, name="recipes"),
]
