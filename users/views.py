from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import AppUser
from .serializers import AppUserSerializer, AppUserRegistrationSerializer

# Create your views here.
class HelloWorldViewSet(APIView):

    def get(self, request):
        return Response("hello world")

class AppUserViewSet(ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def get_queryset(self):
        return self.queryset
    
    @action(methods=["post"], detail=False)
    def register(self, request):
        serializer = AppUserRegistrationSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            self.queryset.create(**serializer.validated_data)
            return Response("YES")

        # return Response(request.data)
    
    @action(methods=['get'], detail=True)
    def user(self, request, pk=None):
        serializer = self.serializer_class(self.queryset.get(id=pk))
        return Response(serializer.data)
