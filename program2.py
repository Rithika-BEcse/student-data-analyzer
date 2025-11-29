# Student Analyzer - Program 2
# This script calculates the average score of a student and classifies the performance.

def calculate_average(marks):
    return sum(marks) / len(marks)

def classify_student(avg):
    if avg >= 90:
        return "Outstanding"
    elif avg >= 75:
        return "Excellent"
    elif avg >= 60:
        return "Good"
    elif avg >= 40:
        return "Needs Improvement"
    else:
        return "Fail"

# Sample marks (you can modify later)
marks = [85, 92, 78, 88, 90]

avg_score = calculate_average(marks)
performance = classify_student(avg_score)

print("Student Marks:", marks)
print("Average Score:", avg_score)
print("Performance Level:", performance)
