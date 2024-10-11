# presentation.py

import business_logic

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Exit")

def main():
    business_logic.initialize_app()
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            business_logic.add_task(task)
            print("Task added!")
        elif choice == '2':
            tasks = business_logic.get_all_tasks()
            print("\nYour Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task[1]}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

