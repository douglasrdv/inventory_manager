from django import forms
from .models import Ingredient, Recipe

"""class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Nome ", max_length=100)
    weight = forms.IntegerField(label="Peso ", initial=295, max_value="1000000", min_value=1)
    cost = forms.FloatField(label="Custo ", max_value=1000, min_value=0)"""


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

class RecipeUpdateForm(forms.ModelForm):
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
