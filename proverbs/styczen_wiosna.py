import numpy as np
from functools import reduce
from ed.proverb import Proverb


class StyczenWiosna(Proverb):
    """
    Bój się w styczniu wiosny, bo marzec zazdrosny

    łagodna pogoda w styczniu zapowiada mrozy w marcu
    
    średnia temperatura ze stycznia z wielu lat, tak samo z marca 
    i jeśli w konkretnym roku w styczniu jest wyższa niż ogólna 
    to w marcu powinna być niższa niż ogólna
    """
    TEMP_DELTA = 1

    def __init__(self, data_provider):
        super().__init__(data_provider)

    def __repr__(self):
        return u"Bój się w styczniu wiosny, bo marzec zazdrosny"

    def build_filter(self, year):
        return lambda sheet: sheet[((sheet['DATE'] >= '{0}-01'.format(year)) & (sheet['DATE'] < '{0}-02'.format(year))) |
                                   ((sheet['DATE'] >= '{0}-03'.format(year)) & (sheet['DATE'] < '{0}-04'.format(year)))]

    def process_year(self, place, year):
        january_temps = self.get_month_data(place, year, 1)
        march_temps = self.get_month_data(place, year, 3)

        if len(january_temps) == 0 or len(march_temps) == 0:
            return None

        january_mean = np.mean(january_temps)
        
        if january_mean < self.data['mean'][place]['january'] + self.TEMP_DELTA:
            return None

        march_mean = np.mean(march_temps)

        return march_mean < self.data['mean'][place]['march'] - self.TEMP_DELTA

    def run(self):
        self.populate_data()
        self.prepare_data()
        self.process_data()
        self.cleanup_results()
        return self.results
    
    def prepare_data(self):
        self.data['mean'] = {}
        for place in self.data_provider.get_places():            
            january_temps = reduce((lambda x, y: x+y), [self.get_month_data(place, y, 1) for y in self.data[place].keys()])
            march_temps   = reduce((lambda x, y: x+y), [self.get_month_data(place, y, 3) for y in self.data[place].keys()])
            
            self.data['mean'][place] = {
                'january': np.mean(january_temps),
                'march': np.mean(march_temps)
                }

    def get_month_data(self, place, year, month):
        sheet = self.data[place][year]
        return [float(x) for x in list(sheet[((sheet['DATE'] >= '{0}-{1:02d}'.format(year, month)) & (sheet['DATE'] < '{0}-{1:02d}'.format(year, month+1))) &
                                             (~sheet['TAVG'].isin(['-']))]['TAVG'])]
