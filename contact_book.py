# Task 10: Contact Book Using Dictionaries

def add_contact(contacts):
    print("\n--- Add Contact ---")
    phone = input("Enter phone number: ").strip()

    if phone == "":
        print("Phone number cannot be empty.")
        return

    if not phone.isdigit():
        print("Invalid phone number. Please enter digits only.")
        return

    # Prevent duplicate phone numbers
    if phone in contacts:
        print("A contact with this phone number already exists!")
        return

    name = input("Enter name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return

    email = input("Enter email (or press Enter to skip): ").strip()
    if email == "":
        email = "Not provided"

    contacts[phone] = {
        "name": name,
        "email": email
    }
    print(f"Contact '{name}' added successfully.")


def search_contact(contacts):
    print("\n--- Search Contact ---")
    search_term = input("Enter phone number or name to search: ").strip()

    if search_term == "":
        print("Search input cannot be empty.")
        return

    # Try to find by phone number key using .get()
    contact = contacts.get(search_term)
    if contact is not None:
        print(f"Found -> Phone: {search_term} | Name: {contact['name']} | Email: {contact['email']}")
        return

    # If not a phone number match, check contact names
    found = False
    for phone, info in contacts.items():
        if search_term.lower() in info["name"].lower():
            print(f"Found -> Phone: {phone} | Name: {info['name']} | Email: {info['email']}")
            found = True

    if not found:
        print("Contact not found.")


def update_contact(contacts):
    print("\n--- Update Contact ---")
    phone = input("Enter the phone number of the contact to update: ").strip()

    if phone == "":
        print("Phone number cannot be empty.")
        return

    if phone not in contacts:
        print("Contact not found.")
        return

    current = contacts[phone]
    print(f"Current details -> Name: {current['name']} | Email: {current['email']}")

    new_name = input("Enter new name (press Enter to keep current): ").strip()
    new_email = input("Enter new email (press Enter to keep current): ").strip()

    if new_name != "":
        contacts[phone]["name"] = new_name
    if new_email != "":
        contacts[phone]["email"] = new_email

    print("Contact updated successfully.")


def delete_contact(contacts):
    print("\n--- Delete Contact ---")
    phone = input("Enter the phone number of the contact to delete: ").strip()

    if phone == "":
        print("Phone number cannot be empty.")
        return

    if phone not in contacts:
        print("Contact not found.")
        return

    removed_name = contacts[phone]["name"]
    del contacts[phone]
    print(f"Contact '{removed_name}' ({phone}) deleted successfully.")


def view_all_contacts(contacts):
    print("\n--- All Contacts ---")
    if len(contacts) == 0:
        print("Contact book is empty.")
        return

    count = 1
    for phone, info in contacts.items():
        print(f"{count}. Phone: {phone} | Name: {info['name']} | Email: {info['email']}")
        count += 1


def main():
    # Preloaded sample contacts (phone number is the key)
    contacts = {
        "9876543210": {"name": "Aarav Sharma", "email": "aarav@gmail.com"},
        "9123456780": {"name": "Priya Verma", "email": "priya@yahoo.com"},
        "9988776655": {"name": "Rohan Patel", "email": "rohan@outlook.com"}
    }

    print("Welcome to the Python Contact Book!")

    while True:
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            view_all_contacts(contacts)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
