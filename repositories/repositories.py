from repositories.abc import JsonLinesRepository


class CitiesRepository(JsonLinesRepository):

    def __init__(self):
        super().__init__('cities.jsonl')

    def add(self, city):
        if self._city_already_saved(city.name):
            return

        super().add(city)

    def _city_already_saved(self, city_name):
        cities_names = [city.name for city in self.get_all()]
        return city_name in cities_names
