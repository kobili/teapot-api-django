from uuid import uuid4
from django.db import models
from django.conf import settings
from django_cryptography.fields import encrypt

# Create your models here.
class PaymentInfo(models.Model):
    payment_id = models.UUIDField(primary_key=True, default=uuid4)
    card_number = encrypt(models.CharField())
    expiry_date = encrypt(models.CharField())
    card_holder = encrypt(models.CharField())
    app_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payment_methods")
