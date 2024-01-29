import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
from task_manager import TaskManager, Task, TaskStatus
import json
from datetime import datetime

# Define get_task_status function
def get_task_status(status_str):
    try:
        return TaskStatus[status_str.upper()]
    except KeyError:
        print("Invalid status. Defaulting to НОВАЯ.")
        return TaskStatus.НОВАЯ

class TaskManagerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Менеджер задач")
        self.geometry("500x300")

        self.task_manager = TaskManager()

        try:
            self.task_manager.load_from_file("tasks.json")
            messagebox.showinfo("Успех", "Данные успешно загружены.")
        except FileNotFoundError:
            messagebox.showinfo("Файл не найден", "Начинаем с пустого списка задач.")

        self.create_widgets()

    def create_widgets(self):
        menu_frame = tk.Frame(self)
        menu_frame.pack(pady=10)

        add_button = tk.Button(menu_frame, text="Добавить задачу", command=self.add_task)
        add_button.grid(row=0, column=0, padx=10)

        change_status_button = tk.Button(menu_frame, text="Изменить статус задачи", command=self.change_status)
        change_status_button.grid(row=0, column=1, padx=10)

        view_history_button = tk.Button(menu_frame, text="Просмотреть историю", command=self.view_history)
        view_history_button.grid(row=0, column=2, padx=10)

        delete_button = tk.Button(menu_frame, text="Удалить задачу", command=self.delete_task)
        delete_button.grid(row=0, column=3, padx=10)

        save_exit_button = tk.Button(menu_frame, text="Сохранить и выйти", command=self.save_and_exit)
        save_exit_button.grid(row=0, column=4, padx=10)

    def add_task(self):
        title = simpledialog.askstring("Ввод", "Введите название задачи:")
        description = simpledialog.askstring("Ввод", "Введите описание задачи:")

        # Создаем список вариантов для статуса задачи
        status_options = [status.value for status in TaskStatus]

        # Создаем переменную для хранения выбранного статуса
        selected_status = tk.StringVar(self)
        selected_status.set(TaskStatus.НОВАЯ.value)  # Установим первый статус по умолчанию

        # Создаем OptionMenu с вариантами статусов
        status_option_menu = tk.OptionMenu(self, selected_status, *status_options)
        status_option_menu.pack(pady=10)

        def on_ok():
            try:
                task_status = TaskStatus[selected_status.get().upper()]
                self.task_manager.add_task(title, description, task_status)
                messagebox.showinfo("Успех", "Задача успешно добавлена!")

                # Закрываем окно после добавления задачи
                status_option_menu.destroy()
                ok_button.destroy()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при добавлении задачи: {str(e)}")

        ok_button = tk.Button(self, text="OK", command=on_ok)
        ok_button.pack(pady=10)

    def change_status(self):
        task_titles = [task.title for task in self.task_manager.tasks]

        if not task_titles:
            messagebox.showinfo("Информация", "Список задач пуст. Нет задач для изменения статуса.")
            return

        task_listbox = tk.Listbox(self, selectmode=tk.SINGLE, height=min(10, len(task_titles)))
        for title in task_titles:
            task_listbox.insert(tk.END, title)

        task_listbox.pack(pady=10)

        new_status_var = tk.StringVar(self)
        new_status_var.set(TaskStatus.НОВАЯ.value)  # Установим первый статус по умолчанию

        # Создаем OptionMenu с вариантами статусов
        status_options = [status.value for status in TaskStatus]
        status_option_menu = tk.OptionMenu(self, new_status_var, *status_options)
        status_option_menu.pack(pady=10)

        def on_ok():
            selected_index = task_listbox.curselection()
            if selected_index:
                selected_task = task_titles[selected_index[0]]
                try:
                    task_status = TaskStatus[new_status_var.get().upper()]
                    self.task_manager.change_task_status(selected_task, task_status)
                    messagebox.showinfo("Успех", "Статус задачи успешно изменен!")
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Ошибка при изменении статуса задачи: {str(e)}")

                # Закрываем окно после выбора нового статуса
                task_listbox.destroy()
                status_option_menu.destroy()
                ok_button.destroy()

        ok_button = tk.Button(self, text="OK", command=on_ok)
        ok_button.pack(pady=10)

        self.mainloop()  # Уберем этот вызов, так как он не нужен в данном случае

    def view_history(self):
        task_titles = [task.title for task in self.task_manager.tasks]

        if not task_titles:
            messagebox.showinfo("Информация", "Список задач пуст. Нет задач для просмотра истории.")
            return

        task_listbox = tk.Listbox(self, selectmode=tk.SINGLE, height=min(10, len(task_titles)))
        for title in task_titles:
            task_listbox.insert(tk.END, title)

        task_listbox.pack(pady=10)

        def on_ok():
            selected_index = task_listbox.curselection()
            if selected_index:
                selected_task = task_titles[selected_index[0]]
                task = next((t for t in self.task_manager.tasks if t.title == selected_task), None)
                if task:
                    history_text = f"{task.title} - {task.status} ({task.status_change_date})"
                    messagebox.showinfo("История задачи", history_text)

                # Закрываем окно после выбора задачи
                task_listbox.destroy()
                ok_button.destroy()

        ok_button = tk.Button(self, text="OK", command=on_ok)
        ok_button.pack(pady=10)

        self.mainloop()  # Уберем этот вызов, так как он не нужен в данном случае

    def delete_task(self):
        task_titles = [task.title for task in self.task_manager.tasks]

        if not task_titles:
            messagebox.showinfo("Информация", "Список задач пуст. Нет задач для удаления.")
            return

        task_listbox = tk.Listbox(self, selectmode=tk.SINGLE, height=min(10, len(task_titles)))
        for title in task_titles:
            task_listbox.insert(tk.END, title)

        task_listbox.pack(pady=10)

        def on_ok():
            selected_index = task_listbox.curselection()
            if selected_index:
                selected_task = task_titles[selected_index[0]]
                confirmation = messagebox.askquestion("Подтверждение удаления",
                                                      f"Вы уверены, что хотите удалить задачу:\n\n{selected_task}")
                if confirmation == 'yes':
                    self.task_manager.delete_task(selected_task)
                    messagebox.showinfo("Успех", "Задача успешно удалена!")
                task_listbox.destroy()

        ok_button = tk.Button(self, text="OK", command=on_ok)
        ok_button.pack(pady=10)

        task_listbox.mainloop()

    def save_and_exit(self):
        try:
            self.task_manager.save_to_file("tasks.json")
            messagebox.showinfo("Успех", "Данные успешно сохранены. Завершение работы.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при сохранении данных: {str(e)}")

if __name__ == "__main__":
    app = TaskManagerGUI()
    app.mainloop()
