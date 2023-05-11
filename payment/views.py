from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import PaymentInfo
from .serializers import PaymentInfoSerializer
from users.utils import get_user_by_id, user_not_found_response

# Create your views here.
class PaymentInfoViewset(GenericViewSet):
    queryset = PaymentInfo.objects.all()
    serializer_class = PaymentInfoSerializer

    def get_queryset(self):
        return self.queryset

    def create(self, request, user_id=None):
        user = get_user_by_id(user_id)
        if not user:
            return user_not_found_response(user_id)
        
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        payment = self.get_queryset().create(app_user=user, **serializer.validated_data)

        return Response(
            self.serializer_class(payment).data,
            status=status.HTTP_201_CREATED,
        )
    
    def update(self, request, user_id=None, pk=None):
        user = get_user_by_id(user_id)
        if not user:
            return user_not_found_response(user_id)
        
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        try:
            payment = self.queryset.get(app_user=user, payment_id=pk)
        except PaymentInfo.DoesNotExist:
            return Response(
                {"error": f"Could not find payment method {pk}"},
                status=status.HTTP_404_NOT_FOUND,
            )
        
        serializer = self.serializer_class(payment, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
