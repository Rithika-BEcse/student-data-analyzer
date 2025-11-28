# Student Data Analyzer (Simple Python Project)
# This script analyzes students' scores and prints performance insights

students = [
    {"name": "Arun", "marks": 78},
    {"name": "Riya", "marks": 92},
    {"name": "Kavin", "marks": 65},
    {"name": "Sara", "marks": 88},
]

# Calculate class average
total = sum(s["marks"] for s in students)
avg = total / len(students)

print(f"Class Average: {avg}")

# Print students scoring above average
print("\nStudents above class average:")
for s in students:
    if s["marks"] > avg:
        print(f"- {s['name']} ({s['marks']} marks)")
