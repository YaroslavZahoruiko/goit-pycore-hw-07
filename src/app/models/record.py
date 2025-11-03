from .name import Name
from .phone import Phone


class Record:
    def __init__(self, name):
        self.__name = Name(name)
        self.__phones = []

    @property
    def name(self):
        return self.__name

    @property
    def phones(self):
        return self.__phones

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        print(phone)
        if not phone:
            return False
        phone.value = new_phone

        return True

    def find_phone(self, looking_phone):
        return next((phone for phone in self.phones if phone == looking_phone), None)

    def add_phone(self, new_phone: str) -> bool:
        new_phone = Phone(new_phone)
        self.__phones.append(new_phone)

        return False

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
