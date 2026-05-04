import pytest
from calculator import GradeCalculator
from models import Student, Subject


def test_calculate_total_marks():
    calculator = GradeCalculator()
    subjects = [Subject(name='Python', marks=90), Subject(name='Math', marks=80)]
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=subjects)
    calculator.calculate_total_marks(student)
    assert student.total_marks == 170


def test_calculate_average_marks():
    calculator = GradeCalculator()
    subjects = [Subject(name='Python', marks=90), Subject(name='Math', marks=80)]
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=subjects)
    calculator.calculate_total_marks(student)
    calculator.calculate_average_marks(student)
    assert student.average_marks == 85


def test_calculate_average_marks_no_subjects():
    calculator = GradeCalculator()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    calculator.calculate_total_marks(student)
    calculator.calculate_average_marks(student)
    assert student.average_marks == 0.0


def test_assign_grade_A():
    calculator = GradeCalculator()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    student.average_marks = 95
    calculator.assign_grade(student)
    assert student.grade == 'A'


def test_assign_grade_B():
    calculator = GradeCalculator()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    student.average_marks = 85
    calculator.assign_grade(student)
    assert student.grade == 'B'


def test_assign_grade_C():
    calculator = GradeCalculator()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    student.average_marks = 75
    calculator.assign_grade(student)
    assert student.grade == 'C'


def test_assign_grade_D():
    calculator = GradeCalculator()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    student.average_marks = 65
    calculator.assign_grade(student)
    assert student.grade == 'D'


def test_assign_grade_F():
    calculator = GradeCalculator()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    student.average_marks = 55
    calculator.assign_grade(student)
    assert student.grade == 'F'
