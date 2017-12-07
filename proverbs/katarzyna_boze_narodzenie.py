from proverbs.correspondence import Day2Day


class KatarzynaBozeNarodzenie(Day2Day):

    def __repr__(self):
        return u"Na Katarzyny gęś po wodzie, Boże Narodzenie po lodzie"

    def build_filter(self, year):
        return lambda sheet: (sheet[(sheet['DATE'] == '{0}-11-25'.format(year))],
                              sheet[(sheet['DATE'] == '{0}-12-25'.format(year))])

    def process_year(self, place, year):
        kat, bn = self.get_first_day_data(place, year), self.get_second_day_data(place, year)

        return kat > 0 > bn if kat is not None and bn is not None and kat > 0 else None
