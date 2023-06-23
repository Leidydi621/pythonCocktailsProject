from rest_framework import serializers
from .models import Cocktail, Category

class CocktailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cocktail
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = '__all__'