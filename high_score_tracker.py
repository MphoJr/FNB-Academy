# high_score_tracker.py

# Step 1: Start infinite loop
while True:
    # Step 2: Ask for score
    user_input = input("Enter your game score (or type 'stop' to quit): ")

    # Step 3: Check for stop command
    if user_input.strip().lower() == "stop":
        print("Game session ended!")
        break

    # Step 4: Convert input to integer and check score
    try:
        score = int(user_input)
        if score > 100:
            print("Wow! That’s a new high score!")
        else:
            print("Good try, keep playing!")
    except ValueError:
        print("⚠️ Invalid input. Please enter a number or 'stop'.")
