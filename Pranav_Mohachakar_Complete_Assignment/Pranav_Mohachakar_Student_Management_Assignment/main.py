"""
Student Record and Academic Management System
Student: Pranav Mohachakar | PRN: 2126 | Course: UMLM1016

Run with: python main.py
Data is held in memory during the current run; it is not saved between runs.
"""

from student_management import StudentManagementSystem


def prompt_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a whole number.")


def prompt_marks():
    while True:
        raw = input("Enter marks separated by commas (example 78, 85, 91): ").strip()
        try:
            marks = [float(item.strip()) for item in raw.split(",") if item.strip()]
            if not marks or any(mark < 0 or mark > 100 for mark in marks):
                raise ValueError
            return marks
        except ValueError:
            print("Enter one or more numeric marks between 0 and 100.")


def add_student(system):
    print("\n--- Add Student ---")
    roll = input("Roll number: ").strip()
    name = input("Full name: ").strip()
    department = input("Department: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()
    subjects = [s.strip() for s in input("Subjects separated by commas: ").split(",") if s.strip()]
    marks = prompt_marks()
    attendance = input("Attendance percentage (0-100): ").strip()
    try:
        attendance = float(attendance)
    except ValueError:
        print("Attendance must be numeric.")
        return
    student = {
        "roll_number": roll,
        "name": name,
        "department": department,
        "email": email,
        "address": address,
        "subjects": subjects,
        "marks": marks,
        "attendance": attendance,
    }
    try:
        system.add_student(student)
        print("Student record added successfully.")
    except ValueError as error:
        print(f"Could not add record: {error}")


def print_student(student):
    print("-" * 45)
    print(f"Roll number : {student['roll_number']}")
    print(f"Name        : {student['name']}")
    print(f"Department  : {student['department']}")
    print(f"Email       : {student['email']}")
    print(f"Address     : {student['address']}")
    print(f"Subjects    : {', '.join(student['subjects'])}")
    print(f"Marks       : {', '.join(map(str, student['marks']))}")
    print(f"Average     : {student['average']:.2f}")
    print(f"Attendance  : {student['attendance']:.2f}%")
    print("-" * 45)


def main():
    system = StudentManagementSystem()
    menu = """
====== STUDENT RECORD MANAGEMENT SYSTEM ======
1. Add student
2. Search by roll number
3. Update student
4. Delete student
5. Display all students
6. Calculate class average
7. Find highest scorer
8. List students by department
9. Count students
0. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student(system)
        elif choice == "2":
            roll = input("Enter roll number: ").strip()
            student = system.search_student(roll)
            if student:
                print_student(student)
            else:
                print("No student found with that roll number.")
        elif choice == "3":
            roll = input("Enter roll number to update: ").strip()
            student = system.search_student(roll)
            if not student:
                print("Student not found.")
                continue
            print("Leave a field blank to keep its current value.")
            updates = {}
            for field, label in [("name", "Name"), ("department", "Department"),
                                 ("email", "Email"), ("address", "Address")]:
                value = input(f"{label} [{student[field]}]: ").strip()
                if value:
                    updates[field] = value
            subjects = input("Subjects, comma-separated (blank to keep): ").strip()
            if subjects:
                updates["subjects"] = [s.strip() for s in subjects.split(",") if s.strip()]
            marks = input("Marks, comma-separated (blank to keep): ").strip()
            if marks:
                try:
                    parsed = [float(x.strip()) for x in marks.split(",") if x.strip()]
                    if not parsed or any(x < 0 or x > 100 for x in parsed):
                        raise ValueError
                    updates["marks"] = parsed
                except ValueError:
                    print("Invalid marks; marks were not updated.")
            attendance = input("Attendance percentage (blank to keep): ").strip()
            if attendance:
                try:
                    value = float(attendance)
                    if not 0 <= value <= 100:
                        raise ValueError
                    updates["attendance"] = value
                except ValueError:
                    print("Invalid attendance; attendance was not updated.")
            try:
                system.update_student(roll, updates)
                print("Student record updated.")
            except ValueError as error:
                print(error)
        elif choice == "4":
            roll = input("Enter roll number to delete: ").strip()
            if system.delete_student(roll):
                print("Student record deleted.")
            else:
                print("Student not found.")
        elif choice == "5":
            records = system.list_students()
            if not records:
                print("No records available.")
            for student in records:
                print_student(student)
        elif choice == "6":
            average = system.class_average()
            print("Class average:", "No marks available" if average is None else f"{average:.2f}")
        elif choice == "7":
            student = system.highest_scorer()
            if student:
                print("Highest scorer:")
                print_student(student)
            else:
                print("No marks available.")
        elif choice == "8":
            department = input("Department name: ").strip()
            records = system.by_department(department)
            for student in records:
                print_student(student)
            if not records:
                print("No students found in that department.")
        elif choice == "9":
            print("Total students:", system.count_students())
        elif choice == "0":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid option. Choose from the menu.")


if __name__ == "__main__":
    main()
