def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please type name and number"
        except KeyError:
            return "Name does not exist"
        except IndexError:
            return "Provide the name please"

    return inner

@input_error
def add_contact(args, contacts):
        name, phone = args
        contacts[name] = phone
        return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if contacts[name]:
        contacts[name] = phone
        return "Contact changed"

@input_error
def show_phone(args, contacts: dict):
        return f'{contacts[args[0]]}'


def show_all(contacts):
    return f"{contacts}"

# def delete_contact(args, contacts: dict):
#     contacts.pop(*args)
#     return "Contact deleted"