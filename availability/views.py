from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Time_Av
from .serializers import AvailabilitySerializer

@api_view(['GET'])
def get_time_av(request):
    if request.user.is_authenticated:
        time_av = Time_Av.objects.all()
        time_av_serializer = AvailabilitySerializer(time_av, many = True)
        return Response(time_av_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_time_av_by_tutor(request):

    if request.user.is_authenticated:
        time_av = Time_Av.objects.filter(tutor = request.user.id)
        time_av_serializer = AvailabilitySerializer(time_av, many = True)
        return Response(time_av_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

'''@api_view(["GET"])
def get_time_av_by_id(request, id):

    if request.user.is_authenticated:
        time_av = Time_Av.objects.filter(id = id).first()
        time_av_serializer = AvailabilitySerializer(time_av)
        return Response(time_av_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)
'''
@api_view(['POST'])
def insert_time_av(request):
    if request.user.is_authenticated:
        request.data["user"] = request.user.id
        time_av_serializer = AvailabilitySerializer(data = request.data)
        if time_av_serializer.is_valid():
            time_av_serializer.save()
            return Response(time_av_serializer.data, status = status.HTTP_200_OK)
        return Response(time_av_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_time_av(request, id):

    if request.user.is_authenticated:  
        time_av = Time_Av.objects.filter(id = id).first()
        time_av_serializer = AvailabilitySerializer(time_av, data = request.data)
        if time_av_serializer.is_valid():
            time_av_serializer.save()
            return Response(time_av_serializer.data, status = status.HTTP_200_OK)
        return Response(time_av_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_time_av(request, id):

    if request.user.is_authenticated:  
        time_av = Time_Av.objects.filter(id = id).first()
        time_av.delete()
        return Response({"message":"Sesion eliminada correctamente"}, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

