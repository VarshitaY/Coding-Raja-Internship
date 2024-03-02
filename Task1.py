import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ").lower()
    due_date = input("Enter due date (YYYY-MM-DD): ")
    new_task = {
        "name": task_name,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully.")

# Remove a task
def remove_task(tasks):
    print_tasks(tasks)
    index = int(input("Enter task number to remove: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
        print("Task removed successfully.")
    else:
        print("Invalid task number.")

# Mark a task as completed
def mark_completed(tasks):
    print_tasks(tasks)
    index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Print tasks in a list
def print_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']} (Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']})")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            print_tasks(tasks)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
