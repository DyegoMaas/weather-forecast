from repositories.repositories import CitiesRepository
from repositories.entities import City
import pytest
import os


class TestCitiesRepository:

    @pytest.fixture(autouse=True)
    def remove_file_if_exists(self):
        self.repository = CitiesRepository()

        file_to_remove = self.repository._file_name
        if os.path.isfile(file_to_remove):
            os.remove(file_to_remove)

        yield

    def test_reads_no_city_at_the_beginning(self):
        cities = list(self.repository.get_all())

        assert len(cities) == 0

    def test_adds_a_city(self):
        timbo = City('Timbó')
        blumenau = City('Blumenau')

        self.repository.add(timbo)
        self.repository.add(blumenau)

        cities = list(self.repository.get_all())
        assert len(cities) == 2
        assert cities[0].name == timbo.name
        assert cities[1].name == blumenau.name
