import matplotlib.pyplot as plt


class Proverb:
    def __init__(self, data_provider, data_adapter):
        self.data_provider = data_provider
        self.data_adapter = data_adapter()
        self.data = {}

    def prepare_params(self, year):
        return {}

    def populate_data(self):
        for year in range(2009, 2018):
            self.data_provider.set_params(self.prepare_params(year))
            data_full = self.data_provider.fetch_data()
            self.data[year] = [self.filter_relevant(day) for day in data_full]

    def filter_relevant(self, json):
        pass

    def process_data(self):
        pass

    def run(self):
        self.populate_data()
        return self.process_data()

    def show_plot(self, year, param):
        y = [d.get(param) for d in self.data[year]]
        x = [d.get('date') for d in self.data[year]]

        plt.plot(x, y, 'ro', x, y, 'k')
        plt.grid(True)
        plt.title('{0} - {1}'.format(param, year))
        plt.xlabel('day')
        plt.ylabel(param)
        plt.show()
