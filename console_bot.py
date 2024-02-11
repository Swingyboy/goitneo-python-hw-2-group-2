from typing import Tuple
import sys


CONTACTS = {}


def _parse_input(user_input: str) -> Tuple[str, ...]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def _add_contact(*args) -> str:
    if len(args) != 2:
        return "Invalid number of arguments for add command, please try again."

    name, phone = args

    if name in CONTACTS:
        change = input(f"Contact {name.capitalize()} already exists. Do you want to change it?")
        if change.lower() in ["yes", "y"]:
            return _change_contact(name, phone)
        else:
            _hello_bot()
    else:
        CONTACTS[name] = phone
        return f"Contact {name.capitalize()} has been added."


def _change_contact(*args) -> str:
    if len(args) != 2:
        return "Invalid number of arguments for add command, please try again."
    name, phone = args

    if name not in CONTACTS:
        return f"Contact {name.capitalize()} does not exist."
    else:
        CONTACTS[name] = phone
        return f"Contact {name.capitalize()} has been updated."


def _get_all() -> None:
    for name, phone in CONTACTS.items():
        print(f"{name.capitalize()}:\t {phone}")


def _get_phone(*args) -> str:
    if len(args) != 1:
        return "Invalid number of arguments for phone command, please try again."
    name = args[0]
    if name not in CONTACTS:
        return f"Contact {name.capitalize()} does not exist."
    else:
        return f"{name.capitalize()}: {CONTACTS[name]}"


def _exit_bot() -> str:
    return "Goodbye!"


def _hello_bot() -> str:
    return "How can I help you?"


SUPPORTED_COMMANDS = {"exit": _exit_bot, "close": _exit_bot, "hello": _hello_bot, "add": _add_contact,
                      "change": _change_contact, "phone": _get_phone, "all": _get_all
                      }


def bot_event_loop():
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ").strip().lower()
            command, *args = _parse_input(user_input)
            result = SUPPORTED_COMMANDS[command](*args)
            if result:
                print(result)
        except KeyError:
            print(f"Invalid command, supported commands are:")
            for key in SUPPORTED_COMMANDS.keys():
                print(f" - {key}")
            print("Please try again.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)


if __name__ == "__main__":
    bot_event_loop()
