from database.models import CustomUser, Tutor, Student, Language
from rest_framework import serializers

class TutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name']

