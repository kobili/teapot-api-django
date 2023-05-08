from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import AppUser
from .serializers import AppUserSerializer, RegistrationSerializer


# Create your views here.
class AppUserViewSet(ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def get_queryset(self):
        return self.queryset
    
    def create(self, request):
        # Validate request data
        registration_serializer = RegistrationSerializer(data=request.data)
        registration_serializer.is_valid(raise_exception=True)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
