contacts = {}

def add(name, number):
    contacts[name] = number
    print(f"Contact '{name}' added or updated.")

def search(name):
    if name in contacts:
        print(name, ":", contacts[name])
    else:
        print("Contact not found.")

def delete(name):
    if name in contacts:
        contacts.pop(name)
        print(f"Contact '{name}' deleted.")
    else:
        print("No contact found with that name.")

def view():
    if not contacts:
        print("No contacts available.")
    else:
        for name, number in sorted(contacts.items()):
            print(name, ":", number)

print("Contact Book Application")

while True:
    menu = input("\nChoose an option (ADD, SEARCH, DELETE, VIEW, EXIT): ").upper()

    if menu == 'ADD':
        name = input("Enter the name: ").strip()
        number = input("Enter the number: ").strip()
        add(name, number)

    elif menu == 'SEARCH':
        name = input("Enter the name to search: ").strip()
        search(name)

    elif menu == 'DELETE':
        name = input("Enter the name to delete: ").strip()
        delete(name)

    elif menu == 'VIEW':
        view()

    elif menu == 'EXIT':
        print("Thanks for using the contact book.")
        break

    else:
        print("Invalid option.")
