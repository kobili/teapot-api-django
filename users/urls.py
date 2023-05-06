from django.urls import path
from rest_framework import routers
from .views import HelloWorldViewSet, AppUserViewSet

router = routers.DefaultRouter()
router.register(r'users', AppUserViewSet)

urlpatterns = [
    path('hello_world', HelloWorldViewSet.as_view()),
]

urlpatterns += router.urls
