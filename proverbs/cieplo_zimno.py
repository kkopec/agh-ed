import numpy as np
from functools import reduce
from ed.proverb import Proverb


class CieploZimno(Proverb):
    TEMP_DELTA = 1
    month_warm = None
    month_cold = None

    def __init__(self, data_provider):
        super().__init__(data_provider)

    def build_filter(self, year):
        return lambda sheet: sheet[
            ((sheet['DATE'] >= '{0}-{1:02d}'.format(year, self.month_warm)) & (sheet['DATE'] < '{0}-{1:02d}'.format(year, self.month_warm+1))) |
            ((sheet['DATE'] >= '{0}-{1:02d}'.format(year, self.month_cold)) & (sheet['DATE'] < '{0}-{1:02d}'.format(year, self.month_cold+1)))]

    def process_year(self, place, year):
        warm_month_temps = self.get_month_data(place, year, self.month_warm)
        cold_month_temps = self.get_month_data(place, year, self.month_cold)

        if len(warm_month_temps) == 0 or len(cold_month_temps) == 0:
            return None

        january_mean = np.mean(warm_month_temps)

        if january_mean < self.data['mean'][place]['warm'] + self.TEMP_DELTA:
            return None

        march_mean = np.mean(cold_month_temps)

        return march_mean < self.data['mean'][place]['cold'] - self.TEMP_DELTA

    def run(self):
        self.populate_data()
        self.prepare_data()
        self.process_data()
        self.cleanup_results()
        return self.results

    def prepare_data(self):
        self.data['mean'] = {}
        for place in self.data_provider.get_places():
            warm_month_temps = reduce((lambda x, y: x + y), [self.get_month_data(place, y, self.month_warm) for y in self.data[place].keys()])
            cold_month_temps = reduce((lambda x, y: x + y), [self.get_month_data(place, y, self.month_cold) for y in self.data[place].keys()])

            self.data['mean'][place] = {
                'warm': np.mean(warm_month_temps),
                'cold': np.mean(cold_month_temps)
            }

    def get_month_data(self, place, year, month):
        sheet = self.data[place][year]
        return [float(x) for x in list(sheet[((sheet['DATE'] >= '{0}-{1:02d}'.format(year, month)) & (
                sheet['DATE'] < '{0}-{1:02d}'.format(year, month + 1))) &
                                             (~sheet['TAVG'].isin(['-']))]['TAVG'])]


class StyczenWiosna(CieploZimno):
    """
    Bój się w styczniu wiosny, bo marzec zazdrosny

    łagodna pogoda w styczniu zapowiada mrozy w marcu
    
    średnia temperatura ze stycznia z wielu lat, tak samo z marca 
    i jeśli w konkretnym roku w styczniu jest wyższa niż ogólna 
    to w marcu powinna być niższa niż ogólna
    """
    month_warm = 1
    month_cold = 3

    def __repr__(self):
        return u"Bój się w styczniu wiosny, bo marzec zazdrosny"


class LutyCieply(CieploZimno):
    """
    Gdy ciepło w lutym, zimno w marcu bywa, długo potrwa zima, rzecz to niewątpliwa
    """
    month_warm = 2
    month_cold = 3

    def __repr__(self):
        return u"Gdy ciepło w lutym, zimno w marcu bywa, długo potrwa zima, rzecz to niewątpliwa"
