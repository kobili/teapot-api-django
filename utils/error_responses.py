from rest_framework.response import Response
from rest_framework import status

def user_not_found_response(user_id=None):
    return Response(
        {"error": f"Could not find user {user_id}"},
        status=status.HTTP_404_NOT_FOUND,
    )
