from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException

from users.utils import get_user_by_id
from category.models import Category
from category.exceptions import CategoryNotFoundException
from category.utils import get_category_by_id

from .models import Product, Image
from .serializers import (
    ImageSerializer,
    ProductSerializer,
    ReducedProductSerializer,
    CreateProductRequestSerializer,
    UpdateProductRequestSerializer,
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
        # TODO: for admins, allow unavailable products to be queried
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
    
    def update(self, request, *args, **kwargs):
        request_serializer = UpdateProductRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        instance: Product = self.get_object()

        # # TODO: See if there's a way to get this update logic into the request serializer
        instance.name = request_serializer.validated_data["name"]
        instance.description = request_serializer.validated_data["description"]
        instance.price = request_serializer.validated_data["price"]
        instance.stock = request_serializer.validated_data["stock"]
        
        new_category = get_category_by_id(request_serializer.validated_data["category_id"])
        instance.category = new_category

        instance.save()

        return Response(
            data=ProductSerializer(instance).data,
            status=status.HTTP_200_OK,
        )
    
    def destroy(self, request, *args, **kwargs):
        instance: Product = self.get_object()
        instance.is_available = False
        instance.save(update_fields=["is_available"])

        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageViewSet(GenericViewSet, RetrieveModelMixin, DestroyModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        
        queryset = self.queryset

        product = Product.objects.filter(product_id=product_id).first()
        if product:
            queryset = queryset.filter(product=product)

        return queryset

    def create(self, *args, **kwargs):
        product_id = kwargs["product_id"]
        product = Product.objects.filter(product_id=product_id).first()

        if not product:
            raise APIException(
                f"Could not find product with id {product_id}",
                code=404,
            )
        
        image = Image.objects.create(product=product)

        return Response(
            data=self.serializer_class(instance=image).data,
            status=status.HTTP_201_CREATED,
        )
