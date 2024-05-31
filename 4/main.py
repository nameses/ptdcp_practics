import tkinter as tk
from tkinter import messagebox
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# Функція для додавання даних у базу
def add_record():
    def submit_data():
        name = entry_name.get()
        age = entry_age.get()
        gender = entry_gender.get().lower()
        diagnosis = entry_diagnosis.get()

        if not name or not age or not gender or not diagnosis:
            messagebox.showerror("Error", "All fields are required")
            return

        if gender not in ['male', 'female']:
            messagebox.showerror("Error", "Gender must be 'male' or 'female'")
            return

        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Error", "Age must be an integer")
            return

        conn = sqlite3.connect('medical_institute.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO patients (name, age, gender, diagnosis) VALUES (?, ?, ?, ?)",
                       (name, age, gender, diagnosis))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data added successfully")
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add Record")

    tk.Label(add_window, text="Name").grid(row=0)
    tk.Label(add_window, text="Age").grid(row=1)
    tk.Label(add_window, text="Gender (male/female)").grid(row=2)
    tk.Label(add_window, text="Diagnosis").grid(row=3)

    entry_name = tk.Entry(add_window)
    entry_age = tk.Entry(add_window)
    entry_gender = tk.Entry(add_window)
    entry_diagnosis = tk.Entry(add_window)

    entry_name.grid(row=0, column=1)
    entry_age.grid(row=1, column=1)
    entry_gender.grid(row=2, column=1)
    entry_diagnosis.grid(row=3, column=1)

    tk.Button(add_window, text='Submit', command=submit_data).grid(row=4, column=1, sticky=tk.W, pady=4)


# Функція для редагування даних у базі
def edit_record():
    def submit_edit():
        selected_id = entry_id.get()
        name = entry_name.get()
        age = entry_age.get()
        gender = entry_gender.get().lower()
        diagnosis = entry_diagnosis.get()

        if not selected_id or not name or not age or not gender or not diagnosis:
            messagebox.showerror("Error", "All fields are required")
            return

        if gender not in ['male', 'female']:
            messagebox.showerror("Error", "Gender must be 'male' or 'female'")
            return

        try:
            age = int(age)
            selected_id = int(selected_id)
        except ValueError:
            messagebox.showerror("Error", "ID and Age must be integers")
            return

        conn = sqlite3.connect('medical_institute.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE patients SET name = ?, age = ?, gender = ?, diagnosis = ? WHERE id = ?",
                       (name, age, gender, diagnosis, selected_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data updated successfully")
        edit_window.destroy()

    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Record")

    tk.Label(edit_window, text="ID").grid(row=0)
    tk.Label(edit_window, text="Name").grid(row=1)
    tk.Label(edit_window, text="Age").grid(row=2)
    tk.Label(edit_window, text="Gender (male/female)").grid(row=3)
    tk.Label(edit_window, text="Diagnosis").grid(row=4)

    entry_id = tk.Entry(edit_window)
    entry_name = tk.Entry(edit_window)
    entry_age = tk.Entry(edit_window)
    entry_gender = tk.Entry(edit_window)
    entry_diagnosis = tk.Entry(edit_window)

    entry_id.grid(row=0, column=1)
    entry_name.grid(row=1, column=1)
    entry_age.grid(row=2, column=1)
    entry_gender.grid(row=3, column=1)
    entry_diagnosis.grid(row=4, column=1)

    tk.Button(edit_window, text='Submit', command=submit_edit).grid(row=5, column=1, sticky=tk.W, pady=4)


# Пошук даних у базі
def search_data():
    search_term = entry_search.get()

    conn = sqlite3.connect('medical_institute.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE name LIKE ?", ('%' + search_term + '%',))
    results = cursor.fetchall()
    conn.close()

    search_results.delete(1.0, tk.END)
    for row in results:
        search_results.insert(tk.END, str(row) + '\n')


# Візуалізація даних по віку
def visualize_age_distribution():
    conn = sqlite3.connect('medical_institute.db')
    df = pd.read_sql_query("SELECT * FROM patients", conn)
    conn.close()

    plt.figure(figsize=(10, 5))
    df['age'].hist()
    plt.title('Age Distribution of Patients')
    plt.xlabel('Age')
    plt.ylabel('Number of Patients')
    plt.show()


# Візуалізація даних по захворюваннях
def visualize_diagnosis_distribution():
    conn = sqlite3.connect('medical_institute.db')
    df = pd.read_sql_query("SELECT * FROM patients", conn)
    conn.close()

    diagnosis_counts = df['diagnosis'].value_counts()
    plt.figure(figsize=(10, 5))
    diagnosis_counts.plot(kind='bar')
    plt.title('Distribution of Diagnoses')
    plt.xlabel('Diagnosis')
    plt.ylabel('Number of Patients')
    plt.show()


# Створення GUI
root = tk.Tk()
root.title("Medical Information System")

tk.Button(root, text='Add Record', command=add_record).grid(row=0, column=0, sticky=tk.W, pady=4)
tk.Button(root, text='Edit Record', command=edit_record).grid(row=0, column=1, sticky=tk.W, pady=4)

tk.Label(root, text="Search by Name").grid(row=1)
entry_search = tk.Entry(root)
entry_search.grid(row=1, column=1)
tk.Button(root, text='Search', command=search_data).grid(row=2, column=1, sticky=tk.W, pady=4)

search_results = tk.Text(root, height=10, width=50)
search_results.grid(row=3, column=0, columnspan=2)

tk.Button(root, text='Visualize Age Distribution', command=visualize_age_distribution).grid(row=4, column=0,
                                                                                            sticky=tk.W, pady=4)
tk.Button(root, text='Visualize Diagnosis Distribution', command=visualize_diagnosis_distribution).grid(row=4, column=1,
                                                                                                        sticky=tk.W,
                                                                                                        pady=4)


root.mainloop()