# phone_directory.py

# Step 1: Create dictionary of contacts
contacts = {
    "Mpho": "0821112222",
    "Sipho": "0833334444",
    "Thandi": "0845556666"
}

# Step 2: Ask user for a name
name = input("Enter the name of the friend you want to look up: ").strip()

# Step 3: Conditional check
if name in contacts:
    print(f"Found! {name}'s number is {contacts[name]}")
else:
    print("Contact not found.")
