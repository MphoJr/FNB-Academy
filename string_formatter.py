# string_formatter.py

# Step 1: Collect user input with validation
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
bio = input("Enter a short bio message: ").strip()

# Validation: Ensure names are not empty
if not first_name or not last_name:
    print("Error: First name and last name cannot be empty.")
    exit()

# Validation: Limit bio length (e.g., max 150 characters)
MAX_BIO_LENGTH = 150
if len(bio) > MAX_BIO_LENGTH:
    print(f"Error: Bio is too long! Please keep it under {MAX_BIO_LENGTH} characters.")
    exit()

# Step 2: Create username (first initial + last name, lowercase)
username = (first_name[0] + last_name).lower()

# Step 3: Format full name in Title Case
full_name = f"{first_name} {last_name}".title()

# Step 4: Count characters in bio
bio_length = len(bio)

# Step 5: Replace 'I am' with 'I'm'
formatted_bio = bio.replace("I am", "I'm")

# Step 6: Display formatted profile output
print("\n--- USER PROFILE ---")
print(f"Username: {username}")
print(f"Full Name: {full_name}")
print(f"Bio: {formatted_bio}")
print(f"Bio Length: {bio_length} characters")
print("---------------------")
