from rest_framework import serializers
from category.serializers import CategorySerializer
from .models import Product, Image


class ImageSerializer(serializers.ModelSerializer):

    presigned_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = [
            "image_id",
            "presigned_url"
        ]

    def get_presigned_url(self, obj):
        # TODO: Fetch presigned urls from here
        return f"This will become a presigned url from s3 for the image {obj.image_id}"


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
        ]


class ReducedProductSerializer(serializers.ModelSerializer):
    """
    The serializer to be used when returning a limited amount of data for a Product
    """
    class Meta:
        model = Product
        fields = [
            'product_id',
            'name',
            'price',
            'seller',
        ]
        read_only_fields = fields


class CreateProductRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    stock = serializers.IntegerField()
    image_count = serializers.IntegerField()
    category_id = serializers.UUIDField()
