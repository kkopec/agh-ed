import matplotlib.pyplot as plt


class Proverb:
    def __init__(self, data_provider):
        self.data_provider = data_provider()
        self.data = {}

    def populate_data(self):
        for year in self.data_provider.fetch_data():
            self.data[year] = self.data_provider.filter_data(self.build_filter(year))

    def process_data(self):
        return [self.process_year(y) for y in self.data.keys()]

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

    def build_filter(self, year):
        pass

    def process_year(self, year):
        pass
