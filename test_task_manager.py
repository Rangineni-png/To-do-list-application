import pytest
from task_manager import TaskManager
from models import Task
from exceptions import InvalidTaskError, TaskNotFoundError, FileOperationError
import os
import json

@pytest.fixture
def task_manager(tmp_path):
    file_path = tmp_path / 'tasks.json'
    return TaskManager(file_path=str(file_path))

@pytest.fixture
def sample_task():
    return Task(1, 'Sample Task')

# Test add_task

def test_add_task(task_manager):
    task_manager.add_task('New Task')
    assert len(task_manager.view_tasks()) == 1
    assert task_manager.view_tasks()[0].description == 'New Task'

def test_add_task_empty_description(task_manager):
    with pytest.raises(InvalidTaskError):
        task_manager.add_task('')

# Test view_tasks

def test_view_tasks(task_manager):
    task_manager.add_task('Task 1')
    task_manager.add_task('Task 2')
    tasks = task_manager.view_tasks()
    assert len(tasks) == 2
    assert tasks[0].description == 'Task 1'
    assert tasks[1].description == 'Task 2'

# Test mark_task_completed

def test_mark_task_completed(task_manager):
    task_manager.add_task('Task to Complete')
    task_manager.mark_task_completed(1)
    assert task_manager.view_tasks()[0].completed is True

def test_mark_task_completed_invalid_id(task_manager):
    with pytest.raises(TaskNotFoundError):
        task_manager.mark_task_completed(999)

# Test delete_task

def test_delete_task(task_manager):
    task_manager.add_task('Task to Delete')
    task_manager.delete_task(1)
    assert len(task_manager.view_tasks()) == 0

def test_delete_task_invalid_id(task_manager):
    with pytest.raises(TaskNotFoundError):
        task_manager.delete_task(999)

# Test save_tasks and load_tasks

def test_save_and_load_tasks(task_manager):
    task_manager.add_task('Persistent Task')
    task_manager.save_tasks()
    new_manager = TaskManager(file_path=task_manager.file_path)
    assert len(new_manager.view_tasks()) == 1
    assert new_manager.view_tasks()[0].description == 'Persistent Task'

# Test file operation errors

def test_load_tasks_file_not_found(tmp_path):
    file_path = tmp_path / 'non_existent.json'
    manager = TaskManager(file_path=str(file_path))
    assert len(manager.view_tasks()) == 0

# Test internal helper method _find_task_by_id

def test_find_task_by_id(task_manager, sample_task):
    task_manager.add_task(sample_task.description)
    task = task_manager._find_task_by_id(1)
    assert task is not None
    assert task.id == 1
    assert task.description == sample_task.description

def test_find_task_by_id_invalid(task_manager):
    task = task_manager._find_task_by_id(999)
    assert task is None
