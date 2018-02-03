from tkinter import *


def Start():
    print('Введите число')


root = Tk()
btn = Button(root,
             text="Введите первое число",
             width=30, height=5,
             bg="white", fg="black")
btn.bind("<Button-1>", Start())
btn.pack()
root.mainloop()
