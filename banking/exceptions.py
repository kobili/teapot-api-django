from rest_framework.exceptions import APIException


class BankingInfoNotFoundException(APIException):
    status_code = 404
    default_code = "banking info not found"
    default_detail = "Could not find banking info"

    def __init__(self, banking_id: str=None):
        if banking_id:
            self.detail = f"{self.default_detail} {banking_id}"
        else:
            self.detail = self.default_detail
