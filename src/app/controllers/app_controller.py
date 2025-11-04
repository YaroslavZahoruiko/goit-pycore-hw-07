from typing import Callable


class AppController:
    def __init__(self, model, view):
        self.service = model
        self.view = view
        self.commands: dict[str, Callable[[list[str]], None]] = {
            "help": self.cmd_help,
            "hello": self.cmd_hello,
            "add": self.cmd_add,
            "change": self.cmd_change,
            "phone": self.cmd_show_phone,
            "all": self.cmd_show_all,
            "add-birthday": self.cmd_add_birthday,
            "show-birthday": self.cmd_show_birthday,
            "birthdays": self.cmd_birthdays,
            "exit": self.cmd_exit,
            "quit": self.cmd_exit,
        }
        self._running = True

    def run(self):
        self.view.welcome_message()
        self.view.help_proposal()

        while self._running:
            raw = self.view.prompt("> ")
            if not raw:
                continue
            cmd, *args = raw.split()
            handler = self.commands.get(cmd.lower())
            if handler:
                try:
                    handler(args)
                except Exception as exc:
                    self.view.show_error(str(exc))
            else:
                self.view.invalid_command()

    def cmd_hello(self):
        self.view.hello_message()

    def cmd_help(self, _):
        self.view.show_help()

    def cmd_add(self, args):
        if len(args) < 2:
            raise ValueError("Usage: add [name] [phone]")
        name, phone = args[0], args[1]
        action, record = self.service.add_record(name, phone)

        if action == "created":
            self.view.show(f"New {record} was successful created")
        else:
            self.view.show(
                "This contact already exists, we added new phone to existed contact"
            )

    def cmd_change(self, args):
        if len(args) < 3:
            raise ValueError("Usage: change [name] [old_phone] [new_phone]")
        name, old_phone, new_phone, *_ = args
        success = self.service.change_phone(name, old_phone, new_phone)
        if success:
            self.view.show("Your phone number was successfully changed.")

    def cmd_show_phone(self, args):
        if len(args) < 1:
            raise ValueError("Usage: phone [name]")
        name, *_ = args
        phones = self.service.find_phone(name)
        if phones:
            self.view.show_list(f"{name}'s phone numbers are:", phones)
        else:
            self.view.contact_not_found(name)

    def cmd_show_all(self, _args):
        records = self.service.all()
        self.view.show_list("Contacts:", records)

    def cmd_add_birthday(self, args):
        if len(args) < 2:
            raise ValueError("Usage: add-birthday [name] [birthday]")
        name, birthday, *_ = args
        success = self.service.add_birthday(name, birthday)
        if success:
            self.view.show("Contact's birthday was successfully changed.")

    def cmd_show_birthday(self, args):
        if len(args) < 1:
            raise ValueError("Usage: show-birthday [name]")
        name, *_ = args
        birthday = self.service.show_birthday(name)
        if birthday:
            self.view.show(f"{name}'s birthday: {birthday}")
        else:
            self.view.contact_not_found(name)

    def cmd_birthdays(self, _args):
        records = self.service.birthdays()
        if records:
            self.view.show_list("Upcomming birthdays:", records)
        else:
            self.view.show("No upcomming birthdays were found")

    def cmd_exit(self, _):
        self._running = False
        self.view.show("Bye!")
