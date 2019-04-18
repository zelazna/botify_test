from voluptuous import Schema, Required, Any

from towns.dsl.parsers.filters_parser import PREDICATE_MAP

ALLOWED_FIELDS = [
    'name',
    'town_code',
    'departement_code',
    'population'
]

schema = Schema({
    Required('fields'): ALLOWED_FIELDS,
    "filters": {
        Required('fields'): Any(*ALLOWED_FIELDS),
        Required('value'): Any(int, str),
        'predicate': Any(*list(PREDICATE_MAP.keys()))
    }
})
