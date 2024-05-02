from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from .models import Ingredient, Recipe, Product, RecipeIngredient
from .forms import IngredientForm, RecipeForm, ProductForm


def index(request):
    return render(request, 'index.html')


def list_all_ingredients(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredient_list.html', {'ingredients': ingredients})


def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})


def list_all_products(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def ingredient_registration(request):

    if request.method == 'POST':

        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredients-list')

    else:
        form = IngredientForm()

    return render(request, 'ingredient_registration.html', {'form': form})


def ingredient_delete(request, id):
    ingredient = Ingredient.objects.get(id=id)
    ingredient.delete()

    return redirect('ingredients-list')


def ingredient_update(request, id):
    ingredient = Ingredient.objects.get(id=id)

    if request.method == 'POST':

        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredients-list')

    else:
        form = IngredientForm(instance=ingredient)

    context = {'form': form, 'ingredient': ingredient}
    return render(request, 'ingredient_update.html', context)


def recipe_delete(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return redirect('recipes-list')


def recipe_update(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':

        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes-list')

    else:
        form = RecipeForm(instance=recipe)

    context = {'form': form, 'recipe': recipe}
    return render(request, 'recipe_update.html', context)


def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    IngredientFormset = inlineformset_factory(Recipe, RecipeIngredient, fields=('ingredient', 'quantity'), can_delete=True, extra=1)

    if request.method == 'POST':
        formset = IngredientFormset(request.POST, instance=recipe)
        if formset.is_valid():
            formset.save()

            return redirect('recipes-list')

    formset = IngredientFormset(instance=recipe)

    return render(request, 'recipe_details.html', {'formset' : formset, 'recipe_name': recipe.name})


def recipe_registration(request):

    if request.method == 'POST':

        form = RecipeForm(request.POST)
        if form.is_valid():
            nova_receita = form.save()
            return redirect('recipe-details', recipe_id=nova_receita.id)

    else:
        form = RecipeForm()

    return render(request, 'recipe_registration.html', {'form': form})


def product_registration(request):

    if request.method == 'POST':

        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products-list')

    else:
        form = ProductForm()

    return render(request, 'product_registration.html', {'form': form})


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('products-list')


def product_update(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':

        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products-list')

    else:
        form = ProductForm(instance=product)

    context = {'form': form, 'product': product}
    return render(request, 'product_update.html', context)
