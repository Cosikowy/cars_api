from rest_framework import serializers
from .models import Car, Rate


class CarsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'model']


class CarsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('__all__')


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        extra_kwargs = {
            'make': {'required': True, },
            'model': {'required': True, },
            'rate': {'required': True, },
            'car': {'read_only': False, },
        }
        fields = ('__all__')
