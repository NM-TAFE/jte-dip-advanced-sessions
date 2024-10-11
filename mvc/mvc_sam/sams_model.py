# todo_app.py
from __future__ import annotations


class data:

    _instances = None

    def __new__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__new__(cls)
            cls._instances._tasks = []
        return cls._instances

    def get_tasks(self):
        return self._tasks

    def add_task(self,new_task):
        self._tasks.append(new_task)

class Presentation:
    _instances = None


    def __new__(cls, data_cls , *args, **kwargs):
        if cls._instances is None:

            cls._instances = super().__new__(cls)
            cls._instances._data_interface: object = data_cls
            #cls._data_interface = None
        return cls._instances

    def list_tasks(self):  # presintaions
        print("\nYour Tasks:")
        for idx, task in enumerate(self._data_interface.get_tasks(), start=1):
            print(f"{idx}. {task}")

    def accspet_input(self):
        while True:
            print("\nTo-Do List Menu:")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                task = input("Enter a new task: ")
                self._data_interface.add_task(task)
                print("Task added!")
            elif choice == '2':
                self.list_tasks()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")

the_data = data()
the_presintation = Presentation(the_data)

def main():
    the_presintation.accspet_input()

if __name__ == "__main__":
    main()