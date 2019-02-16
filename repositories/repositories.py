from repositories.abc import JsonLinesRepository


class CitiesRepository(JsonLinesRepository):

    def __init__(self):
        super().__init__('cities.jsonl')


class CitiesRepositoryProxy(CitiesRepository):

    def __init__(self, city_repository, open_weather_api):
        self._repository = city_repository
        self._open_weather_api = open_weather_api

    def get_all(self):
        return self._repository.get_all()

    def add(self, city):
        if self._open_weather_api.verify_city_exists(city.name):
            self._repository.add(city)
