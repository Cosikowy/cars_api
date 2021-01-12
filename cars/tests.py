import json

from cars.models import Car
from cars.serializers import CarsListSerializer
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CarsTestCase(APITestCase):

    def setUp(self):
        data = {
            "model": "Civic",
            "make": "HONDA",
        }
        self.client.post("/cars/", data)

    def test_create_car(self):
        data = {
            "model": "Accord",
            "make": "HONDA",
        }
        response = self.client.post("/cars/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_cars(self):
        response = self.client.get("/cars/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_rate(self):
        data = {
            'model': 'Civic',
            'make': 'HONDA',
            'rate': 3
        }
        response = self.client.post("/rates/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_popular(self):
        response = self.client.get("/popular/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLessEqual(len(response.data), 5)
