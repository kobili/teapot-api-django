from uuid import uuid4
from django.db import models


class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField()
