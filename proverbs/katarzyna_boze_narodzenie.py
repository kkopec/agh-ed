from ed.proverb import Proverb


class KatarzynaBozeNarodzenie(Proverb):
    """
    Na Katarzyny gęś po wodzie Boże Narodzenie po lodzie

    temperatura > 0 w 25.11 to 25.12 temperatura < 0
    """

    def __init__(self, data_provider):
        super().__init__(data_provider)

    def __repr__(self):
        return u"Na Katarzyny gęś po wodzie, Boże Narodzenie po lodzie"

    def build_filter(self, year):
        return lambda sheet: sheet[(sheet['DATE'] == '{0}-11-25'.format(year)) | (sheet['DATE'] == '{0}-12-25'.format(year))]

    def process_year(self, place, year):
        sheet = self.data[place][year]

        avg_temps = [float(x) for x in list(sheet[(~sheet['TAVG'].isin(['-']))]['TAVG'])]

        if len(avg_temps) != 2:
            return None

        kat, bn = avg_temps

        return kat > 0 > bn if kat > 0 else None

