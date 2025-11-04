from app.views.console import ConsoleView
from app.controllers.app_controller import AppController
from app.models import AddressBook


def main():
    service = AddressBook()
    view = ConsoleView()
    controller = AppController(service, view)
    controller.run()


if __name__ == "__main__":
    main()
