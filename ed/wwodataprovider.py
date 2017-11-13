from ed.settings import *
import requests


class WWODataProvider:
    def __init__(self):
        self.query_params = {
            'key': WWO_API_KEY,
            'format': 'json',
            'q': 'Krakow,Poland',  # FIXME: hardcoded city
        }
        self.data = {}

    def get_data(self):
        # cache_lookup()
        data = self.fetch_data()

    def fetch_data(self):
        #cache_lookup()
        res = requests.get('http://api.worldweatheronline.com/premium/v1/past-weather.ashx', self.query_params).json()

        return res.get('data').get('weather')

    def set_params(self, params):
        self.query_params.update(params)
