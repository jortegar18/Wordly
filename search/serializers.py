from database.models import CustomUser, Tutor, Student, Session
from rest_framework import serializers

class TutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutor
        fields = "__all__"

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'