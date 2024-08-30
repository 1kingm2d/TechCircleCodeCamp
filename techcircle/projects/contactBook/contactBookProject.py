import json

filePath = "contacts.json"

def loadContact():
    try:
        with open(filePath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def saveContacts(contacts):
    with open(filePath, "w") as file:
        json.dump(contacts, file)

def addContact(name, phone):
    contacts = loadContact()
    newName = name.lower()
    contacts[newName] = phone
    saveContacts(contacts)
    print(f"Contact '{name}' added successfully")

def viewContact():
    contacts = loadContact()

    if contacts:
        print("\n--Contact List--")

        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

    else:
        print("No contacts Found")

def searchContact(name):
    contacts = loadContact()

    if name in contacts:
        print(f"Found: {name} - {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")


while True:
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Quit")

    choice = input("Choose an option (1 - 4 ): ")

    if choice == "1":
        name = input("Enter name: ")

        phone = input("Enter Phone number: ")

        addContact(name, phone)

    elif choice == "2":
        viewContact()

    elif choice == "3":
        name = input("Enter name: ")

        newName = name.lower()

        searchContact(newName)

    elif choice == "4":
        print("Goodbye!")

        break
    else:
        print("invalid operation")