from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet
from .views import DiaryViewSet
from .views import FoodViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'diaries', DiaryViewSet)
router.register(r'foods', FoodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]