from rest_framework import routers
from django.urls import path, include
from .views import BankingInfoViewSet


router = routers.DefaultRouter()
router.register(r'users/(?P<user_id>\S+)/banking', BankingInfoViewSet, basename="banking")

urlpatterns = [
    path('', include(router.urls))
]
