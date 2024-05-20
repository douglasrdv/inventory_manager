from django import forms
from .models import Ingredient, Recipe, Product, IngredientToInventory, RecipeToInventory, ProductToInventory
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
            "expiration_days",
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
            "expiration_days"
        ]
        

class IngredientToInventoryForm(forms.ModelForm):
    class Meta:
        model = IngredientToInventory
        fields = [
            'ingredient',
            'quantity',
            'total_cost',
            'expiration_date'
        ]
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'})
        }



class RecipeToInventoryForm(forms.ModelForm):
    class Meta:
        model = RecipeToInventory
        fields = [
            'recipe',
            'quantity',
            'amount_yield',
        ]


class ProductToInventoryForm(forms.ModelForm):
    class Meta:
        model = ProductToInventory
        fields = [
            'product',
            'quantity',
            'total_price',
        ]
