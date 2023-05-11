from rest_framework import routers
from django.urls import path, include
from .views import PaymentInfoViewset


router = routers.DefaultRouter()
router.register(r'users/(?P<user_id>\S+)/payment', PaymentInfoViewset, basename="payment")

urlpatterns = [
    path('', include(router.urls))
]
