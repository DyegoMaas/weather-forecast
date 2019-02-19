from repositories.repositories import CitiesRepository
from repositories.entities import City
import pytest
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

    def test_prevents_adding_duplicates(self):
        timbo = City('Timbó')

        repository = CitiesRepository()
        repository.add(timbo)
        repository.add(timbo)

        cities = list(repository.get_all())
        assert len(cities) == 1
