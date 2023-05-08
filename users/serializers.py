from rest_framework import serializers
from .models import AppUser
from address.serializers import AddressSerializer

class AppUserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, required=False)

    class Meta:
        model = AppUser
        fields = ['user_id', 'email', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff', 'addresses']

class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    phone_number = serializers.CharField()

class UpdateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
