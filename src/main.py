from commands import (
    parse_input, show_help, add_contact, change_contact, 
    show_phone, show_all, add_birthday, show_birthday, birthdays
)
from address_book import AddressBook


def main():
    """Main function that runs the assistant bot."""
    book = AddressBook()
    print("Welcome to the assistant bot!")
    
    try:
        while True:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)
            
            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break

                case "hello":
                    print("How can I help you?")

                case "help":
                    print(show_help())

                case "add":
                    print(add_contact(args, book))

                case "change":
                    print(change_contact(args, book))

                case "phone":
                    print(show_phone(args, book))

                case "all":
                    print(show_all(args, book))

                case "add-birthday":
                    print(add_birthday(args, book))

                case "show-birthday":
                    print(show_birthday(args, book))

                case "birthdays":
                    print(birthdays(args, book))

                case "":
                    continue  # Skip empty inputs

                case _:
                    print("Invalid command. Type 'help' for available commands.")
    
    except KeyboardInterrupt:
        print("\nGood bye!")


if __name__ == "__main__":
    main()
