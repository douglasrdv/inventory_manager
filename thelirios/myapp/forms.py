from django import forms
from .models import Ingredient, Recipe, Product
from .common.helper import MEASURE_TYPE_CHOICES as mtc


class IngredientForm(forms.ModelForm):
    measure_type = forms.ChoiceField(choices=mtc, label="Tipo de Medida")

    class Meta:
        model = Ingredient
        fields = ["name", "weight", "brand", "measure_type",]


class RecipeForm(forms.ModelForm):
    measure_type = forms.ChoiceField(choices=mtc, label="Tipo de Medida")
    
    class Meta:
        model = Recipe
        fields = [
            "name",
            "cooking_time",
            "measure_type",
        ]
            


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
        ]
