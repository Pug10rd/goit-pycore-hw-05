from commands.commands_list import add_contact, change_contact, show_phone, show_all #, delete_contact

def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}
    print("Welcome to the Choco.py assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        elif command in ["close", "exit"]:
            print("Goodbye!")
            break
        
        # Potentialy useful and practical option:

        # elif command == "delete":
        #     print(delete_contact(args, contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()