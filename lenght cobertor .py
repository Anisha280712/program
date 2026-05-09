import tkinter as tk

def convert_length():
    try:
        value = float(entry.get())
        meters = value / 100
        result_label.config(text=f"{value} cm = {meters} m", fg="darkblue")
    except ValueError:
        result_label.config(text="Enter a valid number.", fg="red")


root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

title_label = tk.Label(root, text="Length Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Enter length (cm): ").grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(frame, width=20)
entry.grid(row=0, column=1, padx=5, pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_length, bg="#87CEEB")
convert_button.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
