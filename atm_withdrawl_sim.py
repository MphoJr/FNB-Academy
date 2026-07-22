# atm_withdrawal_simulator_loop.py

# Step 1: Set a fixed bank balance
balance = 500.0

print("\n--- SMART ATM SIMULATOR ---")
print(f"Your starting balance is: R{balance:.2f}")

# Step 2: Loop for multiple transactions
while True:
    withdrawal = float(input("\nEnter the amount you want to withdraw (or 0 to exit): R"))

    # Step 3: Check conditions
    if withdrawal == 0:
        print("Transaction ended. Thank you for using Smart ATM.")
        break
    elif withdrawal < 0:
        print("Invalid amount. You must withdraw more than R0.")
    elif withdrawal <= balance:
        balance -= withdrawal
        print(f"Withdrawal successful! Remaining balance: R{balance:.2f}")
        if balance == 0:
            print("Your balance is now R0. No further withdrawals possible.")
            break
    else:
        print("Declined. Insufficient funds.")

    # Optional: Ask if user wants another transaction
    choice = input("Do you want another transaction? (yes/no): ").lower()
    if choice != "yes":
        print("Transaction session ended. Goodbye!")
        break
