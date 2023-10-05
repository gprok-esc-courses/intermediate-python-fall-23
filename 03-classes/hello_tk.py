from tkinter import Tk, Label, Button


def button_clicked():
    value = label.cget("text")
    next = int(value) + 1
    label.config(text=str(next))


window = Tk()

label = Label(window, text="0")
label.grid(row=0, column=0)
button = Button(window, text="Increase", command=button_clicked)
button.grid(row=1, column=0)

window.mainloop()


