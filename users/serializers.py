from rest_framework.serializers import ModelSerializer
from .models import AppUser

class AppUserSerializer(ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']
