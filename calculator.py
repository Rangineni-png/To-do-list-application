from models import Student


class GradeCalculator:
    def calculate_total_marks(self, student: Student):
        student.total_marks = sum(subject.marks for subject in student.subjects)

    def calculate_average_marks(self, student: Student):
        if not student.subjects:
            student.average_marks = 0.0
        else:
            student.average_marks = student.total_marks / len(student.subjects)

    def assign_grade(self, student: Student):
        if student.average_marks >= 90:
            student.grade = 'A'
        elif student.average_marks >= 80:
            student.grade = 'B'
        elif student.average_marks >= 70:
            student.grade = 'C'
        elif student.average_marks >= 60:
            student.grade = 'D'
        else:
            student.grade = 'F'