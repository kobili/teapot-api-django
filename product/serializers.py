from rest_framework import serializers
from category.serializers import CategorySerializer
from .models import Product, Image

from .s3_client import get_s3_object, create_s3_object


class GetImageSerializer(serializers.ModelSerializer):
    get_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = [
            "image_id",
            "get_url",
        ]
    
    def get_get_url(self, obj):
        return get_s3_object(str(obj.image_id))


class UpdateImageSerializer(GetImageSerializer):
    put_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = [
            "image_id",
            "put_url",
            "get_url",
        ]

    def get_put_url(self, obj):
        return create_s3_object(str(obj.image_id))


class ProductSerializer(serializers.ModelSerializer):
    """
    The main serializer for returning all of a Product's details in an API response
    """
    category = CategorySerializer(read_only=True)
    images = GetImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'product_id',
            'name',
            'description',
            'price',
            'stock',
            'seller',
            'category',
            'images',
            'is_available',
        ]

class CreateProductSerializer(ProductSerializer):
    """
    The serializer used to serializer create Product responses
    The images array includes PutObject urls
    """
    images = UpdateImageSerializer(many=True, read_only=True)


class ReducedProductSerializer(serializers.ModelSerializer):
    """
    The serializer to be used when returning a limited amount of data for a Product
    """
    image = GetImageSerializer(read_only=True, source='first_image')

    class Meta:
        model = Product
        fields = [
            'product_id',
            'name',
            'price',
            'seller',
            'image',
        ]


class CreateProductRequestSerializer(serializers.Serializer):
    """
    Serializer used to validate Create Product requests
    """
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    stock = serializers.IntegerField()

    # The initial number of images to create
    # the client can update these images as needed
    # If they want to add more they'll have to call the update endpoint to provision more
    image_count = serializers.IntegerField()
    category_id = serializers.UUIDField()


class UpdateProductRequestSerializer(serializers.Serializer):
    """
    Serializer used to validate Update Product requests
    """
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    stock = serializers.IntegerField()

    category_id = serializers.UUIDField()
