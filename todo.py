import json
import os

FILE_NAME = "todo.json"

def load_tasks():
    """Loads tasks from the JSON file. Returns an empty list if file doesn't exist."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: JSON file is corrupted. Starting fresh.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while loading: {e}")
        return []

def save_tasks(tasks):
    """Saves the list of tasks to a JSON file."""
    try:
        with open(FILE_NAME, 'w') as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task(task_name):
    """Adds a new task to the list and saves it."""
    if not task_name.strip():
        print("Error: Task name cannot be empty.")
        return
    
    tasks = load_tasks()
    tasks.append({"task": task_name.strip(), "done": False})
    save_tasks(tasks)
    print(f"Success! Added task: '{task_name}'")

def list_tasks():
    """Prints all tasks with their current completion status."""
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks found. You're all caught up!")
        return
    
    print("\n🚀 My Awesome To-Do List 🚀")
    for index, task in enumerate(tasks, 1):
        status = "[x]" if task.get("done") else "[ ]"
        print(f"{index}. {status} {task['task']}")
    print("------------------\n")

if __name__ == "__main__":
    # A quick way to test our functions
    print("Welcome to your AI-generated Todo CLI!")
    list_tasks()
    add_task("Learn Git PR workflow")
    add_task("Build Python Todo App")
    list_tasks()
