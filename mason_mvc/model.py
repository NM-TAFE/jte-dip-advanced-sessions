'''
Model

contains the task list
adds tasks to list
get the tasks in the list
'''

class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks