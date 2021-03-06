
# # Create your views here.
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world")


from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken, ReportingEntitySerializer, ReportingEntityAddressSerializer, UserToEntitySerializer
from .models import ReportingEntity, ReportingEntityAddress, UserToEntity
from .permissions import UserEntityPermission

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportingEntityViewSet(viewsets.ModelViewSet):
    permission_classes = [UserEntityPermission] # Custom permission class used
    queryset = ReportingEntity.objects.all().order_by('id')
    serializer_class = ReportingEntitySerializer


class ReportingEntityAddressViewSet(viewsets.ModelViewSet):
    permission_classes = [UserEntityPermission]
    queryset = ReportingEntityAddress.objects.all().order_by('id')
    serializer_class = ReportingEntityAddressSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = UserToEntity.objects.all()
    serializer_class = UserToEntitySerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)