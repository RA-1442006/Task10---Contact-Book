# Task 10: Contact Book Using Dictionaries

## About the Project
This is a simple command-line Contact Book built in Python for **Task 10 (Level 1, Day 10)**. It uses a Python dictionary as the main data structure to store and manage contacts. Each phone number acts as a unique key, and the contact details (name and email) are stored as its value.

Features included:
- **Add Contact**: Add a new contact with duplicate phone number checking and basic input validation.
- **Search Contact**: Look up a contact by phone number (using `.get()`) or by name.
- **Update Contact**: Edit an existing contact's name or email.
- **Delete Contact**: Remove a contact from the dictionary using its phone number.
- **View All Contacts**: Display all saved contacts in a clean list.
- Comes with sample contacts preloaded so you can test it right away.

## How to Run It
1. Make sure you have Python 3 installed.
2. Open a terminal in the project folder.
3. Run the program:
   ```bash
   python contact_book.py
   ```

## Sample Output
```text
Welcome to the Python Contact Book!

===== CONTACT BOOK MENU =====
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Exit
Enter your choice (1-6): 5

--- All Contacts ---
1. Phone: 9876543210 | Name: Aarav Sharma | Email: aarav@gmail.com
2. Phone: 9123456780 | Name: Priya Verma | Email: priya@yahoo.com
3. Phone: 9988776655 | Name: Rohan Patel | Email: rohan@outlook.com

===== CONTACT BOOK MENU =====
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Exit
Enter your choice (1-6): 1

--- Add Contact ---
Enter phone number: 9001122334
Enter name: Neha Gupta
Enter email (or press Enter to skip): neha@gmail.com
Contact 'Neha Gupta' added successfully.

===== CONTACT BOOK MENU =====
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Exit
Enter your choice (1-6): 2

--- Search Contact ---
Enter phone number or name to search: 9001122334
Found -> Phone: 9001122334 | Name: Neha Gupta | Email: neha@gmail.com

===== CONTACT BOOK MENU =====
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Exit
Enter your choice (1-6): 6
Exiting Contact Book. Goodbye!
```

## What I Learned About Dictionaries
Working on this task helped me understand how useful dictionaries are for real-world CRUD operations:
- Using a unique value like a **phone number as the key** makes checking for duplicates (`if phone in contacts`) and looking up records super fast without needing to loop through the whole collection every time.
- You can store another dictionary inside a dictionary (nested dictionaries) to keep multiple fields like `name` and `email` organized under one key.
- Using `.items()` makes it easy to loop through both keys and values when displaying all contacts, and `del contacts[phone]` cleanly removes an entry.

## Interview Questions

**1. What is a dictionary?**  
A dictionary in Python is a built-in, mutable data structure that stores data as a collection of key-value pairs inside curly braces `{}`. Unlike lists that use numeric indexes, dictionaries let you look up values quickly using unique, immutable keys.

**2. What is a key-value pair?**  
A key-value pair is a single item inside a dictionary where the **key** acts as a unique identifier (like a phone number `"9876543210"`) and the **value** is the data linked to that key (like the contact's name and email). They are written with a colon between them, such as `"name": "Aarav Sharma"`.

**3. What happens if you access a dictionary key that does not exist?**  
If you try to access a missing key using square brackets like `contacts["0000000000"]`, Python raises a `KeyError` and crashes the program if it isn't handled. Using `contacts.get("0000000000")` avoids this error because `.get()` safely returns `None` (or a default value you specify) when the key is not found.
