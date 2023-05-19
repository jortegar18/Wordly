
from database.models import CustomUser, Session, Tutor, Student
from rest_framework import viewsets, permissions, generics
from .serializers import TutorSerializer, CustomUserSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

class CustomUserAPI(generics.RetrieveAPIView):
    permissions_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user
    

@api_view(['POST'])
def updatePersonalDataTutor(request):
    if request.user.is_authenticated:
        user_serializer = TutorSerializer(request.user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updatePersonalDataStudent(request):
    if request.user.is_authenticated:
        user_serializer = StudentSerializer(request.user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)

