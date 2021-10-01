# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 21:00:48 2021

@author: enzoa
"""

from tkinter import *
from PIL import ImageTk, Image

# Janela
root = Tk()
# título
root.title('Images')
# ícone
root.iconbitmap('C:/Users/enzoa/Dev/Spyder notebooks/Estudos/Tkinter/icon.ico')

# Frame
frame = LabelFrame(root, text="This is my frame...", padx=50, pady=50)
frame.pack(padx=100, pady=100)

# Botão
b = Button(frame, text="Não clique aqui!")
b2 = Button(frame, text="... e não aqui!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

# botão de rádio
#r = IntVar()
#r.set("2")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
    ]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack()

def clicked(value):
    label = Label(frame, text=value)
    label.grid(row=4, column=0)
    

#Radiobutton(frame, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).grid(row=2, column=0)
#Radiobutton(frame, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).grid(row=3, column=0)

button = Button(frame, text="Click Me!", command=lambda: clicked(pizza.get()))
button.grid(row=5, column=0)

root.mainloop()
