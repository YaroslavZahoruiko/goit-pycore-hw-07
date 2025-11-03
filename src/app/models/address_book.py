from .record import Record


class AddressBook:
    def __init__(self) -> None:
        self.__data = {}

    @property
    def data(self) -> dict:
        return self.__data

    def find(self, name: str) -> Record:
        return self.__data.get(name)

    def delete(self, name: str) -> Record:
        return self.__data.pop(name, None)

    def add_record(self, record: Record) -> bool:
        self.__data[record.name.value] = record
