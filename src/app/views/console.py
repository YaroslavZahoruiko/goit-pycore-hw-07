# src/app/views/console.py
class ConsoleView:
    HELP = """
Commands:
    - add [name] [phone]: Add a new contact with a name and phone number, or add a phone number to an existing contact.
    - change [name] [old phone] [new phone]: Change the phone number for the specified contact.
    - phone [name]: Show the phone numbers for the specified contact.
    - all: Show all contacts in the address book.
    - add-birthday [name] [birthday]: Add a birthday for the specified contact, format: DD.MM.YYYY
    - show-birthday [name]: Show the birthday of the specified contact.
    - birthdays: Show birthdays that will occur within the next week.
    - hello: Receive a greeting from the bot.
    - close or exit: Close the program.
    """

    def help_proposal(self):
        print("Type 'help' for commands.")

    def show(self, message: str = ""):
        if message:
            print(message)

    def prompt(self, message: str = "> ") -> str:
        return input(message).strip()

    def show_error(self, message: str):
        print(f"Error: {message}")

    def show_record(self, record):
        print(record)

    def show_list(self, message, items):
        self.show(message)
        for item in items:
            print(item)

    def welcome_message(self):
        print("Welcome to the assistant bot!")

    def show_help(self):
        print(self.HELP)

    def invalid_command(self):
        print("Invalid command. Type 'help'.")

    def contact_not_found(self, name):
        print(f"Contact with {name} was not found.")
