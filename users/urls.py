from rest_framework import routers
from django.urls import path, include
from .views import AppUserViewSet
from .authtoken import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'users', AppUserViewSet, basename='user')

urlpatterns = [
    path('signin/', obtain_auth_token),
    path('', include(router.urls))
]
