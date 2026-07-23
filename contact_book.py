# contact_book.py

# Step 1: Initialize contact list
contacts = []

# Step 2: Define functions
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"✅ Contact '{name}' added successfully!")

def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None

def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"🗑️ Contact '{name}' deleted successfully!")
            return
    print(f"⚠️ Contact '{name}' not found.")

def view_all():
    if not contacts:
        print("📭 No contacts available.")
    else:
        print("\n--- CONTACT LIST ---")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print("--------------------")

# Step 3: Menu loop
while True:
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        name = input("Enter name to search: ")
        result = search_contact(name)
        if result:
            print(f"🔎 Found: Name: {result['name']}, Phone: {result['phone']}, Email: {result['email']}")
        else:
            print("⚠️ Contact not found.")
    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "4":
        view_all()
    elif choice == "5":
        print("👋 Exiting Contact Book. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please select 1-5.")
