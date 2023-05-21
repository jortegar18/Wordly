from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Language, CustomUser, Student, Tutor
from language.serializers import LanguageSerializer

@api_view(['GET'])
def get_language(request):
    if request.user.is_authenticated:
        language = Language.objects.all()
        language_serializer = LanguageSerializer(language, many = True)
        return Response(language_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_language_by_user(request):

    if request.user.is_authenticated:
        language = Language.objects.filter(user = request.user.id)
        language_serializer = LanguageSerializer(language, many = True)
        return Response(language_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def insert_language(request):
    if request.user.is_authenticated:
        request.data._mutable=True
        request.data["user"] = request.user.id
        language_serializer = LanguageSerializer(data = request.data)
        if language_serializer.is_valid():
            language_serializer.save()
            return Response(language_serializer.data, status = status.HTTP_200_OK)
        return Response(language_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_language(request, id):

    if request.user.is_authenticated:  
        language = Language.objects.filter(id = id).first()
        language_serializer = LanguageSerializer(language, data = request.data)
        if language_serializer.is_valid():
            language_serializer.save()
            return Response(language_serializer.data, status = status.HTTP_200_OK)
        return Response(language_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)



@api_view(["DELETE"])
def delete_language(request, id):

    if request.user.is_authenticated:  
        language = Language.objects.filter(id = id).first()
        language.delete()
        return Response({"message":"Idioma eliminado correctamente"}, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)
