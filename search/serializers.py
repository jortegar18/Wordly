from database.models import CustomUser, Tutor, Time_Av
from rest_framework import serializers

    
class AvailabilitySerializer(serializers.ModelSerializer):
    
    

    class Meta:
        model = Time_Av
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    availability = AvailabilitySerializer(many=True, read_only=True)
    

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'name', 'last_name', 'availability', 'cost', 'calification']


class TutorSerializer(serializers.HyperlinkedModelSerializer):

    #availability = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Tutor
        fields = ['username', 'email', 'name', 'last_name', 'gender', 'birthday', 'description', 'payment','expire_date','ccv', 'password']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name']

