from rest_framework import serializers
from category.serializers import CategorySerializer
from .models import Product, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "image_id",
        ]


class ProductSerializer(serializers.ModelSerializer):    
    category_id = serializers.UUIDField(write_only=True)
    image_count = serializers.IntegerField(write_only=True)
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
            'category_id',
            'image_count',
            'seller',
            'category',
            'images',
        ]
        read_only_fields = [
            'seller',
            'category',
            'images',
        ]


class ReducedProductSerializer(serializers.ModelSerializer):
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
    image_count = serializers.IntegerField()
    category_id = serializers.UUIDField()
