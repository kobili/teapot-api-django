from django.contrib.auth import get_user_model
from .exceptions import UserNotFoundException


def get_user_by_id(user_id=None):
    """
    Attempts to find an active user with the provided ID
    Raises UserNotFoundException if the user does not exist
    """
    UserModel = get_user_model()
    try:
        return UserModel.objects.get(user_id=user_id, is_active=True)
    except UserModel.DoesNotExist:
        raise UserNotFoundException(user_id)
