import re
from .field import Field


class Phone(Field):
    @Field.value.setter
    def value(self, value):
        s = str(value).strip()
        if not re.fullmatch(r"\d{10}", s):
            raise ValueError("Phone must be exactly 10 digits")
        self._value = s
