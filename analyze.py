# Analyzing student data (basic example)

students = [
    {"name": "Arun", "marks": 78},
    {"name": "Riya", "marks": 92},
    {"name": "Kavin", "marks": 65},
    {"name": "Sara", "marks": 88},
]

# Print high scorers
for s in students:
    if s["marks"] > 80:
        print(f"{s['name']} scored above 80")
