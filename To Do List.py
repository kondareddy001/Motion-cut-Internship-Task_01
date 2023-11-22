import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Set background color to light green
        self.root.config(bg="#c9ffaf")

        self.tasks = []

        # Task Entry Widgets
        tk.Label(root, text="Task Description:").grid(row=0, column=0, padx=10, pady=5)
        self.task_description_entry = tk.Entry(root, width=30)
        self.task_description_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Due Date:").grid(row=1, column=0, padx=10, pady=5)
        self.due_date_entry = tk.Entry(root, width=30)
        self.due_date_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Priority:").grid(row=2, column=0, padx=10, pady=5)
        self.priority_entry = tk.Entry(root, width=30)
        self.priority_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(root, text="Add Task", command=self.add_task).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Display Tasks", command=self.display_tasks).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Mark as Complete", command=self.mark_as_complete).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Exit", command=self.root.destroy).grid(row=6, column=0, columnspan=2, pady=10)

    def add_task(self):
        description = self.task_description_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()

        new_task = Task(description, due_date, priority)
        self.tasks.append(new_task)

        messagebox.showinfo("Task Added", "Task added successfully!")

        # Clear entry fields after adding a task
        self.task_description_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    def display_tasks(self):
        if not self.tasks:
            messagebox.showinfo("No Tasks", "No tasks to display.")
            return

        # Sort tasks based on priority
        sorted_tasks = sorted(self.tasks, key=lambda x: int(x.priority) if x.priority else 0)

        display_window = tk.Toplevel(self.root)
        display_window.title("Task List")

        task_list_label = tk.Label(display_window, text="Task List", font=("Helvetica", 16, "bold"))
        task_list_label.grid(row=0, column=0, columnspan=3, pady=10)

        for index, task in enumerate(sorted_tasks, start=1):
            status = "Completed" if task.completed else "Pending"
            task_text = f"{index}. {task.description} - Due: {task.due_date}, Priority: {task.priority}, Status: {status}"
            tk.Label(display_window, text=task_text).grid(row=index, column=0, columnspan=3)

    def mark_as_complete(self):
        if not self.tasks:
            messagebox.showinfo("No Tasks", "No tasks to mark as complete.")
            return

        task_index = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            messagebox.showinfo("Task Completed", "Task marked as complete!")
        else:
            messagebox.showwarning("Invalid Task Number", "Please enter a valid task number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
