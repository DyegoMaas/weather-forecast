import os
import jsonpickle


class CitiesRepository:

    _file_name = 'cities.jsonl'

    def get_all(self):
        def read_lines():
            if not os.path.isfile(f'./{CitiesRepository._file_name}'):
                return []

            with open(CitiesRepository._file_name, 'r', encoding='utf8') as file:
                for json in file:
                    yield jsonpickle.decode(json.strip())

        return read_lines()

    def add(self, city):
        with open(CitiesRepository._file_name, 'a', encoding='utf8') as file:
            city = jsonpickle.encode(city) + '\n'
            file.write(city)
