from rest_framework import serializers
from database.models import Time_Av

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Time_Av
        fields = ['id', 'user', 'day_of_week', 'start_time', 'end_time']
