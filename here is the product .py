import tkinter as tk

def calculate_product():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        product = n1 * n2
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"Product: {product}")
    except ValueError:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Please enter valid numbers.")


root = tk.Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

# Description label
desc_label = tk.Label(root, text="This app multiplies two numbers.", font=("Arial", 12))
desc_label.pack(pady=10)

# Number 1 label + entry
label1 = tk.Label(root, text="Enter first number:")
label1.pack()
entry1 = tk.Entry(root, width=20)
entry1.pack(pady=5)

# Number 2 label + entry
label2 = tk.Label(root, text="Enter second number:")
label2.pack()
entry2 = tk.Entry(root, width=20)
entry2.pack(pady=5)

# Button
calc_button = tk.Button(root, text="Calculate Product", command=calculate_product, bg="#87CEEB")
calc_button.pack(pady=10)

# Text box for result
result_box = tk.Text(root, height=3, width=30)
result_box.pack(pady=10)

root.mainloop()
