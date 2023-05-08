from rest_framework import routers
from django.urls import path, include
from .views import AddressViewSet


router = routers.DefaultRouter()
router.register(r'users/(?P<user_id>\S+)/address', AddressViewSet, basename="address")

urlpatterns = [
    path('', include(router.urls)),
]
