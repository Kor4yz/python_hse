from task_manager import Task, TaskStatus, TaskManager
import argparse

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    parser.add_argument("file", help="JSON file for tasks")
    args = parser.parse_args()

    task_manager = TaskManager()
    task_manager.load_from_file(args.file)

    while True:
        print("\n===== Task Manager Menu =====")
        print("1. Add Task")
        print("2. Change Task Status")
        print("3. View History")
        print("4. Save and Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            status = TaskStatus.NEW
            creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status_change_date = creation_date
            task = Task(title, description, status, creation_date, status_change_date)
            task_manager.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            task_title = input("Enter task title: ")
            new_status = input("Enter new task status (новая, выполняется, ревью, выполнено, отменено): ")
            try:
                new_status_enum = TaskStatus(new_status)
                task_manager.change_task_status(task_title, new_status_enum)
                print(f"Task status changed successfully to {new_status_enum.value}")
            except ValueError:
                print("Invalid status. Please enter a valid status.")

        elif choice == "3":
            task_manager.view_history()

        elif choice == "4":
            task_manager.save_to_file(args.file)
            print(f"Tasks saved to {args.file}. Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
