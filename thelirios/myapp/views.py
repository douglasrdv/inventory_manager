from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.template import loader
from .models import Ingredient
from .forms import ProductForm


def home(request):
    return render(request, "index.html")


def listIngredients(request):
    ingredients = Ingredient.objects.all()
    return render(request, "ingredient_list.html", {"ingredients": ingredients})


def productRegistration(request):

    if request.method == "POST":

        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

    else:
        form = ProductForm()

    return render(request, "ingredient_registration.html", {"form": form})
