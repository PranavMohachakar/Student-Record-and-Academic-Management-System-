import unittest
from student_management import StudentManagementSystem


def sample(roll="101", name="Asha", dept="AI & ML", marks=None):
    return {
        "roll_number": roll, "name": name, "department": dept,
        "email": "asha@example.com", "address": "Pune",
        "subjects": ["Python", "Maths"], "marks": marks or [80, 90],
        "attendance": 92.0
    }


class StudentManagementTests(unittest.TestCase):
    def setUp(self):
        self.system = StudentManagementSystem()

    def test_add_and_search(self):
        self.system.add_student(sample())
        found = self.system.search_student("101")
        self.assertEqual(found["name"], "Asha")
        self.assertEqual(found["average"], 85)

    def test_duplicate_roll_rejected(self):
        self.system.add_student(sample())
        with self.assertRaises(ValueError):
            self.system.add_student(sample())

    def test_update(self):
        self.system.add_student(sample())
        self.system.update_student("101", {"name": "Asha Patil"})
        self.assertEqual(self.system.search_student("101")["name"], "Asha Patil")

    def test_delete(self):
        self.system.add_student(sample())
        self.assertTrue(self.system.delete_student("101"))
        self.assertIsNone(self.system.search_student("101"))

    def test_invalid_marks_rejected(self):
        with self.assertRaises(ValueError):
            self.system.add_student(sample(marks=[105]))

    def test_department_filter(self):
        self.system.add_student(sample())
        self.assertEqual(len(self.system.by_department("ai & ml")), 1)

    def test_count_and_class_average(self):
        self.system.add_student(sample())
        self.assertEqual(self.system.count_students(), 1)
        self.assertEqual(self.system.class_average(), 85)

    def test_empty_class_average(self):
        self.assertIsNone(self.system.class_average())


if __name__ == "__main__":
    unittest.main(verbosity=2)
