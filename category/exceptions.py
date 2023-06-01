from rest_framework.exceptions import APIException


class CategoryNotFoundException(APIException):
    status_code = 404
    default_detail = "Could not find category"
    default_code = "category not found"

    def __init__(self, category_id: str = None):
        if category_id:
            self.detail = f"Could not find category with id {category_id}"
        else:
            self.detail = self.default_code
