PREDICATE_MAP = {
    "gt": ">",
    "lt": "<",
    "equal": "="
}


class FiltersParser:

    @staticmethod
    def parse(filters):
        if not filters:
            return ""

        predicate = filters.get('predicate')
        filter_operator = PREDICATE_MAP.get(predicate, "=")

        return f"WHERE {filters['fields']} {filter_operator} {filters['value']}"
