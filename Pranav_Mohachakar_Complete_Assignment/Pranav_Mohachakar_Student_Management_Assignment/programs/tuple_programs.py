"""Tuple exercises: immutable student identifiers."""
def main():
    roll_number = input("Enter roll number: ").strip()
    registration_number = input("Enter registration number: ").strip()
    date_of_birth = input("Enter date of birth (DD-MM-YYYY): ").strip()
    student_identifiers = (roll_number, registration_number, date_of_birth)
    print("Student identifiers (tuple):", student_identifiers)
    print("Roll number:", student_identifiers[0])
if __name__ == "__main__":
    main()
