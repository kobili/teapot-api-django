from uuid import uuid4
from django.db import models
from django.utils.functional import cached_property
from django.conf import settings
from django_cryptography.fields import encrypt

# Create your models here.
class PaymentInfo(models.Model):
    payment_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    card_number = encrypt(models.CharField())
    expiry_date = encrypt(models.CharField())
    card_holder = encrypt(models.CharField())
    cvv = encrypt(models.CharField())
    app_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payment_methods")

    @cached_property
    def card_ending_digits(self):
        return self.card_number[-4:]
