from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=60, null=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name