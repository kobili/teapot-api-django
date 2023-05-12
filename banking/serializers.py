from rest_framework import serializers
from .models import BankingInfo


class BankingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankingInfo
        fields = [
            'banking_id',
            'transit_number',
            'institution_number',
            'account_number',
            'account_holder',
        ]