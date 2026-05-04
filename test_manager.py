import pytest
from manager import StudentManager
from models import Student, Subject
from exceptions import InvalidDataError, StudentNotFoundError, DataPersistenceError


def test_add_student():
    manager = StudentManager()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    manager.add_student(student)
    assert len(manager.students) == 1


def test_add_student_duplicate_id():
    manager = StudentManager()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    manager.add_student(student)
    with pytest.raises(InvalidDataError):
        manager.add_student(student)


def test_update_student():
    manager = StudentManager()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    manager.add_student(student)
    manager.update_student('S001', name='Jane Doe')
    assert manager.students[0].name == 'Jane Doe'


def test_update_student_invalid_attribute():
    manager = StudentManager()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    manager.add_student(student)
    with pytest.raises(InvalidDataError):
        manager.update_student('S001', age=20)


def test_delete_student():
    manager = StudentManager()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    manager.add_student(student)
    manager.delete_student('S001')
    assert len(manager.students) == 0


def test_delete_student_not_found():
    manager = StudentManager()
    with pytest.raises(StudentNotFoundError):
        manager.delete_student('S001')


def test_search_student_by_id():
    manager = StudentManager()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    manager.add_student(student)
    results = manager.search_student('S001')
    assert len(results) == 1
    assert results[0].student_id == 'S001'


def test_search_student_by_name():
    manager = StudentManager()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    manager.add_student(student)
    results = manager.search_student('john')
    assert len(results) == 1
    assert results[0].name == 'John Doe'


def test_search_student_not_found():
    manager = StudentManager()
    with pytest.raises(StudentNotFoundError):
        manager.search_student('S001')


def test_display_all_students():
    manager = StudentManager()
    student1 = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    student2 = Student(student_id='S002', name='Jane Doe', email='jane@example.com', course='CS', subjects=[])
    manager.add_student(student1)
    manager.add_student(student2)
    students = manager.display_all_students()
    assert len(students) == 2


def test_save_data_to_file(tmp_path):
    manager = StudentManager()
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=[])
    manager.add_student(student)
    file_path = tmp_path / "students.json"
    manager.save_data_to_file(file_path)
    assert file_path.exists()


def test_generate_report():
    manager = StudentManager()
    subjects = [Subject(name='Python', marks=90), Subject(name='Math', marks=80)]
    student = Student(student_id='S001', name='John Doe', email='john@example.com', course='CS', subjects=subjects)
    manager.add_student(student)
    report = manager.generate_report()
    assert len(report) == 1
    assert report[0]['student_id'] == 'S001'
    assert report[0]['grade'] == 'B'
