from repositories.repositories import CitiesRepository
from web_apis.forecasts import OpenWeatherMapAPI
from injector import inject


class CitiesService:

    @inject
    def __init__(self, city_repository: CitiesRepository, open_weather_api: OpenWeatherMapAPI):
        self._repository = city_repository
        self._open_weather_api = open_weather_api

    def get_forecast_for(self, city):
        """Gets 5 days worth of forecasts for the city.
        If any data is found, the city is saved for further use.
        """
        forecast = self._open_weather_api.get_city_forecast_for_next_5_days(city.name)

        if forecast.found_data():
            self._repository.add(city)

        return forecast

    def list_cities(self):
        return self._repository.get_all()
