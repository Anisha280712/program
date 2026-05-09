import tkinter as tk
import random

# Function to decide winner
def play(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    result_text = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n"

    if user_choice == computer_choice:
        result_text += "Result: It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result_text += "Result: You win!"
    else:
        result_text += "Result: Computer wins!"

    result_label.config(text=result_text)

# Main window
root = tk.Tk()
root.title("Length Converter App")  # as given in the task
root.geometry("400x400")

# Heading label
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Instruction label
instruction_label = tk.Label(root, text="Click a button to make your choice:")
instruction_label.pack(pady=5)

# Buttons for user choice
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("rock"))
paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("paper"))
scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("scissors"))

rock_button.grid(row=0, column=0, padx=5)
paper_button.grid(row=0, column=1, padx=5)
scissors_button.grid(row=0, column=2, padx=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
