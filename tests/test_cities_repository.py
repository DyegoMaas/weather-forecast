from repositories.cities_repository import CitiesRepository
from repositories.city import City
import pytest
import os


class TestCitiesRepository:

    @pytest.fixture(autouse=True)
    def remove_file_if_exists(self):
        file_to_remove = CitiesRepository._file_name
        if os.path.isfile(file_to_remove):
            os.remove(file_to_remove)

        yield

    def test_reads_no_city_at_the_beginning(self):
        repository = CitiesRepository()

        cities = list(repository.get_all())

        assert len(cities) == 0

    def test_adds_a_city(self):
        repository = CitiesRepository()
        timbo = City('Timbó')
        blumenau = City('Blumenau')

        repository.add(timbo)
        repository.add(blumenau)

        cities = list(repository.get_all())
        assert len(cities) == 2
        assert cities[0].name == timbo.name
        assert cities[1].name == blumenau.name

