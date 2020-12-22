from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecipeSerializer
from .serializers import DiarySerializer
from .serializers import FoodSerializer
from .serializers import SlideSerializer
from .models import Recipe
from .models import Diary
from .models import Food
from .models import Slide

# Create your views here.

# 食谱视图
class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    def get_queryset(self, username=None):
        queryset = Recipe.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(owner=username)
            return queryset
        else:
            queryset = Recipe.objects.all()
            return queryset


# 食物视图
class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


# 轮播视图
class SlideViewSet(viewsets.ModelViewSet):
    serializer_class = SlideSerializer
    queryset = Slide.objects.all()


# 日记视图
class DiaryViewSet(viewsets.ModelViewSet):
    serializer_class = DiarySerializer
    def get_queryset(self, username=None):
        queryset = Diary.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(owner=username)
            return queryset
        else:
            queryset = Diary.objects.all()
            return queryset
