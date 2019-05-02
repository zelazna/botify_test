class FieldsParser:
    def __init__(self):
        self.clause = None

    def parse(self, fields):
        self.clause = ", ".join(fields)
        return self

    def dump(self):
        return self.clause
