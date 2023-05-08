from django.contrib.auth import get_user_model


def get_user_by_id(user_id=None):
    UserModel = get_user_model()
    try:
        return UserModel.objects.get(user_id=user_id, is_active=True)
    except UserModel.DoesNotExist:
        return None