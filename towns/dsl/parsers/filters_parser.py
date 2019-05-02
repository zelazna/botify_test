from towns.dsl.parsers.constants import PREDICATE_MAP, WHERE, FILTERS


class FiltersParser:
    def __init__(self):
        self.clauses = None
        self.cond = None

    def parse(self, filters):
        self.clauses = []
        if not filters:
            return ""

        predicate = filters.get('predicate')

        if predicate:
            filter_operator = PREDICATE_MAP.get(predicate, PREDICATE_MAP['equal'])
            self.clauses.append(f"WHERE {filters['fields']} {filter_operator} {filters['value']}")

        else:
            cond = list(filters.keys())[0]

            if cond in FILTERS:
                for idx, f in enumerate(filters[cond]):
                    self.clauses.append(WHERE) if idx == 0 else self.clauses.append(cond.upper())
                    self.parse_clause(f)

        return self

    def parse_clause(self, query_filter):
        predicate = PREDICATE_MAP[query_filter['predicate']]
        value = f"'%{query_filter['value']}%'" if predicate == PREDICATE_MAP["contains"] else query_filter['value']
        self.clauses.append(f"{query_filter['field']} {predicate} {value}")

    def dump(self):
        return " ".join(self.clauses)
