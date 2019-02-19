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

        try:
            return read_lines()
        except Exception as exception:
            raise FileDataBaseException(exception)

    def add(self, entity):
        try:
            with open(self._file_name, 'a', encoding=self._encoding) as file:
                inline_json = jsonpickle.encode(entity) + '\n'
                file.write(inline_json)
        except Exception as exception:
            raise FileDataBaseException(exception)


class FileDataBaseException(Exception):

    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors
