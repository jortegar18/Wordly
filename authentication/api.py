from rest_framework import generics, permissions
from rest_framework.response import Response 
from knox.models import AuthToken
from .serializers import TutorSerializer, RegisterTutorSerializer, RegisterStudentSerializer, LoginSerializer, StudentSerializer, CustomUserSerializer    

class RegisterTutorAPI(generics.GenericAPIView):
    serializer_class = RegisterTutorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tutor = serializer.save()
        return Response({
            "user": TutorSerializer(tutor, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(tutor)[1]
        }) 

class RegisterStudentAPI(generics.GenericAPIView):
    serializer_class = RegisterStudentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        return Response({
            "user": StudentSerializer(student, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(student)[1]
        }) 

# Login Student API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

#Get Tutor API
class TutorAPI(generics.RetrieveAPIView):
    permissions_classes = [
        permissions.IsAuthenticated,
        ]
    serializer_class = TutorSerializer

    def get_object(self):
        return self.request.user

#Get Student API

class StudentAPI(generics.RetrieveAPIView):
    permissions_classes = [
        permissions.IsAuthenticated,
        ]
    serializer_class = StudentSerializer

    def get_object(self):
        return self.request.user