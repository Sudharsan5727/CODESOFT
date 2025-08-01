import os

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "correct" if self.completed else "Wrong"
        return f"[{status}] {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))
        print("Task added successfully")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list")
            return
        print("\nYour To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print("Task marked as completed")
        else:
            print("Invalid number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Deleted task: {removed.description}")
        else:
            print("Invalid number.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            task_desc = input("Enter description: ")
            todo.add_task(task_desc)
        elif choice == '2':
            todo.show_tasks()
        elif choice == '3':
            todo.show_tasks()
            try:
                task_no = int(input("Enter task number to mark as completed: ")) - 1
                todo.mark_completed(task_no)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            todo.show_tasks()
            try:
                task_no = int(input("Enter number to delete: ")) - 1
                todo.delete_task(task_no)
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            print("Exiting Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 to 5.")

if __name__ == "__main__":
    main()
