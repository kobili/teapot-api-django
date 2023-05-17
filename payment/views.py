from django.contrib.auth.models import AbstractBaseUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import PaymentInfo
from .serializers import PaymentInfoSerializer
from users.utils import get_user_by_id
from .exceptions import PaymentInfoNotFoundException

# Create your views here.
class PaymentInfoViewset(GenericViewSet):
    queryset = PaymentInfo.objects.all()
    serializer_class = PaymentInfoSerializer

    def get_queryset(self):
        return self.queryset

    def create(self, request, user_id: str=None):
        user = get_user_by_id(user_id)
        
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        payment = self.get_queryset().create(app_user=user, **serializer.validated_data)

        return Response(
            self.serializer_class(payment).data,
            status=status.HTTP_201_CREATED,
        )
    
    def update(self, request, user_id: str=None, pk: str=None):
        user = get_user_by_id(user_id)
        
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        payment = self._get_user_payment_by_id(user, pk)
        
        serializer = self.serializer_class(payment, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def destroy(self, request, user_id: str=None, pk: str=None):
        user = get_user_by_id(user_id)
        payment = self._get_user_payment_by_id(user, pk)

        payment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        
    def _get_user_payment_by_id(self, user: AbstractBaseUser, payment_id: str=None):
        try:
            return self.queryset.get(app_user=user, payment_id=payment_id)
        except PaymentInfo.DoesNotExist:
            raise PaymentInfoNotFoundException(payment_id)
