from functools import reduce
from ed.proverb import Proverb


class KatarzynaNowyRok(Proverb):
    """
    Jak się Katarzyna(25.11) głosi, tak się nowy rok nosi

    Maksymalna różnica średnich temperatur: 2
    Podobne opady
    """
    MAX_TEMP_DIFF=2
    MAX_PRCP_DIFF=1

    def __repr__(self):
        return u"Jak się Katarzyna głosi, tak się nowy rok nosi"

    def build_filter(self, year):
        return lambda sheet: sheet[(sheet['DATE'] == '{0}-11-25'.format(year)) | (sheet['DATE'] == '{0}-01-01'.format(year+1))]

    def process_year(self, place, year):
        sheet = self.data[place][year]

        avg_temps = [float(x) for x in list(sheet[(~sheet['TAVG'].isin(['-']))]['TAVG'])]
        precip    = [float(x) for x in list(sheet[(~sheet['PRCP'].isin(['-']))]['PRCP'])]

        # pair of values needed
        if len(avg_temps) != 2 or len(precip) != 2:
            return None

        diff_temp = self.compare_days(avg_temps)
        diff_prcp = self.compare_days(precip)

        return diff_temp <= self.MAX_TEMP_DIFF and diff_prcp <= self.MAX_PRCP_DIFF

    def compare_days(self, days):
        return reduce((lambda x,y: abs(abs(x)-abs(y))), days)
