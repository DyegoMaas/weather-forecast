from abc import ABC
import os
import jsonpickle


def try_access_file(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exception:
            raise FileDataBaseException(exception)
    return func_wrapper


class JsonLinesRepository(ABC):

    def __init__(self, file_name):
        self._file_name = file_name
        self._encoding = 'utf8'

    @try_access_file
    def get_all(self):
        if not self._database_file_exists():
            return []

        with open(self._file_name, 'r', encoding=self._encoding) as file:
            return [jsonpickle.decode(json.strip()) for json in file]

    @try_access_file
    def add(self, entity):
        with open(self._file_name, 'a', encoding=self._encoding) as file:
            inline_json = jsonpickle.encode(entity) + '\n'
            file.write(inline_json)

    def _database_file_exists(self):
        return os.path.isfile(self._file_name)


class FileDataBaseException(Exception):

    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors
