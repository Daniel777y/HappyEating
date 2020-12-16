from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api import RegisterApi
from .views import UserViewSet, RegisterViewSet


router = DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'registers', RegisterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/register', RegisterApi.as_view()),
]