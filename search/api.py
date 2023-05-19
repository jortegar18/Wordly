from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import CustomUser, Student, Tutor
from search.serializers import TutorSerializer, StudentSerializer

@api_view(['GET'])
def get_tutors(request):
    if request.user.is_authenticated:
        tutors = CustomUser.objects.filter(user_type = "Tutor")
        tutors_serializer = TutorSerializer(tutors, many = True)
        return Response(tutors_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def tutors_by_language(request):
    if request.user.is_authenticated:
        tutors = CustomUser.objects.filter(user_type = "Tutor", languages__name=request.data['name']).distinct()
        tutors_serializer = TutorSerializer(tutors, many = True)
        return Response(tutors_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def students_by_language(request):
    if request.user.is_authenticated:
        students = CustomUser.objects.filter(user_type = "Student", languages__name=request.data['name']).distinct()
        students_serializer = StudentSerializer(students, many = True)
        return Response(students_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)