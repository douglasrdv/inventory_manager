from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new-ingredient", views.productRegistration, name="new-ingredient"),
    path("register", views.productRegistration, name="register"),
    path("list", views.listIngredients, name="list"),
]
