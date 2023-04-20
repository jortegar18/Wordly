from rest_framework import serializers
from database.models import Session, CustomUser, Tutor, Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = '__all__'