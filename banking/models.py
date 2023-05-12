from uuid import uuid4
from django.db import models
from django.utils.functional import cached_property
from django.conf import settings
from django_cryptography.fields import encrypt


class BankingInfo(models.Model):
    banking_id = models.UUIDField(primary_key=True, default=uuid4)
    transit_number = encrypt(models.CharField())
    institution_number = encrypt(models.CharField())
    account_number = encrypt(models.CharField())
    account_holder = encrypt(models.CharField())
    app_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="banking_infos")
