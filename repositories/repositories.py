from repositories.abc import JsonLinesRepository


class CitiesRepository(JsonLinesRepository):

    def __init__(self):
        super().__init__('cities.jsonl')
