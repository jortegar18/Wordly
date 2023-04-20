from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Work_Experience, CustomUser, Student, Tutor
from workexp.serializers import WorkExperienceSerializer

@api_view(['GET'])
def get_workexp(request):
    if request.user.is_authenticated:
        workexp = Work_Experience.objects.all()
        workexp_serializer = WorkExperienceSerializer(workexp, many = True)
        return Response(workexp_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_workexp_by_tutor(request):

    if request.user.is_authenticated:
        workexp = Work_Experience.objects.filter(tutor = request.user.id)
        workexp_serializer = WorkExperienceSerializer(workexp, many = True)
        return Response(workexp_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_workexp_by_id(request, id):

    if request.user.is_authenticated:
        workexp = Work_Experience.objects.filter(id = id).first()
        workexp_serializer = WorkExperienceSerializer(workexp)
        return Response(workexp_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_workexp(request):
    if request.user.is_authenticated:
        request.data["tutor"] = request.user.id
        workexp_serializer = WorkExperienceSerializer(data = request.data)
        if workexp_serializer.is_valid():
            workexp_serializer.save()
            return Response(workexp_serializer.data, status = status.HTTP_200_OK)
        return Response(workexp_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_workexp(request, id):

    if request.user.is_authenticated:  
        workexp = Work_Experience.objects.filter(id = id).first()
        workexp_serializer = WorkExperienceSerializer(workexp, data = request.data)
        if workexp_serializer.is_valid():
            workexp_serializer.save()
            return Response(workexp_serializer.data, status = status.HTTP_200_OK)
        return Response(workexp_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_workexp(request, id):

    if request.user.is_authenticated:  
        workexp = Work_Experience.objects.filter(id = id).first()
        workexp.delete()
        return Response({"message":"Sesion eliminada correctamente"}, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)
