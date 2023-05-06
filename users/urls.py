from django.urls import path
from rest_framework import routers
from .views import HelloWorldViewSet

# router = routers.DefaultRouter()
# router.register(r'hello_world', HelloWorldViewSet, basename='hello-world')

urlpatterns = [
    path('hello_world', HelloWorldViewSet.as_view()),
]

# urlpatterns = router.urls
