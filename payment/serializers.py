from rest_framework import serializers
from .models import PaymentInfo


class PaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = [
            'payment_id',
            'card_number',
            'expiry_date',
            'cvv',
            'card_holder',
        ]
