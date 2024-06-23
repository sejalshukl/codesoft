import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.geometry("400x300")

        self.tasks = []

        # Entry field for new tasks
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(master, textvariable=self.task_var, width=30)
        self.task_entry.pack(pady=10)

        # Button to add a new task
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(master, width=40)
        self.task_listbox.pack(pady=10)

        # Button to remove a selected task
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        # Button to update a selected task
        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.load_tasks()

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_var.set("")  # Clear the entry field
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_task(self):
        try:
            index = self.task_listbox.curselection()[0]  # Get the index of the selected task
            task = self.task_var.get()
            if task:
                self.tasks[index] = task  # Update the task at the selected index
                self.update_task_listbox()
                self.task_var.set("")  # Clear the entry field
            else:
                messagebox.showwarning("Warning", "Please enter a task to update.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Insert each task into the listbox

    def load_tasks(self):
        # Load tasks from a file or database if needed
        pass

    def save_tasks(self):
        # Save tasks to a file or database if needed
        pass

    def on_closing(self):
        self.save_tasks()
        self.master.destroy()

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
