class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def __str__(self):
        return str(self.value)

    def __eq__(self, other_value):
        return self.value == other_value
