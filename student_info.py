# student_info.py

# Collect user input
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age (integer): "))
favourite_number = float(input("Enter your favourite number (float): "))

# Display formatted greeting
full_name = f"{first_name} {surname}"
print(f"\nWelcome, {full_name}!")

# String manipulations
print("Name in UPPERCASE:", full_name.upper())
print("Name in Title Case:", full_name.title())

# Arithmetic calculation
age_in_months = age * 12
print(f"Your age in months: {age_in_months}")

# Round favourite number
rounded_number = round(favourite_number, 2)
print(f"Your favourite number rounded to 2 decimals: {rounded_number}")

# Display data types
print("\nData Types:")
print("First name:", type(first_name))
print("Surname:", type(surname))
print("Age:", type(age))
print("Favourite number:", type(favourite_number))
