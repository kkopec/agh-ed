class Proverb:
    def __init__(self, data_provider):
        self.data_provider = data_provider()
        self.data = {}
        self.results = {}

    def populate_data(self):
        for place in self.data_provider.get_places():
            self.data[place] = {}
            for year in self.data_provider.fetch_data(place):
                self.data[place][year] = self.data_provider.filter_data(self.build_filter(year))

    def process_data(self):
        for place in self.data_provider.get_places():
            self.results[place] = [self.process_year(place, y) for y in self.data[place].keys()]

    def cleanup_results(self):
        for place in self.data_provider.get_places():
            self.results[place] = [res for res in self.results[place] if res is not None]

    def run(self):
        self.populate_data()
        self.process_data()
        self.cleanup_results()
        return self.results

    def print_summary(self):
        print('-------------------------------')
        print('# {0}:'.format(self))
        [print('    - {0: <10}{1}/{2}'.format(place, sum(r for r in res), len(res))) for (place, res) in self.results.items()]

    def build_filter(self, year):
        pass

    def process_year(self, place, year):
        pass
