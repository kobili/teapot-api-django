from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet


router = DefaultRouter()
router.register(r'users/(?P<user_id>\S+)/product', ProductViewSet, basename="product")

urlpatterns = [
    path('', include(router.urls)),
]
