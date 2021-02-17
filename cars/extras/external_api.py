import pandas as pd
import requests
import json


class VpicApi:
    api_url = 'https://vpic.nhtsa.dot.gov/api/vehicles/'

    def makes(self):
        try:
            car_makes = requests.get(
                f'{self.api_url}GetAllMakes?format=json')
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        makes_dict = json.loads(car_makes.content)
        return pd.DataFrame(makes_dict['Results'])

    def models(self, make):
        try:
            car_models = requests.get(
                f'{self.api_url}GetModelsForMake/{make}?format=json')
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        car_models_dict = json.loads(car_models.content)
        return pd.DataFrame(car_models_dict['Results'])
