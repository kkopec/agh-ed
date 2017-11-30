from enum import Enum
import pandas as pd

POSTFIX = "New"


class Place(Enum):
    BALICE  = "Balice"
    LEBA    = "Łeba"
    OKECIE  = "Okecie"
    SIEDLCE = "Siedlce"

    @classmethod
    def all(cls):
        return [place.value for place in cls]


class NoaaDataProvider:
    def __init__(self):
        self.data = None

    def get_places(self):
        return Place.all()

    def fetch_data(self, place=Place.BALICE.value):
        xls = pd.ExcelFile('data/noaa/{0}.xls'.format(place+POSTFIX))
        self.data = xls.parse()
        return list(sorted(set([int(d[:4]) for d in self.data['DATE']])))

    def filter_data(self, filter_clb):
        return filter_clb(self.data)
