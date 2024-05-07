from django.db import models


class Recipe(models.Model):
    MEASURE_TYPE_CHOICES = [
        ("g", "gramas"),
        ("ml", "mililitros"),
        ("un", "unidades"),
    ]

    name = models.CharField(max_length=60, null=False)
    ingredients = models.ManyToManyField('Ingredient', through='RecipeIngredient')
    cooking_time = models.IntegerField(help_text="minutes")
    measure_type = models.CharField(max_length=2, choices=MEASURE_TYPE_CHOICES)
    description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    MEASURE_TYPE_CHOICES = [
        ("g", "gramas"),
        ("ml", "mililitros"),
        ("un", "unidades"),
    ]

    name = models.CharField(max_length=60, null=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    brand = models.CharField(max_length=15)
    measure_type = models.CharField(max_length=2, choices=MEASURE_TYPE_CHOICES)
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
        return f"{self.recipe.name} - {self.ingredient.name} - {self.quantity}"