from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=60, null=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=60, null=False)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    amount_yield = models.FloatField(max_length=6)
    cooking_time = models.IntegerField(max_length=4, help_text="minutes")
    description = models.TextField(max_length=300)
    cost = models.FloatField(max_length=6)

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.recipe.title} - {self.ingredient.name}"
