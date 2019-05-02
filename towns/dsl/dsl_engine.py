from django.db import connection
from voluptuous import MultipleInvalid

from towns.dsl.parsers import FiltersParser, FieldsParser
from towns.dsl.schema import schema


class DSLEngine:
    template = "SELECT id, {fields} FROM towns_town {filters}"

    def __init__(self, parsers=None):
        if parsers is None:
            self.parsers = {'fields': FieldsParser(), 'filters': FiltersParser()}
        else:
            self.parsers = parsers

    def execute(self, **kwargs):
        result = self._format(kwargs)
        if isinstance(result, Exception):
            return result
        with connection.cursor() as cursor:
            cursor.execute(result)
            rows = cursor.fetchall()

        return rows

    def _format(self, kwargs):

        try:
            schema(kwargs)
        except MultipleInvalid as e:
            return e

        parsed_dict = {name: parser.parse(kwargs[name]).dump() for name, parser in self.parsers.items()}
        return self.template.format(**parsed_dict)
