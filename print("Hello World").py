print("Hello World")

#Lindsey Southall
#CIS261
#WK10 VIBE Coding

FILENAME = "student_grades.txt"

class Student:
    def __init__(self, name, student_id, test1, test2, test3):
        self.name = name
        self.student_id = student_id
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        return (self.test1 + self.test2 + self.test3) / 3

    def calculate_grade(self):
        if self.average >= 90:
            return "A"
        elif self.average >= 80:
            return "B"
        elif self.average >= 70:
            return "C"
        elif self.average >= 60:
            return "D"
        else:
            return "F"

    def to_file_string(self):
        return (
            f"{self.name}|{self.student_id}|"
            f"{self.test1}|{self.test2}|{self.test3}|"
            f"{self.average}|{self.grade}"
        )


def get_test_score(test_name):
    while True:
        try:
            score = float(input(f"Enter {test_name} score: "))

            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def add_student(students):
    print("\nAdd New Student")

    name = input("Enter student name: ")

    if name.upper() == "ESC":
        return

    student_id = input("Enter student ID: ")

    test1 = get_test_score("Test 1")
    test2 = get_test_score("Test 2")
    test3 = get_test_score("Test 3")

    student = Student(
        name,
        student_id,
        test1,
        test2,
        test3
    )

    students.append(student)

    print("\nStudent added successfully.")
    print(f"Average: {student.average:.2f}")
    print(f"Letter Grade: {student.grade}")


def display_all_students(students):
    if len(students) == 0:
        print("\nNo student records found.")
        return

    print("\n" + "=" * 82)
    print("STUDENT GRADE REPORT")
    print("=" * 82)

    print(
        f"{'Name':<20}"
        f"{'ID':<12}"
        f"{'Test 1':>9}"
        f"{'Test 2':>9}"
        f"{'Test 3':>9}"
        f"{'Average':>10}"
        f"{'Grade':>8}"
    )

    print("-" * 82)

    for student in students:
        print(
            f"{student.name:<20}"
            f"{student.student_id:<12}"
            f"{student.test1:>9.2f}"
            f"{student.test2:>9.2f}"
            f"{student.test3:>9.2f}"
            f"{student.average:>10.2f}"
            f"{student.grade:>8}"
        )


def display_class_statistics(students):
    if len(students) == 0:
        print("\nNo student records available.")
        return

    averages = []

    for student in students:
        averages.append(student.average)

    highest_average = max(averages)
    lowest_average = min(averages)
    class_average = sum(averages) / len(averages)

    print("\n" + "=" * 40)
    print("CLASS STATISTICS")
    print("=" * 40)

    print(f"Highest Average: {highest_average:.2f}")
    print(f"Lowest Average:  {lowest_average:.2f}")
    print(f"Class Average:   {class_average:.2f}")


def search_student(students):
    search_name = input("\nEnter student name to search: ")

    found = False

    for student in students:
        if student.name.lower() == search_name.lower():
            print("\nStudent Found")
            print("-" * 30)
            print("Name:", student.name)
            print("Student ID:", student.student_id)
            print(f"Test 1: {student.test1:.2f}")
            print(f"Test 2: {student.test2:.2f}")
            print(f"Test 3: {student.test3:.2f}")
            print(f"Average: {student.average:.2f}")
            print("Letter Grade:", student.grade)

            found = True

    if not found:
        print("\nStudent not found.")


def save_students_to_file(students, filename):
    try:
        with open(filename, "w") as file:
            for student in students:
                file.write(student.to_file_string() + "\n")

        print("Student records saved successfully.")

    except Exception as error:
        print("Error saving student records:", error)


def load_students_from_file(filename):
    students = []

    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) == 7:
                    student = Student(
                        parts[0],
                        parts[1],
                        float(parts[2]),
                        float(parts[3]),
                        float(parts[4])
                    )

                    students.append(student)

        print("Student records loaded successfully.")

    except FileNotFoundError:
        print("No existing student file found.")
        print("Starting with an empty student list.")

    except Exception as error:
        print("Error loading student records:", error)

    return students


def display_menu():
    print("\n" + "=" * 45)
    print("STUDENT GRADE CALCULATOR")
    print("=" * 45)
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Display Class Statistics")
    print("4. Search for Student")
    print("Type ESC to save and exit")


def main():
    students = load_students_from_file(FILENAME)

    while True:
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_all_students(students)

        elif choice == "3":
            display_class_statistics(students)

        elif choice == "4":
            search_student(students)

        elif choice.upper() == "ESC":
            save_students_to_file(students, FILENAME)
            print("\nThank you for using Student Grade Calculator.")
            break

        else:
            print("Invalid choice. Please try again.")


main()

