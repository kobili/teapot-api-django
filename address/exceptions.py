from rest_framework.exceptions import APIException


class AddressNotFoundException(APIException):
    status_code = 404
    default_detail = "Could not find address"
    default_code = "address not found"

    def __init__(self, address_id=None):
        if address_id:
            self.detail = f"Could not find address {address_id}"
        else:
            self.detail = self.default_code
