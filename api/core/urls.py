from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet
from .views import SlideViewSet
from .views import DiaryViewSet
from .views import FoodViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='Recipe')
router.register(r'diaries', DiaryViewSet, basename='Diary')
router.register(r'foods', FoodViewSet)
router.register(r'slides', SlideViewSet)

urlpatterns = [
    path('', include(router.urls)),
]