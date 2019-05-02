from voluptuous import Schema, Required, Any, Optional, Exclusive, All, ALLOW_EXTRA

from towns.dsl.constants import PREDICATE_MAP, ALLOWED_FIELDS

filter_schema = Schema({
    Optional('fields'): Any(*ALLOWED_FIELDS),
    Optional('field'): Any(*ALLOWED_FIELDS),
    Optional('value'): Any(int, str),
    'predicate': Any(*list(PREDICATE_MAP.keys())),
}, extra=ALLOW_EXTRA)

and_schema = Schema({Required('and'): [filter_schema]})
or_schema = Schema({Required('or'): [filter_schema]})

schema = Schema({
    Required('fields'): ALLOWED_FIELDS,
    "filters": Any(
        filter_schema,
        Any(and_schema, or_schema)
    )
})
