import pytest
import json
from data_parser import load_data_from_file
from models import Student, Subject
from exceptions import DataPersistenceError


def test_load_data_from_file(tmp_path):
    data = [
        {
            'student_id': 'S001',
            'name': 'John Doe',
            'email': 'john@example.com',
            'course': 'CS',
            'subjects': [
                {'name': 'Python', 'marks': 90},
                {'name': 'Math', 'marks': 80}
            ]
        }
    ]
    file_path = tmp_path / "students.json"
    with open(file_path, 'w') as file:
        json.dump(data, file)

    students = load_data_from_file(file_path)
    assert len(students) == 1
    assert students[0].student_id == 'S001'
    assert len(students[0].subjects) == 2


def test_load_data_from_file_invalid_json(tmp_path):
    file_path = tmp_path / "students.json"
    with open(file_path, 'w') as file:
        file.write("Invalid JSON")

    with pytest.raises(DataPersistenceError):
        load_data_from_file(file_path)


def test_load_data_from_file_io_error():
    with pytest.raises(DataPersistenceError):
        load_data_from_file("non_existent_file.json")
