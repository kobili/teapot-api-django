from rest_framework.exceptions import APIException


class PaymentInfoNotFoundException(APIException):
    status_code = 404
    default_detail = "Could not find payment info"
    default_code = "payment info not found"

    def __init__(self, payment_id=None):
        if payment_id:
            self.detail = f"{self.default_detail} {payment_id}"
        else:
            self.detail = self.default_detail
