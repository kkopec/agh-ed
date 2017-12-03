import numpy as np
from functools import reduce
from ed.noaa import Param
from ed.proverb import Proverb


class Correspondence(Proverb):

    def run(self):
        self.populate_data()
        self.prepare_data()
        self.process_data()
        self.cleanup_results()
        return self.results

    def get_month_data(self, place, year, param=Param.TAVG.value, index=0):
        sheet = self.data[place][year][index]
        return [float(x) for x in list(sheet[(~sheet[param].isin(['-']))][param])]

    def prepare_data(self):
        pass


class Month2Month(Correspondence):
    FIRST_MONTH = None
    SECOND_MONTH = None

    def build_filter(self, year):
        return lambda sheet: (sheet[((sheet['DATE'] >= '{0}-{1:02d}'.format(year, self.FIRST_MONTH)) &
                                     (sheet['DATE'] < '{0}-{1:02d}'.format(year, self.FIRST_MONTH + 1)))],
                              sheet[((sheet['DATE'] >= '{0}-{1:02d}'.format(year, self.SECOND_MONTH)) &
                                     (sheet['DATE'] < '{0}-{1:02d}'.format(year, self.SECOND_MONTH + 1)))])

    def prepare_data(self):
        self.data['mean'] = {}
        for place in self.data_provider.get_places():
            first_month_temps = reduce((lambda x, y: x + y), [self.get_first_month_data(place, y) for y in self.data[place].keys()])
            second_month_temps = reduce((lambda x, y: x + y), [self.get_second_month_data(place, y) for y in self.data[place].keys()])

            self.data['mean'][place] = {
                'first': np.mean(first_month_temps),
                'second': np.mean(second_month_temps)
            }

    def get_first_month_data(self, place, year):
        return self.get_month_data(place, year, index=0)

    def get_second_month_data(self, place, year):
        return self.get_month_data(place, year, index=1)


class Warm2Cold(Month2Month):
    TEMP_DELTA = 1

    def process_year(self, place, year):
        first_month_temps = self.get_first_month_data(place, year)
        second_month_temps = self.get_second_month_data(place, year)

        if len(first_month_temps) == 0 or len(second_month_temps) == 0:
            return None

        first_mean = np.mean(first_month_temps)

        if first_mean < self.data['mean'][place]['first'] + self.TEMP_DELTA:
            return None

        second_mean = np.mean(second_month_temps)

        return second_mean < self.data['mean'][place]['second'] - self.TEMP_DELTA
