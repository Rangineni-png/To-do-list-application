import json
from models import Student, Subject
from exceptions import DataPersistenceError


def load_data_from_file(filename: str):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            students = []
            for item in data:
                subjects = [Subject(name=sub['name'], marks=sub['marks']) for sub in item['subjects']]
                student = Student(
                    student_id=item['student_id'],
                    name=item['name'],
                    email=item['email'],
                    course=item['course'],
                    subjects=subjects
                )
                students.append(student)
            return students
    except (IOError, json.JSONDecodeError):
        raise DataPersistenceError("Failed to load data from file.")