from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet
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
    
    def create(self, request, user_id):
        UserModel = get_user_model()

        user = UserModel.objects.get(user_id=user_id, is_active=True)
        if not user:
            return Response(
                {"error": "Could not find user {}".format(user_id)},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        address = self.get_queryset().create(**serializer.validated_data)
        address.app_user = user
        address.save()

        return Response(
            serializer.validated_data,
            status=status.HTTP_201_CREATED,
        )
