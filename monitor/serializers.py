from rest_framework import serializers
from .models import Driver,Bus,DrowsinessEvent

class DriverSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Driver
        fields="__all__"

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields="__all__"

class DrowsinessEventSerializer(serializers.ModelSerializer):
    class Meta:
        model=DrowsinessEvent
        fields="__all__"
    def create(self, validated_data):
        event= super().create(validated_data)
        driver=validated_data['driver']
        driver.total_drowsies+=1
        driver.save()
        return event
