from abc import ABC
import os
import jsonpickle


class JsonLinesRepository(ABC):

    def __init__(self, file_name):
        self._file_name = file_name
        self._encoding = 'utf8'

    def get_all(self):
        def read_lines():
            if not os.path.isfile(self._file_name):
                return []

            with open(self._file_name, 'r', encoding=self._encoding) as file:
                for json in file:
                    yield jsonpickle.decode(json.strip())

        return read_lines()

    def add(self, entity):
        with open(self._file_name, 'a', encoding=self._encoding) as file:
            inline_json = jsonpickle.encode(entity) + '\n'
            file.write(inline_json)


class CitiesRepository(JsonLinesRepository):

    def __init__(self):
        super().__init__('cities.jsonl')
