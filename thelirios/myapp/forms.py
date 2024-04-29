from django import forms
from .models import Ingredient, Recipe, Product


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        print(model)
        fields = ["name", "weight", "cost"]


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "ingredients",
            "amount_yield",
            "cooking_time",
            "description",
            "cost",
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
