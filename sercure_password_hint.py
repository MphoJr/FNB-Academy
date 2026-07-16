# secure_password_hint.py

# Step 1: Ask the user for their secret password
password = input("Enter your secret password: ")

# Step 2: Clean up accidental spaces
password = password.strip()

# Validation: Ensure password is not empty
if len(password) == 0:
    print("Error: Password cannot be empty.")
else:
    # Step 3: Grab the first and last letters
    first_letter = password[0].upper()
    last_letter = password[-1].upper()

    # Step 4: Get password length
    password_length = len(password)

    # Step 5: Print the secure hint
    print(f"Your password hint: It starts with {first_letter} and ends with {last_letter}.")
    print(f"Your password is {password_length} characters long.")
