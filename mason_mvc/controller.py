'''
Controller

run loop
control showing options
prompt user for choice
control what happens when user choice selected
handle exits
'''

from model import TaskModel
from view import TaskView

class TaskController:
    def __init__(self):
        self.model = TaskModel()
        self.view = TaskView()

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_user_choice()

            if choice == '1':
                task = self.view.get_task_input()
                self.model.add_task(task)
                self.view.display_message("Task has been added!")
            elif choice == '2':
                tasks = self.model.list_tasks()
                self.view.display_tasks(tasks)
            elif choice == '3':
                self.view.display_message("See you later!")
                break
            else:
                self.view.display_message("Invalid selection. Try again.")