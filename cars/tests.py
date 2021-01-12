import json

from cars.models import Car
from cars.serializers import CarsListSerializer
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CarsTestCase(APITestCase):


    def setUp(self):
        Car.objects.create_(make='HONDA', model='Civic')
    
    
    def test_create_car(self):
        data = {
            "model" : "Accord",
            "make" : "HONDA",
    }
        response = self.client.post("/cars/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    
    def test_get_cars(self):        
        response = self.client.get("/cars/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response.data,)
       
        
    
    def test_get_rates(self):
        data = {
            'model' : 'Civic',
            'make' : 'HONDAY',
            'rate' : 3
        }
        response = self.client.post("/rates/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
