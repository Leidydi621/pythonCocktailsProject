from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CocktailSerializer
from .models import Cocktail


# Create your views here.

class TaskView(viewsets.ModelViewSet):
    

    serializer_class = CocktailSerializer
    queryset = Cocktail.objects.all()


# class MyViews(APIView):
        
    # def get(self, request):
    #    response = request.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')
    #    cockData = response.json()

    #    cockData2 = {
    #      'id': str(cockData['idDrink']),
    #      'name': str(cockData['strDrink']),
    #      'instructions': str(cockData['strInstructions']),
    #      'glass': str(cockData['strGlass']),
    #      'img': str(cockData['strDrinkThumb']),
    #    }

    #    data = Cocktail(**cockData2)
    #    category = Category(cockData['category'])
    #    data.save()
    #    category.save()

    #    print(data)

    #    return Response('datos guardados correctamente')
