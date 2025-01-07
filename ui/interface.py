from tkinter import *
import os

def update_text_color(enabled):
    if enabled:
        middle_label.config(fg="green")
    else:
        middle_label.config(fg="red")

def start_tkinter():
    global middle_label

    window = Tk()
    window.geometry('350x400')
    window.resizable(False, False)
    window.title('TurboDrag')


    icon_path = os.path.join(os.path.dirname(__file__), '../images/logo.png')
    icon = PhotoImage(file=icon_path)
    window.iconphoto(True, icon)

    window.config(background='#192029')

    image = icon.subsample(15, 15)
    label = Label(window,
                  text="TurboDrag",
                  font=("Comic Sans MS", 14),
                  bg="#10151c",
                  fg="#2b67ba",
                  image=image,
                  compound="left")
    label.pack(anchor="n", fill="x")



    middle_label = Label(
        window,
        text="Press F2 to ENABLE/DISABLE",
        font=("Comic Sans MS", 16, "bold"),
        bg="#10151c",
        fg="red"
    )
    middle_label.place(relx=0.5, rely=0.5, anchor=CENTER)





    credits_label = Label(
        window,
        text="CREDITS: catamarioo",
        font=("Comic Sans MS", 10, "italic"),
        bg="#10151c",
        fg="white"
    )
    credits_label.pack(side=BOTTOM, pady=10)

    window.mainloop()


