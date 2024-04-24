from django import forms
from .models import Ingredient

'''class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Nome ", max_length=100)
    weight = forms.IntegerField(label="Peso ", initial=295, max_value="1000000", min_value=1)
    cost = forms.FloatField(label="Custo ", max_value=1000, min_value=0)'''

class ProductForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'weight', 'cost']