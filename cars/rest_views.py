import json

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from django.http.request import QueryDict

import pandas as pd
import requests

from .models import Car, Rate
from .serializers import CarsCreateSerializer, CarsListSerializer, RateSerializer
from .extras.external_api import VpicApi


class CarsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    queryset = Car.objects.all()

    def get_serializer_class(self,  *args, **kwargs):
        if self.action == 'list':
            return CarsListSerializer
        if self.action == 'create':
            return CarsCreateSerializer

    def create(self, request, *args, **kwargs):
        make = request.data['make']
        model = request.data['model']

        makes = VpicApi.make()
        if makes['Make_Name'].isin({'Make_name': make}).any():
            return Response(status=400, data={'msg': 'Invalid make', 'data': [make, makes['Make_Name'].head(10)]})

        models_df = VpicApi.models(make)
        if models_df['Model_Name'].isin({'Model_Name': model}).any():
            return Response(status=400, data='Wrong model')

        return super().create(request, *args, **kwargs)


class RatesViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    def create(self, request, *args, **kwargs):

        make = request.data['make']
        model = request.data['model']
        cars = Car.objects.get(
            make__contains=make, model__contains=model)
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
            request.data['car'] = cars.id
            request.data._mutable = False
        else:
            request.data['car'] = cars.id
        return super().create(request, *args, **kwargs)


class PopularViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Car.objects.all()[:4]
    serializer_class = CarsListSerializer
