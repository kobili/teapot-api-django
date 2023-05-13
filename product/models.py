from uuid import uuid4
from django.db import models

from teapot_api import settings
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField()
    description = models.CharField()
    price = models.FloatField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
