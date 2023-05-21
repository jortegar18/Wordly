from rest_framework import serializers
from database.models import CustomUser, Language


class UserSerializer(serializers.ModelSerializer):

    language = serializers.StringRelatedField(many=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'language']


class LanguageSerializer(serializers.ModelSerializer):
    
    #user = serializers.CharField(source='user.id', read_only=True)

    class Meta:
        model = Language
        fields = '__all__'

