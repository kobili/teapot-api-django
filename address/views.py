from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Address
from .serializers import AddressSerializer

from utils.fetchers import get_user_by_id
from utils.error_responses import user_not_found_response


# Create your views here.
class AddressViewSet(GenericViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        return self.queryset
    
    def create(self, request, user_id=None):
        user = get_user_by_id(user_id)
        if not user:
            return user_not_found_response(user_id)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        address = self.get_queryset().create(app_user=user, **serializer.validated_data)

        return Response(
            self.serializer_class(address).data,
            status=status.HTTP_201_CREATED,
        )
    
    def retrieve(self, request, user_id=None, pk=None):
        user = get_user_by_id(user_id)
        if not user:
            return user_not_found_response(user_id)

        address = self._get_user_address_by_id(app_user=user, address_id=pk)
        if not address:
            return self._address_not_found_response(pk)
        
        return Response(
            self.serializer_class(address).data,
            status=status.HTTP_200_OK,
        )
    
    def list(self, request, user_id=None):
        user = get_user_by_id(user_id)
        if not user:
            return user_not_found_response(user_id)
        
        addresses = self.get_queryset().filter(app_user=user)

        return Response(
            self.serializer_class(addresses, many=True).data,
            status=status.HTTP_200_OK,
        )
    
    def update(self, request, user_id=None, pk=None):
        user = get_user_by_id(user_id)
        if not user:
            return user_not_found_response(user_id)
        
        address = self._get_user_address_by_id(app_user=user, address_id=pk)
        if not address:
            return self._address_not_found_response(address_id=pk)
        
        serializer = self.serializer_class(address, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
        
    def _get_user_address_by_id(self, app_user=None, address_id=None):
        try:
            return self.queryset.get(app_user=app_user, address_id=address_id)
        except Address.DoesNotExist:
            return None
        
    def _address_not_found_response(self, address_id=None):
        return Response(
            {"error": f"Could not find address {address_id}"},
            status=status.HTTP_404_NOT_FOUND,
        )
