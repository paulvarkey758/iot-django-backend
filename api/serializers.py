from dataclasses import field
from rest_framework import serializers
from .models import Component,Sensor

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Component
        fields='__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sensor
        fields='__all__'        