# fuel_cost_calculator.py

# Step 1: Ask the user for kilometers to drive
kilometers = float(input("Enter the number of kilometers you want to drive: "))

# Step 2: Ask for current petrol price per liter
petrol_price = float(input("Enter the current petrol price per liter (e.g., 22.45): "))

# Step 3: Calculate liters needed (1 liter per 10 km)
liters_needed = kilometers / 10

# Step 4: Calculate total cost
total_cost = liters_needed * petrol_price

# Step 5: Round to 2 decimal places
total_cost = round(total_cost, 2)

# Step 6: Calculate cost per 100 km
cost_per_100km = round((100 / 10) * petrol_price, 2)

# Step 7: Display results
print("\n--- FUEL COST CALCULATOR ---")
print(f"Distance to drive: {kilometers:.2f} km")
print(f"Petrol price: R{petrol_price:.2f} per liter")
print(f"Liters needed: {liters_needed:.2f} L")
print(f"Total cost: R{total_cost:.2f}")
print(f"Cost per 100 km: R{cost_per_100km:.2f}")
print("-----------------------------")
