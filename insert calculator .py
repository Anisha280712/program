import tkinter as tk

def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        # Simple Interest
        si = (p * t * r) / 100

        # Compound Interest
        ci = p * ((1 + r/100) ** t) - p

        result_label.config(
            text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}",
            fg="darkblue"
        )
    except ValueError:
        result_label.config(text="Please enter valid numbers.", fg="red")


root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")

title_label = tk.Label(root, text="Interest Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

frame = tk.Frame(root)
frame.pack(pady=10)

# Labels and Entries side by side
tk.Label(frame, text="Principal: ").grid(row=0, column=0, padx=5, pady=5, sticky="e")
principal_entry = tk.Entry(frame, width=20)
principal_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Time (years): ").grid(row=1, column=0, padx=5, pady=5, sticky="e")
time_entry = tk.Entry(frame, width=20)
time_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Rate (%): ").grid(row=2, column=0, padx=5, pady=5, sticky="e")
rate_entry = tk.Entry(frame, width=20)
rate_entry.grid(row=2, column=1, padx=5, pady=5)

calc_button = tk.Button(root, text="Calculate", command=calculate_interest, bg="#87CEEB")
calc_button.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 13))
result_label.pack(pady=10)

root.mainloop()
