from services.cities_service import CitiesService
from repositories.repositories import CitiesRepository
from repositories.entities import City
from web_apis.forecasts import OpenWeatherMapAPI, ForecastData
from mox import IgnoreArg, Mox
import pytest


class TestCitiesRepositoryProxy:

    @pytest.fixture()
    def valid_forecast_data(self):
        return ForecastDataStub(True)

    @pytest.fixture()
    def invalid_forecast_data(self):
        return ForecastDataStub(False)

    def test_inserts_known_city(self, valid_forecast_data):
        mocker = Mox()
        cities_repository_fake = CitiesRepositoryFake()
        open_weather_mock = mocker.CreateMock(OpenWeatherMapAPI)
        open_weather_mock.get_city_forecast_for_next_5_days('Tokyo').AndReturn(valid_forecast_data)
        mocker.ReplayAll()

        service = CitiesService(cities_repository_fake, open_weather_mock)
        forecast = service.get_forecast_for(City('Tokyo'))

        assert forecast == valid_forecast_data
        cities = service.list_cities()
        assert len(cities) == 1

    def test_does_not_insert_unknown_city(self, invalid_forecast_data):
        mocker = Mox()
        cities_repository_fake = CitiesRepositoryFake()
        open_weather_mock = mocker.CreateMock(OpenWeatherMapAPI)
        open_weather_mock.get_city_forecast_for_next_5_days(IgnoreArg()).AndReturn(invalid_forecast_data)
        mocker.ReplayAll()

        service = CitiesService(cities_repository_fake, open_weather_mock)
        forecast = service.get_forecast_for(City('Rio dos Cedros'))

        assert forecast == invalid_forecast_data
        cities = service.list_cities()
        assert len(cities) == 0


class CitiesRepositoryFake(CitiesRepository):

    def __init__(self):
        self.cities = []

    def get_all(self):
        return self.cities

    def add(self, city):
        self.cities.append(city)


class ForecastDataStub(ForecastData):

    def __init__(self, found_data):
        self.did_found_data = found_data

    def found_data(self) -> bool:
        return self.did_found_data

    def extract(self) -> list:
        return []
