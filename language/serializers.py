from rest_framework import serializers
from database.models import CustomUser, Language

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):


    class Meta:
        model = Language
        fields = '__all__'