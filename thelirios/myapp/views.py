from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.template import loader
from .models import Ingredient, Recipe, Product
from .forms import IngredientForm, RecipeForm, ProductForm


def home(request):
    return render(request, "index.html")


def list_all_ingredients(request):
    ingredients = Ingredient.objects.all()
    return render(request, "ingredient_list.html", {"ingredients": ingredients})


def list_all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes})


def list_all_products(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})


def ingredient_registration(request):

    if request.method == "POST":

        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ingredients-list")

    else:
        form = IngredientForm()

    return render(request, "ingredient_registration.html", {"form": form})


def recipe_registration(request):

    if request.method == "POST":

        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipes-list")

    else:
        form = RecipeForm()

    return render(request, "recipe_registration.html", {"form": form})


def product_registration(request):

    if request.method == "POST":

        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products-list")

    else:
        form = ProductForm()

    return render(request, "product_registration.html", {"form": form})
