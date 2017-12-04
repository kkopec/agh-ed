from ed.noaa import Param
from proverbs.correspondence import Day2Period


class WalentynkiDeszcz(Day2Period):

    def __repr__(self):
        return u'Gdy na święty Walek deszcze, mrozy wrócą jeszcze'

    def build_filter(self, year):
        return lambda sheet: (sheet[(sheet['DATE'] == '{0}-02-14'.format(year))],
                              sheet[(sheet['DATE'] > '{0}-02-21'.format(year)) & (sheet['DATE'] < '{0}-04-01'.format(year))])

    def process_year(self, place, year):
        vd_rain = self.get_day_data(place, year, Param.PRCP.value)

        if sum(vd_rain) == 0:
            return None

        mean_temps = self.get_period_data(place, year)
        below0 = next((t for t in mean_temps if t < 0), None)

        return below0 is not None
