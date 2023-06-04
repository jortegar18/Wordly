from database.models import CustomUser, Tutor, Time_Av, Work_Experience, Calification
from rest_framework import serializers

    
class AvailabilitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Time_Av
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work_Experience
        fields = '__all__'

class CalificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calification
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    availability = AvailabilitySerializer(many=True, read_only=True)
    work_exp = WorkExperienceSerializer(many = True, read_only=True)
    calification = CalificationSerializer(many=True, read_only = True)
    

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'name', 'last_name', 'profile_picture','file','video', 'availability', 'work_exp','cost', 'calification']


class TutorSerializer(serializers.HyperlinkedModelSerializer):

    #availability = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Tutor
        fields = ['username', 'email', 'name', 'last_name', 'gender', 'birthday', 'description', 'payment','expire_date','ccv', 'password']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name']

