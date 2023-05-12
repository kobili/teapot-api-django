from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from .serializers import CategorySerializer
from .models import Category


class CategoryViewSet(GenericViewSet, ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
