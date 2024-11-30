import os
import json

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from the file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    task_name = input("Enter task name: ").strip()
    if not task_name:
        print("Task name cannot be empty.")
        return
    priority = input("Enter priority (Low, Medium, High): ").capitalize()
    tasks.append({"name": task_name, "priority": priority, "completed": False})
    save_tasks(tasks)
    print(f"Task '{task_name}' added successfully.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\n--- Task List ---")
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx}. {task['name']} | Priority: {task['priority']} | Status: {status}")
    print("-----------------\n")

# Update a task
def update_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to update: "))
        if task_no < 1 or task_no > len(tasks):
            print("Invalid task number.")
            return
        task = tasks[task_no - 1]
        print(f"Updating task: {task['name']}")
        task['name'] = input("Enter new task name (press Enter to keep the current): ").strip() or task['name']
        task['priority'] = input("Enter new priority (Low, Medium, High, press Enter to keep current): ").capitalize() or task['priority']
        status = input("Is the task completed? (yes/no): ").lower()
        task['completed'] = True if status == "yes" else task['completed']
        save_tasks(tasks)
        print("Task updated successfully.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to delete: "))
        if task_no < 1 or task_no > len(tasks):
            print("Invalid task number.")
            return
        task = tasks.pop(task_no - 1)
        save_tasks(tasks)
        print(f"Task '{task['name']}' deleted successfully.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main menu
def main_menu():
    tasks = load_tasks()
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
