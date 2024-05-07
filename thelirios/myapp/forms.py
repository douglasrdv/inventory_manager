from django import forms
from .models import Ingredient, Recipe, Product


class IngredientForm(forms.ModelForm):
    MEASURE_TYPE_CHOICES = [
        ("g", "gramas"),
        ("ml", "mililitros"),
        ("un", "unidades"),
    ]

    measure_type = forms.ChoiceField(choices=MEASURE_TYPE_CHOICES, label="Tipo de Medida")

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
        ]
