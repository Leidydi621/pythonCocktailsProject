from django.db import models

# Create your models here.
class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    instructions = models.TextField(blank=True)
    glass = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)
    img = models.CharField(max_length=300)
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.name
   
    