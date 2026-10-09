"""Core operations for the Student Record Management System."""


class StudentManagementSystem:
    """Manage student dictionaries indexed by unique roll number."""

    def __init__(self):
        self.students = {}  # roll number -> student dictionary

    @staticmethod
    def _validate(student):
        required = ("roll_number", "name", "department", "email", "address",
                    "subjects", "marks", "attendance")
        missing = [field for field in required if field not in student]
        if missing:
            raise ValueError("Missing fields: " + ", ".join(missing))
        if not str(student["roll_number"]).strip():
            raise ValueError("Roll number cannot be empty.")
        if not str(student["name"]).strip():
            raise ValueError("Name cannot be empty.")
        if not isinstance(student["subjects"], list):
            raise ValueError("Subjects must be a list.")
        if not isinstance(student["marks"], list) or not student["marks"]:
            raise ValueError("Enter at least one mark.")
        if any(not isinstance(mark, (int, float)) or mark < 0 or mark > 100
               for mark in student["marks"]):
            raise ValueError("Marks must be numeric values from 0 to 100.")
        attendance = student["attendance"]
        if not isinstance(attendance, (int, float)) or not 0 <= attendance <= 100:
            raise ValueError("Attendance must be between 0 and 100.")

    @staticmethod
    def _with_average(student):
        result = dict(student)
        result["subjects"] = list(student["subjects"])
        result["marks"] = list(student["marks"])
        result["average"] = sum(result["marks"]) / len(result["marks"])
        return result

    def add_student(self, student):
        self._validate(student)
        roll = str(student["roll_number"]).strip()
        if roll in self.students:
            raise ValueError("A record with this roll number already exists.")
        record = dict(student)
        record["roll_number"] = roll
        record["name"] = str(record["name"]).strip()
        record["department"] = str(record["department"]).strip()
        record["email"] = str(record["email"]).strip()
        record["address"] = str(record["address"]).strip()
        self.students[roll] = record

    def search_student(self, roll_number):
        student = self.students.get(str(roll_number).strip())
        return self._with_average(student) if student else None

    def update_student(self, roll_number, updates):
        roll = str(roll_number).strip()
        if roll not in self.students:
            raise ValueError("Student not found.")
        allowed = {"name", "department", "email", "address", "subjects", "marks", "attendance"}
        if not set(updates).issubset(allowed):
            raise ValueError("One or more fields cannot be updated.")
        candidate = dict(self.students[roll])
        candidate.update(updates)
        self._validate(candidate)
        if not candidate["name"].strip():
            raise ValueError("Name cannot be empty.")
        self.students[roll] = candidate

    def delete_student(self, roll_number):
        return self.students.pop(str(roll_number).strip(), None) is not None

    def list_students(self):
        return [self._with_average(self.students[roll]) for roll in sorted(self.students)]

    def class_average(self):
        all_marks = [mark for student in self.students.values() for mark in student["marks"]]
        return sum(all_marks) / len(all_marks) if all_marks else None

    def highest_scorer(self):
        if not self.students:
            return None
        candidates = [self._with_average(student) for student in self.students.values()]
        return max(candidates, key=lambda student: max(student["marks"]))

    def by_department(self, department):
        wanted = str(department).strip().casefold()
        return [self._with_average(student) for student in self.students.values()
                if student["department"].casefold() == wanted]

    def count_students(self):
        return len(self.students)

    def departments(self):
        return {student["department"] for student in self.students.values()}

    def subjects(self):
        return {subject for student in self.students.values() for subject in student["subjects"]}
