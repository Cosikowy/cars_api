from rest_framework import serializers
from models import Car, Rate

class CarsCreateSerializer(serializers.Serializer):
    class Meta:
        model = Car    
        fields = ['make', 'model']

class CarsListSerializer(serializers.Serializer):
    class Meta:
        model = Car
        fields = []

class RateSerializer(serializers.Serializer):
    class Meta:
        model = Rate
        fields = ['car', 'rate']

class PupularSerializer(serializers.Serializer):
    class Meta:
        model = Car
        fields = []
