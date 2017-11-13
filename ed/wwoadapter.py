from ed.jsonadapter import JsonAdapter


class WWOAdapter(JsonAdapter):

    def get_date(self, json):
        return json.get('date')

    def get_min_temp(self, json):
        return int(json.get('mintempC'))

    def get_max_temp(self, json):
        return int(json.get('maxtempC'))

    def get_mean_temp(self, json):
        return sum([int(m.get('tempC')) for m in json.get('hourly')]) / len(json.get('hourly'))

    def get_precipitation(self, json):
        return sum([int(m.get('precipMM')) for m in json.get('hourly')])

    def get_snow(self, json):
        return float(json.get('totalSnow_cm'))

    def get_mean_cloudcover(self, json):
        return sum([int(m.get('cloudcover')) for m in json.get('hourly')]) / len(json.get('hourly'))
