from typing import Optional
from .birthday import Birthday
from .name import Name
from .phone import Phone
from app.helpers.is_birthday_within_next_days import is_birthday_within_next_days


class Record:
    def __init__(self, name: str, phone: str, birthday: Optional[str] = None):
        self._name = Name(name)
        self._phones = []
        self._birthday = None
        self.add_phone(phone)
        if birthday:
            self.birthday = birthday

    @property
    def name(self):
        return self._name

    @property
    def phones(self):
        return self._phones

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, day: str):
        birthday = Birthday(day)
        self._birthday = birthday

        return True

    add_birthday = birthday

    def find_phone(self, looking_phone: str):
        return next((phone for phone in self.phones if phone == looking_phone), None)

    def edit_phone(self, old_phone: str, new_phone: str):
        phone = self.find_phone(old_phone)
        print(phone)
        if not phone:
            return False
        phone.value = new_phone

        return True

    def add_phone(self, new_phone: str) -> bool:
        is_phone_present = bool(self.find_phone(new_phone))
        if is_phone_present:
            raise ValueError("This phone already exists for current contact")

        new_phone = Phone(new_phone)
        self._phones.append(new_phone)

        return True

    def is_birthday_next_week(self):
        return is_birthday_within_next_days(self.birthday.value)

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday or ''}"


# if __name__ == "main":
#     Record("Jhon", "1231231231", "05.11.2000")
