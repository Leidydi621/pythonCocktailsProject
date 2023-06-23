from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.



class ExternalAPI(APIView):
    def getAllCocktail(self, request):
        # Hacer la solicitud GET a la API externa
        response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=')

        # Obtener los datos de la respuesta
        data = response.json()

        # Procesar los datos como desees
        # ...

        return Response(data)

