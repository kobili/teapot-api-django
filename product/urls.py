from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserProductViewSet, ProductViewSet


router = DefaultRouter()
router.register(r'users/(?P<user_id>\S+)/product', UserProductViewSet, basename="user-product")
router.register(r'product', ProductViewSet, basename="product")

urlpatterns = [
    path('', include(router.urls)),
]
