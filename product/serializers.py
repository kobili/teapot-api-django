from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'product_id',
            'name',
            'description',
            'price',
            'stock',
            'category_id',
            'seller',
            'category',
        ]
        read_only_fields = [
            'seller',
            'category',
        ]
        extra_kwargs = {
            'category_id': {'write-only': True},
        }


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
