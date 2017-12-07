from ed.noaa import Param
from proverbs.correspondence import Day2Day


class Serwacy(Day2Day):

    def __repr__(self):
        return u"Dobry w czerwcu Bonifacy, gdy w maju dobry Serwacy"

    def build_filter(self, year):
        return lambda sheet: (sheet[(sheet['DATE'] == '{0}-05-13'.format(year))],
                              sheet[(sheet['DATE'] == '{0}-06-05'.format(year))])

    def process_year(self, place, year):
        ser_p, bon_p = self.get_first_day_data(place, year, Param.PRCP.value), self.get_second_day_data(place, year, Param.PRCP.value)

        if None in [ser_p, bon_p]:
            return None

        return ser_p == bon_p == 0
