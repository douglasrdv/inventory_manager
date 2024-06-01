from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.apps import apps
from datetime import date, timedelta
from itertools import chain

from .models import (Ingredient,
                     Recipe,
                     Product,
                     RecipeIngredient,
                     ProductRecipe,
                     IngredientToInventory,
                     RecipeToInventory,
                     ProductToInventory,
                     IngredientOutOfInventory,
                     RecipeOutOfInventory,
                     ProductOutOfInventory,
                     RecipeInventory,
                     IngredientInventory,
                     ProductInventory)

from .forms import (IngredientForm,
                    RecipeForm,
                    ProductForm,
                    IngredientToInventoryForm,
                    RecipeToInventoryForm,
                    ProductToInventoryForm,
                    RemoveProductForm)



def index(request):
    return render(request, 'index.html')


def combine_history(entry, used):
    for item in used:
            item.quantity *= -1
    return sorted(chain(entry,used), key=lambda instance: instance.created_at, reverse=True,)     


def profile(request):
    return render(request, 'profile.html')


def list_all_objects(request, model_name):
    model = apps.get_model('myapp', model_name)
    objects = model.objects.all()
    template_name = f'{model_name.lower()}s_list.html'
    return render(request, template_name, {'objects': objects, 'model_name': model_name})


def remove_products(request):

    if request.method == 'POST':

        form = RemoveProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory-products-list')

    else:
        form = RemoveProductForm()

    return render(request, 'product_sold.html', {'form': form})


def ingredient_registration(request):

    if request.method == 'POST':

        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredients-list')

    else:
        form = IngredientForm()

    return render(request, 'ingredient_registration.html', {'form': form})


def recipe_registration(request):

    if request.method == 'POST':

        form = RecipeForm(request.POST)
        if form.is_valid():
            new_recipe = form.save()
            return redirect('recipe-details', recipe_id=new_recipe.id)

    else:
        form = RecipeForm()

    return render(request, 'recipe_registration.html', {'form': form})


def product_registration(request):

    if request.method == 'POST':

        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.save()
            return redirect('product-details', product_id=new_product.id)

    else:
        form = ProductForm()

    return render(request, 'product_registration.html', {'form': form})


def ingredient_delete(request, id):
    ingredient = Ingredient.objects.get(id=id)
    ingredient.delete()

    return redirect('ingredients-list')


def recipe_delete(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return redirect('recipes-list')


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('products-list')


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


def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    IngredientFormset = inlineformset_factory(Recipe, RecipeIngredient, fields=('ingredient', 'quantity'), can_delete=True, extra=1)

    if request.method == 'POST':
        formset = IngredientFormset(request.POST, instance=recipe)

        if formset.is_valid():

            formset.save()

            return HttpResponseRedirect('%i' %recipe.id)

    formset = IngredientFormset(instance=recipe)

    return render(request, 'recipe_details.html', {'formset' : formset, 'recipe_name': recipe.name})


def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    ProductFormset = inlineformset_factory(Product, ProductRecipe, fields=('recipe', 'quantity'), can_delete=True, extra=1)

    if request.method == 'POST':

        formset = ProductFormset(request.POST, instance=product)
        
        if formset.is_valid():
            formset.save()

            return HttpResponseRedirect('%i' %product.id)

    formset = ProductFormset(instance=product)

    return render(request, 'product_details.html', {'formset' : formset, 'product_name': product.name})


def ingredient_inventory_list(request):
    addedIngredients = IngredientToInventory.objects.all()
    removedIngredients = IngredientOutOfInventory.objects.all()
    for ingredient in removedIngredients:
        ingredient.quantity *= -1
    ingredients = sorted(chain(addedIngredients,removedIngredients), key=lambda instance: instance.created_at, reverse=True,)
    return render(request, 'ingredient_inventory_history.html', {'ingredients': ingredients})


def recipe_inventory_list(request):
    addedRecipes = RecipeToInventory.objects.all()
    removedRecipes = RecipeOutOfInventory.objects.all()
    for recipe in removedRecipes:
        recipe.quantity *= -1
    recipes = sorted(chain(addedRecipes,removedRecipes), key=lambda instance: instance.created_at, reverse=True,)

    return render(request, 'recipe_inventory_history.html', {'recipes': recipes})


def product_inventory_list(request):
    addedProducts = ProductToInventory.objects.all()
    removedProducts = ProductOutOfInventory.objects.all()
    for product in removedProducts:
        product.quantity *= -1
    products = sorted(chain(addedProducts,removedProducts), key=lambda instance: instance.created_at, reverse=True,)

    return render(request, 'product_inventory_history.html', {'products': products})


def add_ingredients_to_inventory(request):

    if request.method == 'POST':

        form = IngredientToInventoryForm(request.POST)
        if form.is_valid():
            new_ingredient_to_inventory = form.save()
            new_ingredient_to_inventory.add_ingredients_to_inventory()
            return redirect('inventory-ingredients-list')

    else:
        form = IngredientToInventoryForm()

    return render(request, 'add_ingredient_to_inventory.html', {'form': form})


def add_recipes_to_inventory(request):

    if request.method == 'POST':

        form = RecipeToInventoryForm(request.POST)
        if form.is_valid():
            new_recipe_to_inventory = form.save(commit=False)
            new_recipe_to_inventory.expiration_date = date.today() + timedelta(days=new_recipe_to_inventory.recipe.expiration_days)
            new_recipe_to_inventory.save()
            #new_recipe_to_inventory.add_recipes_to_inventory()

            recipeIngredients = RecipeIngredient.objects.filter(recipe=new_recipe_to_inventory.recipe)
            for recipeIngredient in recipeIngredients:
                removed_ingredient = recipeIngredient.ingredient
                removed_ingredient_quantity = recipeIngredient.quantity * new_recipe_to_inventory.quantity
                IngredientOutOfInventory.objects.create(ingredient=removed_ingredient, quantity=removed_ingredient_quantity)

            return redirect('inventory-recipes-list')

    else:
        form = RecipeToInventoryForm()

    return render(request, 'add_recipe_to_inventory.html', {'form': form})


def add_products_to_inventory(request):

    if request.method == 'POST':

        form = ProductToInventoryForm(request.POST)
        if form.is_valid():
            new_product_to_inventory = form.save(commit=False)
            new_product_to_inventory.expiration_date = date.today() + timedelta(days=new_product_to_inventory.product.expiration_days)
            new_product_to_inventory.save()
            new_product_to_inventory.add_products_to_inventory()

            productRecipes = ProductRecipe.objects.filter(product=new_product_to_inventory.product)
            for productRecipe in productRecipes:
                removed_ingredient = productRecipe.recipe
                removed_ingredient_quantity = productRecipe.quantity * new_product_to_inventory.quantity
                RecipeOutOfInventory.objects.create(recipe=removed_ingredient, quantity=removed_ingredient_quantity)

            return redirect('inventory-products-list')

    else:
        form = ProductToInventoryForm()

    return render(request, 'add_product_to_inventory.html', {'form': form})


def ingredient_stock(request):
    addedIngredients = IngredientToInventory.objects.all()
    removedIngredients = IngredientOutOfInventory.objects.all()
    for ingredient in removedIngredients:
        ingredient.quantity *= -1
    ingredients = chain(addedIngredients,removedIngredients)
    stockEntry = {}
    for entry in ingredients:
        name = entry.ingredient.name
        if name in stockEntry:
            stockEntry[name] += entry.quantity 
        else:
            stockEntry[name] = entry.quantity

    return render(request, 'ingredient_inventory_stock.html', {'ingredients': stockEntry})


def recipe_stock(request):
    addedRecipes = RecipeToInventory.objects.all()
    removedRecipes = RecipeOutOfInventory.objects.all()
    for recipe in removedRecipes:
        recipe.quantity *= -1
    recipes = chain(addedRecipes,removedRecipes)
    stockEntry = {}
    for entry in recipes:
        name = entry.recipe.name
        if name in stockEntry:
            stockEntry[name] += entry.quantity 
        else:
            stockEntry[name] = entry.quantity

    return render(request, 'recipe_inventory_stock.html', {'recipes': stockEntry})


def product_stock(request):
    addedProducts = ProductToInventory.objects.all()
    removedProducts = ProductOutOfInventory.objects.all()
    for product in removedProducts:
        product.quantity *= -1
    products = chain(addedProducts,removedProducts)
    stockEntry = {}
    for entry in products:
        name = entry.product.name
        if name in stockEntry:
            stockEntry[name] += entry.quantity 
        else:
            stockEntry[name] = entry.quantity


    return render(request, 'product_inventory_stock.html', {'products': stockEntry})
