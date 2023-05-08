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
        user = get_user_by_id(user_id)
        if not user:
            return user_not_found_response(user_id)
        
        addresses = self.get_queryset().filter(app_user=user)

        return Response(
            self.serializer_class(addresses, many=True).data,
            status=status.HTTP_200_OK,
        )
    
    def update(self, request, user_id=None):
        user = get_user_by_id(user_id)
        if not user:
            return user_not_found_response(user_id)
