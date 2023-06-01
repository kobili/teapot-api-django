from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet

from users.utils import get_user_by_id

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.serializer_class
    
    def create(self, request, user_id: str = None):
        user = get_user_by_id(user_id)

        
