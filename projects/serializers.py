from rest_framework import serializers
from .models import MyUser, Tutor

'''

class UserRegistrationSerializer(serializers.ModelSerializer):
    #Confirmacion de password en el Registration Request
    #password2 = serializers.CharField(style={'input_type':'password'}, write_only = True)    
    class Meta:        
        model = MyUser
        fields = ['username','name','last_name','email','date_of_birth','genre','password']
        extra_kwargs={
            'password':{'write_only': True}
        }

    #def validate(self, attrs):
        #password = attrs.get('password')
        #password2 = attrs.get('password2')
        #if password != password2:
            #raise serializers.ValidationError('Password and Confirm Password does not match')
        #return attrs
    def create(self, validate_data):
        return MyUser.objects.create_user(**validate_data)
    
  
    
class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = MyUser
        fields = ['username', 'password']
        
class TutorLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    class Meta:
        model = Tutor
        fields = ['username', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'last_name', 'email', 'name']

class TutorProfileSerializer(serializers.Serializer):
    class Meta:
        model = Tutor
        fields = ['id', 'username', 'name', 'last_name', 'email', 'experience', 'languages', 'payment_methods', 'availability' ]

class TutorRegistrationSerializer(UserRegistrationSerializer):
    # Agregamos los campos específicos de Tutor
    experience = serializers.CharField()
    languages = serializers.ListField(child=serializers.CharField())
    payment_methods = serializers.ListField(child=serializers.CharField())
    availability = serializers.CharField()

    class Meta:
        model = Tutor
        fields = UserRegistrationSerializer.Meta.fields + ['experience', 'languages', 'payment_methods', 'availability']
        extra_kwargs={
            'password':{'write_only': True}
        }
        
    def create(self, validate_data):
        # Extraemos los campos específicos de Tutor de validated_data y creamos un nuevo objeto Tutor
        tutor_data = {
            'experience': validate_data.pop('experience'),
            'languages': validate_data.pop('languages'),
            'payment_methods': validate_data.pop('payment_methods'),
            'availability': validate_data.pop('availability')
        }
        return Tutor.objects.create_user(**validate_data)'''
        