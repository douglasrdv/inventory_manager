from django.db import models
from .common.helper import MEASURE_TYPE_CHOICES as mtc


class Recipe(models.Model):  
    name = models.CharField(max_length=60, null=False)
    ingredients = models.ManyToManyField('Ingredient', through='RecipeIngredient')
    cooking_time = models.IntegerField(help_text="minutes")
    measure_type = models.CharField(max_length=2, choices=mtc, blank=False, null=False)
    description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):  
    name = models.CharField(max_length=60, null=False)
    weight = models.DecimalField(max_digits=4, decimal_places=0)
    brand = models.CharField(max_length=15)
    measure_type = models.CharField(max_length=2, choices=mtc, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(blank=False, null=False)

    def __str__(self):
        return f"{self.recipe.name} - {self.ingredient.name} - {self.quantity}"


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=300, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    recipes = models.ManyToManyField("Recipe")

    def __str__(self):
        return self.name


class ProductRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.recipe.name} - {self.product.name} - {self.quantity}"
    

class IngredientInventory(models.Model):  
    name = models.ForeignKey(Ingredient, on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)
    expiration_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.name
    
    def cost_per_unit(self):
        if self.quantity > 0:
            cost_per_unity = self.total_cost / self.quantity
            return cost_per_unity
        else:
            return 0
