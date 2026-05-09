
import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)

    if length <= 5:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "yellow"
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "light green"
    else:
        strength = "Very Strong"
        color = "dark green"

    result_label.config(text=f"Strength: {strength}", fg=color)


# Main window
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

entry_label = tk.Label(root, text="Enter your password:")
entry_label.pack()

entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
