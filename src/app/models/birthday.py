from datetime import datetime
from .field import Field


class Birthday(Field):
    @Field.value.setter
    def value(self, val):
        try:
            date = datetime.strptime(val, "%d.%m.%Y").date()
            self._value = date
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self._value.strftime("%d.%m.%Y")
