from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import MyUser
from django.contrib.auth import authenticate

from .serializers import UserRegistrationSerializer, UserLoginSerializer


# Create your views here.

class UserRegistrationView(APIView):

    queryset = MyUser.objects.all()

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg':'Registration Succesful'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                return Response({'msg':'Login Succesful'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Username or password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)