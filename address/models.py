from uuid import uuid4
from django.db import models
from users.models import AppUser

# Create your models here.
class Address(models.Model):
    address_id = models.UUIDField(primary_key=True, default=uuid4)

    first_name = models.CharField()
    last_name = models.CharField()
    address_line_1 = models.CharField()
    address_line_2 = models.CharField(default="")
    city = models.CharField()
    province = models.CharField()
    postal_code = models.CharField()
    phone_number = models.CharField()

    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="addresses")
