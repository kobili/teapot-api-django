from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import AppUser
from .serializers import AppUserSerializer, RegistrationSerializer


# Create your views here.
class AppUserViewSet(ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def get_queryset(self):
        return self.queryset
    
    @action(methods=["post"], detail=False)
    def register(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            UserModel = get_user_model()

            try:
                user = UserModel.objects.create_user(serializer.validated_data.get("email"), serializer.validated_data.get("password"))
            except IntegrityError as err:
                return Response(str(err.__cause__), status=status.HTTP_409_CONFLICT)
            
            user.first_name = serializer.validated_data.get("first_name")
            user.last_name = serializer.validated_data.get("last_name")
            user.phone_number = serializer.validated_data.get("phone_number")
            user.save()

            response = self.serializer_class(user)
            return Response(response.data, status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=True)
    def details(self, request, pk=None):
        serializer = self.serializer_class(self.queryset.get(user_id=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)
