# Generated by Django 5.0.6 on 2024-05-22 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_productinventory_total_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredientinventory',
            options={'verbose_name_plural': 'IngredientInventories'},
        ),
        migrations.AlterModelOptions(
            name='ingredienttoinventory',
            options={'verbose_name_plural': 'IngredientToInventories'},
        ),
        migrations.AlterModelOptions(
            name='productinventory',
            options={'verbose_name_plural': 'ProductInventories'},
        ),
        migrations.AlterModelOptions(
            name='producttoinventory',
            options={'verbose_name_plural': 'ProductToInventories'},
        ),
        migrations.AlterModelOptions(
            name='recipeinventory',
            options={'verbose_name_plural': 'RecipeInventories'},
        ),
        migrations.AlterModelOptions(
            name='recipetoinventory',
            options={'verbose_name_plural': 'RecipeToInventories'},
        ),
    ]
