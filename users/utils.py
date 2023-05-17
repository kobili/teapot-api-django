from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from .models import AppUser
from .exceptions import UserNotFoundException


def get_user_by_id(user_id: str=None) -> AppUser | AbstractBaseUser:
    """
    Attempts to find an active user with the provided ID
    Raises UserNotFoundException if the user does not exist
    """
    UserModel = get_user_model()
    try:
        return UserModel.objects.get(user_id=user_id, is_active=True)
    except UserModel.DoesNotExist:
        raise UserNotFoundException(user_id)
