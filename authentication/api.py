from rest_framework import generics, permissions, status, viewsets, response
from django.conf import settings
from rest_framework.response import Response 
from knox.models import AuthToken
from .serializers import TutorSerializer, RegisterTutorSerializer, RegisterStudentSerializer, LoginSerializer, StudentSerializer, CustomUserSerializer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from database.models import CustomUser   
from . import serializers
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site

class RegisterTutorAPI(generics.GenericAPIView):
    serializer_class = RegisterTutorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tutor = serializer.save()

        current_site = get_current_site(request)
        relativeLink = reverse('email-verify')
        
        absurl = 'http://'+current_site+relativeLink+"?token="+AuthToken.objects.create(tutor)[1]
        email_body = 'Hi ' +tutor.username + 'Use link below to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': tutor.email, 'email_subject': 'Verify your email',}
        

        Util.send_email(data)

        return Response({
            "user": TutorSerializer(tutor, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(tutor)[1]
        }) 


class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass 

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
    
class PasswordReset(generics.GenericAPIView):
    """
    Request for Password Reset Link.
    """

    serializer_class = serializers.EmailSerializer

    def post(self, request):
        """
        Create token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = CustomUser.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
            reset_link = f"https://wordly-zgzi.onrender.com{reset_url}"

            # send the rest_link as mail to the user.

            return response.Response(
                {
                    "message": 
                    f"Your password rest link: {reset_link}"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return response.Response(
                {"message": "User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResetPasswordAPI(generics.GenericAPIView):
    """
    Verify and Reset Password Token View.
    """

    serializer_class = serializers.ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        """
        Verify token & encoded_pk and then reset the password.
        """
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )
