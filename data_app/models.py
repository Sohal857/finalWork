from django.db import models

# Create your models here.
class Data(models.Model):
    temperature = models.FloatField(db_column='temperature', null=True, blank=True, default=00.00)
    relative_humidity = models.FloatField(db_column='relative_humidity', null=True, blank=True, default=00.00)
    barometric_pressure = models.FloatField(db_column='barometric_pressure', null=True, blank=True, default=00.00)
    precipitation = models.FloatField(db_column='precipitation', null=True, blank=True, default=00.00)
    incoming_solar_radiation = models.FloatField(db_column='incoming_solar_radiation', null=True, blank=True, default=00.00)
    outgoing_solar_radiation = models.FloatField(db_column='outgoing_solar_radiation', null=True, blank=True, default=00.00)
    wind_speed = models.FloatField(db_column='wind_speed', null=True, blank=True, default=00.00)
    wind_direction =  models.CharField(db_column='wind_direction', null=True, max_length=255, blank=True)
    photosynthetically_active_radiation = models.FloatField(db_column='photosynthetically_active_radiation', null=True, blank=True, default=00.00)
    captured_sensor_time_date = models.DateTimeField(db_column='captured_sensor_time_date', null=True)
    class Meta:
        db_table = 'Graph_table'
