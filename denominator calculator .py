from tkinter import*
from tkinter import messagebox
from PIL  import image, imageTK




root= Tk()
root.title("denomination counter")
root.configure(bg="lightblue")
root.geometry("650x400")




upload =Image.open ("app_img.jpg")
upload.resize((300, 300))
image = imageTK.photoimage(upload)

label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = label(
    root,
    text="hey user welcome to denomination counter application"
    bg="light blue"
)
label1.place(relx=0.5, y=340, anchor=CENTER)




def msg():
    msgBox = messagebox.showinfo(
        "alert",
        "do you want to calculate the denomination count?"
    )
    if msgBox =="ok":
        topwin()




button1= Button(
    root,
    text="lets get started!"
    command=msg
    bg="brown",
    fg="white"
)
button1.place(x=260, y=360)




def topwin():
    top =  Toplevel()
    top.title("denominations calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    label=Label(top, text="enter total amount", bg= "light grey")
    entry = Entry(top)

    lbl = Label(
        top,
        text="here are the numbe of notes for each denomination"
        bg= "light grey"
    )
    l1 = label(top, Text="2000", bg="light grey")
    l2 = label(top, Text="500", bg="light grey")
    l3 = label(top, Text="100", bg="light grey")


    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)


    def calculator():
        try:
            amount = int (entry.get())

            note2000 = amount // 2000
            amount%= 2000

            note500= amount // 500
            amount%=500

            note100 = amount//100

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except valueError:
            messagebox.showerror("Error"," Please enter a valid number")

    btn= Button(
        top,
        text="calculate",
        command= calculator,
        bg="brown" ,
        fg= "white"
    )

    