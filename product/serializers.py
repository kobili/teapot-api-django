from rest_framework import serializers
from category.serializers import CategorySerializer
from .models import Product, Image


class ImageSerializer(serializers.ModelSerializer):

    put_url = serializers.SerializerMethodField()
    get_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = [
            "image_id",
            "put_url",
            "get_url",
        ]

    def get_put_url(self, obj):
        # TODO: Fetch presigned urls from here
        return f"This will become a PUT presigned url from s3 for the image {obj.image_id}"
    
    def get_get_url(self, obj):
        # TODO: Fetch presigned urls from here
        return f"This will become a GET presigned url from s3 for the image {obj.image_id}"


class ProductSerializer(serializers.ModelSerializer):
    """
    The main serializer for returning all of a Product's details in an API response
    """
    category = CategorySerializer(read_only=True)
    images = ImageSerializer(many=True, read_only=True)

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


class ReducedProductSerializer(serializers.ModelSerializer):
    """
    The serializer to be used when returning a limited amount of data for a Product
    """
    image = ImageSerializer(read_only=True, source='first_image')

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
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    stock = serializers.IntegerField()
    image_count = serializers.IntegerField()
    category_id = serializers.UUIDField()


class UpdateProductRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    stock = serializers.IntegerField()
    new_image_count = serializers.IntegerField()
    deleted_image_ids = serializers.ListField(
        child=serializers.UUIDField(),
        allow_empty=True,
        max_length=5,
    )
    category_id = serializers.UUIDField()
