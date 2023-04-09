from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import MyUser
from django.contrib.auth import authenticate
from django.shortcuts import redirect

from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, TutorRegistrationSerializer, TutorLoginSerializer
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

#Generate Token Manually

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
#Preferencias de Lenguaje. Login required


# Create your views here.


class UserRegistrationView(APIView):
    renderer_class = [UserRenderer]
    

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Registration Succesful'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token, 'msg':'Login Succesful'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Username or password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TutorRegistrationView(APIView):
    def post(self, request):
        serializer = TutorRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TutorLoginView(APIView):
    def post(self, request, format=None):
        serializer = TutorLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            tutor = authenticate(username=username, password=password)
            if tutor is not None and tutor.is_tutor:
                token = get_tokens_for_user(tutor)
                return Response({'token': token, 'msg': 'Login Succesful'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['Username or password is not valid for a tutor']}}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    