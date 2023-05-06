from uuid import uuid4

from django.db import models
from django.db.models.fields import UUIDField, CharField, EmailField, BooleanField
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates a user with the given email and password
        """
        if not email:
            raise ValueError("User must have an email address")
        
        if not password:
            raise ValueError("User must have a valid password")
        
        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password
        """
        if not email:
            raise ValueError("User must have an email address")
        
        if not password:
            raise ValueError("User must have a valid password")
        
        user = self.create_user(email, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class AppUser(AbstractUser):
    username = None
    email = EmailField(unique=True)
    user_id = UUIDField(primary_key=True, default=uuid4())
    phone_number = CharField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
