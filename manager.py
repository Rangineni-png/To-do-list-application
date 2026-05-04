import json
from models import Student, Subject
from exceptions import InvalidDataError, StudentNotFoundError, DataPersistenceError
from calculator import GradeCalculator


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        if any(s.student_id == student.student_id for s in self.students):
            raise InvalidDataError("Student ID already exists.")
        self.students.append(student)

    def update_student(self, student_id: str, **kwargs):
        student = self._find_student(student_id)
        for key, value in kwargs.items():
            if hasattr(student, key):
                setattr(student, key, value)
            else:
                raise InvalidDataError(f"Invalid attribute: {key}")

    def delete_student(self, student_id: str):
        student = self._find_student(student_id)
        self.students.remove(student)

    def search_student(self, query: str):
        results = [s for s in self.students if query.lower() in s.name.lower() or query == s.student_id]
        if not results:
            raise StudentNotFoundError("No student found with the given query.")
        return results

    def display_all_students(self):
        return self.students

    def save_data_to_file(self, filename: str):
        try:
            with open(filename, 'w') as file:
                json.dump([s.__dict__ for s in self.students], file)
        except IOError:
            raise DataPersistenceError("Failed to save data to file.")

    def generate_report(self):
        report = []
        calculator = GradeCalculator()
        for student in self.students:
            calculator.calculate_total_marks(student)
            calculator.calculate_average_marks(student)
            calculator.assign_grade(student)
            report.append({
                'student_id': student.student_id,
                'name': student.name,
                'total_marks': student.total_marks,
                'average_marks': student.average_marks,
                'grade': student.grade
            })
        return report

    def _find_student(self, student_id: str):
        for student in self.students:
            if student.student_id == student_id:
                return student
        raise StudentNotFoundError("Student not found.")