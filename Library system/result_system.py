students = {
    "S101": {"name": "Anu", "marks": {"Python": 88, "Maths": 76, "Stats": 92}},
    "S102": {"name": "Binu", "marks": {"Python": 45, "Maths": 38, "Stats": 52}},
    "S103": {"name": "Cathy", "marks": {"Python": 95, "Maths": 91, "Stats": 89}},
    "S104": {"name": "Dev", "marks": {"Python": 60, "Maths": 72, "Stats": 55}},
    "S105": {"name": "Esha", "marks": {"Python": 72, "Maths": 65, "Stats": 80}},
}
 
 
def calculate_total(marks):
    """Return the sum of all marks."""
    total = 0
    for mark in marks.values():
        total += mark
    return total
 
 
def calculate_average(marks):
    """Return the average rounded to 2 decimals."""
    return round(calculate_total(marks) / len(marks), 2)
 
 
def get_grade(average):
    """Return the grade for an average."""
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"
 
 
def check_result(marks, pass_mark=40):
    """Return 'Pass' only if every subject is at least the pass mark."""
    for mark in marks.values():
        if mark < pass_mark:
            return "Fail"
    return "Pass"
 
 
def student_summary(student):
    """Return a summary dictionary for one student."""
    marks = student["marks"]
    average = calculate_average(marks)
    return {
        "name": student["name"],
        "total": calculate_total(marks),
        "average": average,
        "grade": get_grade(average),
        "result": check_result(marks),
    }
 
 
def add_student(data, student_id, name, **marks):
    """Add a student; return False if the id already exists."""
    if student_id in data:
        return False
    data[student_id] = {"name": name, "marks": dict(marks)}
    return True
 
 
def update_marks(data, student_id, **changes):
    """Update marks of a student; return False if the id does not exist."""
    if student_id not in data:
        return False
    data[student_id]["marks"].update(changes)
    return True
 
 
def remove_student(data, student_id):
    """Remove a student; return False if the id does not exist."""
    if student_id not in data:
        return False
    data.pop(student_id)
    return True
 
 
def print_report(data):
    """Print the report, sorted by average (highest first)."""
    print(f"{'ID':<6}{'Name':<8}{'Total':>6}{'Avg':>8}{'Grade':>7}  Result")
    print("-" * 42)
 
    ranking = []
    for student_id, student in data.items():
        ranking.append((calculate_average(student["marks"]), student_id))
    ranking.sort(reverse=True)
 
    for average, student_id in ranking:
        summary = student_summary(data[student_id])
        print(
            f"{student_id:<6}{summary['name']:<8}{summary['total']:>6}"
            f"{average:>8.2f}{summary['grade']:>7}  {summary['result']}"
        )
 
 
def class_statistics(data, *subjects):
    """Return topper, pass percentage and subject averages."""
    topper_name = ""
    best_average = -1
    passed = 0
    for student in data.values():
        average = calculate_average(student["marks"])
        if average > best_average:
            best_average = average
            topper_name = student["name"]
        if check_result(student["marks"]) == "Pass":
            passed += 1
    pass_percentage = round(passed / len(data) * 100, 1)
 
    if not subjects:
        subjects = []
        for student in data.values():
            for subject in student["marks"]:
                if subject not in subjects:
                    subjects.append(subject)
 
    subject_averages = {}
    for subject in subjects:
        scores = [s["marks"][subject] for s in data.values() if subject in s["marks"]]
        subject_averages[subject] = round(sum(scores) / len(scores), 1)
 
    return {
        "topper": topper_name,
        "pass_percentage": pass_percentage,
        "subject_averages": subject_averages,
    }
 
 
def main():
    print("Task 1: One student")
    print(student_summary(students["S101"]))
    print(check_result(students["S102"]["marks"]))
    print(check_result(students["S102"]["marks"], pass_mark=35))
    print(check_result(students["S102"]["marks"], 35))
    print()
 
    print("Task 2: Report")
    print_report(students)
    print()
 
    print("Task 3: Update marks")
    print(update_marks(students, "S102", Maths=55))
    print(update_marks(students, "S999", Maths=50))
    corrections = {"Python": 50, "Stats": 58}
    print(update_marks(students, "S102", **corrections))
    print(student_summary(students["S102"]))
    print()
 
    print("Task 4: Add student")
    print(add_student(students, "S106", "Farhan", Python=70, Maths=35, Stats=74))
    print(add_student(students, "S101", "Zara"))
    print(students["S106"])
    print()
 
    print("Task 5: Remove student")
    print(remove_student(students, "S104"))
    print(remove_student(students, "S104"))
    print(len(students))
    print()
 
    print("Task 6: Final report and statistics")
    print_report(students)
    stats = class_statistics(students)
    print(f"Topper: {stats['topper']}")
    print(f"Pass percentage: {stats['pass_percentage']}")
    print(f"Subject averages: {stats['subject_averages']}")
    partial = class_statistics(students, "Python", "Stats")
    print(f"Python and Stats only: {partial['subject_averages']}")
 
 
main()
 