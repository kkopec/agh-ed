from ed.proverb import Proverb


class Kwiecien(Proverb):
    """
    Kwiecien plecien...

    dni z temperatura: >17
    dni z temperatura: <2
    duza zmiennosc srednich temperatur?
    jakis snieg?
    """
    MIN_TEMP = 2
    MAX_TEMP = 17
    DAYS_THRESHOLD = 5

    def __init__(self, data_provider):
        super().__init__(data_provider)

    def __repr__(self):
        return u"Kwiecień plecień, bo przeplata trochę zimy trochę lata"

    def build_filter(self, year):
        return lambda sheet: sheet[(sheet['DATE'] >= '{0}-04'.format(year)) & (sheet['DATE'] < '{0}-05'.format(year))]

    def process_year(self, place, year):
        sheet = self.data[place][year]

        # check avgs
        avg_temps = [float(x) for x in list(sheet[(~sheet['TAVG'].isin(['-']))]['TAVG'])]
        # variance = np.var(avg_temps)
        # std = np.std(avg_temps)

        # troche zimy
        min_temps = [float(x) for x in list(sheet[(~sheet['TMIN'].isin(['-']))]['TMIN'])]
        min_temps = min_temps if len(min_temps) >= 0.5*len(avg_temps) else avg_temps  # fallback
        winter_days = sum(x < self.MIN_TEMP for x in min_temps)

        # troche lata
        max_temps = [float(x) for x in list(sheet[(~sheet['TMAX'].isin(['-']))]['TMAX'])]
        max_temps = max_temps if len(max_temps) >= 0.5 * len(avg_temps) else avg_temps
        summer_days = sum(x > self.MAX_TEMP for x in max_temps)

        return winter_days >= self.DAYS_THRESHOLD and summer_days >= self.DAYS_THRESHOLD
