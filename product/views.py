from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework import status

from users.utils import get_user_by_id
from category.models import Category
from category.exceptions import CategoryNotFoundException
from category.utils import get_category_by_id

from .models import Product, Image
from .serializers import (
    ProductSerializer,
    ReducedProductSerializer,
    CreateProductRequestSerializer,
)


class UserProductViewSet(GenericViewSet):
    """
    View set to handle requests from /users/<user_id>/product/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.serializer_class
    
    def create(self, request, user_id: str = None):
        user = get_user_by_id(user_id)

        request_serializer = CreateProductRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        category_id = request_serializer.validated_data.pop("category_id")
        num_images = request_serializer.validated_data.pop("image_count")

        category = Category.objects.filter(category_id=category_id).first()

        if not category:
            raise CategoryNotFoundException(request_serializer.validated_data.get("category_id"))
        
        new_product = Product.objects.create(
            user=user,
            category=category,
            **request_serializer.validated_data,
        )

        for _ in range(0, num_images):
            Image.objects.create(product=new_product)

        response_serializer = ProductSerializer(instance=new_product)

        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)


class ProductViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.filter(is_available=True)

        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)

        category_id = self.request.query_params.get("category")
        if category_id:
            category = get_category_by_id(category_id)
            queryset = queryset.filter(category=category)

        seller_id = self.request.query_params.get("seller")
        if seller_id:
            seller = get_user_by_id(seller_id)
            queryset = queryset.filter(user=seller)

        return queryset
    
    def get_serializer_class(self):
        if self.action == "list":
            return ReducedProductSerializer
        return ProductSerializer
