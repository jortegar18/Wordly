from rest_framework import serializers
from database.models import Session, CustomUser, Work_Experience

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class WorkExperienceSerializer(serializers.ModelSerializer):


    class Meta:
        model = Work_Experience
        fields = '__all__'