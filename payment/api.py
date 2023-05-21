from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Paymenth_Method, CustomUser, Student, Tutor
from payment.serializers import PaymenthSerializer

@api_view(['GET'])
def get_payment(request):
    if request.user.is_authenticated:
        payment = Paymenth_Method.objects.all()
        payment_serializer = PaymenthSerializer(payment, many = True)
        return Response(payment_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_payment_by_user(request):

    if request.user.is_authenticated:
        payment = Paymenth_Method.objects.filter(user = request.user.id)
        payment_serializer = PaymenthSerializer(payment, many = True)
        return Response(payment_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_payment_by_id(request, id):

    if request.user.is_authenticated:
        payment = Paymenth_Method.objects.filter(id = id).first()
        payment_serializer = PaymenthSerializer(payment)
        return Response(payment_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_payment(request):
    if request.user.is_authenticated:
        request.data["user"] = request.user.id
        payment_serializer = PaymenthSerializer(data = request.data)
        if payment_serializer.is_valid():
            payment_serializer.save()
            return Response(payment_serializer.data, status = status.HTTP_200_OK)
        return Response(payment_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_payment(request, id):

    if request.user.is_authenticated:  
        payment = Paymenth_Method.objects.filter(id = id).first()
        payment_serializer = PaymenthSerializer(payment, data = request.data)
        if payment_serializer.is_valid():
            payment_serializer.save()
            return Response(payment_serializer.data, status = status.HTTP_200_OK)
        return Response(payment_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_payment(request, id):

    if request.user.is_authenticated:  
        payment = Paymenth_Method.objects.filter(id = id).first()
        payment.delete()
        return Response({"message":"Sesion eliminada correctamente"}, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)