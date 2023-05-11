from rest_framework.exceptions import APIException

class UserNotFoundException(APIException):
    status_code = 404
    default_detail = 'Could not find user'
    default_code = 'user not found'

    def __init__(self, user_id=None):
        if user_id:
            self.detail = f"Could not find user {user_id}"
        else:
            self.detail = self.default_detail
