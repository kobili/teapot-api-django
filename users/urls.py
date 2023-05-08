from rest_framework import routers
from .views import AppUserViewSet


router = routers.DefaultRouter()
router.register(r'users', AppUserViewSet, basename='user')

urlpatterns = router.urls
