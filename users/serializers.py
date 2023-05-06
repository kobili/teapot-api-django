from rest_framework import serializers
# from django.db.models.fields import EmailField, CharField
from .models import AppUser

# TODO: CHANGE THIS TO A NORMAL SERIALIZER FOR VALIDATION

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']

class AppUserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    phone_number = serializers.CharField()
