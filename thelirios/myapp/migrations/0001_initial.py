# Generated by Django 4.2.11 on 2024-05-07 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('brand', models.CharField(max_length=15)),
                ('measure_type', models.CharField(choices=[('g', 'gramas'), ('ml', 'mililitros'), ('un', 'unidades')], max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('cooking_time', models.IntegerField(help_text='minutes')),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='myapp.RecipeIngredient', to='myapp.ingredient'),
        ),
        migrations.CreateModel(
            name='ProductRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='recipes',
            field=models.ManyToManyField(to='myapp.recipe'),
        ),
    ]
