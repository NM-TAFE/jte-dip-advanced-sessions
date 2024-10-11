# model.py

import business_logic

class TaskModel:
    def __init__(self):
        pass

    def initialize_app(self):
        business_logic.initialize_app()

    def add_task(self, task_description):
        business_logic.add_task(task_description)

    def get_all_tasks(self):
        return business_logic.get_all_tasks()

