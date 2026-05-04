import pytest
from models import Student, Subject


def test_subject_initialization():
    subject = Subject(name='Python', marks=85.0)
    assert subject.name == 'Python'
    assert subject.marks == 85.0


def test_subject_invalid_name_type():
    with pytest.raises(TypeError):
        Subject(name=123, marks=85.0)


def test_subject_invalid_marks_type():
    with pytest.raises(ValueError):
        Subject(name='Python', marks='eighty')


def test_subject_invalid_marks_range():
    with pytest.raises(ValueError):
        Subject(name='Python', marks=105)


def test_student_initialization():
    subjects = [Subject(name='Python', marks=85.0)]
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=subjects)
    assert student.student_id == 'S001'
    assert student.name == 'John Doe'
    assert student.email == 'john@example.com'
    assert student.course == 'CS'
    assert student.subjects == subjects


def test_student_invalid_email_format():
    subjects = [Subject(name='Python', marks=85.0)]
    with pytest.raises(ValueError):
        Student(student_id='S001', name='John Doe', email='johnexample.com', course='CS', subjects=subjects)


def test_student_invalid_subjects_type():
    with pytest.raises(TypeError):
        Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects='Python')
