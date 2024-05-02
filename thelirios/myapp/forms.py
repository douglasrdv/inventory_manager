from django import forms
from .models import Ingredient, Recipe, Product


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name", "weight", "brand"]


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "name",
            "cooking_time",
            "description",
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "recipes",
        ]
