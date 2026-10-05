# Student Performance Analyzer
# Features:
#   - Look up a student's grade or overall average
#   - Rank students from highest to lowest (and lowest to highest)
#   - Class average (total or by subject)
#   - Passing percentage (passing = 70%)
#   - Students needing help
#   - Save and quit / exit without saving

import csv

PASSING_GRADE = 70.0
SUBJECTS = ["math", "science", "english"]


def load_csv(filename):
    students = []
    try:
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(row)
        return students
    except FileNotFoundError:
        print("Gradebook not found!")
        print("Starting with an empty gradebook")
        return []


def calculate_average(student):
    """Return one student's average across all subjects."""
    grades = [float(student[subject]) for subject in SUBJECTS]
    return sum(grades) / len(grades)


def average_grade(students):
    if not students:
        print("No students in gradebook")
        return

    who = input("Enter the student's name: ").strip().lower()

    for student in students:
        if student["name"].strip().lower() == who:
            decision = input("Which subject? (math, science, english, or all): ").strip().lower()

            if decision in SUBJECTS:
                if student[decision]:
                    print(f"{student['name']}'s {decision} grade is {float(student[decision]):.2f}")
                else:
                    print(f"No {decision} grade yet")
            elif decision == "all":
                print(f"{student['name']}'s overall average is {calculate_average(student):.2f}")
            else:
                print("Please enter math, science, english, or all")
            return  # found the student, we're done

    print("Student's name not found")


def highest_student(students):
    if not students:
        print("No students in gradebook")
        return

    ranked = sorted(students, key=calculate_average, reverse=True)

    print("Students sorted by average, highest to lowest:")
    for student in ranked:
        print(f"  {student['name']}: {calculate_average(student):.2f}")


def lowest_student(students):
    if not students:
        print("No students in gradebook")
        return

    ranked = sorted(students, key=calculate_average)

    print("Students sorted by average, lowest to highest:")
    for student in ranked:
        print(f"  {student['name']}: {calculate_average(student):.2f}")


def class_average(students):
    if not students:
        print("No students in gradebook")
        return

    where = input("Average by subject (math, science, english) or total? ").strip().lower()

    if where in ["total", "total average", "all"]:
        everyone = sum(calculate_average(student) for student in students) / len(students)
        print(f"The class total average is {everyone:.2f}")

    elif where in SUBJECTS:
        subject_average = sum(float(student[where]) for student in students) / len(students)
        print(f"The class {where} average is {subject_average:.2f}")

    else:
        print("Invalid option! Please try again!")


def passing_percentage(students):
    if not students:
        print("No students in gradebook")
        return

    passed = 0
    for student in students:
        if calculate_average(student) >= PASSING_GRADE:
            passed += 1

    total_percentage = (passed / len(students)) * 100
    print(f"{total_percentage:.2f}% of students are passing ({passed} of {len(students)})")


def need_help(students):
    if not students:
        print("No students in gradebook")
        return

    struggling = [
        (student["name"], calculate_average(student))
        for student in students
        if calculate_average(student) < PASSING_GRADE
    ]

    if not struggling:
        print("Every student is passing!")
        return

    print("Students below passing who may need help:")
    for name, average in struggling:
        print(f"  {name}: {average:.2f}")


def save_csv(students, filename="New_student.csv"):
    if not students:
        print("No records to save")
        return

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=students[0].keys())
        writer.writeheader()
        for student in students:
            writer.writerow(student)

    print(f"Gradebook saved to {filename} successfully!")


def main(students):
    print("\n" + "=" * 50)
    print("             STUDENT GRADE BOOK")
    print("=" * 50)

    while True:
        print("\n" + "=" * 50)
        print("1. Average grade")
        print("2. Highest student")
        print("3. Lowest student")
        print("4. Class average")
        print("5. Passing percentage")
        print("6. Students needing help")
        print("7. Save and exit")
        print("8. Exit without saving")

        choice = input("Choose one of the eight available options (1-8): ").strip()

        if choice == "1":
            average_grade(students)
        elif choice == "2":
            highest_student(students)
        elif choice == "3":
            lowest_student(students)
        elif choice == "4":
            class_average(students)
        elif choice == "5":
            passing_percentage(students)
        elif choice == "6":
            need_help(students)
        elif choice == "7":
            save_csv(students)
            print("Goodbye!")
            break
        elif choice == "8":
            print("Thanks for using the Student Performance Analyzer! Goodbye!")
            break
        else:
            print("Please enter a valid option")


if __name__ == "__main__":
    students = load_csv("students.csv")
    main(students)
