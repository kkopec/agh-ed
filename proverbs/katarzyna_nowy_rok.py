from ed.noaa import Param
from ed.proverb import Day2Day


class KatarzynaNowyRok(Day2Day):
    MAX_TEMP_DIFF = 2
    MAX_PRCP_DIFF = 1

    def __repr__(self):
        return u"Jak się Katarzyna głosi, tak się nowy rok nosi"

    def build_filter(self, year):
        return lambda sheet: (sheet[(sheet['DATE'] == '{0}-11-25'.format(year))],
                              sheet[(sheet['DATE'] == '{0}-01-01'.format(year+1))])

    def process_year(self, place, year):
        kat_t, nr_t = self.get_first_day_data(place, year), self.get_second_day_data(place, year)
        kat_p, nr_p = self.get_first_day_data(place, year, Param.PRCP.value), self.get_second_day_data(place, year, Param.PRCP.value)

        if None in [kat_t, nr_t, kat_p, nr_p]:
            return None

        diff_temp = self.compare_days(kat_t, nr_t)
        diff_prcp = self.compare_days(kat_p, nr_p)

        return diff_temp <= self.MAX_TEMP_DIFF and diff_prcp <= self.MAX_PRCP_DIFF

    def compare_days(self, day1, day2):
        return abs(abs(day1)-abs(day2))
