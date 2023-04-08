from rest_framework import serializers
from .models import MyUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    #Confirmacion de password en el Registration Request
    #password2 = serializers.CharField(style={'input_type':'password'}, write_only = True)
    class Meta:        
        model = MyUser
        fields = ['username','name','email','date_of_birth','genre','password']
        extra_kwargs={
            'password':{'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('Password and Confirm Password does not match')
        return attrs
    
    def create(self, validate_data):
        return MyUser.objects.create_user(**validate_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = MyUser
        fields = ['username', 'password']