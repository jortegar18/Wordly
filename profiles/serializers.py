from database.models import CustomUser, Tutor, Student, Session
from rest_framework import serializers

class TutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutor
        fields = ['username', 'email', 'name', 'last_name', 'gender', 'birthday', 'description', 'payment','expire_date','ccv', 'password']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'email', 'name', 'last_name', 'gender', 'birthday', 'payment','expire_date','ccv']
 
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'