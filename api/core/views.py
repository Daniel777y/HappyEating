from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecipeSerializer
from .serializers import DiarySerializer
from .serializers import FoodSerializer
from .models import Recipe
from .models import Diary
from .models import Food

# Create your views here.
  
class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class DiaryViewSet(viewsets.ModelViewSet):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()
