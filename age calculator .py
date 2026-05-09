import tkinter as tk
from datetime import date

def calculate_age():
    try:
        name = name_entry.get()
        d = int(day_entry.get())
        m = int(month_entry.get())
        y = int(year_entry.get())

        today = date.today()
        age = today.year - y

        # Adjust if birthday hasn't happened yet this year
        if (today.month, today.day) < (m, d):
            age -= 1

        result_label.config(
            text=f"Hello {name}, you are {age} years old!",
            fg="darkblue"
        )

    except ValueError:
        result_label.config(text="Please enter valid numbers.", fg="red")


root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")

title_label = tk.Label(root, text="Age Calculator", font=("Arial", 16, ")