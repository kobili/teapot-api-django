from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import BankingInfo
from .serializers import BankingInfoSerializer
from .exceptions import BankingInfoNotFoundException
from users.utils import get_user_by_id


class BankingInfoViewSet(GenericViewSet):
    queryset = BankingInfo.objects.all()
    serializer_class = BankingInfoSerializer

    def get_queryset(self):
        return self.queryset
    
    def get_serializer_class(self):
        return self.serializer_class
    
    def create(self, request, user_id: str=None):
        user = get_user_by_id(user_id)

        serializer = self.get_serializer_class()(data=request.data)

        serializer.is_valid(raise_exception=True)

        banking_info = self.get_queryset().create(app_user=user, **serializer.validated_data)

        return Response(
            self.get_serializer_class()(banking_info).data,
            status=status.HTTP_201_CREATED,
        )
