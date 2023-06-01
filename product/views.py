from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from users.utils import get_user_by_id
from category.models import Category
from category.exceptions import CategoryNotFoundException

from .models import Product, Image
from .serializers import ProductSerializer, CreateProductRequestSerializer


class ProductViewSet(GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.serializer_class
    
    def create(self, request, user_id: str = None):
        user = get_user_by_id(user_id)

        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category_id = serializer.validated_data.pop("category_id")
        num_images = serializer.validated_data.pop("image_count")

        category = Category.objects.filter(category_id=category_id).first()

        if not category:
            raise CategoryNotFoundException(serializer.validated_data.get("category_id"))
        
        new_product = Product.objects.create(
            user=user,
            category=category,
            **serializer.validated_data,
        )

        for _ in range(0, num_images):
            Image.objects.create(product=new_product)

        serializer = ProductSerializer(instance=new_product)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
