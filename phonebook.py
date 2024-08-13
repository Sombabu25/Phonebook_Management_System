print("\n********** Phonebook Management System ***********")

contacts = {}

def add_contact():
    user = input("Enter contact name: ")
    if user in contacts:
        print("Contact already exists.")
    else:
        try:
            phone_number = int(input("Enter phone number: "))
            contacts[user] = phone_number
            print("Contact added successfully.")
        except ValueError:
            print("Invalid phone number. Please enter a valid number.")

def search_contact():
    user = input("Search name: ")
    if user in contacts:
        print(f"Contact's number: {contacts[user]}")
    else:
        print("Contact doesn't exist.")

def list_contacts():
    if not contacts:
        print("-- No Contacts Available --")
    else:
        print("Contact Name       Contact Number")
        print("------------       --------------")
        for user, phone_number in contacts.items():
            print(f"{user:<16} {phone_number}")

def delete_contact():
    if not contacts:
        print("-- No Contacts Available --")
    else:
        user = input("Contact name to delete: ")
        if user in contacts:
            del contacts[user]
            print(f"{user} successfully deleted.")
        else:
            print("Contact doesn't exist.")

def main():
    while True:
        choice = input("\n1. Add contacts\n2. Search contacts\n3. List all contacts\n4. Delete contacts\n5. Exit program\nChoose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            list_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("----- Thanks for Using -----")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
