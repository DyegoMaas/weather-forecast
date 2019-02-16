from repositories.repositories import CitiesRepository, CitiesRepositoryProxy
from repositories.entities import City
from web_apis.forecasts import OpenWeatherAPI
import pytest
from mox import MoxTestBase, IgnoreArg
import os


class TestCitiesRepository:

    @pytest.fixture(autouse=True)
    def clean_data_files(self):
        repository = CitiesRepository()
        if os.path.isfile(repository._file_name):
            os.remove(repository._file_name)

        yield

    def test_reads_no_city_at_the_beginning(self):
        repository = CitiesRepository()

        cities = list(repository.get_all())

        assert len(cities) == 0

    def test_adds_cities(self):
        timbo = City('Timbó')
        blumenau = City('Blumenau')

        repository = CitiesRepository()
        repository.add(timbo)
        repository.add(blumenau)

        cities = list(repository.get_all())
        assert len(cities) == 2
        assert cities[0].name == timbo.name
        assert cities[1].name == blumenau.name


class TestCitiesRepositoryProxy(MoxTestBase):

    def test_lets_add_city(self):
        cities_repository_fake = CitiesRepositoryFake()
        open_weather_mock = self.mox.CreateMock(OpenWeatherAPI)
        open_weather_mock.verify_city_exists('Tokyo').AndReturn(True)
        self.mox.ReplayAll()

        proxy = CitiesRepositoryProxy(cities_repository_fake, open_weather_mock)
        proxy.add(City('Tokyo'))

        cities = proxy.get_all()
        assert len(cities) == 1

    def test_prevents_add_city(self):
        cities_repository_fake = CitiesRepositoryFake()
        open_weather_mock = self.mox.CreateMock(OpenWeatherAPI)
        open_weather_mock.verify_city_exists(IgnoreArg()).AndReturn(False)
        self.mox.ReplayAll()

        proxy = CitiesRepositoryProxy(cities_repository_fake, open_weather_mock)
        proxy.add(City('Tokyo'))

        cities = proxy.get_all()
        assert len(cities) == 0


class CitiesRepositoryFake(CitiesRepository):

    def __init__(self):
        self.cities = []

    def get_all(self):
        return self.cities

    def add(self, city):
        self.cities.append(city)


