from dataclasses import dataclass, asdict
from enum import Enum
import json
from typing import List
from datetime import datetime

class TaskStatus(Enum):
    NEW = "новая"
    IN_PROGRESS = "выполняется"
    REVIEW = "ревью"
    DONE = "выполнено"
    CANCELED = "отменено"

@dataclass
class Task:
    title: str
    description: str
    status: TaskStatus
    creation_date: str
    status_change_date: str

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, task: Task):
        self.tasks.append(task)
        self.history.append(f"Добавлена задача: {task.title}")

    def change_task_status(self, task_title: str, new_status: TaskStatus):
        for task in self.tasks:
            if task.title == task_title:
                old_status = task.status
                task.status = new_status
                task.status_change_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.history.append(f"Статус задачи '{task.title}' изменен с {old_status.value} на {new_status.value}")

    def save_to_file(self, file_name: str):
        data = {"tasks": [asdict(task) for task in self.tasks], "history": self.history}
        with open(file_name, "w") as file:
            json.dump(data, file)

    def load_from_file(self, file_name: str):
        with open(file_name, "r") as file:
            data = json.load(file)
            self.tasks = [Task(**task_data) for task_data in data.get("tasks", []) if isinstance(task_data, dict)]
            self.history = data.get("history", [])

    def view_history(self):
        for entry in self.history:
            print(entry)
