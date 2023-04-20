from rest_framework import serializers
from database.models import CustomUser, Tutor, Student
from django.contrib.auth.hashers import make_password, check_password

#CustomUserSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'last_name', 'gender', 'birthday', 'user_type']


# Tutor Serializer
class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tutor
        fields = ['username', 'email', 'name', 'last_name', 'gender', 'birthday', 'description', 'language', 'payment']

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = ['username', 'email', 'name', 'last_name', 'gender', 'birthday', 'language', 'level', 'payment']

# Register Tutor Serializer
class RegisterTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tutor
        fields=['username', 'email', 'name', 'last_name', 'gender', 'birthday', 'description', 'language', 'payment', 'password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        tutor = Tutor.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            description=validated_data['description'],
            birthday=validated_data['birthday'],
            language=validated_data['language'],
            payment=validated_data['payment'],
            user_type="Tutor",
            password=validated_data['password']
        )
        return tutor

class RegisterStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['username', 'email', 'name', 'last_name', 'gender', 'birthday', 'language', 'level', 'payment', 'password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        student = Student.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            birthday=validated_data['birthday'],
            language=validated_data['language'],
            level=validated_data['level'],
            payment=validated_data['payment'],
            user_type="Student",
            password=validated_data['password']
        )
        return student


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = CustomUser.objects.get(email=data['email'])
        check_pw = check_password(data['password'], user.password)
        if check_pw and user.is_active:
            return user 

        raise serializers.ValidationError("Credenciales incorrectas, verifique")