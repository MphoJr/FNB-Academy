# grade_classifier.py

# Step 1: Collect learner name and marks
name = input("Enter learner's name: ")
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Step 2: Calculate average
average = (subject1 + subject2 + subject3) / 3

# Step 3: Assign grade using conditionals
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Step 4: Assign status (Pass/Fail)
status = "Pass" if average >= 50 else "Fail"

# Step 5: Check for intervention flags
interventions = []
if subject1 < 40:
    interventions.append("Subject 1 needs intervention")
if subject2 < 40:
    interventions.append("Subject 2 needs intervention")
if subject3 < 40:
    interventions.append("Subject 3 needs intervention")

# Step 6: Display formatted report card
print("\n--- STUDENT REPORT CARD ---")
print(f"Learner Name: {name}")
print(f"Subject 1 Marks: {subject1}")
print(f"Subject 2 Marks: {subject2}")
print(f"Subject 3 Marks: {subject3}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
print(f"Status: {status}")

# Display intervention flags if any
if interventions:
    print("\nIntervention Required:")
    for flag in interventions:
        print(f"- {flag}")
else:
    print("\nNo interventions required.")
print("----------------------------")
