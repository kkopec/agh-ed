from ed.proverb import Proverb
import numpy as np


class Kwiecien(Proverb):
    """
    Kwiecien plecien...

    dni z temperatura: 15+
    dni z temperatura: <2
    duza zmiennosc srednich temperatur
    jakis snieg?
    """

    def __init__(self, data_provider, data_adapter):
        super().__init__(data_provider, data_adapter)

    def prepare_params(self, year):
        return {
            'date': '{0}-10-01'.format(year),
            'enddate': '{0}-10-30'.format(year)
        }

    def filter_relevant(self, day):
        return {
            'date': self.data_adapter.get_date(day)[-2:],
            'maxTemp': self.data_adapter.get_max_temp(day),
            'minTemp': self.data_adapter.get_min_temp(day),
            'meanTemp': self.data_adapter.get_mean_temp(day),
            'snow': self.data_adapter.get_snow(day)
        }

    def process_data(self):
        # TODO: implement proper processing
        years = list(self.data.keys())
        mean_temps = dict([(k, [x.get('meanTemp') for x in v]) for (k, v) in self.data.items()])
        snow = dict([(k, [x.get('snow') for x in v]) for (k, v) in self.data.items()])
        variances = [np.var(v) for (k, v) in mean_temps.items()]
        stds = [np.std(v) for (k, v) in mean_temps.items()]
        means = [np.mean(v) for (k, v) in mean_temps.items()]
        over15 = [sum([1 for x in v if x > 15]) for (k, v) in mean_temps.items()]
        below2 = [sum([1 for x in v if x < 2]) for (k, v) in mean_temps.items()]
        snow_days = [sum([1 for x in v if x > 0.0]) for (k, v) in snow.items()]

        print('years', years)
        print('over15', over15)
        print('below2', below2)
        print('means', means)
        print('variances', variances)
        print('stds', stds)
        print('snow_days', snow_days)
        return False
