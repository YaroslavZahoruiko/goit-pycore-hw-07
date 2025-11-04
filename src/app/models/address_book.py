from typing import Optional
from app.models.birthday import Birthday
from app.models.phone import Phone
from .record import Record


class AddressBook:
    def __init__(self) -> None:
        self._data = {}

    @property
    def data(self) -> dict:
        return self._data

    def add_record(self, name, phone):
        record = self._data.get(name)
        if record:
            record.add_phone(phone)
            return "updated", record
        else:
            record = Record(name, phone)
            self._data[name] = record
            return "created", record

    def change_phone(self, name, old_phone, new_phone):
        self.find(name).change_phone(old_phone, new_phone)

    def find_phone(self, name: str) -> list[Phone]:
        return self.find(name).phones

    def all(self) -> list[dict[str, Record]]:
        return list(self._data.values())

    def add_birthday(self, name: str, birthday: str) -> bool:
        self.find(name).birthday = birthday
        return True

    def show_birthday(self, name: str) -> Optional[Birthday]:
        record = self.find(name)
        if record:
            return record.birthday
        else:
            return None

    def birthdays(self):
        return list(filter(lambda record: record.is_birthday_next_week(), self.all()))

    def find(self, name: str) -> Record:
        return self._data.get(name)

    def delete(self, name: str) -> Record:
        return self._data.pop(name, None)

    # def add_record(self, record: Record) -> bool:
    #     self._data[record.name.value] = record
