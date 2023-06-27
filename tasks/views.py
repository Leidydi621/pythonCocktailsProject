from django.shortcuts import render, redirect
from .models import Cocktail, Category


# Create your views here.

def list_cocktail(request):
    return render(request,'list_cocktails.html')

def letter_name(request):
    letter = request.POST

    letter= request.POST['letter'].lower()
    return redirect('/cocktails/')
