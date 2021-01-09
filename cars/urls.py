from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import rest_views

app_name = 'cars'


# https://vpic.nhtsa.dot.gov/api/  api
# /vehicles/GetAllMakes?format=csv ALL makes
# /vehicles/GetModelsForMake/honda?format=json - models for makes

router = DefaultRouter()
router.register('cars', rest_views.CarsViewSet, basename='cars')
router.register('rates', rest_views.RatesViewSet, basename='rates')
router.register('popular', rest_views.PopularViewSet, basename='popular')

urlpatterns = [
    path("", include(router.urls)),
    ]
