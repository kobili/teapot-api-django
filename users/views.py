from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class HelloWorldViewSet(APIView):

    def get(self, request):
        return Response("hello world")

