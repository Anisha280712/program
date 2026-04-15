from tkinter import*
from tkinter import messagebox


root =Tk()
root.geometry("500x500")


def msg():
    messagebox.showwarning("alert, ""stop!""Virus found.")

button = Button(root, text="scan for virus", command=msg)
button.place(x=40, y=10)

root.mainloop()