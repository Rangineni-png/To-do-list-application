import json
import os
from models import Task
from exceptions import InvalidTaskError, TaskNotFoundError, FileOperationError

class TaskManager:
    def __init__(self, file_path='tasks.json'):
        self.file_path = file_path
        self.tasks = []
        self.load_tasks()

    def add_task(self, description):
        description = description.strip()
        if not description:
            raise InvalidTaskError('Task description cannot be empty.')
        task_id = len(self.tasks) + 1
        task = Task(task_id, description)
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        return self.tasks

    def mark_task_completed(self, task_id):
        task = self._find_task_by_id(task_id)
        if task:
            task.completed = True
            self.save_tasks()
        else:
            raise TaskNotFoundError(f'Task with ID {task_id} not found.')

    def delete_task(self, task_id):
        task = self._find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
        else:
            raise TaskNotFoundError(f'Task with ID {task_id} not found.')

    def save_tasks(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump([task.to_dict() for task in self.tasks], file)
        except IOError:
            raise FileOperationError('Failed to save tasks to file.')

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            return
        try:
            with open(self.file_path, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(data) for data in tasks_data]
        except (IOError, json.JSONDecodeError):
            raise FileOperationError('Failed to load tasks from file.')

    def _find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
