from rest_framework.serializers import ModelSerializer
from .models import Address

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "first_name",
            "last_name",
            "address_line_1",
            "address_line_2",
            "city",
            "province",
            "postal_code",
            "phone_number",
        ]
