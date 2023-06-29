from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CocktailSerializer
from .models import Cocktail
from .services import get_username

import requests
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class TaskView(viewsets.ModelViewSet):    
    apiInfo = get_username()
    data = Cocktail(
        id = apiInfo['id'], 
        name = apiInfo['name'], 
        img = apiInfo['img'], 
        categoryName = apiInfo['categoryName'],
        glass = apiInfo['glass'],
        instructions=apiInfo['instructions'],
        ingredients=apiInfo['ingredients'],
        )
    data.save()

    serializer_class = CocktailSerializer
    queryset = Cocktail.objects.all()

  


    

# class MyViews(APIView):
        

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
