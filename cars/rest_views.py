import json

from rest_framework import mixins, viewsets
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

import pandas as pd
import requests

from .models import Car, Rate
from .serializers import CarsCreateSerializer, CarsListSerializer, RateSerializer, PupularSerializer


class CarsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    queryset = Car.objects.all()

    def get_serializer_class(self,  *args, **kwargs):
        if self.action == 'list':
            return CarsListSerializer
        if self.action == 'create':
            return CarsCreateSerializer

    def list(self, request, *args, **kwargs):

        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        make = request.data['make']
        model = request.data['model']

        car_makes = requests.get(
            'https://vpic.nhtsa.dot.gov/api/vehicles/GetAllMakes?format=json')
        makes_dict = json.loads(car_makes.content)
        makes = pd.DataFrame(makes_dict['Results'])
        if makes['Make_Name'].isin({'Make_name': make}).any():
            return Response(status=400, data={'msg': 'Invalid make', 'data': [make, makes['Make_Name'].head(10)]})

        car_models = requests.get(
            f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json')
        car_models_dict = json.loads(car_models.content)
        models_df = pd.DataFrame(car_models_dict['Results'])
        if models_df['Model_Name'].isin({'Model_Name': model}).any():
            return Response(status=400, data='Wrong model')

        return super().create(request, *args, **kwargs)


class RatesViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    def create(self, request, *args, **kwargs):
        if not 1 <= request.data['rate'] <= 5:
            return Response(status=400, data={'msg': 'Rate must be beetwen 1 and 5'})

        make = request.data['make']
        model = request.data['model']
        cars = Car.objects.filter(
            make__contains=make, model__contains=model).first()
        request.data['car'] = cars.id

        return super().create(request, *args, **kwargs)


class PopularViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Car.objects.all()[0:4]
    serializer_class = PupularSerializer
