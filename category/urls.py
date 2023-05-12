from rest_framework import routers
from django.urls import path, include
from .views import CategoryViewSet


router = routers.DefaultRouter()
router.register("categories", CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls))
]
