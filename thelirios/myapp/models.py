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
    ingredients = models.ManyToManyField(Ingredient)
    amount_yield = models.FloatField(max_length=6)
    cooking_time = models.IntegerField(help_text="minutes")
    description = models.TextField(max_length=300, blank=True, null=True)
    cost = models.FloatField(max_length=6)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=300, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    recipes = models.ManyToManyField("Recipe")

    def __str__(self):
        return self.name
