import json
import os

# File path to store tasks
FILE_PATH = "tasks.json"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    else:
        return {"tasks": []}

# Function to save tasks to file
def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file)

# Function to add a new task
def add_task(tasks, title, priority, due_date):
    tasks["tasks"].append({"title": title, "priority": priority, "due_date": due_date, "completed": False})
    save_tasks(tasks)

# Function to remove a task
def remove_task(tasks, index):
    del tasks["tasks"][index]
    save_tasks(tasks)


# Function to mark a task as completed
def mark_task_completed(tasks, index):
    tasks["tasks"][index]["completed"] = True
    save_tasks(tasks)

# Function to display tasks
def display_tasks(tasks):
    for i, task in enumerate(tasks["tasks"], 1):
        print(f"{i}. Title: {task['title']}, Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")

# Main function
def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Mark Task as Completed\n4. Display Tasks\n5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, title, priority, due_date)
        elif choice == "2":
            display_tasks(tasks)
            index = int(input("Enter task index to remove: ")) - 1
            remove_task(tasks, index)
        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter task index to mark as completed: ")) - 1
            mark_task_completed(tasks, index)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
