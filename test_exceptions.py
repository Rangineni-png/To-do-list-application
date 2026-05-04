from exceptions import InvalidDataError, StudentNotFoundError, DataPersistenceError


def test_invalid_data_error():
    try:
        raise InvalidDataError("Invalid data")
    except InvalidDataError as e:
        assert str(e) == "Invalid data"


def test_student_not_found_error():
    try:
        raise StudentNotFoundError("Student not found")
    except StudentNotFoundError as e:
        assert str(e) == "Student not found"


def test_data_persistence_error():
    try:
        raise DataPersistenceError("Persistence error")
    except DataPersistenceError as e:
        assert str(e) == "Persistence error"
