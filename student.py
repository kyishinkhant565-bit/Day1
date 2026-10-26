# Student Performance Report System

# Fixed grade categories stored in a tuple
GRADE_CATEGORIES = ("A", "B", "C", "D", "F")

# List of dictionaries to store student records
students = []


def classify_grade(score):
    """Classify a student's Python score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_average(records):
    """Calculate the average Python score."""
    total = 0
    for student in records:
        total += student["python_score"]
    return total / len(records) if records else 0


def count_passing_students(records):
    """Count students who pass with a score of 60 or above."""
    count = 0
    for student in records:
        if student["python_score"] >= 60:
            count += 1
    return count


def get_valid_score():
    """Accept only scores between 0 and 100."""
    while True:
        try:
            score = float(input("Enter Python score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Invalid score! Enter a score from 0 to 100.")
        except ValueError:
            print("Please enter a valid number.")


def get_valid_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age > 0:
                return age
            print("Age must be greater than 0.")
        except ValueError:
            print("Please enter a valid whole number.")


def get_valid_study_hours():
    while True:
        try:
            hours = float(input("Enter study hours: "))
            if hours >= 0:
                return hours
            print("Study hours cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


def collect_student_data():
    """Collect data for at least five students."""
    while True:
        try:
            number = int(input("How many students? (Minimum 5): "))
            if number >= 5:
                break
            print("Please enter at least 5 students.")
        except ValueError:
            print("Please enter a valid whole number.")

    for i in range(number):
        print(f"\nEnter information for student {i + 1}")

        name = input("Enter student name: ").strip()
        while not name:
            print("Name cannot be empty.")
            name = input("Enter student name: ").strip()

        age = get_valid_age()
        study_hours = get_valid_study_hours()
        score = get_valid_score()

        student = {
            "name": name,
            "age": age,
            "study_hours": study_hours,
            "python_score": score
        }

        students.append(student)


def display_report(records):
    """Display the complete student performance report."""
    print("\n" + "=" * 75)
    print("             STUDENT PERFORMANCE REPORT")
    print("=" * 75)

    print(f"{'Name':<18}{'Age':<8}{'Study Hours':<15}"
          f"{'Python Score':<15}{'Grade':<8}")
    print("-" * 75)

    for student in records:
        grade = classify_grade(student["python_score"])

        print(
            f"{student['name']:<18}"
            f"{student['age']:<8}"
            f"{student['study_hours']:<15.1f}"
            f"{student['python_score']:<15.1f}"
            f"{grade:<8}"
        )

    average = calculate_average(records)
    passed = count_passing_students(records)
    failed = len(records) - passed

    print("-" * 75)
    print(f"Total students : {len(records)}")
    print(f"Average score  : {average:.2f}")
    print(f"Passing        : {passed}")
    print(f"Failing        : {failed}")
    print(f"Grade categories: {', '.join(GRADE_CATEGORIES)}")
    print("=" * 75)
    


# Main program
collect_student_data()
display_report(students)