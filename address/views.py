from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework import status

from .models import Address
from .serializers import AddressSerializer

# Create your views here.
class AddressViewSet(GenericViewSet):
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
    
    def retrieve(self, request, user_id=None, pk=None):

        user = self._get_user(user_id=user_id)
        if not user:
            return Response(
                {"error": f"Could not find user {user_id}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        
        try:
            address = self.queryset.get(app_user=user, address_id=pk)
        except Address.DoesNotExist:
            return Response(
                {"error": "Could not find address with id {}".format(pk)},
                status=status.HTTP_404_NOT_FOUND,
            )
        
        return Response(
            self.serializer_class(address).data,
            status=status.HTTP_200_OK,
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
    
    def _get_user(self, user_id=None):
        UserModel = get_user_model()

        try:
            return UserModel.objects.get(user_id=user_id, is_active=True)
        except UserModel.DoesNotExist:
            return None
