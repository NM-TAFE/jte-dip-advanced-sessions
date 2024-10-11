class View:
    def show_menu(self):
        print("\nTo-Do List Menu:\n1. Add Task\n2. List Tasks\n3. Exit")
    def get_choice(self):
        return input("Choose an option: ")
    def get_task(self):
        return input("Enter a new task: ")
    def show_tasks(self, tasks):
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    def show_message(self, message):
        print(message)
#==============================================================================
class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_choice()
            if choice == '1':
                task = self.view.get_task()
                self.model.add_task(task)
                self.view.show_message("Task added!")
            elif choice == '2':
                tasks = self.model.list_tasks()
                self.view.show_tasks(tasks)
            elif choice == '3':
                self.view.show_message("Goodbye!")
                break
            else:
                self.view.show_message("Invalid option. Try again.")
#==============================================================================
class Model:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def list_tasks(self):
        return self.tasks
#============================================================================== 
if __name__ == "__main__":
    view = View()
    model = Model()
    controller = Controller(view, model)
    controller.run()