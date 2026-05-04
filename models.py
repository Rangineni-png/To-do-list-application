class Subject:
    def __init__(self, name: str, marks: float):
        if not isinstance(name, str):
            raise TypeError("Subject name must be a string.")
        if not isinstance(marks, (int, float)) or not (0 <= marks <= 100):
            raise ValueError("Marks must be a number between 0 and 100.")
        self.name = name
        self.marks = marks


class Student:
    def __init__(self, student_id: str, name: str, email: str, course: str, subjects: list):
        if not isinstance(student_id, str) or not student_id.isalnum():
            raise ValueError("Student ID must be an alphanumeric string.")
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(email, str) or '@' not in email:
            raise ValueError("Invalid email format.")
        if not isinstance(course, str):
            raise TypeError("Course must be a string.")
        if not isinstance(subjects, list) or not all(isinstance(s, Subject) for s in subjects):
            raise TypeError("Subjects must be a list of Subject instances.")
        self.student_id = student_id
        self.name = name
        self.email = email
        self.course = course
        self.subjects = subjects
        self.total_marks = 0.0
        self.average_marks = 0.0
        self.grade = ""