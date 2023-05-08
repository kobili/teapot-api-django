from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status


def get_user_by_id(user_id=None):
    UserModel = get_user_model()
    try:
        return UserModel.objects.get(user_id=user_id, is_active=True)
    except UserModel.DoesNotExist:
        return None

def user_not_found_response(user_id=None):
    return Response(
        {"error": f"Could not find user {user_id}"},
        status=status.HTTP_404_NOT_FOUND,
    )