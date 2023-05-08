from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import AppUser
from .serializers import AppUserSerializer, RegistrationSerializer


# Create your views here.
class AppUserViewSet(GenericViewSet, RetrieveModelMixin):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def get_queryset(self):
        return self.queryset
    
    def create(self, request):
        serializer = RegistrationSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        UserModel = get_user_model()

        if UserModel.objects.filter(email=serializer.validated_data.get("email")).exists():
            return Response(
                {"error": "User with email '{}' already exists".format(serializer.validated_data.get("email"))},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = UserModel.objects.create_user(serializer.validated_data.get("email"), serializer.validated_data.get("password"))
        
        user.first_name = serializer.validated_data.get("first_name")
        user.last_name = serializer.validated_data.get("last_name")
        user.phone_number = serializer.validated_data.get("phone_number")
        user.save()

        response = self.serializer_class(user)
        return Response(response.data, status=status.HTTP_201_CREATED)

