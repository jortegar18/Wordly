from rest_framework import serializers
from database.models import CustomUser, Tutor, Student, Language
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode


class EmailSerializer(serializers.Serializer):
    """
    Reset Password Email Request Serializer.
    """

    email = serializers.EmailField()

    class Meta:
        fields = ("email",)



class ResetPasswordSerializer(serializers.Serializer):
    """
    Reset Password Serializer.
    """

    password = serializers.CharField(
        write_only=True,
        min_length=1,
    )

    class Meta:
        field = ("password")

    def validate(self, data):
        """
        Verify token and encoded_pk and then set new password.
        """
        password = data.get("password")
        token = self.context.get("kwargs").get("token")
        encoded_pk = self.context.get("kwargs").get("encoded_pk")

        if token is None or encoded_pk is None:
            raise serializers.ValidationError("Missing data.")

        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = CustomUser.objects.get(pk=pk)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("The reset token is invalid")

        user.set_password(password)
        user.save()
        return data


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email','is_verified', 'name', 'last_name', 'gender', 'birthday', 'user_type']


# Tutor Serializer
class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tutor
        fields = ['username', 'email','is_verified', 'name', 'last_name', 'gender', 'birthday', 'description', 'payment','expire_date','ccv', 'password']

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = ['username', 'email', 'is_verified', 'name', 'last_name', 'gender', 'birthday', 'payment','expire_date','ccv', 'password']


        
    
#language Serializer

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name', 'level']

# Register Tutor Serializer
class RegisterTutorSerializer(serializers.ModelSerializer):

    #language = serializers.PrimaryKeyRelatedField(many=True, queryset=True)
    
    class Meta:
        model=Tutor
        fields=['username', 'email','is_verified', 'name', 'last_name', 'gender', 'birthday', 'description', 'payment','expire_date','ccv', 'password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        tutor = Tutor.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            is_verified = False,
            name=validated_data['name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            description=validated_data['description'],
            birthday=validated_data['birthday'],
            payment=validated_data['payment'],
            expire_date=validated_data['expire_date'],
            ccv=validated_data['ccv'],   
            user_type="Tutor",
            password=validated_data['password']
        )
        return tutor

class RegisterStudentSerializer(serializers.ModelSerializer):

    #language = serializers.PrimaryKeyRelatedField(many=True, queryset=True)

    class Meta:
        model=Student
        fields=['username', 'email', 'name','is_verified', 'last_name', 'gender', 'birthday', 'payment','expire_date','ccv', 'password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        student = Student.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            is_verified = False,
            name=validated_data['name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            birthday=validated_data['birthday'],
            payment=validated_data['payment'],
            expire_date=validated_data['expire_date'],
            ccv=validated_data['ccv'],         
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