from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework import status

from .models import Address
from .serializers import AddressSerializer

# Create your views here.
class AddressViewSet(GenericViewSet, RetrieveModelMixin):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        return self.queryset
    
    def create(self, request, user_id=None):
        UserModel = get_user_model()

        user = UserModel.objects.get(user_id=user_id, is_active=True)
        if not user:
            return Response(
                {"error": "Could not find user {}".format(user_id)},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        address = self.get_queryset().create(app_user=user, **serializer.validated_data)

        return Response(
            self.serializer_class(address).data,
            status=status.HTTP_201_CREATED,
        )
    
    def list(self, request, user_id=None):
        UserModel = get_user_model()

        user = UserModel.objects.get(user_id=user_id, is_active=True)
        if not user:
            return Response(
                {"error": "Could not find user {}".format(user_id)},
                status=status.HTTP_404_NOT_FOUND,
            )
        
        addresses = self.get_queryset().filter(app_user=user)

        return Response(
            self.serializer_class(addresses, many=True).data,
            status=status.HTTP_200_OK,
        )
