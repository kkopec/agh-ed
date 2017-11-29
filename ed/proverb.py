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

    def build_filter(self, year):
        pass

    def process_year(self, place, year):
        pass
