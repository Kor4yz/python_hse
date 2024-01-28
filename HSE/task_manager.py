# task_manager.py
import json
from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    НОВАЯ = "Новая"
    ВЫПОЛНЯЕТСЯ = "Выполняется"
    РЕВЬЮ = "Ревью"
    ВЫПОЛНЕНО = "Выполнено"
    ОТМЕНЕНО = "Отменено"


class Task:
    def __init__(self, title, description, status, creation_date=None, status_change_date=None):
        self.title = title
        self.description = description
        self.status = status
        self.creation_date = creation_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status_change_date = status_change_date or self.creation_date

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "creation_date": self.creation_date.strftime("%Y-%m-%dT%H:%M:%S"),
            "status_change_date": self.status_change_date.strftime("%Y-%m-%dT%H:%M:%S"),
        }

    @staticmethod
    def from_dict(data):
        title = data["title"]
        description = data["description"]

        try:
            status = TaskStatus[data["status"]]
        except KeyError:
            status = TaskStatus.НОВАЯ

        creation_date_str = data["creation_date"]
        creation_date = datetime.strptime(creation_date_str, "%Y-%m-%dT%H:%M:%S")

        status_change_date_str = data["status_change_date"]
        status_change_date = datetime.strptime(status_change_date_str, "%Y-%m-%dT%H:%M:%S")

        return Task(title, description, status, creation_date, status_change_date)


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, status, creation_date=None, status_change_date=None):
        if creation_date is None:
            creation_date = datetime.now().replace(microsecond=0)

        if status_change_date is None:
            status_change_date = datetime.now().replace(microsecond=0)

        task = Task(title, description, status, creation_date, status_change_date)
        self.tasks.append(task)
        print("Task added successfully!")

    def change_task_status(self, title, new_status):
        for task in self.tasks:
            if task.title == title:
                task.status = new_status
                task.status_change_date = datetime.now().replace(microsecond=0)

    def view_history(self):
        for task in self.tasks:
            print(f"{task.title} - {task.status} ({task.status_change_date})")

    def delete_task(self, title):
        existing_tasks = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.title != title]
        if len(self.tasks) < existing_tasks:
            print("Task deleted successfully!")
        else:
            print("Task not found.")

    def save_to_file(self, filename):
        data = {"tasks": [task.to_dict() for task in self.tasks]}
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def load_from_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task_data) for task_data in data["tasks"]]
        except FileNotFoundError:
            raise FileNotFoundError("File not found.")
