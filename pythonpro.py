import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

task_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 14), width=25)
task_entry.pack(pady=10)

TASK_FILE = "tasks.txt"

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Enter a task first!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showerror("Error", "No task selected")

def mark_done():
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        if "[Done]" not in task:
            task_listbox.delete(index)
            task_listbox.insert(index, f"{task} [Done]")
            save_tasks()
    except:
        messagebox.showerror("Error", "No task selected")

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task_listbox.insert(tk.END, line.strip())

# Buttons
add_button = tk.Button(root, text="Add Task", width=20, command=add_task, bg="#90ee90")
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task, bg="#ff7f7f")
delete_button.pack(pady=5)

done_button = tk.Button(root, text="Mark as Done", width=20, command=mark_done, bg="#add8e6")
done_button.pack()

load_tasks()
root.mainloop()
