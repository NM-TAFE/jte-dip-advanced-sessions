# Week 1: Introduction to Software Architecture and Design Patterns

## Objectives

By the end of this lesson, you will be able to:

- Understand the importance of software architecture in application development.
- Describe common architectural patterns and their purposes.
- Explain what design patterns are and why they matter.
- Recognize the historical context and significance of the MVC pattern.
- Analyze a simple Python application to identify architectural components.

## Lesson Plan

### Section introduction

- Transition from fundamental algorithms and data structures to software architecture.
- What is software architecture?
- How does it relate to design patterns?
- Where does MVC fit in all of this?
- MVC in the context of modern web frameworks.


### Architectural patterns

- Monolithic
- Client-server
- Layered
- Microservices
  

### Discuss

What dimensions of software development are the concerns of architecture?

Pair and share: identify an application that falls into each of the categories (research) and present to the class (why and how you determined that it is so)
Try and think about why the designers of that particular application chose that architecture.



### Design patterns

- **What Are Design Patterns?**
- **Categories of Design Patterns**
  - **Creational Patterns** (e.g., Singleton, Factory)
  - **Structural Patterns** (e.g., Adapter, Composite)
  - **Behavioral Patterns** (e.g., Observer, Strategy)
- Addendum: design pattern and software principles (SOLID)


### The MVC pattern
- **MVC Components**
  - **Model:** Manages data and business logic.
  - **View:** Handles the display of information.
  - **Controller:** Interprets user inputs and commands.
- **Impact on Modern Frameworks**
  - How MVC influenced frameworks like Django and Ruby on Rails.


#### Practical: Simple Python application and MVC
**Exercise Objective:** Identify architectural components in a Python application.



```python
# todo_app.py

tasks = []

def add_task(task):
    tasks.append(task)

def list_tasks():
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            add_task(task)
            print("Task added!")
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
```



**Analysis Questions:**

- Which parts of the code handle data management (Model)?
- Which parts are responsible for the user interface (View)?
- Where is the control flow managed (Controller)?
- How well does this application separate concerns?

**Tasks**

1. Add a persistence layer to the application.
2. Create an intermediate layer between the persistence layer (data) and the user (view).
3. Discuss the minimal architecture you created in terms of:
   1. Separation of concerns
   2. Single responsibility
   3. Loose coupling
   4. MVC
