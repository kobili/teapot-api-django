from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from .models import AppUser
from .serializers import AppUserSerializer, RegistrationSerializer, UpdateUserSerializer


# Create your views here.
class AppUserViewSet(GenericViewSet, RetrieveModelMixin):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def get_queryset(self):
        return self.queryset
    
    # POST users/
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

    # PUT users/{user_id}/
    def update(self, request, pk=None):
        serializer = UpdateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.queryset.get(user_id=pk)

        if not user:
            return Response(
                {"error": "Could not find user {}".format(pk)},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if self.queryset.filter(email=serializer.validated_data.get("email")).exists():
            return Response(
                {"error": "User with email '{}' already exists".format(serializer.validated_data.get("email"))},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user.email = serializer.validated_data.get("email")
        user.first_name = serializer.validated_data.get("first_name")
        user.last_name = serializer.validated_data.get("last_name")
        user.phone_number = serializer.validated_data.get("phone_number")
        user.save()

        response = self.serializer_class(user)
        return Response(response.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        user = self.queryset.get(user_id=pk)

        if not user:
            return Response(
                {"error": "Could not find user {}".format(pk)},
                status=status.HTTP_404_NOT_FOUND
            )
        
        user.is_active = False
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=["PUT"], detail=True)
    def restore(self, request, pk=None):
        user = self.queryset.get(user_id=pk)

        if not user:
            return Response(
                {"error": "Could not find user {}".format(pk)},
                status=status.HTTP_404_NOT_FOUND
            )
        
        user.is_active = True
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
