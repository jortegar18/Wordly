from rest_framework import serializers
from database.models import CustomUser, Paymenth_Method

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class PaymenthSerializer(serializers.ModelSerializer):


    class Meta:
        model = Paymenth_Method
        fields = '__all__'