import argparse
from task_manager import TaskManager, Task, TaskStatus

def get_task_status(status_str):
    try:
        return TaskStatus[status_str.upper()]
    except KeyError:
        print("Invalid status. Defaulting to НОВАЯ.")
        return TaskStatus.НОВАЯ

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    parser.add_argument("file", help="Path to the tasks file")
    args = parser.parse_args()

    task_manager = TaskManager()

    try:
        task_manager.load_from_file(args.file)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("File not found. Starting with an empty task list.")

    while True:
        print("\n===== Task Manager Menu =====")
        print("1. Add Task")
        print("2. Change Task Status")
        print("3. View History")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            status = input("Enter task status (новая, выполняется, ревью, выполнено, отменено): ").strip().lower()
            task_manager.add_task(title, description, get_task_status(status))
            print("Task added successfully!")

        elif choice == "2":
            title = input("Enter task title: ").strip()
            new_status = input(
                "Enter new task status (новая, выполняется, ревью, выполнено, отменено): ").strip().lower()

            try:
                task_manager.change_task_status(title, get_task_status(new_status))
                print("Task status changed successfully!")
            except KeyError:
                print("Invalid status. Please enter a valid status.")

        elif choice == "3":
            task_manager.view_history()

        elif choice == "4":
            title_to_delete = input("Enter the title of the task to delete: ").strip()
            task_manager.delete_task(title_to_delete)
            print("Task deleted successfully!")

        elif choice == "5":
            task_manager.save_to_file(args.file)
            print("Data saved successfully. Exiting.")
            break
    else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
