from django.urls import path
from .views import list_cocktail, letter_name

urlpatterns = [
    path('', list_cocktail),
    path('letter/', letter_name),
]

