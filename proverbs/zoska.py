from ed.proverb import Proverb


class ZimnaZoska(Proverb):
    """
    Zimnej Zośki/Zimnych Ogrodników

    12-16 maja temperatura poniżej: 3
    """
    LOW_TEMP = 3

    def __init__(self, data_provider):
        super().__init__(data_provider)

    def __repr__(self):
        return u"Zimnej Zośki/Zimnych Ogrodników"

    def build_filter(self, year):
        return lambda sheet: sheet[(sheet['DATE'] >= '{0}-05-12'.format(year)) & (sheet['DATE'] <= '{0}-05-16'.format(year))]

    def process_year(self, place, year):
        sheet = self.data[place][year]

        min_temps = [float(x) for x in list(sheet[(~sheet['TMIN'].isin(['-']))]['TMIN'])]

        return min(min_temps) < self.LOW_TEMP if len(min_temps) > 0 else None
