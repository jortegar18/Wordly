from database.models import CustomUser, Tutor, Student, Language
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name']

class TutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutor
        fields = ['username', 'email', 'name', 'last_name', 'gender', 'birthday', 'description', 'payment','expire_date','ccv', 'password']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name']

