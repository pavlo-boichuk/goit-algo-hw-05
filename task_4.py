def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Contact [{name}] already exist!"
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if not name in contacts:
        return f"Contact [{name}] not found!"
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    name = args[0]
    if not name in contacts:
        return f"Contact [{name}] not found!"
    return contacts[name]


def show_all(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts)) 
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))    
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
