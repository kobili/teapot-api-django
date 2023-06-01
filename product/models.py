from uuid import uuid4
from django.db import models
from django.utils.functional import cached_property

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    @cached_property
    def seller(self):
        return {
            "seller_id": self.user.user_id,
            "name": f"{self.user.first_name} {self.user.last_name}",
        }


class Image(models.Model):
    image_id = models.UUIDField(primary_key=True, default=uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
