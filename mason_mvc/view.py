'''
View

show the options
prompt the user for their choice

prompt the user for their task name

display tasks from the model

general display (print) function
'''
class TaskView:
    def show_menu(self):
        self.display_message("\nTo-Do List Menu:")
        self.display_message("1. Add Task")
        self.display_message("2. List Tasks")
        self.display_message("3. Exit")

    def get_user_choice(self):
        return input("Choose an option: ")

    def get_task_input(self):
        return input("Enter a new task: ")

    def display_tasks(self, tasks):
        self.display_message("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            self.display_message(f"{idx}. {task}")

    def display_message(self, message):
        print(message)