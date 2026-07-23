# grade_report.py

# Step 1: Store students as list of dictionaries
students = [
    {"name": "Mpho", "maths": 85, "english": 72, "science": 90},
    {"name": "Sipho", "maths": 60, "english": 55, "science": 70},
    {"name": "Thandi", "maths": 45, "english": 38, "science": 50},
    {"name": "Naledi", "maths": 78, "english": 82, "science": 88},
    {"name": "Kabelo", "maths": 30, "english": 40, "science": 35}
]

# Step 2: Results list
results = []

# Step 3: Grade logic function
def assign_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

# Step 4: Process each student
for student in students:
    average = (student["maths"] + student["english"] + student["science"]) / 3
    grade = assign_grade(average)
    status = "Pass" if average >= 50 else "Fail"
    results.append({
        "name": student["name"],
        "average": round(average, 2),
        "grade": grade,
        "status": status
    })

# Step 5: Class statistics
averages = [r["average"] for r in results]
class_average = sum(averages) / len(averages)
highest_mark = max(averages)
lowest_mark = min(averages)

# Step 6: Display report
print("\n--- CLASS REPORT ---")
for r in results:
    print(f"Name: {r['name']}, Average: {r['average']}, Grade: {r['grade']}, Status: {r['status']}")
print("\n--- CLASS STATISTICS ---")
print(f"Class Average: {class_average:.2f}")
print(f"Highest Average: {highest_mark:.2f}")
print(f"Lowest Average: {lowest_mark:.2f}")
print("----------------------")

# Step 7: Search loop
while True:
    search_name = input("\nEnter a student name to search (or type 'exit' to quit): ").strip().lower()
    if search_name == "exit":
        print("Search session ended.")
        break
    found = None
    for r in results:
        if r["name"].lower() == search_name:
            found = r
            break
    if found:
        print(f"🔎 Found: Name: {found['name']}, Average: {found['average']}, Grade: {found['grade']}, Status: {found['status']}")
    else:
        print("⚠️ Student not found.")
