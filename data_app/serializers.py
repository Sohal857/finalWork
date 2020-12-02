from rest_framework import serializers

from .models import Data

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'temperature', 'relative_humidity', 'barometric_pressure', 'precipitation', 'incoming_solar_radiation', 'outgoing_solar_radiation', 'wind_speed', 'wind_direction', 'photosynthetically_active_radiation', 'captured_sensor_time_date')
