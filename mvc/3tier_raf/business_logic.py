# business_logic.py

import data_layer

def initialize_app():
    data_layer.initialize_database()

def add_task(task_description):
    data_layer.add_task_to_db(task_description)

def get_all_tasks():
    return data_layer.get_all_tasks_from_db()

