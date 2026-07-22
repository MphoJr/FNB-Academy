# calculator.py

# Step 1: Collect user input safely
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n--- CALCULATOR RESULTS ---")

# Step 2: Perform calculations
addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

# Handle division by zero
if num2 == 0:
    division = "Error (division by zero)"
    floor_division = "Error (division by zero)"
    modulus = "Error (division by zero)"
else:
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)

# Step 3: Display results in formatted table
print(f"{'Operation':<15}{'Result'}")
print("-" * 30)
print(f"{'Addition':<15}{addition}")
print(f"{'Subtraction':<15}{subtraction}")
print(f"{'Multiplication':<15}{multiplication}")
print(f"{'Division':<15}{division}")
print(f"{'Floor Division':<15}{floor_division}")
print(f"{'Modulus':<15}{modulus}")
print("-" * 30)
