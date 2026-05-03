class Task:
    def __init__(self, task_id, description, completed=False):
        self.id = task_id
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data['id'], data['description'], data['completed'])

    def __str__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f'Task {self.id}: {self.description} [{status}]'
