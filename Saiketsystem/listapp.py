# To-Do List Application

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔ Completed" if self.completed else "✘ Not Completed"
        return f"{self.description} - {status}"


def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")


tasks = []

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        description = input("Enter task description: ")
        task = Task(description)
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to complete.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            task_num = int(input("Enter task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1].mark_completed()
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please try again.")
