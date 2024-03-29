from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Session, CustomUser, Student, Tutor
from session.serializers import SessionSerializer
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site

@api_view(['GET'])
def get_sessions(request):
    if request.user.is_authenticated:
        sessions = Session.objects.all()
        sessions_serializer = SessionSerializer(sessions, many = True)
        return Response(sessions_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_sessions_by_tutor(request):

    if request.user.is_authenticated:
        sessions = Session.objects.filter(tutor = request.user.id)
        sessions_serializer = SessionSerializer(sessions, many = True)
        return Response(sessions_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_sessions_by_student(request):

    if request.user.is_authenticated:
        sessions = Session.objects.filter(student = request.user.id)
        sessions_serializer = SessionSerializer(sessions, many = True)
        return Response(sessions_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_session_by_id(request, id):

    if request.user.is_authenticated:
        session = Session.objects.filter(id = id).first()
        session_serializer = SessionSerializer(session)
        return Response(session_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_session(request):

    request.data._mutable=True

    if request.user.is_authenticated:
        
        request.data["student"] = request.user.id
        sessions_serializer = SessionSerializer(data = request.data)
        
        if sessions_serializer.is_valid():
            sessions_serializer.save()
            
            '''current_site = 'http://127.0.0.1:8000'
            
            tutor_id = request.data['tutor']
            print(tutor_id)
            email_body = 'Hi ' + CustomUser.objects.filter(id=tutor_id).values_list('username', flat=True) + 'A new session was added'
            to_email = CustomUser.objects.values('email')
            data = {'email_body': email_body, 'to_email': to_email, 'email_subject': 'Verify your email'}
        

            Util.send_email(data)'''

            return Response(sessions_serializer.data, status = status.HTTP_200_OK)
        return Response(sessions_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def update_session(request, id):

    if request.user.is_authenticated:  
        session = Session.objects.filter(id = id).first()
        session_serializer = SessionSerializer(session, data = request.data)
        if session_serializer.is_valid():
            session_serializer.save()
            return Response(session_serializer.data, status = status.HTTP_200_OK)
        return Response(session_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_session(request, id):

    if request.user.is_authenticated:  
        session = Session.objects.filter(id = id).first()
        session.delete()
        return Response({"message":"Sesion eliminada correctamente"}, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getVolunteerRequests(request):
    if request.user.is_authenticated:
        requestV = VolunteerRequest.objects.filter(organization=request.user)
        request_serializer = VolunteerRequestSerializer(requestV, many=True)
        return Response(request_serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_turn(request, id):

    if request.user.is_authenticated:
        volunteer = CustomUser.objects.filter(id=request.user.id).first()
        session = Session.objects.filter(id=id).first()
        turn = Turn(available=request.data['available'], full=request.data['full'], start_time=request.data['start_time'], end_time=request.data['end_time'], session=session)
        turn.save()
        turn_serializer = TurnSerializer(session)
        return Response(turn_serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def insert_volunteer_in_session(request, id):

    if request.user.is_authenticated:
        volunteer = CustomUser.objects.filter(id = request.user.id).first()
        if (volunteer == None):
            return Response({"message": "El id ingresado no corresponde a un usuario validov"}, status = status.HTTP_400_BAD_REQUEST) 
        session = Session.objects.filter(id = id).first()
        session.volunteer.add(request.user.id)
        session.save()
        sessions_serializer = SessionSerializer(session)
        return Response(sessions_serializer.data, status = status.HTTP_200_OK)
    return Response({"message": "Primero debe iniciar sesion"}, status = status.HTTP_400_BAD_REQUEST)
