from voluptuous import Schema, Required, Any

from towns.dsl.parsers.constants import PREDICATE_MAP

ALLOWED_FIELDS = [
    'name',
    'town_code',
    'departement_code',
    'population'
]


def filter_schema_r(v):
    return filter_schema(v)


filter_schema = Schema({
    Required('fields'): Any(*ALLOWED_FIELDS),
    Required('value'): Any(int, str),
    'predicate': Any(*list(PREDICATE_MAP.keys()))
})

conditional_filter_schema = Schema({
    Required('field'): Any(*ALLOWED_FIELDS),
    Required('value'): Any(int, str),
    'predicate': Any(*list(PREDICATE_MAP.keys())),
    'and': filter_schema_r,
    'or': filter_schema_r
})

schema = Schema({
    Required('fields'): ALLOWED_FIELDS,
    "filters": Any(
        filter_schema,
        Schema({"and": [conditional_filter_schema]}),
        Schema({"or": [conditional_filter_schema]})
    )
})
