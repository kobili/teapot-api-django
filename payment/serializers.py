from rest_framework import serializers
from .models import PaymentInfo


class PaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = [
            'payment_id',
            'card_ending_digits',
            'card_number',
            'expiry_date',
            'cvv',
            'card_holder',
        ]
        read_only_fields = [
            'card_ending_digits',
        ]
        extra_kwargs = {
            'card_number': {'write_only': True},
            'cvv': {'write_only': True},
        }
